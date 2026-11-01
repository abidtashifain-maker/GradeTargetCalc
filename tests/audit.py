from pathlib import Path
from html.parser import HTMLParser
import json,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]/'dist'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h1=0;self.title=0;self.desc=[];self.canonical=[];self.jsons=[];self.injson=False;self.ids=[];self.scripts=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if 'id' in d:self.ids.append(d['id'])
  if t=='a':self.links.append(d.get('href',''))
  if t=='h1':self.h1+=1
  if t=='title':self.title+=1
  if t=='meta' and d.get('name')=='description':self.desc.append(d['content'])
  if t=='link' and d.get('rel')=='canonical':self.canonical.append(d['href'])
  if t in ['script','link'] and (d.get('src') or d.get('href','').startswith('/assets/')):self.scripts.append(d.get('src') or d.get('href'))
  if t=='script' and d.get('type')=='application/ld+json':self.injson=True
 def handle_data(self,d):
  if self.injson:self.jsons.append(json.loads(d))
 def handle_endtag(self,t):
  if t=='script':self.injson=False
seen=set();descs=set();pages=list(ROOT.rglob('*.html'))
for page in pages:
 p=Parser();p.feed(page.read_text());assert p.h1==1,(page,p.h1);assert p.title==1;assert len(p.desc)==1;assert len(p.canonical)==1;assert len(set(p.ids))==len(p.ids),(page,'duplicate ids');assert p.jsons
 assert p.desc[0] not in descs,(page,'duplicate description');descs.add(p.desc[0]);assert p.canonical[0] not in seen;seen.add(p.canonical[0])
 for href in p.links+p.scripts:
  if href.startswith('/'):
   path=href.split('#')[0];dest=ROOT/path.lstrip('/');dest=dest/'index.html' if dest.is_dir() else dest
   assert dest.is_file(),(page,href,'broken local target')
   if '#' in href:
    anchor=href.split('#')[1];assert f'id="{anchor}"' in dest.read_text(),(page,href,'missing anchor')
 for text in ['G-XXXXXXXX','ca-pub-000','TODO','Lorem ipsum']:assert text not in page.read_text()
ET.parse(ROOT/'sitemap.xml')
assert (ROOT/'CNAME').read_text().strip()=='gradetargetcalc.com'
assert (ROOT/'.nojekyll').exists()
assert sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file())<1500000
print(f'Static audit passed: {len(pages)} HTML pages, valid local links/assets/fragments, unique metadata, JSON-LD, sitemap, CNAME; entire site under 1.5 MB.')

assert len(pages)==41, 'Expected 30 calculator pages, home, guides, policies and 404'
assert sum('data-calculator=' in p.read_text() for p in pages)==31
assert len(ET.parse(ROOT/'sitemap.xml').getroot())==40
assert all(p.stat().st_size<45000 for p in pages), 'Individual page exceeds 45 KB budget'
