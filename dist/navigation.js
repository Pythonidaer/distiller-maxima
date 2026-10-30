/* Shared responsive navigation: native disclosures work without JavaScript. */
(()=>{
 'use strict';
 const header=document.querySelector('.site-header'),toggle=document.getElementById('nav-toggle'),links=document.getElementById('site-navigation');
 if(!header||!toggle||!links)return;
 const compact=matchMedia('(max-width:700px)'),hover=matchMedia('(hover:hover) and (pointer:fine)');
 const groups=[...links.querySelectorAll('.nav-group')];
 document.documentElement.classList.add('nav-enhanced');
 function resetGroups(){groups.forEach(g=>{g.open=false;g.classList.toggle('has-current',!!g.querySelector('[aria-current]'));});}
 function setNavigation(open,returnFocus=false){
  const expanded=compact.matches&&open;
  links.classList.toggle('is-open',expanded);toggle.setAttribute('aria-expanded',String(expanded));
  toggle.setAttribute('aria-label',expanded?'Close navigation':'Open navigation');links.inert=compact.matches&&!expanded;
  if(!expanded&&!compact.matches)groups.forEach(g=>g.open=false);
  if(returnFocus&&compact.matches)toggle.focus({preventScroll:true});
 }
 resetGroups();setNavigation(false);
 toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';if(open)resetGroups();setNavigation(open);});
 groups.forEach(group=>{
  group.addEventListener('pointerenter',()=>{if(!compact.matches&&hover.matches){groups.forEach(g=>{if(g!==group)g.open=false;});group.open=true;}});
  group.addEventListener('pointerleave',()=>{if(!compact.matches&&!group.contains(document.activeElement))group.open=false;});
  group.addEventListener('focusout',()=>{requestAnimationFrame(()=>{if(!compact.matches&&!group.contains(document.activeElement))group.open=false;});});
  group.addEventListener('toggle',()=>{if(group.open&&!compact.matches)groups.forEach(g=>{if(g!==group)g.open=false;});});
 });
 links.addEventListener('click',e=>{if(e.target.closest('a'))setNavigation(false,true);});
 document.addEventListener('keydown',e=>{
  if(e.key!=='Escape')return;
  const group=groups.find(g=>g.open&&g.contains(document.activeElement));
  if(group&&!compact.matches){e.preventDefault();group.open=false;group.querySelector('summary').focus();return;}
  if(toggle.getAttribute('aria-expanded')==='true'){e.preventDefault();setNavigation(false,true);}else groups.forEach(g=>g.open=false);
 });
 document.addEventListener('click',e=>{if(!e.target.closest('.site-header'))setNavigation(false);});
 document.addEventListener('focusin',e=>{if(!e.target.closest('.site-header'))setNavigation(false);});
 compact.addEventListener('change',()=>{const focusWasInLinks=links.contains(document.activeElement);resetGroups();setNavigation(false,focusWasInLinks&&compact.matches);});
 const root=document.getElementById('siteShell')||window;
 const hero=document.querySelector('.home-page .hero');
 const update=()=>{
  header.classList.toggle('is-scrolled',(root===window?window.scrollY:root.scrollTop)>8);
  header.classList.toggle('is-past-hero',!!hero&&hero.getBoundingClientRect().top+hero.offsetHeight*.6<=header.getBoundingClientRect().bottom);
 };
 update();root.addEventListener('scroll',update,{passive:true});window.addEventListener('resize',update);
})();
