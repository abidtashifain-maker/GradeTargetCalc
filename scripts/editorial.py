"""Accessible, static rendering for the calculator learning library."""
from pathlib import Path
import html,json,re,math
ROOT=Path(__file__).resolve().parents[1]
def esc(text):return html.escape(str(text),quote=True)
def word_count(text):return len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b",text))
def load_articles():
    articles={}
    for path in sorted((ROOT/'content').glob('articles-*.json')):
        group=json.loads(path.read_text())
        if set(group)&set(articles):raise ValueError('Duplicate article keys')
        articles.update(group)
    return articles

def render_article(key,title,article,related):
    sections=article['sections'];visual=article['visual']
    jump=''.join(f'<a href="#learn-{esc(s["id"])}">{esc(s["heading"])}</a>' for s in sections)
    step_html=''.join(f'<li><span class="flow-number" aria-hidden="true">{i}</span><span class="flow-label">{esc(s["label"])}</span><strong>{esc(s["value"])}</strong><p>{esc(s["detail"])}</p></li>' for i,s in enumerate(visual['steps'],1))
    diagram=f'''<figure class="learning-visual" aria-labelledby="visual-title" aria-describedby="visual-caption"><div class="visual-heading"><span class="visual-symbol" aria-hidden="true">∑</span><div><span class="eyebrow">Worked example · Visual walkthrough</span><h2 id="visual-title">{esc(visual['title'])}</h2></div></div><ol class="infographic-flow">{step_html}</ol><figcaption id="visual-caption">{esc(visual['caption'])}</figcaption></figure>'''
    boxes=[]
    for i,s in enumerate(sections,1):
        ps=''.join(f'<p>{esc(p)}</p>' for p in s.get('paragraphs',[]))
        bullets='<ul>'+''.join(f'<li>{esc(p)}</li>' for p in s['bullets'])+'</ul>' if s.get('bullets') else ''
        anchor='<span id="formula" class="anchor-target"></span>' if s['id']=='formula' else ''
        boxes.append(f'<section id="learn-{esc(s["id"])}" class="learning-box box-{esc(s["id"])}">{anchor}<div class="box-heading"><span class="box-number" aria-hidden="true">{i:02}</span><h2>{esc(s["heading"])}</h2></div>{ps}{bullets}</section>')
    faqs=''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in article['faqs'])
    body=diagram+'<div class="reading-grid">'+''.join(boxes)+'</div><section class="learning-faq"><span class="eyebrow">Quick answers</span><h2>Frequently asked questions</h2>'+faqs+'</section>'
    # Count actual article text, including diagram labels and FAQ answers, not navigation/UI.
    plain=html.unescape(re.sub('<[^>]+>',' ',body));count=word_count(plain)
    if not 1100<=count<=1300:raise ValueError(f'{key}: rendered article has {count} words; required 1100–1300')
    mins=math.ceil(count/220)
    return f'''<div class="learning-hub"><header class="learning-intro"><div><span class="eyebrow">Understand the result</span><h2>Your guide to using this calculator</h2></div><span class="reading-time">{mins} min read · Examples &amp; explanations</span></header><nav class="learning-nav" aria-label="On this page"><span>Jump to a topic</span><div>{jump}<a href="#learning-faq">FAQs</a></div></nav><article class="learning-article" aria-label="{esc(title)} guide" data-article-key="{esc(key)}" data-word-count="{count}">{body.replace('class="learning-faq"','class="learning-faq" id="learning-faq"')}</article><aside class="next-tools"><h2>Continue your plan</h2><div class="related">{related}</div><p><a href="/methodology/">How our calculations work</a> · <a href="/guides/">Explore the study guides</a> · <a href="#main">Back to calculator ↑</a></p></aside></div>''',count
