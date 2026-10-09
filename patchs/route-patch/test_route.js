// node test_route.js [fichier] — la route (vélo, scooter) et la soirée ; navigateur sans écran.
const {chromium}=require('playwright');const FILE=process.argv[2]||'/tmp/claude-0/v91j.html',O='/home/claude/work/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});const p=await b.newPage({viewport:{width:390,height:800}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.addInitScript(()=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.place',JSON.stringify('oire'));localStorage.setItem('manuora.cfg',JSON.stringify({name:'Vini',body:'#2F80D8',belly:'#F6F1E7',night:'off'}));});
await p.goto('file://'+FILE);await p.waitForTimeout(1500);const clear=()=>p.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');});await clear();
console.log('dock ville',await p.evaluate(()=>[...document.querySelectorAll('#qDock [data-a]')].map(x=>x.textContent).join('/')));
await p.evaluate(()=>openPlace());console.log('bouton',await p.evaluate(()=>!!$('#plRoute')));await p.evaluate(()=>$('#plRoute').click());await p.screenshot({path:O+'rt0.png'});
for(const v of ['s','b']){ await p.evaluate(v=>{openRoute();sheetInner.querySelector('[data-v="'+v+'"]').click();},v); const ids=await p.evaluate(()=>RTS.list.map(x=>x.id).join(','));
  for(let i=0;i<5;i++){ if(i===0) await p.screenshot({path:O+'rt_'+v+'_q.png'}); const good=i!==2; if(i===4 && v==='b'){ await p.waitForTimeout(9300); } else await p.evaluate(good=>{const sc=RTS.list[RTS.i];const k=sc.o.findIndex(o=>o[1]===(good?1:0));sheetInner.querySelector('#rtO [data-v="'+k+'"]').click();},good); await p.waitForTimeout(1300); if(i<2) await p.screenshot({path:O+'rt_'+v+'_a'+i+'.png'}); await p.evaluate(()=>$('#rtNext').click()); }
  console.log(v,ids,await p.evaluate(()=>sheetInner.querySelector('h2').textContent)); await p.screenshot({path:O+'rt_'+v+'_end.png'}); }
await p.evaluate(()=>$('#rtEnd').click());await p.waitForTimeout(300);console.log('fin',await p.evaluate(()=>[$('#sheet').hidden,bubbleEl.textContent.slice(0,40),feathers]));await clear();
// soirée
await p.evaluate(()=>setPlace('po'));await p.waitForTimeout(400);console.log('soirée',await p.evaluate(()=>[curPlace,$('#quiet').className,[...document.querySelectorAll('#qDock>button')].map(x=>x.textContent).join('/')]));await p.screenshot({path:O+'po_scene.png'});
await p.evaluate(()=>openSoiree());await p.screenshot({path:O+'po0.png'});await p.evaluate(()=>$('#poGo').click());
for(let i=0;i<5;i++){ await p.evaluate(i=>{const sc=SOIRS.list[SOIRS.i];const k=sc.o.findIndex(o=>o[1]===(i===1?0:1));sheetInner.querySelector('#poO [data-v="'+k+'"]').click();},i); await p.waitForTimeout(150); if(i<2) await p.screenshot({path:O+'po_a'+i+'.png'}); await p.evaluate(()=>$('#poNext').click()); }
console.log('soirée fin',await p.evaluate(()=>[sheetInner.querySelector('h2').textContent,SOIRS.list.map(x=>x.id).join(','),SOIRS.ok]));await p.screenshot({path:O+'po_end.png'});
await p.evaluate(()=>$('#poHelp').click());await p.waitForTimeout(300);console.log('aide ouverte',await p.evaluate(()=>!$('#crisis').hidden));
console.log('errs',errs);await b.close();})();
