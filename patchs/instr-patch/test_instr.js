// node test_instr.js [fichier] — fabriquer, décorer, jouer : la pousse avance pour la bonne famille seulement.
const {chromium}=require('playwright');const FILE=process.argv[2]||'/tmp/claude-0/v91j.html',O='/home/claude/work/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});const p=await b.newPage({viewport:{width:390,height:800}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.addInitScript(()=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');});
await p.goto('file://'+FILE);await p.waitForTimeout(1500);await p.evaluate(()=>{try{closeRing()}catch(e){};closeSheet();bubbleEl.classList.remove('show');});
await p.evaluate(()=>openGarden());console.log('carte atelier',await p.evaluate(()=>!!$('#insOpen')));await p.evaluate(()=>$('#insOpen').click());await p.screenshot({path:O+'ins0.png'});
await p.evaluate(()=>sheetInner.querySelector('[data-make="toere"]').click());console.log('sans bois',await p.evaluate(()=>[!insGet().toere]));
await p.evaluate(()=>{garden.store.tou=4;garden.store.uru=4;garden.store.haari=2;garden.store.poe=1;feathers=40;store.set('feathers',40);saveGarden();openInstr();});
for(const id of ['uke','toere','pahu']){ await p.evaluate(id=>sheetInner.querySelector('[data-make="'+id+'"]').click(),id); await p.evaluate(()=>$('#insBack').click()); }
console.log('fabriqués',await p.evaluate(()=>[Object.keys(insGet()).join(),garden.store.tou,garden.store.uru,garden.store.haari,feathers]));await p.screenshot({path:O+'ins1.png'});
await p.evaluate(()=>sheetInner.querySelector('[data-fin="toere"]').click());await p.evaluate(()=>sheetInner.querySelector('[data-f="nacre"]').click());console.log('nacré',await p.evaluate(()=>[insGet().toere.fin,garden.store.poe]));await p.screenshot({path:O+'ins2.png'});
// des plots : un arbre (tou), une fleur (tiare), un fruit (meia)
const before=await p.evaluate(()=>{const n=Date.now();garden.plots[0]={p:'tou',t:n};garden.plots[1]={p:'tiare',t:n};garden.plots[2]={p:'meia',t:n};saveGarden();return garden.plots.slice(0,3).map(x=>x.t);});
await p.evaluate(()=>{openInstr();sheetInner.querySelector('[data-play="toere"]').click();});await p.waitForTimeout(300);await p.screenshot({path:O+'ins3.png'});
const after=await p.evaluate(()=>garden.plots.slice(0,3).map(x=>x.t));console.log('tōʻere nacré : avance (h) tou/tiare/meia',before.map((t,i)=>Math.round((t-after[i])/36e5)));
await p.evaluate(()=>{openInstr();});console.log('une fois par jour',await p.evaluate(()=>sheetInner.querySelector('[data-play="toere"]').disabled));
console.log('pahu bloqué le même jour',await p.evaluate(()=>sheetInner.querySelector('[data-play="pahu"]').disabled));await p.evaluate(()=>{const O=insGet();O.toere.day='2026-01-01';store.set('instr',O);openInstr();sheetInner.querySelector('[data-play="pahu"]').click();});const a2=await p.evaluate(()=>garden.plots.slice(0,3).map(x=>x.t));console.log('lendemain, pahu naturel : meia',Math.round((after[2]-a2[2])/36e5),'h');
console.log('errs',errs);await b.close();})();
