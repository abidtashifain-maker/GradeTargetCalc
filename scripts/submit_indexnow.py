"""Notify IndexNow after a successful Pages deployment; no account credentials needed."""
from pathlib import Path
import json,os,re,subprocess,time,urllib.request,urllib.error,urllib.parse,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
HOST='gradetargetcalc.com';BASE='https://'+HOST
ENDPOINT='https://api.indexnow.org/indexnow'
def sitemap_urls(path):
 ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
 urls=[e.text for e in ET.parse(path).findall('s:url/s:loc',ns)]
 if not urls or len(urls)!=len(set(urls)):raise ValueError('Empty or duplicate sitemap URLs')
 for u in urls:
  p=urllib.parse.urlsplit(u)
  if p.scheme!='https' or p.netloc!=HOST or p.query or p.fragment:raise ValueError('Only canonical HTTPS site URLs may be submitted')
 return urls

def changed_urls(paths):
 result=[]
 for path in paths:
  if path=='dist/index.html':result.append(BASE+'/')
  elif path.startswith('dist/') and path.endswith('/index.html'):
   slug=path[len('dist/'):-len('/index.html')]
   if not slug or '..' in slug.split('/') or slug=='404':continue
   result.append(BASE+'/'+slug+'/')
 return list(dict.fromkeys(result))

def select_urls(all_urls,paths,key_changed=False,event='push'):
 if key_changed or event=='workflow_dispatch':return all_urls
 return changed_urls(paths)

def main():
 config=json.loads((ROOT/'site-config.json').read_text());key=config.get('indexnow_key','')
 if not re.fullmatch('[a-f0-9]{32}',key):raise ValueError('Configure a valid32-character IndexNow verification key')
 all_urls=sitemap_urls(ROOT/'dist/sitemap.xml')
 diff=subprocess.run(['git','diff','--name-only','HEAD^','HEAD'],cwd=ROOT,text=True,capture_output=True,check=True).stdout.splitlines()
 bootstrap=f'dist/{key}.txt' in diff
 urls=select_urls(all_urls,diff,bootstrap,os.environ.get('GITHUB_EVENT_NAME','push'))
 if not urls:print('IndexNow: no changed public HTML URLs; nothing submitted.');return
 if len(urls)>10000:raise ValueError('IndexNow batch limit exceeded')
 location=BASE+'/'+key+'.txt'
 for attempt in range(6):
  try:
   with urllib.request.urlopen(location,timeout=20) as r:body=r.read().decode('utf-8').strip()
   if body!=key:raise ValueError('Published verification file content mismatch')
   break
  except (urllib.error.URLError,ValueError):
   if attempt==5:raise
   time.sleep(min(2**(attempt+1),30))
 print('IndexNow: live HTTPS verification file checked.')
 payload=json.dumps({'host':HOST,'key':key,'keyLocation':location,'urlList':urls}).encode('utf-8')
 request=urllib.request.Request(ENDPOINT,data=payload,headers={'Content-Type':'application/json; charset=utf-8','User-Agent':'GradeTargetCalc-IndexNow/1.0'},method='POST')
 with urllib.request.urlopen(request,timeout=45) as response:status=response.status
 if status not in (200,202):raise RuntimeError('Unexpected IndexNow response status: '+str(status))
 outcome='submitted successfully' if status==200 else 'accepted; key validation pending'
 print(f'IndexNow HTTP {status}: {len(urls)} URLs {outcome}. This does not confirm indexing.')
 summary=os.environ.get('GITHUB_STEP_SUMMARY')
 if summary:
  with open(summary,'a') as f:f.write(f'## IndexNow\n\nLive key file verified. **HTTP {status}**: **{len(urls)} URLs** {outcome}. Search-engine indexing is a separate process.\n')
if __name__=='__main__':main()
