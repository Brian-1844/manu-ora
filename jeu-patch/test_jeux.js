// Test des jeux de la cour (v2) : node test_jeux.js b|f|p [fichier]
// Deux utilisateurs simulés (Teva, Hina), base simulée, navigateur sans écran. Jamais un vrai téléphone.
const {chromium}=require('playwright');
const K=process.argv[2]||'b', FILE=process.argv[3]||'/tmp/claude-0/v91j.html';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const db={};const mk=async(code,name)=>{const ctx=await b.newContext({viewport:{width:390,height:800},timezoneId:'Pacific/Tahiti'});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
 await p.exposeFunction('dbOp',(method,path,body)=>{const ks=path.split('/').filter(Boolean);let o=db;if(method==='GET'){for(const k of ks){o=o&&o[k];}return o===undefined?null:JSON.parse(JSON.stringify(o));}
   const last=ks.pop();for(const k of ks){o[k]=o[k]||{};o=o[k];}const v=body?JSON.parse(body):null;
   if(method==='PUT')o[last]=v;else if(method==='PATCH'){o[last]=o[last]||{};for(const k in v){if(v[k]===null)delete o[last][k];else o[last][k]=v[k];}}else if(method==='DELETE')delete o[last];return {};});
 await p.addInitScript(([code,name])=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.code',JSON.stringify(code));localStorage.setItem('manuora.share',JSON.stringify({on:true,name}));localStorage.setItem('manuora.place',JSON.stringify('haapii'));
   window.fetch=async(u,o)=>{o=o||{};const path=String(u).replace(/^https?:\/\/[^/]+\//,'').replace(/\.json$/,'');const r=await window.dbOp(o.method||'GET',path,o.body||null);return {ok:true,json:async()=>r};};},[code,name]);
 await p.goto('file://'+FILE);await p.waitForTimeout(1200);await p.evaluate(()=>closeSheet());return p;};
const A=await mk('AAAA2222','Teva'),Bp=await mk('BBBB3333','Hina');
await A.evaluate(()=>{friends.push({code:'BBBB3333',name:'Hina'});store.set('friends',friends)});await Bp.evaluate(()=>{friends.push({code:'AAAA2222',name:'Teva'});store.set('friends',friends)});
for(const P of [A,Bp]){await P.evaluate(()=>pushHeart());}await A.waitForTimeout(300);for(const P of [A,Bp]){await P.evaluate(()=>fetchFriends());}
const T=(P)=>P.evaluate(()=>sheetInner.querySelector('h2').textContent);
const clear=P=>P.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};bubbleEl.classList.remove('show');cfg.night='off';renderNight();});
// joue un essai avec le résultat voulu, via les mêmes fonctions que le doigt
const attempt=async(P,good,n)=>{
  await P.waitForFunction(n=>BK.game&&BK.game.s&&BK.res.length===n&&!BK.ending,n,{timeout:9000});
  if(K==='b'){ const v=await P.evaluate(good=>{ if(!good) return [200,-320]; for(let vx=250;vx<=700;vx+=20)for(let vy=-950;vy<=-450;vy+=20){const o=BK.game.sim(vx,vy,4.5);if(o.score)return [vx,vy];} return [200,-320]; },good); await P.evaluate(v=>BK.game.shoot(v[0],v[1]),v); }
  else if(K==='f'){ await P.waitForFunction(()=>BK.game.s.phase==='aim',null,{timeout:5000}); await P.evaluate(good=>{ const s=BK.game.s, W=$('#bkCv').clientWidth, H=$('#bkCv').clientHeight, hw=W*.3, gh=H*.46; if(good){ const side=s.dive===0?1:-s.dive; BK.game.fire(W/2+side*hw*.85, gh*.8, .5); } else BK.game.fire(W/2+(s.dive===0?hw*.2:s.dive*hw*.3), gh*.3, .5); },good); }
  else { for(let i=0;i<700;i++){ const st=await P.evaluate(good=>{ const s=BK.game&&BK.game.s; if(!s) return null; const W=$('#bkCv').clientWidth; BK.game.setPad(good?s.ball.x:(s.ball.x<W/2?W-40:40)); return BK.res.length; },good); if(st===n+1) break; await P.waitForTimeout(25); } }
  await P.waitForFunction(n=>BK.res.length===n+1,n,{timeout:9000}); };
const play=async(P,shots)=>{ for(let i=0;i<5;i++){ await attempt(P,shots[i],i); if(i===1) await P.screenshot({path:'/home/claude/work/g_'+K+'_mid.png'}); } await P.waitForFunction(()=>BK.i===6&&!!$('#bkEnd'),null,{timeout:9000}); };
await A.evaluate(()=>openPlace());console.log('bouton',await A.evaluate(()=>!!$('#plBall')));await A.evaluate(()=>$('#plBall').click());await A.screenshot({path:'/home/claude/work/g_menu.png'});await A.evaluate((K)=>sheetInner.querySelector('[data-k="'+K+'"]').click(),K);console.log(await T(A));
await A.evaluate(()=>$('#bkGo').click());await play(A,[true,true,false,true,false]);console.log(await T(A),await A.evaluate(()=>[BK.res.join(','),feathers,!!$('#bkFriends')]));await A.screenshot({path:'/home/claude/work/g_'+K+'_end.png'});
await A.evaluate(()=>document.querySelector('#bkFriends [data-f="BBBB3333"]').click());await A.waitForTimeout(500);console.log('invite',JSON.stringify(db.visits.BBBB3333),await A.evaluate(()=>JSON.stringify(store.get('bkOut')).slice(0,30)));
await Bp.evaluate(()=>pollVisits());let ok=false;for(let i=0;i<25;i++){await Bp.waitForTimeout(2000);ok=await Bp.evaluate(()=>{if(RING.open)closeRing();return !!bubbleEl.querySelector('[data-m^="bk:go:"]')&&bubbleEl.classList.contains('show');});if(ok)break;}
console.log('B invitée',ok,await Bp.evaluate(()=>bubbleEl.textContent.slice(0,70)));
await Bp.evaluate(()=>bubbleEl.querySelector('[data-m^="bk:go:"]').click());console.log(await T(Bp));await Bp.evaluate(()=>$('#bkGo').click());await play(Bp,[false,true,true,true,true]);console.log(await T(Bp),JSON.stringify(db.visits.AAAA2222));
await A.waitForTimeout(500);await A.evaluate(()=>{ if(AWAY.on) comeBack(true); });await A.waitForTimeout(4000);
await A.evaluate(()=>{bubbleEl.classList.remove('show');return pollVisits();});ok=false;for(let i=0;i<25;i++){await A.waitForTimeout(2000);ok=await A.evaluate(()=>{if(RING.open)closeRing();const y=!!bubbleEl.querySelector('[data-m^="bk:bravo:"]')&&bubbleEl.classList.contains('show');if(!y)bubbleEl.classList.remove('show');return y;});if(ok)break;}
console.log('A équipe',ok,await A.evaluate(()=>[bubbleEl.textContent.slice(0,60),JSON.stringify(store.get('bkOut'))]));
await A.evaluate(()=>bubbleEl.querySelector('[data-m^="bk:bravo:"]').click());await A.waitForTimeout(400);console.log('bravo',JSON.stringify(db.visits.BBBB3333));
// fermer en pleine partie : la boucle s'arrête
await A.evaluate(()=>openSport('b',null));await A.evaluate(()=>$('#bkGo').click());await A.waitForTimeout(300);await A.evaluate(()=>$('#sx').click());console.log('fermeture propre',await A.evaluate(()=>[BK.game===null,$('#sheet').hidden]));
console.log('errs',A.errs,Bp.errs);await b.close();})();
