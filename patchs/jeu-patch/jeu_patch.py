# Patch "les jeux de la cour : basket, tirs au but, ping-pong — version 2 (geste direct, physique, feedback)".
# Base : v91 ou plus. Usage : python3 jeu_patch.py <site>/index.html <manu-ora.html>
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    rep(".pepes{position:absolute;",""".bkst{flex:none;position:relative;border-radius:18px;overflow:hidden;background:#BEE5F6;margin:8px 0}
.bkst canvas{display:block;touch-action:none;user-select:none;-webkit-user-select:none;-webkit-tap-highlight-color:transparent}
.bkst .bkbird{position:absolute;left:3%;bottom:10px;width:56px;pointer-events:none}
.bkfx{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.bkpop{position:absolute;transform:translate(-50%,-50%);font-family:var(--display);font-weight:900;font-size:1.2rem;color:#16303B;text-shadow:0 1px 0 #fff,0 0 10px #fff;animation:bkPop 1s ease-out forwards;white-space:nowrap}
.bkpop.big{font-size:1.9rem}
@keyframes bkPop{from{opacity:0;transform:translate(-50%,-30%) scale(.6)}18%{opacity:1;transform:translate(-50%,-50%) scale(1.12)}to{opacity:0;transform:translate(-50%,-160%) scale(1)}}
.bkflash{position:absolute;inset:0;background:#fff;opacity:.4;animation:bkFlash .1s ease-out forwards}
@keyframes bkFlash{to{opacity:0}}
.bktxt{text-align:center;font-weight:800;min-height:2.6em;margin:4px 0 8px}
.bkdots{display:flex;gap:8px;justify-content:center;margin:4px 0}.bkdots span{width:16px;height:16px;border-radius:50%;border:2px solid var(--line,#cfd8d6)}.bkdots span.in{background:#F08A2B;border-color:#F08A2B}.bkdots span.out{background:#DDE5E4}
.bkpick{display:grid;gap:10px;margin-top:6px}.bkpick button{display:block;width:100%;text-align:left;line-height:1.35}
@media (prefers-reduced-motion:reduce){.bkpop{animation:none;opacity:1}.bkflash{display:none}}
.pepes{position:absolute;""")
    rep("${curPlace==='vai'?vaiButtons():''}","${curPlace==='vai'?vaiButtons():''}${curPlace==='haapii'?'<button class=\"btn\" id=\"plBall\">Jouer dans la cour : basket, foot, ping-pong</button>':''}")
    rep("{ const sf=$('#plSurf'); if(sf) sf.onclick=()=>openSurf();","{ const bk=$('#plBall'); if(bk) bk.onclick=()=>openYardGames(); const sf=$('#plSurf'); if(sf) sf.onclick=()=>openSurf();")
    rep("    else if(v.g==='pardon'){ for(let i=0;i<6;i++)","    else if(v.g==='jeu'){ setTimeout(()=>bkInvite(v),9200); }\n    else if(v.g==='jeuOk'){ bkTeamDone(v); for(let i=0;i<8;i++) setTimeout(()=>petal(mx+(Math.random()*60-30),my-10),i*180); }\n    else if(v.g==='pardon'){ for(let i=0;i<6;i++)")
    rep(":(tupLine(v)||duoLine(v)||direLine(v)||GEST[v.g].t)}",":(tupLine(v)||duoLine(v)||direLine(v)||bkLine(v)||GEST[v.g].t)}")
    rep("if(m.indexOf('love:')===0){ loveBtn(m.slice(5)); return; }","if(m.indexOf('bk:')===0){ bkBtn(m.split(':')); return; } if(m.indexOf('love:')===0){ loveBtn(m.slice(5)); return; }")
    new = r"""/* ---------- les jeux de la cour (v2) : basket, tirs au but, ping-pong — geste direct, physique, seul ou à deux, sans classement ---------- */
GEST.jeu={l:'', t:'tʼinvite à jouer dans la cour.'}; GEST.jeuOk={l:'', t:'a fini la partie à deux.'}; GEST.bravo={l:'', t:'te dit : bien joué !'};
let BK={};
const BK_N=5;
const SP={
 b:{name:'Le panier de basket', u:n=>`${n} panier${n>1?'s':''}`, un:'paniers', vb:'a marqué', turn:'Tir', go:'Prendre le ballon', stageH:300,
    tip:'Glisse ton doigt du ballon vers le panier, puis lâche. Plus le geste est long, plus le tir est fort.',
    intro:'Cinq tirs. Glisse le doigt pour lancer : la direction et la longueur du geste font le tir. Le panier change de place à chaque fois.',
    learn:'Ce que le jeu apprend : un tir raté ne dit rien du suivant. On le laisse derrière soi, on respire, et on retire.',
    carry:'Je porte le ballon à ', end:'Bien joué. Raté ou réussi, tu as tiré tes cinq ballons.'},
 f:{name:'Les tirs au but', u:n=>`${n} but${n>1?'s':''}`, un:'buts', vb:'a marqué', turn:'Tir', go:'Poser le ballon', stageH:280,
    tip:'Regarde de quel côté penche le tupa, puis glisse ton doigt du ballon jusquʼau coin libre. Le ballon part là où ton doigt sʼarrête.',
    intro:'Cinq tirs au but. Le tupa garde la cage et penche vers le côté où il va plonger. Regarde-le, puis glisse ton doigt du ballon jusquʼau coin libre : le ballon part là où ton doigt sʼarrête. Un geste vif part plus vite. Parfois, il feinte.',
    learn:'Ce que le jeu apprend : regarder avant dʼagir. Une seconde pour lire la situation, puis on y va franchement.',
    carry:'Je porte le ballon à ', end:'Bien joué. Tu as pris le temps de regarder avant de tirer.'},
 p:{name:'Le ping-pong', u:n=>`${n} échange${n>1?'s':''}`, un:'échanges réussis', vb:'a réussi', turn:'Balle', go:'Prendre la raquette', stageH:320,
    tip:'Glisse le doigt pour déplacer ta raquette. Cinq renvois, et lʼéchange est réussi.',
    intro:'Cinq balles. Ton manu sert, tu renvoies, il renvoie… Tenez lʼéchange ensemble jusquʼà cinq renvois. La balle accélère un peu à chaque coup, et le bord de la raquette lʼenvoie de biais.',
    learn:'Ce que le jeu apprend : répondre au bon moment, en regardant la balle plutôt que sa raquette. Dans une discussion, cʼest pareil : on écoute, puis on répond.',
    carry:'Je porte la raquette à ', end:'Bien joué. Trouver le bon moment, ça sʼapprend balle après balle.'}
};
function bkScore(p){ const m=/^([bfp])(\d)(?::(\d))?$/.exec(String(p||'')); return m ? {k:m[1], a:Math.min(BK_N,+m[2]), b:m[3]===undefined?null:Math.min(BK_N,+m[3])} : null; }
function bkLine(v){ const q=bkScore(v.p); if(!q) return null; const S=SP[q.k];
  if(v.g==='jeu') return `${S.vb} <b>${S.u(q.a)}</b> sur ${BK_N} (${S.name.toLowerCase()}) et tʼinvite à jouer avec lui.`;
  if(v.g==='jeuOk') return q.b!==null ? `a joué à son tour : à vous deux, <b>${q.a+q.b}</b> ${S.un} sur ${BK_N*2} !` : null; return null; }
function bkInvite(v){ const q=bkScore(v.p); if(!q) return; if(!visitFree() || bubbleEl.classList.contains('show')){ setTimeout(()=>bkInvite(v),5000); return; } const S=SP[q.k];
  sayHTML(`${esc(v.name)} ${S.vb} ${S.u(q.a)} (${S.name.toLowerCase()}) et tʼattend pour finir la partie. On additionne : ce nʼest pas lʼun contre lʼautre, cʼest vous deux ensemble.<div class="mini"><button data-m="bk:go:${v.from}:${q.a}:${q.k}">Jouer à mon tour</button><button data-m="bk:no">Plus tard</button></div>`, 40000); }
function bkTeamDone(v){ const q=bkScore(v.p); if(!q || q.b===null) return; const o=store.get('bkOut',{})||{}; if(!o[v.from]) return; delete o[v.from]; store.set('bkOut',o); bkReward(); setTimeout(()=>bkTeamSay(v,q,0), 9200); }
function bkTeamSay(v,q,n){ if(n>14) return; if(!visitFree() || bubbleEl.classList.contains('show')){ setTimeout(()=>bkTeamSay(v,q,n+1),5000); return; } sayHTML(`À vous deux : <b>${q.a+q.b}</b> sur ${BK_N*2}. ${q.a+q.b>=7?'Belle équipe !':'Lʼimportant, cʼest dʼavoir joué ensemble.'}<div class="mini"><button data-m="bk:bravo:${v.from}">Lui dire « bien joué »</button></div>`, 30000); }
function bkReward(){ try{ const k=dayKey(Date.now()); if(store.get('bkDay','')!==k){ store.set('bkDay',k); feathers+=1; store.set('feathers',feathers); renderFeathers(); const m=store.get('placeDays',{})||{}, a=Array.isArray(m.haapii)?m.haapii:[]; if(!a.includes(k)){ a.push(k); m.haapii=a.slice(-60); store.set('placeDays',m); } } }catch(e){} }
function bkBtn(a){ bubbleEl.classList.remove('show'); if(a[1]==='go'){ const f=friends.find(x=>x.code===a[2]); if(f) openSport(SP[a[4]]?a[4]:'b',{code:f.code, name:f.name||fmtCode(f.code), their:Math.min(BK_N,+a[3]||0)}); } else if(a[1]==='bravo'){ const f=friends.find(x=>x.code===a[2]); if(f) sendGesture(f.code,'bravo',f.name||fmtCode(f.code)); } }
function bkHead(t){ return `<div class="head"><div><div class="eyebrow">Te fare haʻapiʻiraʻa · la cour</div><h2>${t}</h2></div><button class="x" id="sx" aria-label="Fermer">×</button></div>`; }
function bkStopGame(){ try{ if(BK.game){ BK.game.stop(); BK.game=null; } }catch(e){} clearTimeout(BK.tm); }
function bkQuit(){ bkStopGame(); BK.i=-1; closeSheet(); }
function openYardGames(){ bkStopGame(); BK={};
  openSheet(bkHead('Jouer dans la cour')+`<p>Trois jeux, cinq essais chacun. Seul·e, ou avec un cœur lié : à deux, vos scores sʼadditionnent.</p><div class="bkpick"><button class="btn" data-k="b"><b>Le panier de basket</b><br><span class="small muted">Rater, et tirer quand même le suivant.</span></button><button class="btn" data-k="f"><b>Les tirs au but</b><br><span class="small muted">Regarder avant dʼagir.</span></button><button class="btn" data-k="p"><b>Le ping-pong</b><br><span class="small muted">Répondre au bon moment.</span></button></div>`);
  $('#sx').onclick=()=>closeSheet(); sheetInner.querySelectorAll('[data-k]').forEach(b=>b.onclick=()=>openSport(b.dataset.k,null)); }
function openBasket(team){ openSport('b',team); }
function openSport(k,team){ bkStopGame(); BK={k:SP[k]?k:'b', i:0, res:[], team:team||null, game:null, tm:0, ending:false}; bkStep(); }
function bkStage(){ const S=SP[BK.k], k=BK.k; const bird = k==='p' ? 'left:6px;top:4px;bottom:auto;width:40px' : k==='f' ? 'left:5%;bottom:4px;width:46px' : 'left:2%;bottom:8px;width:56px';
  return `<div class="bkst" id="bkSt" style="height:${S.stageH}px"><canvas id="bkCv" role="img" aria-label="${esc(S.name)}"></canvas><div class="bkbird" style="${bird}">${birdSVG(cfg,'bk')}</div></div>`; }
function bkMount(){ const st=$('#bkSt'), cv=$('#bkCv'); if(!st||!cv) return null; const W=st.clientWidth||340, H=st.clientHeight||SP[BK.k].stageH, dpr=Math.min(2,window.devicePixelRatio||1); cv.width=Math.round(W*dpr); cv.height=Math.round(H*dpr); cv.style.width=W+'px'; cv.style.height=H+'px'; const ctx=cv.getContext('2d'); ctx.setTransform(dpr,0,0,dpr,0,0); return {st,cv,ctx,W,H}; }
function bkFx(st,cv){ let box=st.querySelector('.bkfx'); if(!box){ box=document.createElement('div'); box.className='bkfx'; st.appendChild(box); }
  return { pop(t,x,y,c,big){ const d=document.createElement('div'); d.className='bkpop'+(big?' big':''); d.textContent=t; d.style.left=x+'px'; d.style.top=y+'px'; if(c) d.style.color=c; box.appendChild(d); setTimeout(()=>d.remove(),1100); },
    shake(px,ms){ if(RM) return; const t0=performance.now(); const f=()=>{ const k=1-(performance.now()-t0)/ms; if(k<=0 || !cv.isConnected){ cv.style.transform=''; return; } cv.style.transform=`translate(${(Math.random()*2-1)*px*k}px,${(Math.random()*2-1)*px*k}px)`; requestAnimationFrame(f); }; f(); },
    flash(){ if(RM) return; const d=document.createElement('div'); d.className='bkflash'; box.appendChild(d); setTimeout(()=>d.remove(),140); },
    clear(){ box.innerHTML=''; cv.style.transform=''; } }; }
function bkBurst(P,x,y,n,cols){ if(RM) return; for(let i=0;i<n;i++){ const a=Math.random()*Math.PI*2, v=120+Math.random()*220; P.push({x,y,vx:Math.cos(a)*v,vy:Math.sin(a)*v-90,life:.5+Math.random()*.45,t:0,c:cols[i%cols.length],r:2+Math.random()*2.5}); } }
function bkParts(ctx,P,dt){ for(let i=P.length-1;i>=0;i--){ const p=P[i]; p.t+=dt; if(p.t>p.life){ P.splice(i,1); continue; } p.vy+=600*dt; p.x+=p.vx*dt; p.y+=p.vy*dt; ctx.globalAlpha=Math.max(0,1-p.t/p.life); ctx.fillStyle=p.c; ctx.beginPath(); ctx.arc(p.x,p.y,p.r,0,Math.PI*2); ctx.fill(); } ctx.globalAlpha=1; }
function bkLoop(fn){ let raf=0, last=0, on=false; const tick=t=>{ if(!on) return; const dt=Math.min(.034,Math.max(.001,(t-last)/1000)); last=t; try{ fn(dt,t); }catch(e){} raf=requestAnimationFrame(tick); }; return { start(){ if(on) return; on=true; last=performance.now(); raf=requestAnimationFrame(tick); }, stop(){ on=false; cancelAnimationFrame(raf); } }; }
function bkPointer(cv,h){ let id=null, p0=null, t0=0; const pt=e=>{ const r=cv.getBoundingClientRect(); return {x:e.clientX-r.left, y:e.clientY-r.top}; };
  cv.addEventListener('pointerdown', e=>{ if(id!==null) return; id=e.pointerId; try{ cv.setPointerCapture(id); }catch(x){} p0=pt(e); t0=performance.now(); e.preventDefault(); if(h.down) h.down(p0); });
  cv.addEventListener('pointermove', e=>{ const p=pt(e); if(id!==null && e.pointerId===id){ if(h.drag) h.drag(p0,p); } else if(id===null && e.pointerType==='mouse' && h.hover) h.hover(p); });
  const up=e=>{ if(id===null || e.pointerId!==id) return; const p=pt(e); id=null; if(h.up) h.up(p0,p,performance.now()-t0); };
  cv.addEventListener('pointerup',up); cv.addEventListener('pointercancel',up); }
function bkRR(ctx,x,y,w,h,r){ ctx.beginPath(); ctx.moveTo(x+r,y); ctx.lineTo(x+w-r,y); ctx.arcTo(x+w,y,x+w,y+r,r); ctx.lineTo(x+w,y+h-r); ctx.arcTo(x+w,y+h,x+w-r,y+h,r); ctx.lineTo(x+r,y+h); ctx.arcTo(x,y+h,x,y+h-r,r); ctx.lineTo(x,y+r); ctx.arcTo(x,y,x+r,y,r); ctx.closePath(); }
function bkBallDraw(ctx,x,y,r){ ctx.fillStyle='#F08A2B'; ctx.beginPath(); ctx.arc(x,y,r,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#8A4A12'; ctx.lineWidth=1.2; ctx.stroke(); ctx.lineWidth=1; ctx.beginPath(); ctx.moveTo(x-r,y); ctx.lineTo(x+r,y); ctx.moveTo(x,y-r); ctx.lineTo(x,y+r); ctx.moveTo(x-r*.72,y-r*.7); ctx.quadraticCurveTo(x-r*.1,y,x-r*.72,y+r*.7); ctx.moveTo(x+r*.72,y-r*.7); ctx.quadraticCurveTo(x+r*.1,y,x+r*.72,y+r*.7); ctx.stroke(); }
function bkFootDraw(ctx,x,y,r){ ctx.fillStyle='#fff'; ctx.beginPath(); ctx.arc(x,y,r,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#22323A'; ctx.lineWidth=1.1; ctx.stroke(); ctx.fillStyle='#22323A'; ctx.beginPath(); for(let i=0;i<5;i++){ const a=-Math.PI/2+i*Math.PI*2/5; const px=x+Math.cos(a)*r*.42, py=y+Math.sin(a)*r*.42; if(i) ctx.lineTo(px,py); else ctx.moveTo(px,py); } ctx.closePath(); ctx.fill(); }
const BK_GAMES={};
/* basket : glisser pour lancer, gravité, cercle, planche, filet */
BK_GAMES.b=function(G,fx,api){ const {cv,ctx,W,H}=G, g=1500, R=10, RIM=27; let s=null, P=[], net=0, streak=0, preview=[]; const loop=bkLoop(update);
  function hoopFor(i){ const bands=[[.70,.42],[.65,.36],[.76,.47],[.71,.32],[.78,.40]]; const b=bands[(i-1)%bands.length]; return {cx:W*(b[0]+Math.random()*.06-.03), ry:H*(b[1]+Math.random()*.05-.025)}; }
  function reset(){ const i=api.level(); const h=hoopFor(i); s={b:{x:W*.2,y:H-R-8,vx:0,vy:0,py:H-R-8}, flying:false, t:0, hoop:h, rim:false, board:false, high:false, maxX:0, scored:false, ended:false, drag:null, freeze:0, moving:streak>=3, drift:Math.random()*6.28}; preview=[]; }
  const hx=()=>s.hoop.cx+(s.moving?Math.sin(s.drift)*22:0);
  function phys(b,dt,cx,ry){ b.vy+=g*dt; b.x+=b.vx*dt; b.y+=b.vy*dt; const f0=cx-RIM, b1=cx+RIM, bd=b1+12; let ev='';
    if(b.x+R>bd && b.y>ry-80 && b.y<ry+16 && b.vx>0){ b.x=bd-R; b.vx=-b.vx*.5; ev='board'; }
    for(const rx of [f0,b1]){ const dx=b.x-rx, dy=b.y-ry, d=Math.hypot(dx,dy); if(d>0 && d<R+3){ const nx=dx/d, ny=dy/d, dot=b.vx*nx+b.vy*ny; if(dot<0){ b.vx-=1.55*dot*nx; b.vy-=1.55*dot*ny; } b.x=rx+nx*(R+3); b.y=ry+ny*(R+3); ev=ev||'rim'; } }
    if(b.py<ry && b.y>=ry && b.vy>0 && b.x>f0+6 && b.x<b1-6) ev='score';
    if(b.y+R>H-6){ b.y=H-6-R; b.vy=-b.vy*.42; b.vx*=.72; if(Math.abs(b.vy)<70) b.vy=0; ev=ev||'ground'; }
    b.py=b.y; return ev; }
  function sim(vx,vy,maxT){ const b={x:s.b.x,y:s.b.y,vx,vy,py:s.b.y}; const cx=hx(), ry=s.hoop.ry; const out={pts:[],score:false,rim:false,board:false,maxX:b.x}; let t=0, acc=0;
    while(t<maxT){ const ev=phys(b,1/120,cx,ry); t+=1/120; acc+=1/120; if(acc>=.04){ acc=0; out.pts.push({x:b.x,y:b.y}); } if(ev==='rim') out.rim=true; if(ev==='board') out.board=true; out.maxX=Math.max(out.maxX,b.x); if(ev==='score'){ out.score=true; break; } if(maxT<1 && (ev==='rim'||ev==='board')) break; if(b.x>W+40||b.x<-40||(b.vy===0&&b.y>=H-6-R-.5)) break; } return out; }
  function shoot(vx,vy){ if(!s || s.flying) return; const sp=Math.hypot(vx,vy); if(sp>1500){ vx*=1500/sp; vy*=1500/sp; } s.b.vx=vx; s.b.vy=vy; s.flying=true; s.t=0; preview=[]; }
  bkPointer(cv,{ down(p){ if(s && !s.flying) s.drag=p; },
    drag(p0,p){ if(!s || !s.drag || s.flying) return; const dx=p.x-p0.x, dy=p.y-p0.y; preview = (dy<-10 && Math.hypot(dx,dy)>18) ? sim(dx*5.4,dy*5.4,.5).pts.slice(0,12) : []; },
    up(p0,p){ if(!s || !s.drag || s.flying){ preview=[]; return; } s.drag=null; const dx=p.x-p0.x, dy=p.y-p0.y; if(dy<-10 && Math.hypot(dx,dy)>18) shoot(dx*5.4,dy*5.4); else preview=[]; } });
  function onScore(){ s.scored=true; s.ended=true; s.freeze=.07; net=1; streak++; const cx=hx(); bkBurst(P,cx,s.hoop.ry+8,22,['#F2C94C','#F08A2B','#fff']); fx.flash(); const swish=!s.rim&&!s.board; s.b.vx*=.3; s.b.vy*=.5;
    fx.pop(swish?'Que du filet !':s.board?'Avec la planche !':'Panier !', cx, s.hoop.ry-42, '#C8402F', true); api.done(true, (swish?'Que du filet !':s.board?'Avec la planche, ça compte aussi.':'Panier !')+(streak===3?' Trois de suite : le panier se met à bouger.':'')); }
  function onMiss(){ s.ended=true; streak=0; const cx=hx(); let m; if(s.rim) m='Sur le cercle. Si près !'; else if(s.board) m='Trop long, sur la planche.'; else if(s.maxX<cx-RIM-8) m='Trop court.'; else if(!s.high) m='Trop bas.'; else m='Trop long.'; fx.pop('Raté', s.b.x, Math.max(30,s.b.y-34), '#C8402F'); api.done(false, m+' On respire, et on tire le suivant.'); }
  function update(dt,t){ if(!s) return; if(s.moving) s.drift+=dt*1.6;
    if(s.freeze>0) s.freeze-=dt; else if(s.flying){ const cx=hx(), ry=s.hoop.ry; for(let k=0;k<4;k++){ const ev=phys(s.b,dt/4,cx,ry); if(ev==='rim'){ if(!s.rim) fx.shake(2,90); s.rim=true; } else if(ev==='board') s.board=true; else if(ev==='score' && !s.scored) onScore(); } s.t+=dt; if(s.b.y<ry) s.high=true; s.maxX=Math.max(s.maxX,s.b.x);
      if(!s.ended && (s.t>4.5 || s.b.x>W+40 || s.b.x<-40 || (s.b.vy===0 && s.b.y>=H-6-R-.5 && Math.abs(s.b.vx)<8))) onMiss(); }
    net*=Math.pow(.02,dt); draw(t,dt); }
  function draw(t,dt){ const gr=ctx.createLinearGradient(0,0,0,H); gr.addColorStop(0,'#BEE5F6'); gr.addColorStop(.62,'#F7FBF0'); gr.addColorStop(.62,'#EFE3C6'); gr.addColorStop(1,'#E4D5B0'); ctx.fillStyle=gr; ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='#D8C9A2'; ctx.lineWidth=2; ctx.beginPath(); ctx.moveTo(0,H-6); ctx.lineTo(W,H-6); ctx.stroke();
    const cx=hx(), ry=s.hoop.ry, f0=cx-RIM, b1=cx+RIM, bd=b1+12;
    ctx.fillStyle='#8A97A0'; ctx.fillRect(bd+3,ry-40,7,H-6-(ry-40)); ctx.fillStyle='#FFF9EE'; ctx.fillRect(bd,ry-80,7,96); ctx.strokeStyle='#C8402F'; ctx.lineWidth=2; ctx.strokeRect(bd,ry-80,7,96);
    const sway=Math.sin(t/55)*9*net; ctx.strokeStyle='rgba(255,255,255,.95)'; ctx.lineWidth=1.3; ctx.beginPath(); for(let k=0;k<=6;k++){ const x0=f0+(b1-f0)*k/6; const x1=cx+(x0-cx)*.55+sway; ctx.moveTo(x0,ry+1); ctx.lineTo(x1,ry+34); } ctx.moveTo(f0+6+sway*.5,ry+16); ctx.lineTo(b1-6+sway*.5,ry+16); ctx.moveTo(cx-(b1-f0)*.28+sway,ry+34); ctx.lineTo(cx+(b1-f0)*.28+sway,ry+34); ctx.stroke();
    const sh=Math.max(0,.32-(H-6-s.b.y)/H*.3); ctx.fillStyle=`rgba(30,40,50,${sh.toFixed(2)})`; ctx.beginPath(); ctx.ellipse(s.b.x,H-5,R*1.1,3.2,0,0,Math.PI*2); ctx.fill();
    preview.forEach((p,i)=>{ ctx.globalAlpha=.55*(1-i/preview.length); ctx.fillStyle='#fff'; ctx.beginPath(); ctx.arc(p.x,p.y,3,0,Math.PI*2); ctx.fill(); }); ctx.globalAlpha=1;
    bkBallDraw(ctx,s.b.x,s.b.y,R);
    ctx.strokeStyle='#E4583F'; ctx.lineWidth=4; ctx.beginPath(); ctx.moveTo(f0,ry); ctx.lineTo(b1,ry); ctx.stroke(); ctx.fillStyle='#C8402F'; for(const rx of [f0,b1]){ ctx.beginPath(); ctx.arc(rx,ry,3.2,0,Math.PI*2); ctx.fill(); }
    bkParts(ctx,P,dt); }
  return { start(){ reset(); loop.start(); }, next(){ reset(); P=[]; fx.clear(); }, stop(){ loop.stop(); fx.clear(); }, preview(){ reset(); draw(0,0); }, get s(){ return s; }, shoot, sim }; };
/* tirs au but : le tupa penche vers son côté, on lit, puis on glisse vers le coin libre */
BK_GAMES.f=function(G,fx,api){ const {cv,ctx,W,H}=G, gl=H*.66, cy=H*.2, gx0=W*.2, gx1=W*.8, hw=(gx1-gx0)/2, gh=gl-cy; let s=null, P=[], ripple=0; const loop=bkLoop(update);
  function pickIntent(){ const i=api.level(); const side=Math.random()<.12?0:(Math.random()<.5?-1:1); s.feint = i>=3 && Math.random()<.2; s.intent=side; s.dive=s.feint?-side:side; s.leanT=1.5+Math.random()*1.4; }
  function reset(){ s={ball:{x:W/2,y:H-26,r:13}, phase:'aim', t:0, intent:0, lean:0, leanT:0, feint:false, dive:0, dSide:0, dX:0, diveK:0, late:false, drag:null, aim:null, tx:0, hgt:0, T:.5, res:'', hold:false, reach:0}; pickIntent(); }
  function target(p0,p){ let tx=p.x, ty=p.y; const y0=s.ball.y; if(ty>gl-8){ const k=(y0-(gl-8))/Math.max(1,(y0-ty)); tx=s.ball.x+(p.x-s.ball.x)*k; ty=gl-8; } return {tx:Math.max(gx0-60,Math.min(gx1+60,tx)), hgt:Math.min(gh+40,Math.max(8,gl-ty))}; }
  function shoot(p0,p,ms){ const t=target(p0,p); const len=Math.hypot(p.x-p0.x,p.y-p0.y); const spd=len/Math.max(60,ms||200); const T=Math.max(.42, Math.min(.66, .68-spd*.16)); fire(t.tx,t.hgt,T); }
  function fire(tx,hgt,T){ if(!s || s.phase!=='aim') return; s.phase='fly'; s.t=0; s.tx=tx; s.hgt=hgt; s.T=T; s.aim=null; const shotSide = tx<W/2-10?-1:tx>W/2+10?1:0; const i=api.level();
    s.late = T>=.54 && Math.random()<(.2+.08*(i-1)); s.dSide = s.late ? shotSide : s.dive; const reach = s.late ? .5 : (s.dSide===0?.38:.74); s.reach=reach*hw; s.dX=s.dSide*hw*.62;
    let res='goal'; const inX = tx>gx0 && tx<gx1; if(Math.abs(tx-gx0)<7 || Math.abs(tx-gx1)<7) res='post'; else if(!inX) res='wide'; else if(hgt>gh) res='over';
    else { let covered; if(s.dSide===0) covered=Math.abs(tx-W/2)<s.reach; else { const u=(tx-W/2)*s.dSide; covered = u>-hw*.12 && u<s.reach; } if(covered && hgt<gh*.72) res='save'; } s.res=res; }
  bkPointer(cv,{ down(p){ if(s && s.phase==='aim') s.drag=p; }, drag(p0,p){ if(!s||!s.drag||s.phase!=='aim') return; const dx=p.x-p0.x, dy=p.y-p0.y; if(dy<-20 && Math.hypot(dx,dy)>24){ const t=target(p0,p); s.aim={tx:t.tx, ty:gl-t.hgt}; } else s.aim=null; },
    up(p0,p,ms){ if(!s||!s.drag) return; s.drag=null; s.aim=null; const dx=p.x-p0.x, dy=p.y-p0.y; if(s.phase==='aim' && dy<-20 && Math.hypot(dx,dy)>24) shoot(p0,p,ms); } });
  function onRes(){ const r=s.res;
    if(r==='goal'){ ripple=1; s.ended=true; bkBurst(P,s.tx,gl-s.hgt,24,['#fff','#F2C94C','#3B8C58']); fx.flash(); const luc=s.hgt>gh*.72 && Math.abs(s.tx-W/2)>hw*.6; fx.pop(luc?'Lucarne !':'But !', s.tx, cy-16, '#C8402F', true); api.done(true, luc?'Lucarne ! Haut et précis : imparable.':s.late?'But ! Il a plongé tard, tu as été plus rapide.':'But ! Tu as tiré là où il nʼétait pas.'); }
    else if(r==='save'){ s.hold=true; fx.shake(2,80); fx.pop('Arrêté', W/2+s.dX, gl-34, '#16303B'); api.done(false, s.feint?'Il a feinté : il penchait dʼun côté et a plongé de lʼautre. Ça arrive. On regarde encore, et on retire.':s.late?'Arrêté : il a attendu ton geste. Un tir plus franc passe avant lui.':'Arrêté : tu as tiré du côté où il penchait. Regarde-le, puis vise lʼautre coin.'); }
    else if(r==='post'){ fx.shake(3,110); fx.pop('Poteau !', s.tx, cy+gh/2, '#16303B'); api.done(false,'Sur le poteau ! Si près. Vise un peu plus à lʼintérieur.'); }
    else if(r==='wide'){ fx.pop('À côté', s.tx<W/2?gx0-10:gx1+10, cy+gh/2, '#16303B'); api.done(false,'À côté. Un geste un peu moins large, la prochaine fois.'); }
    else { fx.pop('Au-dessus', s.tx, cy-14, '#16303B'); api.done(false,'Au-dessus ! Un geste plus court garde le ballon sous la barre.'); } }
  function update(dt,t){ if(!s) return;
    if(s.phase==='aim'){ s.leanT-=dt; if(s.leanT<=0) pickIntent(); s.lean+=(s.intent-s.lean)*Math.min(1,dt*5); }
    else if(s.phase==='fly'){ s.t+=dt; const k=Math.min(1,s.t/s.T); const ex=s.tx, ey=gl-s.hgt, y0=H-26; s.ball.x=W/2+(ex-W/2)*k; s.ball.y=y0+(ey-y0)*k-Math.sin(k*Math.PI)*s.hgt*.25; s.ball.r=13-6*k; const d0=s.late?.35:0; s.diveK=Math.max(0,Math.min(1,(s.t/s.T-d0)/(1-d0))); if(k>=1){ s.phase='res'; s.t=0; onRes(); } }
    else if(s.phase==='res'){ s.t+=dt; if(s.res==='post'){ s.ball.x+=(W/2-s.ball.x)*dt*2; s.ball.y+=150*dt; } else if(s.res==='wide'||s.res==='over'){ s.ball.x+=(s.tx-W/2)*dt*1.4; s.ball.y-=70*dt; } else if(s.res==='goal'){ s.ball.y+=(gl-8-s.ball.y)*dt*4; } }
    ripple*=Math.pow(.03,dt); draw(t,dt); }
  function tupa(x,y,rot,ext,side){ ctx.save(); ctx.translate(x,y); ctx.rotate(rot); ctx.strokeStyle='#8E4A2B'; ctx.lineWidth=2.4; ctx.lineCap='round'; ctx.beginPath(); ctx.moveTo(-12,4); ctx.lineTo(-19,12); ctx.moveTo(-8,8); ctx.lineTo(-11,16); ctx.moveTo(12,4); ctx.lineTo(19,12); ctx.moveTo(8,8); ctx.lineTo(11,16); ctx.stroke();
    const claw=(cx0,sgn)=>{ const e = side===sgn ? ext : 0; ctx.fillStyle='#D9713F'; ctx.strokeStyle='#8E4A2B'; ctx.lineWidth=1.2; ctx.beginPath(); ctx.ellipse(cx0+sgn*e,-8-e*.5,7,5,sgn*.5,0,Math.PI*2); ctx.fill(); ctx.stroke(); if(e>2){ ctx.beginPath(); ctx.moveTo(cx0,-2); ctx.lineTo(cx0+sgn*e,-8-e*.5); ctx.stroke(); } }; claw(-13,-1); claw(13,1);
    ctx.fillStyle='#D9713F'; ctx.strokeStyle='#8E4A2B'; ctx.lineWidth=1.4; ctx.beginPath(); ctx.ellipse(0,0,15,10,0,0,Math.PI*2); ctx.fill(); ctx.stroke();
    ctx.strokeStyle='#8E4A2B'; ctx.lineWidth=1.6; ctx.beginPath(); ctx.moveTo(-5,-9); ctx.lineTo(-5,-15); ctx.moveTo(5,-9); ctx.lineTo(5,-15); ctx.stroke(); for(const ex of [-5,5]){ ctx.fillStyle='#fff'; ctx.beginPath(); ctx.arc(ex,-16,2.6,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#22323A'; ctx.lineWidth=1; ctx.stroke(); ctx.fillStyle='#22323A'; ctx.beginPath(); ctx.arc(ex+side*.8,-16,1,0,Math.PI*2); ctx.fill(); }
    ctx.strokeStyle='#8E4A2B'; ctx.lineWidth=1.3; ctx.beginPath(); ctx.moveTo(-5,3); ctx.quadraticCurveTo(0,6,5,3); ctx.stroke(); ctx.restore(); }
  function draw(t,dt){ const gr=ctx.createLinearGradient(0,0,0,H); const hz=(cy-14)/H; gr.addColorStop(0,'#BEE5F6'); gr.addColorStop(hz,'#F7FBF0'); gr.addColorStop(hz,'#9CCB7A'); gr.addColorStop(1,'#7FB661'); ctx.fillStyle=gr; ctx.fillRect(0,0,W,H);
    ctx.strokeStyle='rgba(255,255,255,.75)'; ctx.lineWidth=1; ctx.beginPath(); for(let x=gx0+12;x<gx1;x+=13){ ctx.moveTo(x,cy); ctx.lineTo(x,gl); } for(let y=cy+12;y<gl;y+=12){ const o=Math.sin(y*.25+t/40)*5*ripple; ctx.moveTo(gx0,y+o); ctx.lineTo(gx1,y+o); } ctx.stroke();
    ctx.strokeStyle='#fff'; ctx.lineWidth=6; ctx.lineJoin='round'; ctx.beginPath(); ctx.moveTo(gx0,gl); ctx.lineTo(gx0,cy); ctx.lineTo(gx1,cy); ctx.lineTo(gx1,gl); ctx.stroke(); ctx.strokeStyle='#B9C4C9'; ctx.lineWidth=1.2; ctx.stroke();
    ctx.strokeStyle='rgba(255,255,255,.85)'; ctx.lineWidth=2; ctx.beginPath(); ctx.moveTo(0,gl+2); ctx.lineTo(W,gl+2); ctx.stroke();
    if(s.aim){ ctx.setLineDash([5,6]); ctx.strokeStyle='rgba(255,255,255,.8)'; ctx.lineWidth=2; ctx.beginPath(); ctx.moveTo(s.ball.x,s.ball.y); ctx.lineTo(s.aim.tx,s.aim.ty); ctx.stroke(); ctx.setLineDash([]); ctx.beginPath(); ctx.arc(s.aim.tx,s.aim.ty,8,0,Math.PI*2); ctx.stroke(); }
    const aim=s.phase==='aim'; const kx=W/2+(aim?s.lean*16:s.dX*s.diveK), ky=gl-6, rot=aim?s.lean*.2:s.dSide*.55*s.diveK, ext=aim?0:s.diveK*26; tupa(kx,ky,rot,ext,aim?Math.sign(s.lean)||0:s.dSide);
    if(s.hold){ bkFootDraw(ctx,kx+s.dSide*18,ky-12,7); } else bkFootDraw(ctx,s.ball.x,s.ball.y,s.ball.r);
    bkParts(ctx,P,dt); }
  return { start(){ reset(); loop.start(); }, next(){ reset(); P=[]; fx.clear(); }, stop(){ loop.stop(); fx.clear(); }, preview(){ reset(); s.lean=.6; draw(0,0); }, get s(){ return s; }, fire, shoot }; };
/* ping-pong : vue de dessus, raquette au doigt, angle selon le point dʼimpact, balle qui accélère */
BK_GAMES.p=function(G,fx,api){ const {cv,ctx,W,H}=G, TX0=12, TX1=W-12, TY0=8, TY1=H-8, PW=58, PH=10, R=6, NEED=5; let s=null, P=[], trail=[]; const loop=bkLoop(update);
  const clampPad=x=>Math.max(TX0+PW/2,Math.min(TX1-PW/2,x));
  function reset(){ const i=api.level(); const v0=H*.6*(1+.07*(i-1)); s={ball:{x:W/2,y:TY0+26,vx:0,vy:0}, v0, v:v0, pad:{x:W/2,sq:0}, manu:{x:W/2,sq:0,target:W/2,aim:0}, ret:0, phase:'serve', t:0, serveT:.8, catching:false, ended:false}; trail=[]; }
  function serve(){ const a=(Math.random()*50-25)*Math.PI/180; s.v=s.v0; s.ball.x=s.manu.x; s.ball.y=TY0+26; s.ball.vx=Math.sin(a)*s.v; s.ball.vy=Math.cos(a)*s.v; s.phase='play'; s.manu.sq=.1; s.manu.aim=(Math.random()*2-1)*PW*.35; }
  function setPad(x){ if(s) s.pad.x=clampPad(x); }
  bkPointer(cv,{ down(p){ setPad(p.x); }, drag(p0,p){ setPad(p.x); }, hover(p){ setPad(p.x); } });
  function onOk(){ s.ended=true; fx.flash(); bkBurst(P,s.ball.x,s.ball.y,20,['#F2C94C','#fff','#3B8C58']); fx.pop('Échange réussi !', W/2, H/2, '#3B8C58', true); api.done(true, `Échange réussi : ${NEED} renvois, et ton manu attrape la balle. Bel échange !`); }
  function onMiss(){ s.ended=true; fx.pop('Passée', Math.max(30,Math.min(W-30,s.ball.x)), TY1-40, '#C8402F'); api.done(false, s.ret===0?'Passée. Regarde la balle arriver, et place la raquette dessous.':`Passée après ${s.ret} renvoi${s.ret>1?'s':''}. Elle allait vite : la suivante repart doucement.`); }
  function update(dt,t){ if(!s) return; const b=s.ball;
    if(s.phase==='serve'){ s.t+=dt; if(s.t>s.serveT) serve(); }
    else if(s.phase==='play'){ b.x+=b.vx*dt; b.y+=b.vy*dt;
      if(b.x<TX0+R){ b.x=TX0+R; b.vx=Math.abs(b.vx); } if(b.x>TX1-R){ b.x=TX1-R; b.vx=-Math.abs(b.vx); }
      const py=TY1-20; if(b.vy>0 && b.y+R>=py-PH/2 && b.y-R<=py+PH/2 && Math.abs(b.x-s.pad.x)<=PW/2+R){ const off=Math.max(-1,Math.min(1,(b.x-s.pad.x)/(PW/2))); const ang=off*60*Math.PI/180; s.v=Math.min(s.v0*2.3,s.v*1.07); b.vx=Math.sin(ang)*s.v; b.vy=-Math.cos(ang)*s.v; b.y=py-PH/2-R; s.ret++; s.pad.sq=.1; fx.pop(String(s.ret), b.x, py-30, s.ret>=NEED?'#3B8C58':'#16303B'); if(s.ret>=NEED) s.catching=true; }
      const my=TY0+20; if(b.vy<0 && b.y-R<=my+PH/2 && b.y+R>=my-PH/2 && Math.abs(b.x-s.manu.x)<=PW/2+R+2){ if(s.catching){ s.phase='done'; b.vx=0; b.vy=0; b.y=my+PH/2+R; onOk(); } else { const off=Math.max(-1,Math.min(1,(b.x-s.manu.x)/(PW/2))); const ang=off*50*Math.PI/180; b.vx=Math.sin(ang)*s.v; b.vy=Math.cos(ang)*s.v; b.y=my+PH/2+R; s.manu.sq=.1; s.manu.aim=(Math.random()*2-1)*PW*.35; } }
      if(b.vy<0){ const tt=(b.y-my)/(-b.vy); let px=b.x+b.vx*tt; const span=TX1-TX0-2*R; let rel=px-(TX0+R); rel=((rel%(2*span))+2*span)%(2*span); if(rel>span) rel=2*span-rel; px=TX0+R+rel; s.manu.target=px+(s.catching?0:s.manu.aim); } else s.manu.target=W/2+(b.x-W/2)*.3;
      const ms=H*1.2*dt; s.manu.x=clampPad(s.manu.x+Math.max(-ms,Math.min(ms,s.manu.target-s.manu.x)));
      if(!s.ended && b.y-R>TY1+10){ s.phase='done'; onMiss(); }
      trail.push({x:b.x,y:b.y}); if(trail.length>7) trail.shift(); }
    s.pad.sq=Math.max(0,s.pad.sq-dt); s.manu.sq=Math.max(0,s.manu.sq-dt); draw(t,dt); }
  function paddle(x,y,sq,col,handleDown){ ctx.save(); ctx.translate(x,y); ctx.scale(1-sq*1.6,1+sq*3); ctx.fillStyle=col; bkRR(ctx,-PW/2,-PH/2,PW,PH,5); ctx.fill(); ctx.fillStyle='#B98552'; ctx.fillRect(-4,handleDown?PH/2-1:-PH/2-13,8,14); ctx.restore(); }
  function draw(t,dt){ ctx.fillStyle='#EFE3C6'; ctx.fillRect(0,0,W,H); ctx.fillStyle='#2F7A5B'; bkRR(ctx,TX0,TY0,TX1-TX0,TY1-TY0,8); ctx.fill(); ctx.strokeStyle='rgba(255,255,255,.9)'; ctx.lineWidth=2; ctx.strokeRect(TX0+4,TY0+4,TX1-TX0-8,TY1-TY0-8); ctx.beginPath(); ctx.moveTo(W/2,TY0+4); ctx.lineTo(W/2,TY1-4); ctx.lineWidth=1; ctx.stroke();
    ctx.fillStyle='#F4FAF8'; ctx.fillRect(TX0-2,H/2-2,TX1-TX0+4,4); ctx.fillStyle='#22323A'; ctx.fillRect(TX0-4,H/2-6,4,12); ctx.fillRect(TX1,H/2-6,4,12);
    for(let i=0;i<NEED;i++){ ctx.fillStyle=i<s.ret?'#F2C94C':'rgba(255,255,255,.35)'; ctx.beginPath(); ctx.arc(TX1-12,H/2+34+i*14,4,0,Math.PI*2); ctx.fill(); }
    trail.forEach((p,i)=>{ ctx.globalAlpha=.25*(i+1)/trail.length; ctx.fillStyle='#FFF3D6'; ctx.beginPath(); ctx.arc(p.x,p.y,R*.8,0,Math.PI*2); ctx.fill(); }); ctx.globalAlpha=1;
    paddle(s.manu.x,TY0+20,s.manu.sq,'#2F80D8',false); paddle(s.pad.x,TY1-20,s.pad.sq,'#C8402F',true);
    if(s.phase==='serve'){ ctx.strokeStyle='rgba(255,255,255,.7)'; ctx.lineWidth=2; ctx.beginPath(); ctx.arc(s.manu.x,TY0+26,8+Math.sin(t/120)*3,0,Math.PI*2); ctx.stroke(); }
    ctx.fillStyle='#FFF3D6'; ctx.beginPath(); ctx.arc(s.ball.x,s.ball.y,R,0,Math.PI*2); ctx.fill(); ctx.strokeStyle='#E08A2B'; ctx.lineWidth=1.6; ctx.stroke();
    bkParts(ctx,P,dt); }
  return { start(){ reset(); loop.start(); }, next(){ reset(); P=[]; fx.clear(); }, stop(){ loop.stop(); fx.clear(); }, preview(){ reset(); draw(0,0); }, get s(){ return s; }, setPad }; };
function bkDots(){ const d=$('#bkDots'); if(!d) return; const n=BK.res.filter(x=>x).length; d.setAttribute('aria-label',`${SP[BK.k].u(n)} sur ${BK.res.length}`); d.innerHTML=[0,1,2,3,4].map(i=>`<span class="${BK.res[i]===true?'in':BK.res[i]===false?'out':''}"></span>`).join(''); }
function bkAttemptEnd(ok,msg){ if(BK.ending || BK.i<1) return; BK.ending=true; const my=BK.i; BK.res.push(ok); bkDots(); const tx=$('#bkTxt'); if(tx) tx.textContent=msg;
  BK.tm=setTimeout(()=>{ if(BK.i!==my) return; BK.ending=false; BK.i++; if(BK.i>BK_N){ bkStopGame(); bkStep(); return; } const h=sheetInner.querySelector('h2'); if(h) h.textContent=`${SP[BK.k].turn} ${BK.i} sur ${BK_N}`; if(tx) tx.textContent=SP[BK.k].tip; if(BK.game) BK.game.next(); }, 1600); }
function bkPlay(){ const S=SP[BK.k]; openSheet(bkHead(`${S.turn} ${BK.i} sur ${BK_N}`)+bkStage()+`<div class="bkdots" id="bkDots"></div><p id="bkTxt" class="bktxt" aria-live="polite">${S.tip}</p><button class="btn ghost" id="bkStop">Arrêter</button>`); sheetInner.scrollTop=0; $('#sx').onclick=bkQuit; $('#bkStop').onclick=bkQuit; bkDots();
  const G=bkMount(); if(!G) return; BK.game=BK_GAMES[BK.k](G,bkFx(G.st,G.cv),{level:()=>Math.max(1,BK.i), done:bkAttemptEnd}); BK.game.start(); }
function bkStep(){ const S=SP[BK.k], T=BK.team, n=BK.res.filter(x=>x).length;
  if(BK.i===0){ openSheet(bkHead(T?`À ton tour, avec ${esc(T.name)}`:S.name)+`<p>${T?`${esc(T.name)} ${S.vb} ${S.u(T.their)}. Vos deux scores sʼadditionnent : vous jouez ensemble. `:''}${S.intro}</p>${bkStage()}<button class="btn primary" id="bkGo">${S.go}</button>`); sheetInner.scrollTop=0; $('#sx').onclick=bkQuit;
    try{ const G=bkMount(); if(G) BK_GAMES[BK.k](G,bkFx(G.st,G.cv),{level:()=>1, done:()=>{}}).preview(); }catch(e){} $('#bkGo').onclick=()=>{ BK.i=1; bkPlay(); }; return; }
  if(BK.i>=1 && BK.i<=BK_N){ bkPlay(); return; }
  const tot=T?n+T.their:n;
  const h=bkHead(T?`À vous deux : ${tot} sur ${BK_N*2}`:`${S.u(n)} sur ${BK_N}`)+`<div class="bkdots">${[0,1,2,3,4].map(i=>`<span class="${BK.res[i]===true?'in':BK.res[i]===false?'out':''}"></span>`).join('')}</div><p>${n<=1?'Pas ton jour, et alors ? Tu es resté·e jusquʼau bout, et cʼest ça qui compte.':n<=3?'Des réussis, des ratés : cʼest exactement ça, jouer.':'Belle adresse ! Et tu as vu : même là, tout nʼest pas passé.'}</p><div class="note">${S.learn}</div>`
    +(T?`<p class="small muted">${esc(T.name)} le saura à sa prochaine ouverture de Manu Ora.</p>`:(SYNC_URL && friends.filter(f=>isMutual(f.code)).length?`<div class="card flat"><div class="eyebrow">Jouer à deux</div><p class="small muted">Envoie ton score à un cœur lié : il ou elle joue à son tour, et vos scores sʼadditionnent. Ce nʼest pas un match, cʼest une équipe.</p><div class="row" id="bkFriends">${friends.filter(f=>isMutual(f.code)).map(f=>`<button class="btn sm" data-f="${f.code}">${esc(f.name||fmtCode(f.code))}</button>`).join('')}</div></div>`:''))
    +`<button class="btn primary" id="bkEnd">Māuruuru</button><button class="btn ghost" id="bkAgain">Rejouer</button><button class="btn ghost" id="bkOther">Un autre jeu</button>`;
  openSheet(h); sheetInner.scrollTop=0; $('#sx').onclick=bkQuit;
  $('#bkAgain').onclick=()=>openSport(BK.k,null); $('#bkOther').onclick=()=>openYardGames(); $('#bkEnd').onclick=()=>{ closeSheet(); say(S.end); };
  const kk=BK.k, fr=$('#bkFriends'); if(fr) fr.addEventListener('click', e=>{ const b=e.target.closest('[data-f]'); if(!b) return; const code=b.dataset.f, f=friends.find(x=>x.code===code), nm=f?(f.name||fmtCode(code)):''; fetch(`${SYNC_URL}/visits/${code}/${myCode}.json`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({g:'jeu', p:kk+n, t:Date.now(), name:share.name||''})}).then(r=>{ if(!r.ok){ toast('Envoi impossible, réessaie plus tard'); return; } const o=store.get('bkOut',{})||{}; o[code]={s:n, k:kk, t:Date.now()}; store.set('bkOut',o); closeSheet(); toast('Invitation envoyée'); say(S.carry+nm+' !'); setTimeout(()=>flyAway(nm),1200); }).catch(()=>toast('Pas de connexion, réessaie plus tard')); });
  if(!BK.sent){ BK.sent=true; if(T){ bkReward(); if(SYNC_URL) fetch(`${SYNC_URL}/visits/${T.code}/${myCode}.json`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({g:'jeuOk', p:kk+T.their+':'+n, t:Date.now(), name:share.name||''})}).catch(()=>{}); } else bkReward(); } }
{ const _csBK=closeSheet; closeSheet=function(){ try{ if(BK.game){ BK.game.stop(); BK.game=null; } }catch(e){} return _csBK.apply(this,arguments); }; }

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
