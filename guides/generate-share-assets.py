"""Regenerate static share art with Pillow. Run from the repository root."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parents[1];out=r/'dist/assets';out.mkdir(exist_ok=True)
font=r/'dist/fonts/GrimeSlimeDripping-Regular.ttf'
ui='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
im=Image.new('RGB',(1200,630),'#050505');d=ImageDraw.Draw(im)
d.text((72,54),'Distiller Maxima',font=ImageFont.truetype(ui,30),fill='#f6f7f8')
d.line((72,104,1128,104),fill='#ff36c9',width=3)
f=ImageFont.truetype(str(font),98)
for text,y in [('Know before',155),('you flow',280)]:d.text((68,y),text,font=f,fill='#ff36c9')
f=ImageFont.truetype(ui,26)
d.text((72,476),'200+ freeCodeCamp bookmarks',font=f,fill='#f6f7f8')
d.text((72,520),'Roadmaps and overview reading guides',font=f,fill='#d8dadd')
im.save(out/'share-v1.png',optimize=True)
for size,name in [(32,'favicon-32.png'),(180,'apple-touch-icon.png')]:
 icon=Image.new('RGB',(size,size),'#050505');draw=ImageDraw.Draw(icon);f=ImageFont.truetype(str(font),int(size*.65));box=draw.textbbox((0,0),'D',font=f);draw.text(((size-(box[2]-box[0]))/2-box[0],(size-(box[3]-box[1]))/2-box[1]),'D',font=f,fill='#ff36c9');icon.save(out/name)
