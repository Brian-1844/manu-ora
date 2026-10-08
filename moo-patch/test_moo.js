const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const p=await b.newPage({viewport:{width:900,height:760}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');});
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1200);
await p.evaluate(()=>{try{closeRing()}catch(e){};closeSheet();});
console.log('verrouillé au départ',await p.evaluate(()=>!has('an:moo')));
// 4 jours de calme : pas encore ; 5e : débloqué
await p.evaluate(()=>{store.set('calmDays',['2026-10-01','2026-10-02','2026-10-03','2026-10-04']);mooTick();});
console.log('après 4 jours',await p.evaluate(()=>has('an:moo')));
await p.evaluate(()=>{store.set('calmDay',dayKey(Date.now()));mooTick();});
console.log('après 5 jours',await p.evaluate(()=>[has('an:moo'),mooDays().length]));
await p.waitForTimeout(3500);console.log('message',await p.evaluate(()=>bubbleEl.textContent.slice(0,60)));
// choix + trait
await p.evaluate(()=>{bubbleEl.classList.remove('show');cfg.animal='moo';saveCfg();renderBird();});
console.log('look',await p.evaluate(()=>myLook().animal));
// tortue : la carapace brille après un souffle
await p.evaluate(()=>{cfg.animal='honu';store.set('shine',null);closeBreath(true);});
console.log('honu brille',await p.evaluate(()=>birdEl.classList.contains('shiny')));
// planche de croissance
await p.evaluate(()=>{closeSheet();const d=document.createElement('div');d.id='pl';d.style.cssText='position:fixed;inset:0;z-index:99999;background:#EAF4F3;display:grid;grid-template-columns:repeat(6,1fr);gap:4px;padding:10px;align-content:start';
 const mk=(an,g,x)=>'<div style="background:#fff;border-radius:12px;padding:4px;text-align:center;font:600 12px sans-serif;color:#16303B">'+birdSVG(Object.assign({},cfg,{animal:an,g,nuit:false,season:false},x||{}),an+g+(x?'x':''))+an+' '+g+'</div>';
 let h='';for(const an of ['moo','honu','manu'])for(let g=1;g<=6;g++)h+=mk(an,g);
 h+=mk('moo',4,{body:'#3B8C58',papale:true,poe:true})+mk('moo',6,{body:'#E4583F',tiare:true,tattoo:'niho'})+mk('moo',5,{body:'#F2C94C',hei:true,pareu:true})+mk('honu',6,{body:'#3B8C58',tattoo:'orama'})+mk('moo',4,{nuit:true})+mk('moo',3,{titia:true});
 d.innerHTML=h;document.body.appendChild(d);});
await p.screenshot({path:'/home/claude/work/moo_sheet.png'});
console.log('errs',errs);await b.close()})();
