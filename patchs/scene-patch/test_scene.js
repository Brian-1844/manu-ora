const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const ctx=await b.newContext({viewport:{width:390,height:800},deviceScaleFactor:2});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
await p.addInitScript(()=>{const S=(k,v)=>localStorage.setItem('manuora.'+k,JSON.stringify(v));if(!localStorage.getItem('manuora.welcomed')){S('welcomed',true);localStorage.setItem('manuora.v','3');S('bedHour',0);S('place','vai');S('cfg',{name:'Vini',body:'#2E86DE',belly:'#F6F1E7',tattoo:'none',animal:'manu',night:'off',tiare:true});}window.fetch=async()=>({ok:true,json:async()=>null});});
await p.goto('file:///tmp/claude-0/v91s.html');await p.waitForTimeout(1800);
const clean=()=>p.evaluate(()=>{try{closeSheet()}catch(e){};if(RING.open){closeRing();release();}bubbleEl.classList.remove('show');const t=$('#toast');if(t)t.classList.remove('show');});
await clean();await p.waitForTimeout(600);await p.screenshot({path:'/home/claude/work/sc_vai0.png'});
console.log('sig0',await p.evaluate(()=>[sceneSig('vai'),sceneSig('tai')]));
await p.evaluate(()=>{store.set('eelDays',['a','b','c','d','e','f']);store.set('hikeDone',['grand','emo','lien']);renderPlace();});await p.waitForTimeout(2500);await clean();await p.waitForTimeout(400);await p.screenshot({path:'/home/claude/work/sc_vai1.png'});
await p.evaluate(()=>{setPlace('tai');});await p.waitForTimeout(500);await clean();await p.screenshot({path:'/home/claude/work/sc_tai0.png'});
await p.evaluate(()=>{store.set('surfDays',['a','b','c','d','e','f','g']);renderPlace();});
let best=0;for(let i=0;i<8;i++){await p.waitForTimeout(1100);await clean();await p.screenshot({path:`/home/claude/work/sc_tai1_${i}.png`});}
console.log('card',await p.evaluate(()=>{openPlace();const c=[...sheetInner.querySelectorAll('.card.flat')].find(x=>x.textContent.includes('grandit'));return c?c.innerText.slice(0,260):null;}));
await p.evaluate(()=>{setPlace('vai');openEels();});await p.waitForTimeout(300);await p.evaluate(()=>{const g=$('#eelGo');if(g)g.click();});await p.waitForTimeout(300);
const hb=await p.$('#eelHold');if(hb){const box=await hb.boundingBox();await p.mouse.move(box.x+box.width/2,box.y+box.height/2);await p.mouse.down();await p.waitForTimeout(9000);await p.screenshot({path:'/home/claude/work/sc_eel.png'});await p.mouse.up();}
console.log('errs',p.errs);await b.close();})();
