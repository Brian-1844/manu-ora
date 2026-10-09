// node test_jardin.js [fichier] — images du coffre, très mûr (×2), première pousse, carte du temps, aube de lʼʻāpetahi.
const {chromium}=require('playwright');const FILE=process.argv[2]||'/tmp/claude-0/v91j.html',O='/home/claude/work/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});const p=await b.newPage({viewport:{width:390,height:800},deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.addInitScript(()=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.cfg',JSON.stringify({name:'Vini',body:'#2F80D8',belly:'#F6F1E7',night:'off'}));});
await p.goto('file://'+FILE);await p.waitForTimeout(1500);const clear=()=>p.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');});await clear();
// première pousse
await p.evaluate(()=>{garden.plots=[null,null,null,null,null,null];garden.got=[];garden.seeds.tiare=2;saveGarden();openGarden();$('#plots [data-plant="0"]').click();});await p.evaluate(()=>$('#plots [data-seed="tiare"]').click());
console.log('première pousse',await p.evaluate(()=>[plotLeft(garden.plots[0]),store.get('firstGrow')]));await p.waitForTimeout(300);
await p.evaluate(()=>{openGarden();$('#plots [data-plant="1"]').click();});await p.evaluate(()=>$('#plots [data-seed="tiare"]').click());console.log('deuxième',await p.evaluate(()=>plotLeft(garden.plots[1])));
// très mûr
await p.evaluate(()=>{const now=Date.now();garden.plots=[{p:'meia',t:now-4*864e5},{p:'anani',t:now-6*864e5},{p:'vi',t:now-6*864e5},{p:'metua',t:now-4*864e5},null,null];saveGarden();openGarden();});
console.log('bouton',await p.evaluate(()=>[...sheetInner.querySelectorAll('[data-vr]')].map(x=>x.dataset.vr+':'+x.textContent).join(' | ')));
await p.evaluate(()=>$('#plots [data-vr="0"]').click());await p.waitForTimeout(100);console.log('attente',await p.evaluate(()=>[vrState(garden.plots[0]),sheetInner.querySelector('#plots .plot').textContent.replace(/\s+/g,' ').slice(0,140)]));
await p.evaluate(()=>{garden.plots[0].slow=Date.now()-2*864e5;garden.plots[1].slow=Date.now()-3*864e5;saveGarden();openGarden();});await p.screenshot({path:O+'jd_plots.png'});
const st0=await p.evaluate(()=>garden.store.meia||0);await p.evaluate(()=>$('#plots [data-keep="0"]').click());console.log('coffre meia',st0,'→',await p.evaluate(()=>garden.store.meia));
const f0=await p.evaluate(()=>feathers);await p.evaluate(()=>{openGarden();$('#plots [data-sell="1"]').click();});console.log('plumes anani ×2',await p.evaluate(f0=>feathers-f0+' (base '+PLANTS.anani.worth+')',f0));
const f1=await p.evaluate(()=>feathers);await p.evaluate(()=>{openGarden();$('#plots [data-sell="2"]').click();});console.log('plumes vi normal',await p.evaluate(f1=>feathers-f1,f1));
await p.evaluate(()=>{openGarden();sheetInner.querySelector('details').open=true;sheetInner.querySelector('details').scrollIntoView();});await p.screenshot({path:O+'jd_temps.png'});console.log('carte',await p.evaluate(()=>sheetInner.querySelector('details').textContent.slice(0,80)));
// coffre : tout
await p.evaluate(()=>{ING.forEach(k=>garden.store[k]=2);Object.keys(ITEMS).forEach(k=>garden.items[k]=1);saveGarden();openGarden();});await p.screenshot({path:O+'jd_seeds.png'});
await p.evaluate(()=>openChest());await p.waitForTimeout(200);await p.screenshot({path:O+'jd_chest1.png'});
console.log('icônes coffre',await p.evaluate(()=>[sheetInner.querySelectorAll('.feather svg.ico').length,ING.length,sheetInner.querySelectorAll('.icoB svg').length,Object.keys(ITEMS).length]));
console.log('sans dessin propre',await p.evaluate(()=>Object.keys(ITEMS).filter(k=>!ICO['i:'+k]&&!ICO[k]).concat(ING.filter(k=>!ICO[k])).concat(Object.keys(PLANTS).filter(k=>!ICO[k])).join(',')||'aucun'));
await p.evaluate(()=>{const c=[...sheetInner.querySelectorAll('.card')].find(x=>/Mes créations/.test(x.textContent));c.scrollIntoView();});await p.screenshot({path:O+'jd_chest2.png'});
await p.evaluate(()=>sheetInner.scrollBy(0,700));await p.screenshot({path:O+'jd_chest3.png'});await p.evaluate(()=>sheetInner.scrollBy(0,700));await p.screenshot({path:O+'jd_chest4.png'});await p.evaluate(()=>sheetInner.scrollBy(0,700));await p.screenshot({path:O+'jd_chest5.png'});
await clear();
// aube
await p.evaluate(()=>{friends.push({code:'CCCC4444',name:'Hina'});});
const mk=()=>p.evaluate(()=>{const days=['2026-10-01','2026-10-02','2026-10-03','2026-10-04','2026-10-05'];const a={},c={};days.forEach(d=>{a[d]=1;c[d]=1;});return {p:'apetahi',by:myCode,care:{[myCode]:a,CCCC4444:c}};});
let d=await mk();await p.evaluate(d=>{apDawnNow=()=>false;renderSharedGarden('CCCC4444',d);},d);console.log('hors aube',await p.evaluate(()=>[!!$('#apDawnGo'),/anciens/.test(sheetInner.textContent)]));
await p.evaluate(d=>{apDawnNow=()=>true;renderSharedGarden('CCCC4444',d);},d);await p.screenshot({path:O+'jd_ap0.png'});console.log('à lʼaube',await p.evaluate(()=>!!$('#apDawnGo')));
await p.evaluate(()=>$('#apDawnGo').click());await p.waitForTimeout(800);await p.screenshot({path:O+'jd_ap1.png'});await p.waitForTimeout(3200);await p.screenshot({path:O+'jd_ap2.png'});
console.log('dessin',await p.evaluate(()=>[garden.items.dessinapetahi,garden.known.includes('dessinapetahi')]));
await p.evaluate(d=>renderSharedGarden('CCCC4444',d),d);console.log('après',await p.evaluate(()=>[!!$('#apDawnGo'),/souvenir/.test(sheetInner.textContent)]));
d.care[await p.evaluate(()=>myCode)]={'2026-10-01':1};await p.evaluate(d=>renderSharedGarden('CCCC4444',d),d);console.log('pas mûre',await p.evaluate(()=>[!!$('#apDawnGo'),/anciens/.test(sheetInner.textContent)]));
console.log('errs',errs);await b.close();})();
