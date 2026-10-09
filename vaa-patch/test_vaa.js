// node test_vaa.js [fichier] — vaʻa : jouer en rythme avec la souris (léger/fort), puis rater exprès ; niveaux.
const {chromium}=require('playwright');const FILE=process.argv[2]||'/tmp/claude-0/v91j.html',O='/home/claude/work/';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--headless=new','--autoplay-policy=no-user-gesture-required']});const p=await b.newPage({viewport:{width:390,height:800}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route('**/test.invalid/**',r=>r.fulfill({status:200,body:'null'}));
await p.addInitScript(()=>{localStorage.setItem('manuora.welcomed','true');localStorage.setItem('manuora.v','3');localStorage.setItem('manuora.place',JSON.stringify('tai'));});
await p.goto('file://'+FILE);await p.waitForTimeout(1500);const clear=()=>p.evaluate(()=>{try{if(RING.open)closeRing()}catch(e){};if(!$('#sheet').hidden)closeSheet();bubbleEl.classList.remove('show');});await clear();
console.log('icône',await p.evaluate(()=>[...document.querySelectorAll('#qDock [data-a]')].map(x=>x.textContent).join('/')));
await p.evaluate(()=>openPlace());console.log('bouton',await p.evaluate(()=>!!$('#plVaa')));await p.evaluate(()=>$('#plVaa').click());await p.screenshot({path:O+'va0.png'});
console.log('niveaux',await p.evaluate(()=>[...document.querySelectorAll('#vaLv button')].map(x=>x.textContent+(x.disabled?'(fermé)':'')).join(' | ')));
const r=await p.evaluate(()=>{const c=$('#bkCv').getBoundingClientRect();return {x:c.left+c.width/2,y:c.top+c.height-40};});
const play=async(mode)=>{ await p.evaluate(()=>$('#vaGo').click()); let shot=false;
  for(let i=0;i<4000;i++){ const st=await p.evaluate(()=>{const s=VAA.game&&VAA.game.s;if(!s)return null;const n=s.notes.find(n=>!n.done);return {over:s.over,dt:n?n.t-s.t:9,strong:n?n.strong:false};}); if(!st||st.over) break;
    if(st.dt<0.025 && st.dt>-0.05){ if(mode==='good'){ await p.mouse.move(r.x,r.y); await p.mouse.down(); await p.waitForTimeout(st.strong?260:50); await p.mouse.up(); } else if(mode==='wrong'){ await p.mouse.down(); await p.waitForTimeout(st.strong?50:260); await p.mouse.up(); } else { await p.waitForTimeout(400); } if(!shot && i>40){ shot=true; await p.screenshot({path:O+'va_'+mode+'.png'}); } }
    else await p.waitForTimeout(8); }
  await p.waitForTimeout(400); return p.evaluate(()=>[Math.round(VAA.game.s.score/VAA.game.s.max*100),$('#vaTxt').textContent.slice(0,60),VAA.game.s.notes.filter(n=>n.res==='ok').length,VAA.game.s.notes.length]); };
console.log('en rythme',await play('good'));await p.screenshot({path:O+'va_end.png'});await p.evaluate(()=>$('#vaGo').click());await p.waitForTimeout(300);console.log('fin',await p.evaluate(()=>[$('#sheet').hidden,vaaDays().length,bubbleEl.textContent.slice(0,40)]));await clear();
await p.evaluate(()=>openVaa());console.log('mauvaise force',await play('wrong'));await p.evaluate(()=>{VAA.game.stop();closeSheet();});
await p.evaluate(()=>openVaa());console.log('ne rien faire',await play('none'));await p.evaluate(()=>{VAA.game.stop();closeSheet();});
await p.evaluate(()=>{store.set('vaaDays',['a','b','c','d','e','f','g']);openVaa();});console.log('niveaux après 7 jours',await p.evaluate(()=>[...document.querySelectorAll('#vaLv button')].filter(x=>!x.disabled).length));await p.evaluate(()=>document.querySelector('#vaLv [data-l="2"]').click());console.log('large choisi',await p.evaluate(()=>[VAA.lv,VAA_LV[VAA.lv].n]));
console.log('errs',errs);await b.close();})();
