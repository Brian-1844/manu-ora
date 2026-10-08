const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const O='/home/claude/work/';const ctx=await b.newContext({viewport:{width:390,height:800},timezoneId:'Pacific/Tahiti'});
const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{if(!localStorage.getItem('manuora.welcomed')){localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');}});
await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1500);
const clear=()=>p.evaluate(()=>{try{closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');cfg.night='off';renderNight();});
await clear();
console.log('départ',await p.evaluate(()=>[JSON.stringify(stonesGot()),!!PLACES.reva,Object.keys(STONE).map(stoneFull).join()]));
await p.evaluate(()=>{const days=n=>Array.from({length:n},(_,i)=>'2026-09-'+String(i+1).padStart(2,'0'));store.set('surfDays',days(10));store.set('eelDays',days(10));store.set('hikeDone',days(6));store.set('placeDays',{oire:days(8),haapii:days(8)});});
console.log('décors complets',await p.evaluate(()=>Object.keys(STONE).map(k=>k+':'+stoneFull(k)).join(' ')));
for(let i=0;i<4;i++){ await clear(); await p.evaluate(()=>stoneTick()); await p.waitForTimeout(300); console.log('pierre',i+1,await p.evaluate(()=>bubbleEl.textContent.slice(0,70))); }
await clear(); await p.evaluate(()=>openPlace()); await p.waitForTimeout(300); console.log('carte pierres',await p.evaluate(()=>sheetInner.querySelectorAll('.stonerow').length)); 
await clear(); await p.evaluate(()=>stoneTick()); await p.waitForTimeout(4600); await p.screenshot({path:O+'sky_portal1.png'}); await p.waitForTimeout(3200); await p.screenshot({path:O+'sky_portal2.png'});
await p.click('.portal'); await p.waitForTimeout(1500); console.log('après passage',await p.evaluate(()=>[curPlace,store.get('portal'),!!document.querySelector('.portal'),bubbleEl.textContent.slice(0,50)]));
await p.evaluate(()=>bubbleEl.classList.remove('show')); await p.screenshot({path:O+'sky_scene.png'});
console.log('dock',await p.evaluate(()=>[...document.querySelectorAll('#qDock>button')].map(x=>x.textContent)));
// nuages : deux tours pour tout connaître
await p.evaluate(()=>{PL={i:0};placeAct()}); await p.waitForTimeout(200); console.log('menu',await p.evaluate(()=>sheetInner.querySelector('h2').textContent));
for(let r=0;r<2;r++){ await p.evaluate(()=>{ if(!$('#rvC')) openReva(); $('#rvC').click(); }); for(let i=0;i<3;i++){ await p.waitForTimeout(150); if(r===0&&i===1) await p.screenshot({path:O+'sky_cloud_q.png'}); await p.evaluate(()=>{const c=RV.list[RV.i];sheetInner.querySelector('[data-v="'+c.ok+'"]').click()}); await p.waitForTimeout(150); if(r===0&&i===1) await p.screenshot({path:O+'sky_cloud_a.png'}); await p.evaluate(()=>$('#rvNext').click()); } await p.waitForTimeout(200); console.log('nuages tour',r+1,await p.evaluate(()=>[store.get('skyC').length,JSON.stringify(revaDone()),feathers])); await p.evaluate(()=>$('#rvEnd').click()); await p.waitForTimeout(200); await clear(); }
// vents
await p.evaluate(()=>{openReva();$('#rvW').click()}); await p.waitForTimeout(200); for(const w of ['maraamu','toerau','maoae','hupe']) await p.click(`.rose [data-w="${w}"]`); await p.screenshot({path:O+'sky_wind.png'});
await p.evaluate(()=>$('#rvIn').click()); await p.waitForTimeout(150); await p.evaluate(()=>sheetInner.querySelector('[data-v="toerau"]').click()); await p.waitForTimeout(200); await p.screenshot({path:O+'sky_wind2.png'});
console.log('vents',await p.evaluate(()=>[JSON.stringify(revaDone()),feathers,!!$('#rvBr')])); await p.evaluate(()=>$('#rvEnd').click()); await p.waitForTimeout(300); await clear(); await p.screenshot({path:O+'sky_scene2.png'});
// rechargement : le lieu reste
await p.reload(); await p.waitForTimeout(1500); console.log('après rechargement',await p.evaluate(()=>[curPlace,!!PLACES.reva,$('#dayScene').innerHTML.length>500]));
console.log('errs',errs); await b.close();})();
