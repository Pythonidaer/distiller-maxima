# Google Material Icons, Apache-2.0. Paths unchanged; wrapper uses currentColor and decorative semantics.
paths={'expand_more':'M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z','arrow_forward':'M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z','menu':'M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z','close':'M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'}
def icon(name):return f'<svg class="material-icon icon-{name}" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true" focusable="false"><path d="{paths[name]}"/></svg>'
# Social brand icons from @mui/icons-material 7.3.4 (MIT).
paths.update({'github': 'M12 1.27a11 11 0 00-3.48 21.46c.55.09.73-.28.73-.55v-1.84c-3.03.64-3.67-1.46-3.67-1.46-.55-1.29-1.28-1.65-1.28-1.65-.92-.65.1-.65.1-.65 1.1 0 1.73 1.1 1.73 1.1.92 1.65 2.57 1.2 3.21.92a2 2 0 01.64-1.47c-2.47-.27-5.04-1.19-5.04-5.5 0-1.1.46-2.1 1.2-2.84a3.76 3.76 0 010-2.93s.91-.28 3.11 1.1c1.8-.49 3.7-.49 5.5 0 2.1-1.38 3.02-1.1 3.02-1.1a3.76 3.76 0 010 2.93c.83.74 1.2 1.74 1.2 2.94 0 4.21-2.57 5.13-5.04 5.4.45.37.82.92.82 2.02v3.03c0 .27.1.64.73.55A11 11 0 0012 1.27', 'linkedin': 'M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.32 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.79M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z'})

for p in dist.glob('*.html'):
 s=p.read_text()
 for name in ['github','linkedin']:s=s.replace('<span data-social="'+name+'"></span>',icon(name))
 s=re.sub(r'<summary>(.*?)</summary>',lambda m:'<summary>'+re.sub(r'<svg.*?</svg>','',m[1])+icon('expand_more')+'</summary>',s)
 s=s.replace('<span aria-hidden="true">↘</span>',icon('arrow_forward')).replace('<span aria-hidden="true">↗</span>',icon('arrow_forward'))
 s=re.sub(r'(<button id="nav-toggle"[^>]*>).*?(</button>)',lambda m:m[1]+icon('menu')+icon('close')+m[2],s)
 if 'typography.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="typography.css"></head>')
 if 'icons.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="icons.css"></head>')
 s=re.sub(r'<link rel="stylesheet" href="design-system.css">','',s)
 s=s.replace('</head>','<link rel="stylesheet" href="design-system.css"></head>')
 p.write_text(s)
(dist/'icons.js').write_text("/* Google Material Icons close, Apache-2.0; decorative SVG wrapper adapted. */\n'use strict';\ndocument.querySelectorAll('[data-icon=close]').forEach(el=>{el.innerHTML="+json.dumps(icon('close'))+";});\n")
