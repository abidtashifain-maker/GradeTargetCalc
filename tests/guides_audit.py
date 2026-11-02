from pathlib import Path
from html.parser import HTMLParser
import json,re,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from guides import load_guides
from editorial import word_count
new=load_guides();existing_texts=set()
for f in (ROOT/'content').glob('articles-*.json'):
 for a in json.loads(f.read_text()).values():
  for s in a['sections']:existing_texts.update(s.get('paragraphs',[]))
class P(HTMLParser):
 def __init__(self):super().__init__();self.depth=0;self.in_article=False;self.words=[];self.anchors=0;self.h1=0;self.jsons=[];self.injson=False;self.links=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='article' and a.get('class')=='study-article':self.in_article=True
  if t=='a':
   self.anchors+=1;assert self.anchors==1,'nested anchors';self.links.append(a.get('href',''))
  if t=='h1':self.h1+=1
  if t=='script' and a.get('type')=='application/ld+json':self.injson=True
 def handle_endtag(self,t):
  if t=='a':self.anchors-=1
  if t=='article':self.in_article=False
  if t=='script':self.injson=False
 def handle_data(self,d):
  if self.in_article:self.words.append(d)
  if self.injson:self.jsons.extend(json.loads(d))
slugs=set();counts=[];metadata=set()
for g in new:
 assert g['slug'] not in slugs;slugs.add(g['slug'])
 assert g['description'] not in metadata;metadata.add(g['description'])
 assert g['primary_keyword'] and 3<=len(g['secondary_keywords'])<=5
 assert 6<=len(g['sections'])<=10
 assert len({s['id'] for s in g['sections']})==len(g['sections'])
 assert 3<=len(g['visual']['steps'])<=4 and len(g['faqs'])>=3
 assert 2<=len(g['tool_slugs'])<=3 and g['sources']
 for s in g['sections']:
  for p in s.get('paragraphs',[]):
   assert word_count(p)<=95,(g['slug'],'dense paragraph')
   assert p not in existing_texts,(g['slug'],'duplicate paragraph');existing_texts.add(p)
 for source in g['sources']:assert source['url'].startswith('https://')
 path=ROOT/'dist/guides'/g['slug']/'index.html';p=P();p.feed(path.read_text())
 assert p.h1==1
 count=word_count(' '.join(p.words));assert 750<=count<=1400,(g['slug'],count);counts.append(count)
 schema=next(x for x in p.jsons if x.get('@type')=='Article');assert schema['wordCount']==count
 assert schema['url']==f'https://gradetargetcalc.com/guides/{g["slug"]}/'
 for slug in g['tool_slugs']:assert f'/{slug}/' in p.links
 hub=(ROOT/'dist/guides/index.html').read_text();assert f'/guides/{g["slug"]}/' in hub
 assert any(f'/guides/{g["slug"]}/' in f.read_text() for f in (ROOT/'dist').glob('*/index.html') if f.parent.name!='guides'),('no calculator link to guide',g['slug'])
assert len(list((ROOT/'dist/guides').glob('*/index.html')))==21
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
for u in ET.parse(ROOT/'dist/sitemap.xml').getroot():assert u.find('s:lastmod',ns) is not None
print(f'Study guide audit passed:18 new original guides ({min(counts)}–{max(counts)} words),21 guides total; valid article schema, hub/calculator links and dated sitemap.')
