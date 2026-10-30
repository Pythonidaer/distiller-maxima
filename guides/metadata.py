"""Static social metadata. Production URLs are the default for GitHub Pages builds."""
from pathlib import Path
from html import escape
import re,os
root=Path(__file__).resolve().parents[1];dist=root/'dist'
production='https://pythonidaer.github.io/distiller-maxima/'
origin=os.environ.get('SITE_ORIGIN',production).rstrip('/')+'/'
descriptions={
 'index.html':'200+ freeCodeCamp bookmarks distilled into roadmaps and overview reading guides. Choose what to explore before settling into focused reading.',
 'programming.html':'Explore a topic roadmap through programming languages, web development, architecture, testing, and careers, with links to the original resources.',
 'data-ai.html':'Explore a topic roadmap through data engineering, machine learning, AI applications, and automation, with links to the original resources.',
 'programming-guide.html':'An overview of the programming and careers collection, explaining what to read, why it matters, where to begin, and something small to try.',
 'data-ai-guide.html':'An overview of the data and AI collection, connecting models, data, tools, and agent applications with suggested reading and practical starting points.',
 'about.html':'How a collection of more than 200 freeCodeCamp bookmarks became Distiller Maxima, with its purpose, process, source mapping, and educational design inspiration.',
 'style-guide.html':'The typography roles, font families, responsive sizes, spacing scale, and semantic color palette used in Distiller Maxima.'}
for file,description in descriptions.items():
 p=dist/file;s=p.read_text();title=re.search(r'<title>(.*?)</title>',s).group(1)
 s=re.sub(r'<!-- social-metadata:start -->.*?<!-- social-metadata:end -->','',s,flags=re.S)
 s=re.sub(r'<meta name="description"[^>]*>','',s)
 s=re.sub(r'<link rel="(?:canonical|icon|apple-touch-icon)"[^>]*>','',s)
 page='' if file=='index.html' else file
 canonical=production+page
 tags=['<!-- social-metadata:start -->',f'<meta name="description" content="{escape(description,quote=True)}">',f'<link rel="canonical" href="{canonical}">']
 values={'og:title':title,'og:description':description,'og:type':'website','og:url':canonical,'og:site_name':'Distiller Maxima','og:locale':'en_US','og:image':origin+'assets/share-v1.png','og:image:type':'image/png','og:image:width':'1200','og:image:height':'630','og:image:alt':'Distiller Maxima. Know before you flow, in neon pink dripping lettering on black. 200+ freeCodeCamp bookmarks, roadmaps and overview reading guides.'}
 tags += [f'<meta property="{k}" content="{escape(v,quote=True)}">' for k,v in values.items()]
 twitter={'twitter:card':'summary_large_image','twitter:title':title,'twitter:description':description,'twitter:image':values['og:image'],'twitter:image:alt':values['og:image:alt']}
 tags += [f'<meta name="{k}" content="{escape(v,quote=True)}">' for k,v in twitter.items()]
 tags += [f'<link rel="icon" type="image/png" sizes="32x32" href="{origin}assets/favicon-32.png">',f'<link rel="apple-touch-icon" sizes="180x180" href="{origin}assets/apple-touch-icon.png">','<!-- social-metadata:end -->']
 s=s.replace('</head>','\n'.join(tags)+'</head>');p.write_text(s)
