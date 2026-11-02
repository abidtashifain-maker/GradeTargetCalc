"""Verify the requested article length against the actual rendered HTML."""
from html.parser import HTMLParser
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from editorial import load_articles,word_count
articles=load_articles()
assert len(articles)==30
paragraphs=set()
for key,a in articles.items():
 ids=[s['id'] for s in a['sections']]
 assert len(ids)==len(set(ids)),(key,'duplicate section IDs')
 assert 'formula' in ids,(key,'missing formula')
 assert len(a['sections'])>=7,(key,'insufficient topic coverage')
 assert 3<=len(a['visual']['steps'])<=4
 assert len(a['faqs'])>=4
 for s in a['sections']:
  for p in s.get('paragraphs',[]):
   assert word_count(p)<=95,(key,'paragraph too dense',word_count(p))
   assert p not in paragraphs,(key,'duplicate paragraph')
   paragraphs.add(p)
class ArticleParser(HTMLParser):
 def __init__(self):super().__init__();self.active=False;self.parts=[];self.key=None;self.expected=None;self.ids=[];self.fragments=[];self.visual=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and a.get('href','').startswith('#'):self.fragments.append(a['href'][1:])
  if tag=='article' and 'data-article-key' in a:self.active=True;self.key=a['data-article-key'];self.expected=int(a['data-word-count'])
  if tag=='figure' and a.get('class')=='learning-visual':self.visual=True
 def handle_endtag(self,tag):
  if tag=='article':self.active=False
 def handle_data(self,data):
  if self.active:self.parts.append(data)
counts={}
for page in (ROOT/'dist').rglob('*.html'):
 p=ArticleParser();p.feed(page.read_text())
 for f in p.fragments:assert f in p.ids,(page,f,'broken same-page anchor')
 if p.key:
  words=word_count(' '.join(p.parts));assert 1100<=words<=1300,(p.key,words)
  assert words==p.expected,(p.key,words,p.expected)
  assert p.visual;counts[p.key]=words
assert set(counts)==set(articles)
print(f'Editorial audit passed: 30 original articles; {min(counts.values())}–{max(counts.values())} rendered words each, {sum(counts.values())} total; 30 accessible visual examples, short paragraphs and valid jump links.')
