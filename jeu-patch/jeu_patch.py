# Patch "le panier de basket de l'école, seul ou à deux" — à appliquer sur la version en cours (v91 ou plus), sur les DEUX fichiers.
# Usage : python3 jeu_patch.py /home/claude/manu-ora-site/index.html /home/claude/manu-ora.html
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    rep(".pepes{position:absolute;",""".bkst{flex:none;position:relative;height:230px;border-radius:18px;overflow:hidden;background:linear-gradient(#BEE5F6 0%,#F7FBF0 62%,#EFE3C6 62%,#E4D5B0 100%);margin:10px 0}
.bkst svg.bg{position:absolute;inset:0;width:100%;height:100%}
.bkst .bkbird{position:absolute;left:8%;bottom:14px;width:62px}
.bkst .bkball{position:absolute;left:calc(8% + 50px);bottom:58px;width:24px;height:24px;margin:0;will-change:transform}
.bkgauge{position:relative;height:22px;border-radius:11px;background:var(--line,#d7e6e6);overflow:hidden;margin:6px 0 10px}
.bkgauge .ok{position:absolute;top:0;bottom:0;left:30%;width:40%;background:#F2C94C;opacity:.55}.bkgauge .best{position:absolute;top:0;bottom:0;left:42%;width:16%;background:#3B8C58;opacity:.7}
.bkgauge .cur{position:absolute;top:-2px;bottom:-2px;width:6px;margin-left:-3px;border-radius:3px;background:#10303B}
.bkdots{display:flex;gap:8px;justify-content:center;margin:4px 0}.bkdots span{width:16px;height:16px;border-radius:50%;border:2px solid var(--line,#cfd8d6)}.bkdots span.in{background:#F08A2B;border-color:#B55A12}.bkdots span.out{background:#C9D2D8;border-color:#9FB0B6}
.bkst .bkkeep{position:absolute;bottom:80px;width:46px;margin-left:-23px;transition:left .35s}
.bkst .bkball.ft{left:calc(50% - 12px);bottom:14px}
.bkst .bkball.pp{left:0;bottom:0;width:13px;height:13px}
.bkgauge .no{position:absolute;top:0;bottom:0;background:#C8402F;opacity:.5}.bkgauge .post{position:absolute;top:0;bottom:0;width:6%;background:#8A97A0;opacity:.6}
.bkpick{display:grid;gap:10px;margin-top:6px}.bkpick button{display:block;width:100%;text-align:left;line-height:1.35}
.pepes{position:absolute;""")
    rep("${curPlace==='vai'?vaiButtons():''}","${curPlace==='vai'?vaiButtons():''}${curPlace==='haapii'?'<button class=\"btn\" id=\"plBall\">Jouer dans la cour : basket, foot, ping-pong</button>':''}")
    rep("{ const sf=$('#plSurf'); if(sf) sf.onclick=()=>openSurf();","{ const bk=$('#plBall'); if(bk) bk.onclick=()=>openYardGames(); const sf=$('#plSurf'); if(sf) sf.onclick=()=>openSurf();")
    rep("    else if(v.g==='pardon'){ for(let i=0;i<6;i++)","    else if(v.g==='jeu'){ setTimeout(()=>bkInvite(v),9200); }\n    else if(v.g==='jeuOk'){ bkTeamDone(v); for(let i=0;i<8;i++) setTimeout(()=>petal(mx+(Math.random()*60-30),my-10),i*180); }\n    else if(v.g==='bravo'){ for(let i=0;i<6;i++) setTimeout(()=>petal(mx+(Math.random()*50-25),my-10),i*220); }\n    else if(v.g==='pardon'){ for(let i=0;i<6;i++)")
    rep(":(tupLine(v)||duoLine(v)||direLine(v)||GEST[v.g].t)}",":(tupLine(v)||duoLine(v)||direLine(v)||bkLine(v)||GEST[v.g].t)}")
    rep("if(m.indexOf('love:')===0){ loveBtn(m.slice(5)); return; }","if(m.indexOf('bk:')===0){ bkBtn(m.split(':')); return; } if(m.indexOf('love:')===0){ loveBtn(m.slice(5)); return; }")
    new = r"""/* ---------- les jeux de la cour : basket, tirs au but, ping-pong — seul ou à deux, sans classement ---------- */
GEST.jeu={l:'', t:'tʼinvite à jouer dans la cour.'}; GEST.jeuOk={l:'', t:'a fini la partie à deux.'}; GEST.bravo={l:'', t:'te dit : bien joué !'};
let BK={};
const BK_N=5;
const SP={
 b:{name:'Le panier de basket', u:n=>`${n} panier${n>1?'s':''}`, un:'paniers', act:'Tirer', turn:'Tir', go:'Prendre le ballon', tip:'Tire quand le repère est au milieu.',
    intro:'Cinq tirs. Au basket comme ailleurs, on rate plus souvent quʼon ne marque. Ce qui compte, cʼest le tir dʼaprès.',
    learn:'Ce que le jeu apprend : un tir raté ne dit rien du suivant. On le laisse derrière soi, on respire, et on retire.',
    carry:'Je porte le ballon à ', end:'Bien joué. Raté ou réussi, tu as tiré tes cinq ballons.'},
 f:{name:'Les tirs au but', u:n=>`${n} but${n>1?'s':''}`, un:'buts', act:'Tirer', turn:'Tir', go:'Poser le ballon', tip:'Le tupa garde le but. Tire là où il nʼest pas.',
    intro:'Cinq tirs au but. Le tupa change de place à chaque fois : regarde où il est, puis choisis ton côté.',
    learn:'Ce que le jeu apprend : regarder avant dʼagir. Une seconde pour voir où il y a de la place, et ensuite on y va.',
    carry:'Je porte le ballon à ', end:'Bien joué. Tu as pris le temps de regarder avant de tirer.'},
 p:{name:'Le ping-pong', u:n=>`${n} balle${n>1?'s':''}`, un:'balles renvoyées', vb:'a renvoyé', act:'Renvoyer', turn:'Balle', go:'Prendre la raquette', tip:'Renvoie la balle après son rebond de ton côté.',
    intro:'Cinq balles. Ton manu te les envoie, tu les renvoies : ni trop tôt, ni trop tard.',
    learn:'Ce que le jeu apprend : répondre au bon moment. Trop vite, on tape dans le vide ; trop tard, la balle est passée. Dans une discussion, cʼest pareil.',
    carry:'Je porte la raquette à ', end:'Bien joué. Trouver le bon moment, ça sʼapprend balle après balle.'}
};
function bkScore(p){ const m=/^([bfp])(\d)(?::(\d))?$/.exec(String(p||'')); return m ? {k:m[1], a:Math.min(BK_N,+m[2]), b:m[3]===undefined?null:Math.min(BK_N,+m[3])} : null; }
function bkLine(v){ const q=bkScore(v.p); if(!q) return null; const S=SP[q.k];
  if(v.g==='jeu') return `${S.vb||'a marqué'} <b>${S.u(q.a)}</b> sur ${BK_N} (${S.name.toLowerCase()}) et tʼinvite à jouer avec lui.`;
  if(v.g==='jeuOk') return q.b!==null ? `a joué à son tour : à vous deux, <b>${q.a+q.b}</b> ${S.un} sur ${BK_N*2} !` : null; return null; }
function bkInvite(v){ const q=bkScore(v.p); if(!q) return; if(!visitFree() || bubbleEl.classList.contains('show')){ setTimeout(()=>bkInvite(v),5000); return; } const S=SP[q.k];
  sayHTML(`${esc(v.name)} ${S.vb||'a marqué'} ${S.u(q.a)} (${S.name.toLowerCase()}) et tʼattend pour finir la partie. On additionne : ce nʼest pas lʼun contre lʼautre, cʼest vous deux ensemble.<div class="mini"><button data-m="bk:go:${v.from}:${q.a}:${q.k}">Jouer à mon tour</button><button data-m="bk:no">Plus tard</button></div>`, 40000); }
function bkTeamDone(v){ const q=bkScore(v.p); if(!q || q.b===null) return; const o=store.get('bkOut',{})||{}; if(!o[v.from]) return; delete o[v.from]; store.set('bkOut',o); bkReward(); setTimeout(()=>{ if(visitFree()) sayHTML(`À vous deux : <b>${q.a+q.b}</b> sur ${BK_N*2}. ${q.a+q.b>=7?'Belle équipe !':'Lʼimportant, cʼest dʼavoir joué ensemble.'}<div class="mini"><button data-m="bk:bravo:${v.from}">Lui dire « bien joué »</button></div>`, 30000); }, 9200); }
function bkReward(){ try{ const k=dayKey(Date.now()); if(store.get('bkDay','')!==k){ store.set('bkDay',k); feathers+=1; store.set('feathers',feathers); renderFeathers(); const m=store.get('placeDays',{})||{}, a=Array.isArray(m.haapii)?m.haapii:[]; if(!a.includes(k)){ a.push(k); m.haapii=a.slice(-60); store.set('placeDays',m); } } }catch(e){} }
function bkBtn(a){ bubbleEl.classList.remove('show'); if(a[1]==='go'){ const f=friends.find(x=>x.code===a[2]); if(f) openSport(SP[a[4]]?a[4]:'b',{code:f.code, name:f.name||fmtCode(f.code), their:Math.min(BK_N,+a[3]||0)}); } else if(a[1]==='bravo'){ const f=friends.find(x=>x.code===a[2]); if(f) sendGesture(f.code,'bravo',f.name||fmtCode(f.code)); } }
function bkHead(t){ return `<div class="head"><div><div class="eyebrow">Te fare haʻapiʻiraʻa · la cour</div><h2>${t}</h2></div><button class="x" id="sx" aria-label="Fermer">×</button></div>`; }
function bkQuit(){ cancelAnimationFrame(BK.raf); clearTimeout(BK.tm); BK.i=-1; closeSheet(); }
function openYardGames(){ cancelAnimationFrame(BK.raf); clearTimeout(BK.tm); BK={};
  openSheet(bkHead('Jouer dans la cour')+`<p>Trois jeux, cinq essais chacun. Seul·e, ou avec un cœur lié : à deux, vos scores sʼadditionnent.</p><div class="bkpick"><button class="btn" data-k="b"><b>Le panier de basket</b><br><span class="small muted">Rater, et tirer quand même le suivant.</span></button><button class="btn" data-k="f"><b>Les tirs au but</b><br><span class="small muted">Regarder avant dʼagir.</span></button><button class="btn" data-k="p"><b>Le ping-pong</b><br><span class="small muted">Répondre au bon moment.</span></button></div>`);
  $('#sx').onclick=()=>closeSheet(); sheetInner.querySelectorAll('[data-k]').forEach(b=>b.onclick=()=>openSport(b.dataset.k,null)); }
function openBasket(team){ openSport('b',team); }
function openSport(k,team){ cancelAnimationFrame(BK.raf); clearTimeout(BK.tm); BK={k:SP[k]?k:'b', i:0, res:[], team:team||null, busy:false, t0:0, raf:0, tm:0, pos:50, keep:50}; bkStep(); }
const BK_BALL=`<circle cx="12" cy="12" r="11" fill="#F08A2B" stroke="#8A4A12" stroke-width="1.2"/><path d="M1 12 h22 M12 1 v22 M4 4 q8 8 0 16 M20 4 q-8 8 0 16" stroke="#8A4A12" stroke-width="1" fill="none"/>`;
const FT_BALL=`<circle cx="12" cy="12" r="11" fill="#fff" stroke="#22323A" stroke-width="1.2"/><path d="M12 7 l4.6 3.3 -1.8 5.4 h-5.6 l-1.8 -5.4 z" fill="#22323A"/><path d="M12 7 V1.5 M16.6 10.3 l5 -1.8 M14.8 15.7 l3.4 4.6 M9.2 15.7 l-3.4 4.6 M7.4 10.3 l-5 -1.8" stroke="#22323A" stroke-width="1.1"/>`;
const TUPA=`<svg viewBox="0 0 46 34" aria-hidden="true"><path d="M8 22 l-6 6 M11 25 l-4 7 M38 22 l6 6 M35 25 l4 7" stroke="#8E4A2B" stroke-width="2.4" stroke-linecap="round"/><path d="M9 16 q-7 -4 -5 -11 q5 2 6 6 z M37 16 q7 -4 5 -11 q-5 2 -6 6 z" fill="#D9713F" stroke="#8E4A2B" stroke-width="1.2"/><ellipse cx="23" cy="20" rx="15" ry="10" fill="#D9713F" stroke="#8E4A2B" stroke-width="1.4"/><path d="M18 11 v-6 M28 11 v-6" stroke="#8E4A2B" stroke-width="1.6"/><circle cx="18" cy="4.5" r="2.6" fill="#fff" stroke="#22323A" stroke-width="1"/><circle cx="28" cy="4.5" r="2.6" fill="#fff" stroke="#22323A" stroke-width="1"/><circle cx="18" cy="4.5" r="1" fill="#22323A"/><circle cx="28" cy="4.5" r="1" fill="#22323A"/><path d="M18 23 q5 3 10 0" stroke="#8E4A2B" stroke-width="1.4" fill="none" stroke-linecap="round"/></svg>`;
function bkStage(){ const k=BK.k;
  if(k==='f') return `<div class="bkst" id="bkSt" style="background:linear-gradient(#BEE5F6 0%,#F7FBF0 65%,#9CCB7A 65%,#7FB661 100%)"><svg class="bg" viewBox="0 0 320 230" preserveAspectRatio="none" aria-hidden="true"><g stroke="#fff" stroke-width="1" opacity=".75">${[52,76,100,124,148,172,196,220,244,268].map(x=>`<path d="M${x} 46 V150"/>`).join('')}${[62,80,98,116,134].map(y=>`<path d="M40 ${y} H280"/>`).join('')}</g><path d="M40 150 V44 H280 V150" fill="none" stroke="#fff" stroke-width="6" stroke-linejoin="round"/><path d="M40 150 V44 H280 V150" fill="none" stroke="#B9C4C9" stroke-width="1.2"/><path d="M0 150 H320" stroke="#fff" stroke-width="2" opacity=".8"/></svg><div class="bkkeep" id="bkKeep" style="left:${12.5+BK.keep*.75}%">${TUPA}</div><div class="bkbird" style="left:3%;width:48px;bottom:8px">${birdSVG(cfg,'bk')}</div><svg class="bkball ft" id="bkBall" viewBox="0 0 24 24" aria-hidden="true">${FT_BALL}</svg></div>`;
  if(k==='p') return `<div class="bkst" id="bkSt"><svg class="bg" viewBox="0 0 320 230" preserveAspectRatio="none" aria-hidden="true"><path d="M0 178 H320" stroke="#D8C9A2" stroke-width="2"/><rect x="198" y="140" width="64" height="5" fill="#F2C94C" opacity=".8"/><rect x="48" y="140" width="224" height="7" rx="2" fill="#2F7A5B"/><rect x="48" y="140" width="224" height="2" fill="#fff" opacity=".7"/><rect x="158" y="124" width="3" height="18" fill="#22323A"/><rect x="152" y="124" width="15" height="14" fill="#fff" opacity=".55"/><path d="M72 147 V200 M248 147 V200" stroke="#5C6B73" stroke-width="5"/><g transform="translate(284 96) rotate(18)"><rect x="-3" y="20" width="6" height="20" rx="2" fill="#B98552"/><ellipse cx="0" cy="8" rx="13" ry="15" fill="#C8402F" stroke="#7E2318" stroke-width="1.4"/></g></svg><div class="bkbird" style="left:1%;width:52px;bottom:74px">${birdSVG(cfg,'bk')}</div><svg class="bkball pp" id="bkBall" viewBox="0 0 24 24" aria-hidden="true" style="${BK.i>=1&&BK.i<=BK_N?'':'visibility:hidden'}"><circle cx="12" cy="12" r="11" fill="#FFF3D6" stroke="#E08A2B" stroke-width="2"/></svg></div>`;
  return `<div class="bkst" id="bkSt"><svg class="bg" viewBox="0 0 320 230" preserveAspectRatio="none" aria-hidden="true"><rect x="262" y="40" width="8" height="150" fill="#8A97A0"/><rect x="232" y="34" width="44" height="34" rx="3" fill="#FFF9EE" stroke="#C8402F" stroke-width="2.4"/><rect x="246" y="46" width="16" height="13" fill="none" stroke="#C8402F" stroke-width="1.6"/><ellipse cx="238" cy="72" rx="17" ry="4.5" fill="none" stroke="#E4583F" stroke-width="3"/><path d="M222 73 l5 22 M230 76 l2 20 M238 77 v20 M246 76 l-2 20 M254 73 l-5 22 M226 86 h24 M228 95 h20" stroke="#fff" stroke-width="1.3" opacity=".9"/><path d="M0 143 H320" stroke="#D8C9A2" stroke-width="2"/></svg><div class="bkbird">${birdSVG(cfg,'bk')}</div><svg class="bkball" id="bkBall" viewBox="0 0 24 24" aria-hidden="true">${BK_BALL}</svg></div>`; }
function bkGauge(){ const k=BK.k;
  if(k==='f'){ const w=bkKeepW(); return `<div class="bkgauge" aria-hidden="true" style="background:#BFE0AE"><span class="post" style="left:0"></span><span class="post" style="right:0"></span><span class="no" style="left:${BK.keep-w}%;width:${w*2}%"></span><span class="cur" id="bkCur" style="left:50%"></span></div>`; }
  if(k==='p') return `<div class="bkgauge" aria-hidden="true"><span class="ok" style="left:64%;width:34%"></span><span class="best" style="left:72%;width:20%"></span><span class="cur" id="bkCur" style="left:0%"></span></div>`;
  return `<div class="bkgauge" aria-hidden="true"><span class="ok"></span><span class="best"></span><span class="cur" id="bkCur" style="left:50%"></span></div>`; }
function bkKeepW(){ return 10+Math.max(0,BK.i-1)*1.5; }
function bkStep(){ const head=bkHead, S=SP[BK.k], T=BK.team, n=BK.res.filter(x=>x).length; let h='';
  const dots=`<div class="bkdots" aria-label="${S.u(n)} sur ${BK.res.length}">${[0,1,2,3,4].map(i=>`<span class="${BK.res[i]===true?'in':BK.res[i]===false?'out':''}"></span>`).join('')}</div>`;
  if(BK.k==='f' && BK.i>=1 && BK.i<=BK_N && BK.keepFor!==BK.i){ BK.keepFor=BK.i; BK.keep=24+Math.random()*52; }
  if(BK.i===0) h=head(T?`À ton tour, avec ${esc(T.name)}`:S.name)+`<p>${T?`${esc(T.name)} ${S.vb||'a marqué'} ${S.u(T.their)}. Vos deux scores sʼadditionnent : vous jouez ensemble. `:''}${S.intro}</p>${bkStage()}<button class="btn primary" id="bkGo">${S.go}</button>`;
  else if(BK.i<=BK_N) h=head(`${S.turn} ${BK.i} sur ${BK_N}`)+bkStage()+dots+bkGauge()+`<p id="bkTxt" style="text-align:center;font-weight:800;min-height:1.6em" aria-live="polite">${S.tip}</p><button class="btn primary" id="bkShoot">${S.act}</button><button class="btn ghost" id="bkStop">Arrêter</button>`;
  else { const tot=T?n+T.their:n; h=head(T?`À vous deux : ${tot} sur ${BK_N*2}`:`${S.u(n)} sur ${BK_N}`)+bkStage()+dots+`<p>${n<=1?'Pas ton jour, et alors ? Tu es resté·e jusquʼau bout, et cʼest ça qui compte.':n<=3?'Des réussis, des ratés : cʼest exactement ça, jouer.':'Belle adresse ! Et tu as vu : même là, tout nʼest pas passé.'}</p><div class="note">${S.learn}</div>`
      +(T?`<p class="small muted">${esc(T.name)} le saura à sa prochaine ouverture de Manu Ora.</p>`:(SYNC_URL && friends.filter(f=>isMutual(f.code)).length?`<div class="card flat"><div class="eyebrow">Jouer à deux</div><p class="small muted">Envoie ton score à un cœur lié : il ou elle joue à son tour, et vos scores sʼadditionnent. Ce nʼest pas un match, cʼest une équipe.</p><div class="row" id="bkFriends">${friends.filter(f=>isMutual(f.code)).map(f=>`<button class="btn sm" data-f="${f.code}">${esc(f.name||fmtCode(f.code))}</button>`).join('')}</div></div>`:''))
      +`<button class="btn primary" id="bkEnd">Māuruuru</button><button class="btn ghost" id="bkAgain">Rejouer</button><button class="btn ghost" id="bkOther">Un autre jeu</button>`; }
  openSheet(h); sheetInner.scrollTop=0; $('#sx').onclick=bkQuit;
  if($('#bkGo')) $('#bkGo').onclick=()=>{ BK.i=1; bkStep(); };
  if($('#bkStop')) $('#bkStop').onclick=bkQuit;
  if($('#bkAgain')) $('#bkAgain').onclick=()=>openSport(BK.k,null);
  if($('#bkOther')) $('#bkOther').onclick=()=>openYardGames();
  if($('#bkEnd')) $('#bkEnd').onclick=()=>{ closeSheet(); say(S.end); };
  const kk=BK.k, fr=$('#bkFriends'); if(fr) fr.addEventListener('click', e=>{ const b=e.target.closest('[data-f]'); if(!b) return; const code=b.dataset.f, f=friends.find(x=>x.code===code), nm=f?(f.name||fmtCode(code)):''; fetch(`${SYNC_URL}/visits/${code}/${myCode}.json`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({g:'jeu', p:kk+n, t:Date.now(), name:share.name||''})}).then(r=>{ if(!r.ok){ toast('Envoi impossible, réessaie plus tard'); return; } const o=store.get('bkOut',{})||{}; o[code]={s:n, k:kk, t:Date.now()}; store.set('bkOut',o); closeSheet(); toast('Invitation envoyée'); say(S.carry+nm+' !'); setTimeout(()=>flyAway(nm),1200); }).catch(()=>toast('Pas de connexion, réessaie plus tard')); });
  if(BK.i>BK_N && !BK.sent){ BK.sent=true; if(T){ bkReward(); if(SYNC_URL) fetch(`${SYNC_URL}/visits/${T.code}/${myCode}.json`,{method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({g:'jeuOk', p:kk+T.their+':'+n, t:Date.now(), name:share.name||''})}).catch(()=>{}); } else bkReward(); }
  if(BK.i>=1 && BK.i<=BK_N){ if(BK.k==='f') ftRun(); else if(BK.k==='p') ppRun(); else bkRun(); } }
function bkNext(my,ok,msg){ const tx=$('#bkTxt'); BK.res.push(ok); if(tx) tx.textContent=msg[Math.floor(Math.random()*msg.length)]; BK.tm=setTimeout(()=>{ if(BK.i!==my) return; cancelAnimationFrame(BK.raf); BK.i++; bkStep(); }, 1300); }
function bkRun(){ const cur=$('#bkCur'), btn=$('#bkShoot'), ball=$('#bkBall'), st=$('#bkSt'); if(!cur||!btn) return; const my=BK.i, speed=.0016+my*.00028; BK.t0=performance.now(); BK.busy=false;
  const tick=t=>{ if(BK.i!==my || !document.body.contains(cur)) return; if(!BK.busy){ BK.pos=50+50*Math.sin((t-BK.t0)*speed*Math.PI); cur.style.left=BK.pos+'%'; } BK.raf=requestAnimationFrame(tick); }; BK.raf=requestAnimationFrame(tick);
  btn.onclick=()=>{ if(BK.busy) return; BK.busy=true; btn.disabled=true; const p=BK.pos, d=Math.abs(p-50); const inn = d<=8 ? true : d<=20 ? Math.random()<.5 : false; const W=st.clientWidth, x0=W*.08+62, hx=W*(238/320), dx=hx-x0; const up=-(172-70);
    const end = inn ? [dx, up+4] : (p<50 ? [dx-34-(50-p)*.9, up+50] : [dx+30+(p-50)*.5, up-6]);
    const fin=()=>bkNext(my,inn, inn ? ['Dedans !','Panier !','Tout en douceur.'] : ['Raté. Respire, et tire le suivant.','Presque ! On ne garde pas ce tir dans la tête.','Dehors. Ça arrive à tout le monde.']);
    if(RM || !ball.animate){ ball.style.transform=`translate(${end[0]}px,${end[1]}px)`; fin(); return; }
    const a=ball.animate([{transform:'translate(0,0)'},{transform:`translate(${end[0]*.55}px,${up-58}px)`,offset:.55},{transform:`translate(${end[0]}px,${end[1]}px)`,offset:.85},{transform:`translate(${end[0]+(inn?0:(p<50?-14:16))}px,${end[1]+(inn?34:70)}px)`}],{duration:1000,easing:'ease-in-out',fill:'forwards'}); a.onfinish=fin; }; }
function ftRun(){ const cur=$('#bkCur'), btn=$('#bkShoot'), ball=$('#bkBall'), st=$('#bkSt'), kp=$('#bkKeep'); if(!cur||!btn) return; const my=BK.i, speed=.0015+my*.00025, w=bkKeepW(); BK.t0=performance.now(); BK.busy=false;
  const tick=t=>{ if(BK.i!==my || !document.body.contains(cur)) return; if(!BK.busy){ BK.pos=50+50*Math.sin((t-BK.t0)*speed*Math.PI); cur.style.left=BK.pos+'%'; } BK.raf=requestAnimationFrame(tick); }; BK.raf=requestAnimationFrame(tick);
  btn.onclick=()=>{ if(BK.busy) return; BK.busy=true; btn.disabled=true; const p=BK.pos, out=(p<6||p>94), saved=!out && Math.abs(p-BK.keep)<=w, goal=!out&&!saved; const W=st.clientWidth;
    const aim = out ? (p<50 ? 4 : 96) : 12.5+p*.75, dx=W*(aim-50)/100, dy = out ? -150 : saved ? -78 : -96-Math.random()*26;
    const fin=()=>bkNext(my,goal, goal ? ['But !','Au fond des filets !','Bien vu, cʼétait libre.'] : saved ? ['Le tupa lʼa arrêté. Regarde où il se place, et retire.','Arrêté ! Ça arrive, on passe au suivant.'] : ['À côté. Vise un peu plus à lʼintérieur.','Sur le poteau ! On respire, et le suivant.']);
    if(saved && kp && !RM && kp.animate) setTimeout(()=>kp.animate([{transform:'translateY(0)'},{transform:'translateY(-12px)'},{transform:'translateY(0)'}],{duration:380}),420);
    if(RM || !ball.animate){ ball.style.transform=`translate(${dx}px,${dy}px) scale(.6)`; fin(); return; }
    const a=ball.animate([{transform:'translate(0,0) scale(1)'},{transform:`translate(${dx}px,${dy}px) scale(.6)`,offset:.7},{transform:`translate(${dx+(saved?(p<BK.keep?-10:10):0)}px,${dy+(goal?18:saved?40:-20)}px) scale(.6)`}],{duration:850,easing:'ease-out',fill:'forwards'}); a.onfinish=fin; }; }
function ppXY(q,W){ const x=W*(.16+q*.0068), tb=230-140, h = q<62 ? 12+44*(1-Math.pow((q-26)/36,2)) : Math.max(0,40*(1-Math.pow((q-84)/22,2))); return [x-6, -(tb+Math.max(0,h))]; }
function ppRun(){ const cur=$('#bkCur'), btn=$('#bkShoot'), ball=$('#bkBall'), st=$('#bkSt'), tx=$('#bkTxt'); if(!cur||!btn) return; const my=BK.i, dur=1900-my*140, W=st.clientWidth; BK.busy=true; BK.pos=0; btn.disabled=true;
  const put=q=>{ const xy=ppXY(q,W); ball.style.transform=`translate(${xy[0]}px,${xy[1]}px)`; cur.style.left=Math.min(100,q)+'%'; }; put(0);
  const done=(ok,msg)=>{ if(BK.i!==my || BK.over) return; BK.over=true; BK.busy=true; btn.disabled=true; cancelAnimationFrame(BK.raf); if(ok){ const xy=ppXY(BK.pos,W), b0=ppXY(0,W); if(!RM && ball.animate){ ball.style.transform=`translate(${b0[0]}px,${b0[1]}px)`; ball.animate([{transform:`translate(${xy[0]}px,${xy[1]}px)`},{transform:`translate(${(xy[0]+b0[0])/2}px,${xy[1]-34}px)`},{transform:`translate(${b0[0]}px,${b0[1]}px)`}],{duration:520,easing:'ease-out'}); } else put(0); } else if(BK.pos>=98){ ball.style.transition='transform .4s ease-in'; ball.style.transform=`translate(${W*.97}px,-30px)`; } else { ball.style.transition='transform .4s ease-in'; const xy=ppXY(BK.pos,W); ball.style.transform=`translate(${xy[0]+26}px,-36px)`; } bkNext(my,ok,msg); };
  BK.over=false;
  BK.tm=setTimeout(()=>{ if(BK.i!==my) return; BK.busy=false; btn.disabled=false; BK.t0=performance.now();
    const tick=t=>{ if(BK.i!==my || BK.over || !document.body.contains(cur)) return; BK.pos=(t-BK.t0)/dur*104; put(BK.pos); if(BK.pos>=104){ done(false,['Trop tard, elle est passée. La suivante arrive.','Passée ! On la laisse filer, et on se prépare.']); return; } BK.raf=requestAnimationFrame(tick); }; BK.raf=requestAnimationFrame(tick); }, 700);
  btn.onclick=()=>{ if(BK.busy || BK.over) return; const q=BK.pos; const ok = (q>=72&&q<=92) ? true : ((q>=64&&q<72)||(q>92&&q<=98)) ? Math.random()<.5 : false;
    done(ok, ok ? ['Renvoyée !','Pile au bon moment.','Bel échange !'] : q<64 ? ['Trop tôt ! Laisse-la rebondir de ton côté.','Un peu vite. Attends le rebond.'] : ['Presque ! Le moment était tout près.','À un cheveu. La suivante arrive.']); }; }

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
