// Guide navigation follows the app's actual scrolling container.
(()=>{
 'use strict';
 const root=document.getElementById('siteShell');
 const article=document.querySelector('.reading-guide article');
 if(!root||!article)return;
 const sections=[...article.querySelectorAll('.guide-section')];
 const headings=[...article.querySelectorAll('.guide-section h2,.guide-topic h3')];
 const wide=matchMedia('(min-width:640px)');
 const aside=document.createElement('aside');aside.className='guide-outline';
 const inner=document.createElement('div');inner.className='outline-sticky';
 const label=document.createElement('h2');label.id='outline-label';label.textContent='On this page';
 const nav=document.createElement('nav');nav.setAttribute('aria-labelledby','outline-label');
 const list=document.createElement('ul');list.className='outline-list';
 const entries=new Map(),groups=new Map();
 function link(heading){const a=document.createElement('a');a.href='#'+heading.id;a.textContent=heading.textContent;entries.set(heading.id,a);return a;}
 sections.forEach(section=>{
  const heading=section.querySelector('h2');const li=document.createElement('li');li.className='outline-group';
  li.append(link(heading));const children=document.createElement('ul');children.className='outline-topics';
  children.id='outline-'+heading.id;
  section.querySelectorAll('h3').forEach(h=>{const item=document.createElement('li');item.append(link(h));children.append(item);});
  li.append(children);list.append(li);groups.set(section,{li,children});
 });
 nav.append(list);inner.append(label,nav);aside.append(inner);article.after(aside);
 document.documentElement.classList.add('guide-outline-ready');
 let active,frame=0,pending=null,settleTimer=0;
 function finishNavigation(){
  if(!pending)return;
  pending=null;clearTimeout(settleTimer);active=undefined;schedule();
 }
 function waitForScrollEnd(){
  if(!pending)return;
  clearTimeout(settleTimer);settleTimer=setTimeout(finishNavigation,180);
 }
 function update(){
  frame=0;
  const top=root.getBoundingClientRect().top+document.querySelector('.site-header').getBoundingClientRect().height+40;
  let current=null;
  for(const h of headings){if(h.getBoundingClientRect().top<=top)current=h;else break;}
  if(root.scrollTop+root.clientHeight>=root.scrollHeight-4)current=headings.at(-1);
  if(pending)current=pending;
  const id=current?.id||null;if(id===active)return;active=id;
  entries.forEach((a,key)=>{if(key===id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});
  const section=current?.closest('.guide-section');
  groups.forEach((group,key)=>{const selected=key===section;group.li.classList.toggle('is-active',selected);group.children.hidden=!selected;});
  const a=entries.get(id);
  if(a&&wide.matches){
   const box=a.getBoundingClientRect(),viewport=nav.getBoundingClientRect();
   if(box.top<viewport.top)nav.scrollTop-=viewport.top-box.top+8;
   else if(box.bottom>viewport.bottom)nav.scrollTop+=box.bottom-viewport.bottom+8;
  }
 }
 function schedule(){if(!frame)frame=requestAnimationFrame(update);}
 function jump(smooth=false){
  if(!location.hash){schedule();return;}
  let id;try{id=decodeURIComponent(location.hash.slice(1));}catch{return;}
  const target=document.getElementById(id);
  if(target)requestAnimationFrame(()=>{target.scrollIntoView({block:'start',behavior:smooth===true&&!matchMedia('(prefers-reduced-motion:reduce)').matches?'smooth':'instant'});schedule();});
 }
 // Handle every outline activation, even when its hash is already selected.
 nav.addEventListener('click',event=>{
  const a=event.target.closest('a[href^="#"]');
  if(!a||event.button!==0||event.metaKey||event.ctrlKey||event.shiftKey||event.altKey)return;
  event.preventDefault();
  pending=document.getElementById(decodeURIComponent(a.hash.slice(1)));
  active=undefined;update();
  // Show the chosen submenu now, without cycling through sections en route.
  clearTimeout(settleTimer);settleTimer=setTimeout(finishNavigation,250);
  if(location.hash!==a.hash)history.pushState(null,'',a.hash);
  jump(true);
 });
 root.addEventListener('scroll',()=>{schedule();waitForScrollEnd();},{passive:true});
 root.addEventListener('scrollend',finishNavigation);
 for(const type of ['wheel','touchstart'])root.addEventListener(type,e=>{if(!aside.contains(e.target))finishNavigation();},{passive:true});
 root.addEventListener('keydown',e=>{if(['ArrowUp','ArrowDown','PageUp','PageDown','Home','End',' '].includes(e.key)&&!aside.contains(e.target))finishNavigation();});
 window.addEventListener('resize',schedule);window.addEventListener('hashchange',jump);
 // Avoid tracking closed groups until the first scroll event.
 update();jump();
})();
