const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const ctx=await b.newContext({viewport:{width:390,height:800},deviceScaleFactor:3});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
await p.addInitScript(()=>{const S=(k,v)=>localStorage.setItem('manuora.'+k,JSON.stringify(v));if(!localStorage.getItem('manuora.welcomed')){S('welcomed',true);localStorage.setItem('manuora.v','3');S('bedHour',0);S('place','oire');S('cfg',{name:'Vini',body:'#2E86DE',belly:'#F6F1E7',tattoo:'none',animal:'manu',night:'off',tiare:true});}window.fetch=async()=>({ok:true,json:async()=>null});});
await p.goto('file:///tmp/claude-0/v91s.html');await p.waitForTimeout(1800);
const clean=()=>p.evaluate(()=>{try{closeSheet()}catch(e){};if(RING.open){closeRing();release();}bubbleEl.classList.remove('show');const t=$('#toast');if(t)t.classList.remove('show');const h=$('#qhint');if(h)h.style.visibility='hidden';});
const vis=()=>p.evaluate(()=>[...document.querySelectorAll('#dayScene .sc-drive')].map(g=>g.getAttribute('display')||'on'));
await clean();console.log('start',await vis());
// freeze vehicles at visible positions for a still picture
const freeze=()=>p.evaluate(()=>{[...document.querySelectorAll('#dayScene .sc-drive')].forEach((g,i)=>{g.style.animation='none';g.style.transform=`translateX(${[40,150,230,20][i%4]}px)`;});});
await freeze();await p.evaluate(()=>bubbleEl.classList.remove('show'));await p.waitForTimeout(400);await p.screenshot({path:'/home/claude/work/v0.png',clip:{x:0,y:575,width:390,height:150}});
await p.evaluate(()=>{store.set('placeDays',{oire:['a','b']});renderPlace();});await p.waitForTimeout(300);console.log('2',await vis());
await p.evaluate(()=>{store.set('placeDays',{oire:['a','b','c','d']});renderPlace();});await p.waitForTimeout(1500);await clean();console.log('4',await vis());
await p.evaluate(()=>{const gs=[...document.querySelectorAll('#dayScene .sc-drive')].filter(g=>g.getAttribute('display')!=='none');gs.forEach((g,i)=>{g.style.animation='none';g.style.transform=`translateX(${[250,20,150][i%3]}px)`;});});
await p.evaluate(()=>{const t=$('#toast');if(t){t.classList.remove('show');t.style.display='none';}bubbleEl.classList.remove('show');});await p.waitForTimeout(400);await p.screenshot({path:'/home/claude/work/v1.png',clip:{x:0,y:575,width:390,height:150}});
console.log('errs',p.errs);await b.close();})();
