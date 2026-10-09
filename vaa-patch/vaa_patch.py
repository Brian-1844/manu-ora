# Patch "le vaʻa : pagayer au rythme, coup léger ou coup fort, trois niveaux" (plage).
# Dépend de jeu-patch (moteur canvas) et dock-patch (icônes). Usage : python3 vaa_patch.py <site>/index.html <manu-ora.html>
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    assert 'function bkLoop(' in s and 'function dockRender(' in s, 'appliquer jeu-patch et dock-patch avant'
    rep("const sf=$('#plSurf');","const va=$('#plVaa'); if(va) va.onclick=()=>openVaa(); const sf=$('#plSurf');")
    rep("+paBtn('dol','plDol')","+paBtn('dol','plDol')+'<button class=\"btn\" id=\"plVaa\">Le vaʻa : pagayer ensemble</button>'")
    new = r"""/* ---------- le vaʻa : pagayer au rythme, ensemble ---------- */
ACT.vaa={t:'Le vaʻa', p:'fetii', d:'Pagayer au même rythme que les autres.'};
function vaaDays(){ const a=store.get('vaaDays',[]); return Array.isArray(a)?a:[]; }
const VAA_LV=[{need:0,n:'Le lagon',bpm:56,strong:'four',notes:20},{need:3,n:'La passe',bpm:70,strong:'mix',notes:24},{need:7,n:'Le large',bpm:84,strong:'mix',notes:28,off:true}];
let VAA={};
function openVaa(){ const n=vaaDays().length; let lv=0; VAA_LV.forEach((L,i)=>{ if(n>=L.need) lv=i; }); const pick=Math.min(lv,(store.get('vaaPick',lv)??lv)); VAA={max:lv, lv:pick, game:null};
  openSheet(`<div class="head"><div><div class="eyebrow">Tahatai · la plage</div><h2>Le vaʻa</h2></div><button class="x" id="sx" aria-label="Fermer">×</button></div>
    <p>Dans une pirogue, on nʼavance que si tout le monde pagaie ensemble. Suis le rythme : <b>petit rond = coup léger</b> (une touche brève), <b>grand rond « HOE » = coup fort</b> (appuie, garde le doigt un instant, puis lâche).</p>
    <div class="opt" id="vaLv">${VAA_LV.map((L,i)=>`<button class="${i===VAA.lv?'on':''}" data-l="${i}" ${i>VAA.max?'disabled':''}>${i>VAA.max?'🔒 ':''}${L.n}</button>`).join('')}</div>
    <p class="small muted">${VAA.max<2?`Niveau suivant après ${VAA_LV[VAA.max+1].need} jours de vaʻa.`:'Tous les niveaux sont ouverts.'}</p>
    <div class="bkst" id="bkSt" style="height:300px"><canvas id="bkCv" role="img" aria-label="La pirogue sur le lagon et la piste du rythme"></canvas></div>
    <p id="vaTxt" class="bktxt" aria-live="polite">Touche la piste en bas au moment où un rond passe dans le cercle.</p><button class="btn primary" id="vaGo">Partir</button><button class="btn ghost" id="vaStop">Arrêter</button>`);
  sheetInner.scrollTop=0; const quit=()=>{ if(VAA.game) VAA.game.stop(); VAA.game=null; closeSheet(); }; $('#sx').onclick=quit; $('#vaStop').onclick=quit;
  $('#vaLv').addEventListener('click', e=>{ const b=e.target.closest('[data-l]'); if(!b || b.disabled) return; store.set('vaaPick',+b.dataset.l); if(VAA.game) VAA.game.stop(); openVaa(); });
  const G=bkMount(); if(!G) return; VAA.game=vaaGame(G,bkFx(G.st,G.cv)); VAA.game.preview();
  $('#vaGo').onclick=()=>{ $('#vaGo').hidden=true; $('#vaTxt').textContent='Suis le rythme…'; VAA.game.start(); }; }
function vaaGame(G,fx){ const {cv,ctx,W,H}=G, L=VAA_LV[VAA.lv], beat=60/L.bpm, HX=56, LY=H-40, SPD=150, LEAD=2.2; let s=null, P=[]; const loop=bkLoop(update);
  function chart(){ const out=[]; let t=LEAD; for(let i=0;i<L.notes;i++){ const strong = L.strong==='four' ? (i%4===3) : (i%4===3 || Math.random()<.22); out.push({t, strong, done:false, res:''}); if(L.off && i%6===4 && i<L.notes-1){ out.push({t:t+beat/2, strong:false, done:false, res:''}); i++; } t+=beat; } return out; }
  function reset(){ s={t:0, notes:chart(), score:0, max:0, x:0, v:0, down:null, over:false, run:false, sch:0, combo:0, stroke:0, last:''}; s.max=s.notes.length; }
  function sound(n){ try{ if(!AC) AC=new (window.AudioContext||window.webkitAudioContext)(); if(AC.state!=='running') AC.resume(); }catch(e){} }
  function schedule(){ try{ if(!AC || AC.state!=='running') return; while(s.sch<s.notes.length && s.notes[s.sch].t < s.t+.25){ const n=s.notes[s.sch]; const at=AC.currentTime+Math.max(0,n.t-s.t); drumHit(at, n.strong?'pahu':'hi'); s.sch++; } }catch(e){} }
  function judge(tDown,dur){ let best=null, bd=1e9; s.notes.forEach(n=>{ if(n.done) return; const d=Math.abs(n.t-tDown); if(d<bd){ bd=d; best=n; } }); if(!best || bd>.24){ s.last='Trop tôt ou trop tard : écoute le tambour.'; fx.pop('·', HX, LY-26, '#8A97A0'); return; }
    best.done=true; const hard=dur>=200; let q = bd<=.09 ? 1 : .6, word = bd<=.09?'Parfait':'Bien'; if(best.strong!==hard){ q*=.4; word = best.strong?'Plus fort !':'Plus léger !'; }
    best.res=q>=.6?'ok':'meh'; s.score+=q; s.combo = q>=.6 ? s.combo+1 : 0; s.v+= q*(best.strong?42:26); s.stroke=1; fx.pop(word+(s.combo>=6&&q>=.6?' ×'+s.combo:''), HX+30, LY-34, q>=.6?(best.strong?'#C8402F':'#0F6E78'):'#8A6A12', best.strong&&q>=.6);
    if(best.strong && q>=.6){ bkBurst(P,W*.5,H*.42,10,['#fff','#BFE6F5']); fx.shake(2,70); } s.last=best.strong!==hard?(best.strong?'Un grand rond, cʼest un coup fort : garde le doigt appuyé un instant.':'Un petit rond, cʼest un coup léger : une touche brève.'):''; }
  bkPointer(cv,{ down(){ if(!s||!s.run||s.over) return; sound(); s.down=s.t; }, up(p0,p,ms){ if(!s||!s.run||s.over||s.down===null) return; const td=s.down; s.down=null; judge(td,ms); } });
  function finish(){ s.over=true; s.run=false; const pct=Math.round(s.score/s.max*100); const tx=$('#vaTxt'); if(tx) tx.textContent=`En rythme : ${pct} %. `+(pct>=80?'La pirogue a filé comme une seule pagaie. Bel équipage !':pct>=50?'Ça avance ! Quand tout le monde est ensemble, ça va encore plus vite.':'Le rythme, ça vient en écoutant. Pas besoin dʼêtre le plus fort : il faut être ensemble.'); fx.flash(); bkBurst(P,W*.5,H*.4,18,['#F2C94C','#fff','#2BB3C0']);
    const go=$('#vaGo'); if(go){ go.hidden=false; go.textContent='Terminer'; go.onclick=()=>{ try{ const k=dayKey(Date.now()), d=vaaDays(); if(!d.includes(k)){ d.push(k); store.set('vaaDays',d.slice(-60)); const nx=VAA_LV.findIndex(x=>x.need===d.length); if(nx>0) setTimeout(()=>toast('Nouveau niveau de vaʻa : '+VAA_LV[nx].n),1400); } }catch(e){} loop.stop(); VAA.game=null; placeDone('vaa','Hoe ! Ensemble, au même rythme : cʼest toute la pirogue qui avance.'); }; } }
  function update(dt){ if(!s) return; if(s.run && !s.over){ s.t+=dt; schedule(); s.notes.forEach(n=>{ if(!n.done && s.t-n.t>.24){ n.done=true; n.res='miss'; s.combo=0; s.v*=.6; fx.pop('Raté', HX, LY-26, '#8A97A0'); } }); const tx=$('#vaTxt'); if(tx && s.last) tx.textContent=s.last; if(s.notes.every(n=>n.done) && s.t>s.notes[s.notes.length-1].t+.5) finish(); }
    s.v*=Math.pow(.55,dt); s.x+=s.v*dt; s.stroke=Math.max(0,s.stroke-dt*3); draw(dt); }
  function draw(dt){ const gr=ctx.createLinearGradient(0,0,0,H); gr.addColorStop(0,'#BEE5F6'); gr.addColorStop(.28,'#E8F6F8'); gr.addColorStop(.28,'#4DB6C9'); gr.addColorStop(.78,'#2E9CB5'); ctx.fillStyle=gr; ctx.fillRect(0,0,W,H);
    ctx.fillStyle='#3B8C58'; ctx.beginPath(); ctx.moveTo(W*.55,H*.28); ctx.quadraticCurveTo(W*.75,H*.12,W*.98,H*.28); ctx.fill();
    ctx.strokeStyle='rgba(255,255,255,.55)'; ctx.lineWidth=2; for(let i=0;i<7;i++){ const x=((i*73-s.x*1.2)%(W+80)+W+80)%(W+80)-40, y=H*.36+i*14; ctx.beginPath(); ctx.moveTo(x,y); ctx.lineTo(x+26,y); ctx.stroke(); }
    const cy=H*.47, cx=W*.5; ctx.fillStyle='#6B4A2A'; ctx.beginPath(); ctx.moveTo(cx-120,cy); ctx.quadraticCurveTo(cx-130,cy-10,cx-112,cy-12); ctx.lineTo(cx+110,cy-12); ctx.quadraticCurveTo(cx+132,cy-10,cx+124,cy); ctx.quadraticCurveTo(cx,cy+16,cx-120,cy); ctx.fill(); ctx.fillStyle='#E9D3A0'; ctx.fillRect(cx-108,cy-14,218,3);
    ctx.strokeStyle='#5C3A1E'; ctx.lineWidth=2.4; ctx.beginPath(); ctx.moveTo(cx-60,cy-10); ctx.lineTo(cx-70,cy-34); ctx.moveTo(cx+30,cy-10); ctx.lineTo(cx+20,cy-34); ctx.stroke(); ctx.beginPath(); ctx.moveTo(cx-78,cy-34); ctx.lineTo(cx+40,cy-34); ctx.stroke(); ctx.fillStyle='#8A5A2B'; ctx.beginPath(); ctx.ellipse(cx-14,cy-36,62,4,0,0,Math.PI*2); ctx.fill();
    const sw=s.stroke; for(let i=0;i<5;i++){ const px=cx-90+i*42, py=cy-22; ctx.fillStyle=['#2F80D8','#E4583F','#F2C94C','#3B8C58','#7FB2C9'][i]; ctx.beginPath(); ctx.ellipse(px,py,9,11,0,0,Math.PI*2); ctx.fill(); ctx.fillStyle='#F6F1E7'; ctx.beginPath(); ctx.arc(px+5,py-12,6,0,Math.PI*2); ctx.fill(); ctx.fillStyle='#F0A23A'; ctx.beginPath(); ctx.moveTo(px+10,py-13); ctx.lineTo(px+15,py-11); ctx.lineTo(px+10,py-9); ctx.fill(); ctx.strokeStyle='#5C3A1E'; ctx.lineWidth=2.2; const a=-.6+sw*1.1; ctx.beginPath(); ctx.moveTo(px+4,py-4); ctx.lineTo(px+4+Math.cos(a+1.2)*30, py-4+Math.sin(a+1.2)*30); ctx.stroke(); }
    ctx.fillStyle='rgba(255,255,255,.88)'; ctx.fillRect(0,LY-30,W,60); ctx.strokeStyle='#B9C4C9'; ctx.lineWidth=1; ctx.beginPath(); ctx.moveTo(0,LY); ctx.lineTo(W,LY); ctx.stroke();
    ctx.strokeStyle='#16303B'; ctx.lineWidth=3; ctx.beginPath(); ctx.arc(HX,LY,20,0,Math.PI*2); ctx.stroke(); if(s.down!==null){ ctx.fillStyle='rgba(15,110,120,.25)'; ctx.beginPath(); ctx.arc(HX,LY,20,0,Math.PI*2); ctx.fill(); }
    s.notes.forEach(n=>{ if(n.done && n.res!=='miss') return; const x=HX+(n.t-s.t)*SPD; if(x<-30||x>W+30) return; ctx.globalAlpha=n.done?.3:1; ctx.fillStyle=n.strong?'#E4583F':'#2BB3C0'; ctx.beginPath(); ctx.arc(x,LY,n.strong?16:9,0,Math.PI*2); ctx.fill(); if(n.strong){ ctx.fillStyle='#fff'; ctx.font='800 9px sans-serif'; ctx.textAlign='center'; ctx.fillText('HOE',x,LY+3); } ctx.globalAlpha=1; });
    const pr=s.max?Math.min(1,s.score/s.max):0; ctx.fillStyle='rgba(22,48,59,.15)'; ctx.fillRect(10,10,W-20,6); ctx.fillStyle='#F2C94C'; ctx.fillRect(10,10,(W-20)*pr,6);
    bkParts(ctx,P,dt||0); }
  return { start(){ reset(); s.run=true; sound(); loop.start(); }, stop(){ loop.stop(); fx.clear(); }, preview(){ reset(); draw(0); }, get s(){ return s; }, hit(dur){ if(!s||!s.run) return; judge(s.t,dur||80); } }; }
setTimeout(()=>{ try{ if(typeof QI!=='undefined'){ QI.vaa='<path d="M2 17 q12 6 24 0 l-2 -3 h-20z" fill="#6B4A2A"/><path d="M6 14 l-2 -6 M18 14 l-2 -6 M3 8 h18" stroke="#5C3A1E" stroke-width="1.6" fill="none"/><path d="M2 22 q3 -2 6 0 t6 0 t6 0 t6 0" stroke="#2F8FB0" stroke-width="2" fill="none"/>';
      const _qa5=qActs; qActs=function(){ const a=_qa5.apply(this,arguments); if(curPlace==='tai') a.push({k:'vaa',l:'Vaʻa',t:'Le vaʻa : pagayer ensemble',go:openVaa}); return a; }; dockRender(); } }catch(e){} },300);

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
