const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});const O='/home/claude/work/';
const db={};const mk=async(code,name)=>{const ctx=await b.newContext({viewport:{width:390,height:800},timezoneId:'Pacific/Tahiti'});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
 await p.exposeFunction('dbOp',(method,path,body)=>{const ks=path.split('/').filter(Boolean);let o=db;if(method==='GET'){for(const k of ks){o=o&&o[k];}return o===undefined?null:JSON.parse(JSON.stringify(o));}
   const last=ks.pop();for(const k of ks){o[k]=o[k]||{};o=o[k];}const v=body?JSON.parse(body):null;if(method==='PUT')o[last]=v;else if(method==='PATCH'){o[last]=o[last]||{};for(const k in v){if(v[k]===null)delete o[last][k];else o[last][k]=v[k];}}else if(method==='DELETE')delete o[last];return {};});
 await p.addInitScript(([code,name])=>{if(localStorage.getItem('manuora.welcomed'))return;localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.code',JSON.stringify(code));localStorage.setItem('manuora.share',JSON.stringify({on:true,name}));
   },[code,name]);
 await p.addInitScript(()=>{window.fetch=async(u,o)=>{o=o||{};const path=String(u).replace(/^https?:\/\/[^/]+\//,'').replace(/\.json$/,'');const r=await window.dbOp(o.method||'GET',path,o.body||null);return {ok:true,json:async()=>r};};});
 await p.goto('file://'+process.argv[2]);await p.waitForTimeout(1200);await p.evaluate(()=>closeSheet());return p;};
const A=await mk('AAAA2222','Teva'),B=await mk('BBBB3333','Hina');
await A.evaluate(()=>{friends.push({code:'BBBB3333',name:'Hina'});store.set('friends',friends)});await B.evaluate(()=>{friends.push({code:'AAAA2222',name:'Teva'});store.set('friends',friends)});
for(const P of [A,B]) await P.evaluate(()=>pushHeart());await A.waitForTimeout(300);for(const P of [A,B]) await P.evaluate(()=>fetchFriends());
console.log('mutuel',await A.evaluate(()=>isMutual('BBBB3333')));
const clear=P=>P.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');cfg.night='off';renderNight();});
const T=P=>P.evaluate(()=>sheetInner.querySelector('h2').textContent);
// A : ciel ouvert, nuages et vents faits
await A.evaluate(()=>{store.set('stones',{vai:'x',tai:'x',oire:'x',haapii:'x'});store.set('portal',true);PLACES.reva=REVA_PLACE;store.set('reva',{clouds:'x',winds:'x'});setPlace('reva');});await clear(A);
await A.evaluate(()=>openReva());console.log('menu',await A.evaluate(()=>[!!$('#rvI'),!!$('#rvF'),!!$('#rvV')]));
await A.evaluate(()=>$('#rvI').click());await A.waitForTimeout(200);for(const id of ['moua','faa','tahatai','tairoto','aau','ava','motu','moana']) await A.click(`.imap [data-i="${id}"]`);await A.screenshot({path:O+'vy_ile.png'});
await A.evaluate(()=>$('#isEnd').click());await A.waitForTimeout(300);console.log('île',await A.evaluate(()=>[JSON.stringify(revaDone()).length>30,bubbleEl.textContent.slice(0,40)]));await clear(A);
// fare : étape 1 sans récolte -> bloqué ; avec récolte -> posé
await A.evaluate(()=>openFare());console.log('fare bloqué',await A.evaluate(()=>$('#frGo').disabled));
await A.evaluate(()=>{garden.store.uru=2;saveGarden();openFare();});await A.screenshot({path:O+'vy_fare0.png'});await A.evaluate(()=>$('#frGo').click());await A.waitForTimeout(200);console.log('étape 1',await T(A),await A.evaluate(()=>[fareGet().n,garden.store.uru]));await A.evaluate(()=>$('#frOk').click());
await A.evaluate(()=>openFare());console.log('même jour',await A.evaluate(()=>!$('#frGo')));
// demander de l'aide à Hina
await A.evaluate(()=>sheetInner.querySelector('#frFr [data-f="BBBB3333"]').click());await A.waitForTimeout(500);console.log('demande',JSON.stringify(db.visits.BBBB3333));
await B.evaluate(()=>pollVisits());let ok=false;for(let i=0;i<25;i++){await B.waitForTimeout(2000);ok=await B.evaluate(()=>{if(RING.open)closeRing();return !!bubbleEl.querySelector('[data-m^="vy:aid:"]')&&bubbleEl.classList.contains('show');});if(ok)break;}
console.log('Hina invitée',ok,await B.evaluate(()=>bubbleEl.textContent.slice(0,60)));await B.evaluate(()=>bubbleEl.querySelector('[data-m^="vy:aid:"]').click());await B.waitForTimeout(500);console.log('aide',JSON.stringify(db.visits.AAAA2222));
await A.waitForTimeout(500);await A.evaluate(()=>{ if(AWAY.on) comeBack(true); });await A.waitForTimeout(4000);await A.evaluate(()=>{bubbleEl.classList.remove('show');return pollVisits();});
ok=false;for(let i=0;i<20;i++){await A.waitForTimeout(2000);ok=await A.evaluate(()=>{if(RING.open)closeRing();return fareGet().gift===1;});if(ok)break;}console.log('étape offerte',ok,await A.evaluate(()=>JSON.stringify(fareGet())));
await A.waitForTimeout(9000);await clear(A);
// étapes 2 (offerte), 3, 4 en avançant les jours
for(let n=2;n<=4;n++){ await clear(A); await A.evaluate(()=>{const F=fareGet();F.day='';store.set('fare',F);garden.store.fara=4;garden.store.tiare=1;saveGarden();openFare();}); if(n===3) await A.screenshot({path:O+'vy_fare2.png'}); await A.evaluate(()=>$('#frGo').click()); await A.waitForTimeout(150); await A.evaluate(()=>$('#frOk').click()); await A.waitForTimeout(300);} 
console.log('fare fini',await A.evaluate(()=>[fareGet().n,fareGet().help.join(),garden.store.haari,revaAllDone()]));await clear(A);await A.evaluate(()=>openFare());await A.screenshot({path:O+'vy_fare4.png'});await clear(A);
// période difficile : le manu attend
await A.evaluate(()=>{const n=Date.now();for(let i=0;i<3;i++)log.push({ts:n-i*864e5,emo:'riri',intensity:2,body:[],text:'',acts:[]});store.set('cstAsk',0);cstTick();});console.log('période difficile → proposé ?',await A.evaluate(()=>bubbleEl.classList.contains('show')));
await A.evaluate(()=>{log.splice(-3,3);const n=Date.now();log.push({ts:n-864e5*20,emo:'riri',intensity:2,body:[],text:'',acts:[]},{ts:n-864e5*9,emo:'hau',intensity:1,body:[],text:'',acts:[]});shells.push({d:'2026-9-1',t:['un rire avec Hina','le soleil ce matin']});cstTick();});console.log('sinon → proposé ?',await A.evaluate(()=>bubbleEl.textContent.slice(0,40)));
await A.evaluate(()=>bubbleEl.querySelector('[data-m="vy:cst"]').click());await A.waitForTimeout(200);const tt=[];for(let i=0;i<4;i++){tt.push(await T(A));if(i===1)await A.screenshot({path:O+'vy_r1.png'});if(i===3)await A.screenshot({path:O+'vy_r3.png'});await A.evaluate(()=>$('#vyNext').click());await A.waitForTimeout(150);}tt.push(await T(A));console.log(tt.join(' | '));await A.screenshot({path:O+'vy_ask.png'});
// "pas encore" : rien ne change
await A.evaluate(()=>$('#vyNo').click());await A.waitForTimeout(300);console.log('pas encore',await A.evaluate(()=>[cstGet().done,bubbleEl.textContent.slice(0,30)]));await clear(A);
await A.evaluate(()=>{openVoyage();VY.i=4;voyStep();});await A.evaluate(()=>{$('#vyShare').checked=true;$('#vyUp').click()});await A.waitForTimeout(3000);await A.screenshot({path:O+'vy_rise1.png'});await A.waitForTimeout(6500);await A.screenshot({path:O+'vy_rise2.png'});await A.click('.cstfx');await A.waitForTimeout(1400);
console.log('après',await T(A),await A.evaluate(()=>[JSON.stringify(cstGet()),document.body.classList.contains('manu-up'),!!$('#callManu')&&!$('#callManu').hidden]));await A.screenshot({path:O+'vy_world.png'});await A.evaluate(()=>$('#vyEnd').click());
await A.evaluate(()=>{cfg.night='on';renderNight();});await A.waitForTimeout(300);await A.screenshot({path:O+'vy_night.png'});
console.log('auto-question coupée',await A.evaluate(()=>{askRing(true);return RING.open;}));
await A.click('#callManu');await A.waitForTimeout(800);console.log('rappelé',await A.evaluate(()=>[cstGet().up,document.body.classList.contains('manu-up'),bubbleEl.textContent.slice(0,30)]));
// Hina voit les étoiles de Teva
await A.evaluate(()=>pushHeart());await A.waitForTimeout(300);console.log('publié star',db.hearts.AAAA2222.cfg.star);await B.evaluate(()=>fetchFriends());await B.evaluate(()=>{cfg.night='on';renderNight();});await B.waitForTimeout(300);console.log('ciel de Hina',await B.evaluate(()=>/Teva/.test($('#nightSky').innerHTML)));await clear(B);await B.evaluate(()=>{cfg.night='on';renderNight();bubbleEl.classList.remove('show')});await B.screenshot({path:O+'vy_nightB.png'});
// retrait du consentement
await A.evaluate(()=>{const c=cstGet();c.share=false;store.set('cst',c);return pushHeart();});await A.waitForTimeout(300);console.log('retiré',db.hearts.AAAA2222.cfg.star);
console.log('errs',A.errs,B.errs);await b.close();})();
