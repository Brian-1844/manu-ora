// node test_recomp.js [fichier] — chaque récompense, le feu allumé par tonton puis éteint, la pancarte du pāuma.
const {chromium}=require('playwright');const FILE=process.argv[2]||'/tmp/claude-0/v91j.html',O='/home/claude/work/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});const p=await b.newPage({viewport:{width:390,height:800}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.addInitScript(()=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.place',JSON.stringify('tai'));localStorage.setItem('manuora.cfg',JSON.stringify({name:'Vini',body:'#2F80D8',belly:'#F6F1E7',night:'off'}));});
await p.goto('file://'+FILE);await p.waitForTimeout(1500);
const clear=()=>p.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');});await clear();
const items=()=>p.evaluate(()=>Object.keys(garden.items).filter(k=>garden.items[k]>0&&['foulard','ballon','raquette','paumafara','casque','heipo','pareuheiva'].includes(k)).join(','));
// foot : 3 buts de suite
await p.evaluate(()=>{openSport('f',null);$('#bkGo').click();});for(let i=0;i<3;i++){ await p.waitForFunction(n=>BK.game&&BK.game.s&&BK.game.s.phase==='aim'&&BK.res.length===n&&!BK.ending,i,{timeout:9000}); await p.evaluate(()=>{const s=BK.game.s,W=$('#bkCv').clientWidth,H=$('#bkCv').clientHeight,hw=W*.3,gh=H*.46;const side=s.dive===0?1:-s.dive;BK.game.fire(W/2+side*hw*.85,gh*.8,.5);}); await p.waitForFunction(n=>BK.res.length===n+1,i,{timeout:9000}); }
console.log('foot',await p.evaluate(()=>BK.res.join(',')),await items());await p.evaluate(()=>bkQuit());await clear();
// basket : le 20e panier
await p.evaluate(()=>{store.set('bkBaskets',19);openSport('b',null);$('#bkGo').click();});await p.waitForFunction(()=>BK.game&&BK.game.s,null,{timeout:5000});
await p.evaluate(()=>{for(let vx=250;vx<=700;vx+=20)for(let vy=-950;vy<=-450;vy+=20){const o=BK.game.sim(vx,vy,4.5);if(o.score){BK.game.shoot(vx,vy);return;}}});await p.waitForFunction(()=>BK.res.length===1,null,{timeout:9000});console.log('basket',await p.evaluate(()=>store.get('bkBaskets')),await items());await p.evaluate(()=>bkQuit());await clear();
// ping-pong : réussite au 5e essai
await p.evaluate(()=>{openSport('p',null);$('#bkGo').click();BK.i=5;BK.res=[true,false,true,true];bkAttemptEnd(true,'test');});console.log('pong',await items());await p.evaluate(()=>bkQuit());await clear();
// pāuma : 3 puis 7 jours
await p.evaluate(()=>{store.set('kiteDays',['a','b','c']);closeSheet();});await p.waitForTimeout(800);console.log('pāuma 3 j → graine fara',await p.evaluate(()=>garden.seeds.fara||0));await p.evaluate(()=>{store.set('kiteDays',['a','b','c','d','e','f','g']);closeSheet();});await p.waitForTimeout(800);console.log('pāuma 7 j',await items());await clear();
await p.evaluate(()=>{openKite();});await p.waitForTimeout(300);await p.screenshot({path:O+'rw_kite.png'});await clear();
// route : 5/5 à vélo puis en scooter
for(const v of ['b','s']){ await p.evaluate(v=>{openRoute();sheetInner.querySelector('[data-v="'+v+'"]').click();},v); for(let i=0;i<5;i++){ await p.evaluate(()=>{const sc=RTS.list[RTS.i];const k=sc.o.findIndex(o=>o[1]===1);sheetInner.querySelector('#rtO [data-v="'+k+'"]').click();}); await p.evaluate(()=>$('#rtNext').click()); } console.log('route',v,await p.evaluate(()=>sheetInner.querySelector('h2').textContent),await items()); await clear(); }
// soirée : rejouer jusqu'à avoir vu les 6 situations
for(let r=0;r<8;r++){ await p.evaluate(()=>{openSoiree();$('#poGo').click();}); for(let i=0;i<5;i++){ await p.evaluate(()=>{const sc=SOIRS.list[SOIRS.i];sheetInner.querySelector('#poO [data-v="1"]').click();}); await p.evaluate(()=>$('#poNext').click()); } await clear(); const n=await p.evaluate(()=>store.get('poSeen').length); if(n===6) break; }
console.log('soirée',await p.evaluate(()=>store.get('poSeen').length),await items());await clear();
// Heiva : tonton allume, graine, invité, jus, extinction
await p.evaluate(()=>{TUNES.forEach(t=>{if(!t.duo)t.ok=()=>true;});hvSync();});await p.waitForTimeout(2500);await clear();await p.evaluate(()=>{cfg.night='off';renderNight();setPlace('heiva');openHeiva();});await p.screenshot({path:O+'rw_hv0.png'});console.log('bouton',await p.evaluate(()=>$('#hvLit').textContent));
await p.evaluate(()=>$('#hvLit').click());await p.waitForTimeout(400);console.log('tonton',await p.evaluate(()=>[bubbleEl.textContent.slice(0,80),garden.seeds.tipanie||0,/tonton/.test($('#dayScene').innerHTML)]));await p.evaluate(()=>bubbleEl.classList.remove('show'));await p.screenshot({path:O+'rw_hv1.png'});
await p.evaluate(()=>hvArrive({from:'CCCC4444',name:'Hina'}));console.log('invité',await items());await clear();
for(const j of ['ana','pam','coco','meli']){ await p.evaluate(()=>{openHeiva();$('#hvBar').click();}); await p.evaluate(j=>document.querySelector('#hvJ [data-j="'+j+'"]').click(),j); await p.waitForTimeout(150); } console.log('recette jus',await p.evaluate(()=>[garden.known.includes('jusheiva'),store.get('hvJuices').length]));await clear();
await p.evaluate(()=>{openHeiva();});await p.screenshot({path:O+'rw_hv2.png'});await p.evaluate(()=>$('#hvEnd').click());await p.waitForTimeout(300);console.log('éteint',await p.evaluate(()=>[hvGet().lit,!!hvGet().out,/hv-fl/.test($('#dayScene').innerHTML),bubbleEl.textContent.slice(0,40)]));await clear();
// le lendemain, un feu oublié : on doit l'éteindre avant de rallumer
await p.evaluate(()=>{const h=hvGet();h.lit='2026-01-01';h.out='';store.set('heiva',h);openHeiva();});console.log('feu dʼhier',await p.evaluate(()=>[sheetInner.querySelector('h2').textContent,!!$('#hvOut'),!$('#hvLit')]));await p.screenshot({path:O+'rw_hv3.png'});await p.evaluate(()=>$('#hvOut').click());await p.waitForTimeout(200);await p.evaluate(()=>openHeiva());console.log('ensuite',await p.evaluate(()=>!!$('#hvLit')));await clear();
await p.evaluate(()=>openChest());await p.waitForTimeout(200);await p.screenshot({path:O+'rw_chest.png',fullPage:false});console.log('coffre',await p.evaluate(()=>['Foulard du tupa','Casque du manu','Hei de nuit'].every(t=>sheetInner.textContent.includes(t))));
console.log('errs',errs);await b.close();})();
