const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new']});
const db={};const mk=async(code,name,friends)=>{const ctx=await b.newContext({viewport:{width:390,height:800},timezoneId:'Pacific/Tahiti'});const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
 await p.exposeFunction('dbOp',(method,path,body)=>{const ks=path.split('/').filter(Boolean);let o=db;if(method==='GET'){for(const k of ks){o=o&&o[k];}return o===undefined?null:JSON.parse(JSON.stringify(o));}
   const last=ks.pop();for(const k of ks){o[k]=o[k]||{};o=o[k];}const v=body?JSON.parse(body):null;
   if(method==='PUT')o[last]=v;else if(method==='PATCH'){o[last]=o[last]||{};for(const k in v){if(v[k]===null)delete o[last][k];else o[last][k]=v[k];}}else if(method==='DELETE')delete o[last];return {};});
 await p.addInitScript(([code,name,friends])=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.code',JSON.stringify(code));localStorage.setItem('manuora.share',JSON.stringify({on:true,name}));localStorage.setItem('manuora.bedHour','0');localStorage.setItem('manuora.friends',JSON.stringify(friends||[]));localStorage.setItem('manuora.place',JSON.stringify('haapii'));localStorage.setItem('manuora.cfg',JSON.stringify({name:'Vini',body:name==='Hina'?'#1AA3B1':'#2E86DE',belly:'#F6F1E7',tattoo:'none',animal:'manu',night:'off',tiare:true}));
   window.fetch=async(u,o)=>{o=o||{};const path=String(u).replace(/^https?:\/\/[^/]+\//,'').replace(/\.json$/,'');const r=await window.dbOp(o.method||'GET',path,o.body||null);return {ok:true,json:async()=>r};};},[code,name,friends]);
 await p.goto('file:///tmp/claude-0/v91j.html');await p.waitForTimeout(1200);await p.evaluate(()=>closeSheet());return p;};

const A=await mk('AAAA2222','Teva',[{code:'BBBB3333',name:'Hina'}]),Bp=await mk('BBBB3333','Hina',[{code:'AAAA2222',name:'Teva'}]);
for(const P of [A,Bp]){await P.evaluate(()=>pushHeart());}await A.waitForTimeout(300);for(const P of [A,Bp]){await P.evaluate(()=>fetchFriends());}
const K=process.argv[2]||'b';
const play=async(P,shots)=>{ for(let i=0;i<5;i++){ await P.waitForFunction((n)=>BK.i===n&&!!document.querySelector('#bkShoot')&&!document.querySelector('#bkShoot').disabled&&!BK.busy,i+1,{timeout:9000});
  if(i===1) await P.screenshot({path:'/home/claude/work/g_'+K+'_wait.png'});
  if(K==='p'){ if(shots[i]) await P.waitForFunction(()=>BK.pos>=76&&BK.pos<=88,null,{polling:'raf',timeout:5000}); await P.evaluate(()=>$('#bkShoot').click()); }
  else await P.evaluate(([good,K])=>{ cancelAnimationFrame(BK.raf); BK.busy=true; if(K==='f') BK.pos=good?(BK.keep>50?BK.keep-30:BK.keep+30):BK.keep; else BK.pos=good?50:96; $('#bkCur').style.left=BK.pos+'%'; BK.busy=false; $('#bkShoot').click(); },[shots[i],K]);
  if(i===0||i===2){ await P.waitForTimeout(K==='p'?250:620); await P.screenshot({path:'/home/claude/work/g_'+K+'_'+(shots[i]?'ok':'ko')+'.png'}); } }
  await P.waitForFunction(()=>BK.i===6,null,{timeout:8000}); await P.waitForTimeout(200); };
const T=(P)=>P.evaluate(()=>sheetInner.querySelector('h2').textContent);
await A.evaluate(()=>openPlace());console.log('button',await A.evaluate(()=>!!$('#plBall')));await A.evaluate(()=>$('#plBall').click());await A.screenshot({path:'/home/claude/work/g_menu.png'});await A.evaluate((K)=>sheetInner.querySelector('[data-k="'+K+'"]').click(),K);console.log(await T(A));await A.screenshot({path:'/home/claude/work/g_'+K+'_0.png'});
await A.evaluate(()=>$('#bkGo').click());await play(A,[true,true,false,true,false]);console.log(await T(A),await A.evaluate(()=>[BK.res.join(','),feathers,!!$('#bkFriends')]));await A.screenshot({path:'/home/claude/work/g_'+K+'_end.png'});
await A.evaluate(()=>document.querySelector('#bkFriends [data-f="BBBB3333"]').click());await A.waitForTimeout(500);console.log('invite',JSON.stringify(db.visits.BBBB3333),await A.evaluate(()=>JSON.stringify(store.get('bkOut')).slice(0,30)));
await Bp.evaluate(()=>pollVisits());let ok=false;for(let i=0;i<25;i++){await Bp.waitForTimeout(2000);ok=await Bp.evaluate(()=>{if(RING.open)closeRing();return !!bubbleEl.querySelector('[data-m^="bk:go:"]')&&bubbleEl.classList.contains('show');});if(ok)break;}
console.log('B invited',ok,await Bp.evaluate(()=>bubbleEl.textContent.slice(0,70)));
await Bp.evaluate(()=>bubbleEl.querySelector('[data-m^="bk:go:"]').click());console.log(await T(Bp));await Bp.evaluate(()=>$('#bkGo').click());await play(Bp,[false,true,true,true,true]);console.log(await T(Bp),JSON.stringify(db.visits.AAAA2222));
await A.waitForTimeout(500);await A.evaluate(()=>{ if(AWAY.on) comeBack(true); });await A.waitForTimeout(4000);
await A.evaluate(()=>{bubbleEl.classList.remove('show');return pollVisits();});ok=false;for(let i=0;i<25;i++){await A.waitForTimeout(2000);ok=await A.evaluate(()=>{if(RING.open)closeRing();return !!bubbleEl.querySelector('[data-m^="bk:bravo:"]')&&bubbleEl.classList.contains('show');});if(ok)break;}
console.log('A team',ok,await A.evaluate(()=>[bubbleEl.textContent.slice(0,60),JSON.stringify(store.get('bkOut'))]));
await A.evaluate(()=>bubbleEl.querySelector('[data-m^="bk:bravo:"]').click());await A.waitForTimeout(400);console.log('bravo',JSON.stringify(db.visits.BBBB3333));
console.log('errs',A.errs,Bp.errs);await b.close();})();
