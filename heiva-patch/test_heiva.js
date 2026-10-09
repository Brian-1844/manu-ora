// node test_heiva.js [fichier avec SYNC_URL factice] — pāuma + Heiva à deux (Teva invite Hina), navigateur sans écran, base simulée.
const {chromium}=require('playwright');
const FILE=process.argv[2]||'/tmp/claude-0/v91j.html', O='/home/claude/work/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const db={};const mk=async(code,name)=>{const ctx=await b.newContext({viewport:{width:390,height:800},timezoneId:'Pacific/Tahiti'});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
 await p.exposeFunction('dbOp',(method,path,body)=>{const ks=path.split('/').filter(Boolean);let o=db;if(method==='GET'){for(const k of ks){o=o&&o[k];}return o===undefined?null:JSON.parse(JSON.stringify(o));}
   const last=ks.pop();for(const k of ks){o[k]=o[k]||{};o=o[k];}const v=body?JSON.parse(body):null;if(method==='PUT')o[last]=v;else if(method==='PATCH'){o[last]=o[last]||{};for(const k in v){if(v[k]===null)delete o[last][k];else o[last][k]=v[k];}}else if(method==='DELETE')delete o[last];return {};});
 await p.addInitScript(([code,name,body])=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.code',JSON.stringify(code));localStorage.setItem('manuora.share',JSON.stringify({on:true,name}));localStorage.setItem('manuora.place',JSON.stringify('tai'));localStorage.setItem('manuora.cfg',JSON.stringify({name:name==='Teva'?'Vini':'Moa',body,belly:'#F6F1E7',night:'off'}));
   window.fetch=async(u,o)=>{o=o||{};const path=String(u).replace(/^https?:\/\/[^/]+\//,'').replace(/\.json$/,'');const r=await window.dbOp(o.method||'GET',path,o.body||null);return {ok:true,json:async()=>r};};},[code,name,code==='AAAA2222'?'#2F80D8':'#E4583F']);
 await p.goto('file://'+FILE);await p.waitForTimeout(1200);await p.evaluate(()=>closeSheet());return p;};
const A=await mk('AAAA2222','Teva'),B=await mk('BBBB3333','Hina');
await A.evaluate(()=>{friends.push({code:'BBBB3333',name:'Hina'});store.set('friends',friends)});await B.evaluate(()=>{friends.push({code:'AAAA2222',name:'Teva'});store.set('friends',friends)});
for(const P of [A,B]) await P.evaluate(()=>pushHeart());await A.waitForTimeout(300);for(const P of [A,B]) await P.evaluate(()=>fetchFriends());
const clear=P=>P.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');});
const T=P=>P.evaluate(()=>sheetInner.querySelector('h2').textContent);
// ---- pāuma
await clear(A);await A.evaluate(()=>openPlace());console.log('bouton pāuma',await A.evaluate(()=>!!$('#plKite')));await A.evaluate(()=>$('#plKite').click());await A.waitForTimeout(300);await A.screenshot({path:O+'hv_kite0.png'});
await A.evaluate(()=>$('#ktGo').click());
// tenir la ligne dans la zone : tirer si tension < .5
let over=null;for(let i=0;i<2600;i++){ over=await A.evaluate(()=>{const s=KT.game&&KT.game.s;if(!s)return 'gone';KT.game.setPull(s.tau<.5);return s.over?[s.ok,$('#ktTxt').textContent,Math.round(s.t)]:null;}); if(over) break; await A.waitForTimeout(30); }
console.log('pāuma tenu →',over);await A.screenshot({path:O+'hv_kite1.png'});
await A.evaluate(()=>$('#ktGo').click());await A.waitForTimeout(400);console.log('après',await A.evaluate(()=>[$('#sheet').hidden,kiteDays().length,bubbleEl.textContent.slice(0,50)]));
// casser la ligne exprès
await clear(A);await A.evaluate(()=>openKite());await A.evaluate(()=>$('#ktGo').click());over=null;for(let i=0;i<600;i++){ over=await A.evaluate(()=>{const s=KT.game.s;KT.game.setPull(true);return s.over?[s.ok,$('#ktTxt').textContent.slice(0,40)]:null;}); if(over) break; await A.waitForTimeout(30);} console.log('ligne cassée →',over);await A.screenshot({path:O+'hv_kite2.png'});await clear(A);
// ---- Heiva : verrouillé tant que les 5 airs ne sont pas connus
console.log('heiva fermé',await A.evaluate(()=>[!!PLACES.heiva,hvSongsOk()]));
// Teva connaît tous les airs
await A.evaluate(()=>{ TUNES.forEach(t=>{ if(!t.duo) t.ok=()=>true; }); hvSync(); });await A.waitForTimeout(2500);console.log('heiva ouvert',await A.evaluate(()=>[!!PLACES.heiva,bubbleEl.textContent.slice(0,60)]));
await clear(A);await A.evaluate(()=>{setPlace('heiva');});await A.waitForTimeout(300);console.log('scène',await A.evaluate(()=>[curPlace,$('#dayScene').hidden,$('#quiet').className,$('#nightSky').hidden,[...document.querySelectorAll('#qDock>button')].map(x=>x.textContent).join('/')]));await A.screenshot({path:O+'hv_scene0.png'});
await A.evaluate(()=>openHeiva());console.log(await T(A));await A.screenshot({path:O+'hv_sheet0.png'});await A.evaluate(()=>$('#hvLit').click());await A.waitForTimeout(400);console.log('feu',await A.evaluate(()=>[hvGet().lit!=='' ,bubbleEl.textContent.slice(0,40),feathers]));await A.evaluate(()=>bubbleEl.classList.remove('show'));await A.screenshot({path:O+'hv_scene1.png'});
await A.evaluate(()=>openHeiva());await A.screenshot({path:O+'hv_sheet1.png'});console.log('actions',await A.evaluate(()=>[!!$('#hvDance'),!!$('#hvInv'),!!$('#hvBar')]));
await A.evaluate(()=>$('#hvBar').click());await A.waitForTimeout(200);await A.screenshot({path:O+'hv_bar.png'});await A.evaluate(()=>document.querySelector('#hvJ [data-j="pam"]').click());await A.waitForTimeout(300);console.log('jus',await A.evaluate(()=>bubbleEl.textContent.slice(0,40)));await clear(A);
// inviter Hina
await A.evaluate(()=>openHeiva());await A.evaluate(()=>$('#hvInv').click());await A.waitForTimeout(200);await A.evaluate(()=>document.querySelector('#hvFr [data-f="BBBB3333"]').click());await A.waitForTimeout(400);console.log('invitation',JSON.stringify(db.visits.BBBB3333));await clear(A);
// Hina ne connaît pas les airs : l'invitation ouvre quand même le Heiva pour la soirée
console.log('Hina avant',await B.evaluate(()=>!!PLACES.heiva));
await B.evaluate(()=>pollVisits());let ok=false;for(let i=0;i<25;i++){await B.waitForTimeout(2000);ok=await B.evaluate(()=>{if(RING.open)closeRing();return !!bubbleEl.querySelector('[data-m^="hv:go:"]')&&bubbleEl.classList.contains('show');});if(ok)break;}
console.log('Hina invitée',ok,await B.evaluate(()=>bubbleEl.textContent.slice(0,60)));await B.evaluate(()=>bubbleEl.querySelector('[data-m^="hv:go:"]').click());await B.waitForTimeout(600);
console.log('Hina après',await B.evaluate(()=>[!!PLACES.heiva,curPlace,hvGuests().map(g=>g.name).join(),bubbleEl.textContent.slice(0,40)]),JSON.stringify(db.visits.AAAA2222));await B.evaluate(()=>bubbleEl.classList.remove('show'));await B.screenshot({path:O+'hv_hina.png'});
// Teva reçoit l'arrivée
await A.waitForTimeout(500);await A.evaluate(()=>{ if(AWAY.on) comeBack(true); });await A.waitForTimeout(4000);await A.evaluate(()=>{bubbleEl.classList.remove('show');return pollVisits();});
ok=false;for(let i=0;i<20;i++){await A.waitForTimeout(2000);ok=await A.evaluate(()=>{if(RING.open)closeRing();return hvGuests().length===1;});if(ok)break;}
console.log('Teva voit Hina',ok,await A.evaluate(()=>[hvGuests().map(g=>g.name+':'+g.look.body).join(),/hv-dance/.test($('#dayScene').innerHTML)]));await A.waitForTimeout(9600);await A.evaluate(()=>bubbleEl.classList.remove('show'));await A.screenshot({path:O+'hv_scene2.png'});
// danser (son : AudioContext absent en headless ? on vérifie seulement qu'il n'y a pas d'erreur)
await A.evaluate(()=>{openHeiva();$('#hvDance').click();});await A.waitForTimeout(200);await A.screenshot({path:O+'hv_dance.png'});await A.evaluate(()=>{const b=sheetInner.querySelector('[data-t]');b&&b.click();});await A.waitForTimeout(800);console.log('danse',await A.evaluate(()=>[UKE.on,$('#sheet').hidden,bubbleEl.textContent.slice(0,30)]));
// le lendemain : le feu s'éteint, les invités repartent, le lieu reste
await A.evaluate(()=>{const h=hvGet();h.lit='2026-01-01';h.circle.BBBB3333='2026-01-01';store.set('heiva',h);hvRefresh();});console.log('lendemain',await A.evaluate(()=>[hvGuests().length,/hv-fl/.test($('#dayScene').innerHTML),!!PLACES.heiva]));
console.log('errs',A.errs,B.errs);await b.close();})();
