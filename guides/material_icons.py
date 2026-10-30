# Google Material Icons, Apache-2.0. Paths unchanged; wrapper uses currentColor and decorative semantics.
paths={'expand_more':'M16.59 8.59L12 13.17 7.41 8.59 6 10l6 6 6-6z','arrow_forward':'M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z','menu':'M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z','close':'M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'}
def icon(name):return f'<svg class="material-icon icon-{name}" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true" focusable="false"><path d="{paths[name]}"/></svg>'
for p in dist.glob('*.html'):
 s=p.read_text()
 s=re.sub(r'<summary>(.*?)</summary>',lambda m:'<summary>'+re.sub(r'<svg.*?</svg>','',m[1])+icon('expand_more')+'</summary>',s)
 s=s.replace('<span aria-hidden="true">↘</span>',icon('arrow_forward')).replace('<span aria-hidden="true">↗</span>',icon('arrow_forward'))
 s=re.sub(r'(<button id="nav-toggle"[^>]*>).*?(</button>)',lambda m:m[1]+icon('menu')+icon('close')+m[2],s)
 if 'icons.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="icons.css"></head>')
 p.write_text(s)
(dist/'icons.js').write_text("/* Google Material Icons close, Apache-2.0; decorative SVG wrapper adapted. */\n'use strict';\ndocument.querySelectorAll('[data-icon=close]').forEach(el=>{el.innerHTML="+json.dumps(icon('close'))+";});\n")
