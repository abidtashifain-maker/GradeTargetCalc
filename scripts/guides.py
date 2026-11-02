"""Static study-guide pages, navigation and topic metadata."""
from pathlib import Path
import json,html,re,math
from editorial import word_count
ROOT=Path(__file__).resolve().parents[1]
PUBLISHED='2026-11-02'
def esc(s):return html.escape(str(s),quote=True)
def load_guides():
    result=[]
    for file in sorted((ROOT/'content').glob('guides-*.json')):result.extend(json.loads(file.read_text()))
    if len(result)!=18:raise ValueError('Expected18 complete new study guides')
    if len({x['slug'] for x in result})!=len(result):raise ValueError('Duplicate study guide slug')
    return result

def guide_cards(guides):
    return ''.join(f'<a class="card guide-card" href="/guides/{esc(g["slug"])}/"><span class="eyebrow">{esc(g["category"])}</span><h3>{esc(g["title"])}</h3><p>{esc(g["excerpt"])}</p><span class="arrow">Read the guide →</span></a>' for g in guides)

def render_guide(g,all_guides,tools,base):
    title=g['title'];slug=g['slug'];url=base+'/guides/'+slug+'/'
    # Link only the first explicit mention of a named tool in the article.
    used=set()
    aliases={t: s for s,t,d,i,k in tools}
    names={esc(name):slug for name,slug in aliases.items()}
    pattern=re.compile('|'.join(re.escape(name) for name in sorted(names,key=len,reverse=True)))
    def prose(text):
        def replace(match):
            name=match.group(0);tool_slug=names[name]
            if tool_slug in used:return name
            used.add(tool_slug)
            return f'<a href="/{tool_slug}/">{name}</a>'
        return pattern.sub(replace,esc(text))
    visual=g['visual']
    steps=''.join(f'<li><span class="flow-number" aria-hidden="true">{i}</span><span class="flow-label">{esc(s["label"])}</span><strong>{esc(s["value"])}</strong><p>{esc(s["detail"])}</p></li>' for i,s in enumerate(visual['steps'],1))
    figure=f'<figure class="learning-visual" aria-labelledby="guide-visual-title" aria-describedby="guide-visual-caption"><div class="visual-heading"><span class="visual-symbol" aria-hidden="true">∑</span><div><span class="eyebrow">Worked example</span><h2 id="guide-visual-title">{esc(visual["title"])}</h2></div></div><ol class="infographic-flow">{steps}</ol><figcaption id="guide-visual-caption">{esc(visual["caption"])}</figcaption></figure>'
    sections=[]
    for i,s in enumerate(g['sections'],1):
        ps=''.join(f'<p>{prose(p)}</p>' for p in s.get('paragraphs',[]))
        bullets='<ul>'+''.join(f'<li>{prose(p)}</li>' for p in s['bullets'])+'</ul>' if s.get('bullets') else ''
        sections.append(f'<section id="guide-{esc(s["id"])}" class="learning-box box-{esc(s["id"])}"><div class="box-heading"><span class="box-number" aria-hidden="true">{i:02}</span><h2>{esc(s["heading"])}</h2></div>{ps}{bullets}</section>')
    faqs=''.join(f'<details><summary>{esc(q)}</summary><p>{prose(a)}</p></details>' for q,a in g['faqs'])
    main=figure+'<div class="reading-grid">'+''.join(sections)+'</div><section class="learning-faq" id="guide-faq"><span class="eyebrow">Quick answers</span><h2>Frequently asked questions</h2>'+faqs+'</section>'
    words=word_count(html.unescape(re.sub('<[^>]+>',' ',main)))
    if words<750:raise ValueError(f'{slug}: guide is too short ({words})')
    toc=''.join(f'<a href="#guide-{esc(s["id"])}">{esc(s["heading"])}</a>' for s in g['sections'])
    links={s:(t,d) for s,t,d,i,k in tools}
    tool_links=''.join(f'<a class="card" href="/{s}/"><span class="eyebrow">Try the calculation</span><h3>{esc(links[s][0])}</h3><p>{esc(links[s][1])}</p><span class="arrow">Open calculator →</span></a>' for s in g['tool_slugs'])
    source_links=''.join(f'<li><a href="{esc(s["url"])}">{esc(s["label"])}</a></li>' for s in g['sources'])
    related=sorted((x for x in all_guides if x['slug']!=slug),key=lambda x:x['category']!=g['category'])[:3]
    body=f'''<div class="wrap"><header class="page-hero"><div class="crumb"><a href="/">Home</a> / <a href="/guides/">Study guides</a></div><span class="eyebrow">{esc(g['category'])}</span><h1>{esc(title)}</h1><p class="lead">{esc(g['description'])}</p><p class="guide-byline">By <a href="/about/">GradeTargetCalc</a> · Published <time datetime="{PUBLISHED}">2 November 2026</time> · {math.ceil(words/220)} min read</p></header><nav class="learning-nav" aria-label="Guide contents"><span>In this guide</span><div>{toc}<a href="#guide-faq">FAQs</a><a href="#guide-sources">Sources</a></div></nav><article class="study-article" data-guide-slug="{esc(slug)}" data-guide-words="{words}">{main}</article><aside class="guide-sources" id="guide-sources"><h2>Sources and scope</h2><p>These references explain the relevant methods or institutional context. Worked numerical scenarios are illustrative; your syllabus and institution determine the rules that apply to you.</p><ul>{source_links}</ul><p><a href="/methodology/">Calculation and editorial methodology</a> · <a href="/contact/">Report a correction</a></p></aside><section class="section"><div class="section-title"><h2>Put the guide into practice</h2></div><div class="grid">{tool_links}</div></section><section class="section"><div class="section-title"><h2>Keep learning</h2><a href="/guides/">All study guides →</a></div><div class="grid">{guide_cards(related)}</div></section></div>'''
    schema={'@context':'https://schema.org','@type':'Article','headline':title,'description':g['description'],'url':url,'mainEntityOfPage':url,'datePublished':PUBLISHED,'author':{'@type':'Organization','name':'GradeTargetCalc','url':base+'/about/'},'publisher':{'@type':'Organization','name':'GradeTargetCalc','url':base+'/'},'inLanguage':'en','articleSection':g['category'],'wordCount':words}
    return body,schema,words
