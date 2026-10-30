import json,re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
root=Path(__file__).resolve().parents[1];dist=root/'dist'
class Page(HTMLParser):
 def __init__(self,s):super().__init__();self.ids=[];self.links=[];self.feed(s)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a':self.links.append(a.get('href',''))
pages={p.name:Page(p.read_text()) for p in dist.glob('*.html')}
for name,p in pages.items():
 assert len(p.ids)==len(set(p.ids)),name
 for href in p.links:
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  target=u.path or name
  if target=='./':target='index.html'
  assert (dist/target).exists(),(name,href)
  if u.fragment:assert u.fragment in pages[target].ids,(name,href)
for n,file,count in [(1,'programming-guide.html',117),(2,'data-ai-guide.html',89)]:
 inv=json.loads((root/'guides/inventory.json').read_text());expected=[a['url'] for a in inv if a['roadmap']==n]
 actual=[u for u in pages[file].links if u.startswith('https://')]
 assert sorted(expected)==sorted(actual) and len(actual)==count
links=json.loads((dist/'guide-links.js').read_text().split(' = ',1)[1].rstrip(';\n'))
for g in links.values():
 for href in [g['url'],*g['topics'].values()]:
  file,anchor=href.split('#');assert anchor in pages[file].ids
print('All 206 source links and 102 guide section targets verified; local page links resolve.')
