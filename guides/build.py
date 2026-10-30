import json,re
from pathlib import Path
from html import escape as e
from collections import OrderedDict
root=Path(__file__).resolve().parents[1];dist=root/'dist'
narr=json.loads((root/'guides/narratives.json').read_text());inventory=json.loads((root/'guides/inventory.json').read_text())
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
nav='''<details class="nav-group"><summary>Roadmaps</summary><div class="nav-submenu"><a href="programming.html">Programming and careers</a><a href="data-ai.html">Data and AI</a></div></details><details class="nav-group"><summary>Guides</summary><div class="nav-submenu"><a href="programming-guide.html">Programming and careers</a><a href="data-ai-guide.html">Data and AI</a></div></details><a href="about.html">About</a>'''
header='''<header class="site-header"><div class="header-inner"><a class="brand" href="./">Distiller Maxima</a><nav id="site-navigation" class="nav-links" aria-label="Main navigation">NAV</nav><button id="nav-toggle" class="nav-toggle" aria-label="Open navigation" aria-expanded="false" aria-controls="site-navigation"><span></span><span></span><span></span></button></div></header>'''
methodology='''<div class="footer-row"><div class="methodology"><details id="methodology"><summary>methodology</summary><div class="methodology-copy"><p>the collection began with 206 bookmarks i saved on oct. 29, 2026. after sending the page titles to Chat-6.1 Sol Light, the titles were matched to source links and grouped by topic. the written resource pages were reviewed and distilled into roadmaps and overview reading guides so i could make sense of the information before diving deeper.</p><p>the approach combines curation, synthesis, plain language, and progressive disclosure. source links remain available for deeper reading. video courses were not watched and tutorial code was not run. the reading order is a suggestion.</p></div><div class="methodology-links"><a href="METHODOLOGY.md">writing and navigation rules (markdown)</a><a href="articles.json">article collection (json)</a></div></details></div><nav class="footer-social" aria-label="Social profiles"><a href="https://github.com/pythonidaer" aria-label="GitHub profile"><span data-social="github"></span></a><a href="https://www.linkedin.com/in/jonamichahammo/" aria-label="LinkedIn profile"><span data-social="linkedin"></span></a></nav></div>'''

lookup={}
for n,title,file,roadmap in [(1,'Programming and careers','programming-guide.html','programming.html'),(2,'Data and AI','data-ai-guide.html','data-ai.html')]:
 groups=OrderedDict()
 for a in inventory:
  if a['roadmap']==n:groups.setdefault(a['group'],OrderedDict()).setdefault(a['topic'],[]).append(a)
 content=[];toc=[]
 for g,topics in groups.items():
  gid=slug(g);lookup[g]={'url':file+'#'+gid,'topics':{}}
  toc.append(f'<li><a href="#{gid}">{e(g)}</a></li>')
  section=[f'<section class="guide-section" aria-labelledby="{gid}"><h2 id="{gid}">{e(g)}</h2>']
  for t,articles in topics.items():
   tid=slug(g+' '+t);lookup[g]['topics'][t]=file+'#'+tid
   section.append(f'<section class="guide-topic" aria-labelledby="{tid}"><h3 id="{tid}">{e(t)}</h3>')
   section.extend('<p>'+e(p)+'</p>' for p in narr[g+'|'+t].split('\n\n'))
   section.append('<h4>Reading in this section</h4><ul class="guide-sources">')
   for a in articles:
    label='Visual style guide' if a['id']==205 else a['title'].replace('Al Assistants','AI Assistants')
    section.append(f'<li><a href="{e(a["url"],quote=True)}">{e(label)}</a></li>')
   section.append('</ul></section>')
  section.append('</section>');content.extend(section)
 currentnav=nav.replace(f'href="{file}"',f'href="{file}" aria-current="page"')
 page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>TITLE reading guide | Distiller Maxima</title><meta name="description" content="A friendly guide to what to read, why it matters, and what to try across the TITLE roadmap."><link rel="stylesheet" href="roadmap.css"><link rel="stylesheet" href="navigation.css"><link rel="stylesheet" href="guides.css"><link rel="stylesheet" href="methodology.css"></head><body class="guide-page"><div id="siteShell" class="site-shell"><a class="skip" href="#main">Skip to content</a>HEADER<main id="main" class="reading-guide"><article><header class="guide-intro"><h1>TITLE reading guide</h1><p class="guide-lead">Choose something you want to understand or make. Here’s what each part of the reading can offer you, where to begin, and a few small ways to try it for yourself.</p><p>You can read one topic at a time. The linked articles are collected beneath each discussion, so it’s easy to return to the original explanation.</p><details class="guide-contents"><summary>Jump to a section</summary><nav aria-label="Guide sections"><ul>TOC</ul></nav></details></header>CONTENT</article><footer>METHODOLOGY</footer></main></div><script src="navigation.js"></script><script src="guide-navigation.js"></script></body></html>'''
 for k,v in [('TITLE',e(title)),('HEADER',header.replace('NAV',currentnav)),('ROADMAP',roadmap),('TOC',''.join(toc)),('CONTENT',''.join(content)),('METHODOLOGY',methodology)]:page=page.replace(k,v)
 (dist/file).write_text(page)
(dist/'guide-links.js').write_text('const readingGuideLinks = '+json.dumps(lookup,ensure_ascii=False)+';\n')
for file in ['programming.html','data-ai.html']:
 p=dist/file;s=p.read_text();s=re.sub(r'<p class="roadmap-guide">.*?</p>','',s);s=re.sub(r'(<nav id="site-navigation"[^>]*>).*?(</nav>)',lambda m:m[1]+nav.replace(f'href="{"programming.html" if file=="programming.html" else file}"',f'href="{"programming.html" if file=="programming.html" else file}" aria-current="page"')+m[2],s)
 guide='programming-guide.html' if file=='programming.html' else 'data-ai-guide.html'
 if 'guide-links.js' not in s:s=s.replace('<script src="app.js">','<script src="guide-links.js"></script><script src="app.js">')
 p.write_text(s)
print('Built two guides and links for',len(lookup),'groups and',sum(len(g['topics']) for g in lookup.values()),'topics')

# Keep methodology consistent across the roadmap and standalone about templates.
for file in ['programming.html','data-ai.html']:
 p=dist/file;s=p.read_text()
 s=re.sub(r'<footer>.*?</footer>','<footer><p>The order is a suggested reading sequence. Each topic can be explored independently.</p>'+methodology+'</footer>',s)
 if 'methodology.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="methodology.css"></head>')
 p.write_text(s)
(dist/'METHODOLOGY.md').write_text((root/'METHODOLOGY.md').read_text())

# Landing template shares the same navigation and methodology content.
home=(root/'guides/home.html').read_text().replace('HEADER',header.replace('NAV',nav)).replace('METHODOLOGY',methodology)
(dist/'index.html').write_text(home)

about=(root/'guides/about.html').read_text().replace('HEADER',header.replace('NAV',nav.replace('href="about.html"','href="about.html" aria-current="page"'))).replace('METHODOLOGY</footer>',methodology+'</footer>')
(dist/'about.html').write_text(about)
# Publish a clean collection schema used to connect resources and guide topics.
(dist/'articles.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
style=(root/'guides/style-guide.html').read_text().replace('HEADER',header.replace('NAV',nav)).replace('METHODOLOGY</footer>',methodology+'</footer>')
(dist/'style-guide.html').write_text(style)
exec((root/'guides/material_icons.py').read_text())

# Metadata lives in delivered HTML, not client-side JavaScript.
exec(compile((root/'guides/metadata.py').read_text(),str(root/'guides/metadata.py'),'exec'))
