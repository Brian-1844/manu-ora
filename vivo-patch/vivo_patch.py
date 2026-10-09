# Patch "le vivo, la flûte nasale cachée : une seconde chance, ou le ʻūʻupa pour une journée (à garder ou à offrir)".
# Dépend de instr-patch et jeu-patch. Usage : python3 vivo_patch.py <site>/index.html <manu-ora.html>
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    assert 'function openInstr(' in s and 'function bkAttemptEnd(' in s, 'appliquer instr-patch et jeu-patch avant'
    rep(".pepes{position:absolute;",""".uupa{position:absolute;left:18px;top:-44px;width:50px;height:42px;z-index:2;pointer-events:none;animation:uupaBob 2.4s ease-in-out infinite}
.uupa svg{width:100%;height:100%;overflow:visible}.uupa .uw{transform-box:fill-box;transform-origin:80% 30%;animation:uupaW .3s ease-in-out infinite alternate}
@keyframes uupaBob{50%{transform:translate(-6px,-8px)}}@keyframes uupaW{to{transform:rotate(-24deg)}}
@media (prefers-reduced-motion:reduce){.uupa,.uupa .uw{animation:none}}
.pepes{position:absolute;""")
    rep("    else if(v.g==='pardon'){ for(let i=0;i<6;i++)","    else if(v.g==='uupa'){ uupaGot(v); }\n    else if(v.g==='pardon'){ for(let i=0;i<6;i++)")
    new = r"""/* ---------- le vivo : la flûte nasale cachée ---------- */
GEST.uupa={l:'', t:'tʼenvoie son ʻūʻupa, le pigeon vert ! Il reste près de ton manu toute la journée.'};
function vivoGet(){ const o=store.get('vivo',null); return (o && typeof o==='object') ? o : {ofe:false, made:false, day:'', retry:''}; }
function vivoReady(){ const O=insGet(); return !!(O.uke && O.toere && O.pahu); }
function uupaGet(){ const o=store.get('uupa',null); return (o && typeof o==='object') ? o : {day:'', from:'', gave:''}; }
function uupaSVG(){ return `<svg viewBox="0 0 40 34" aria-hidden="true"><ellipse cx="20" cy="22" rx="12" ry="9" fill="#6E9A3E"/><ellipse cx="22" cy="26" rx="8" ry="4.5" fill="#F2E28A"/><path d="M8 22 l-7 -3 l1 6z" fill="#8A9AA0"/><g class="uw"><path d="M14 18 q10 -10 20 0 q-8 4 -20 0z" fill="#557F2E"/></g><circle cx="31" cy="13" r="6.5" fill="#9AA6AC"/><path d="M27 8 q4 -4 8 0 q-4 1 -8 0z" fill="#B58AD8"/><circle cx="33" cy="12" r="1.3" fill="#16303B"/><path d="M37 13 l3 1.5 l-3 1z" fill="#D8C24A"/></svg>`; }
function uupaRender(){ try{ const u=uupaGet(), on=u.day===dayKey(Date.now()); let el=birdEl.querySelector('.uupa'); if(on && !el){ el=document.createElement('div'); el.className='uupa'; el.innerHTML=uupaSVG(); birdEl.appendChild(el); } if(!on && el) el.remove(); }catch(e){} }
function uupaGot(v){ try{ const k=dayKey(Date.now()); store.set('uupa',{day:k, from:String(v.name||'').slice(0,12), gave:k}); setTimeout(uupaRender,9300); }catch(e){} }
function vivoSound(){ try{ AC = AC || new (window.AudioContext||window.webkitAudioContext)(); if(AC.state!=='running') AC.resume(); const t=AC.currentTime+.05, o=AC.createOscillator(), g=AC.createGain(), f=AC.createBiquadFilter(); o.type='sine'; f.type='lowpass'; f.frequency.value=1800; [[0,523],[.6,587],[1.2,659],[1.9,587],[2.5,523],[3.3,440]].forEach(q=>o.frequency.setTargetAtTime(q[1],t+q[0],.08)); g.gain.setValueAtTime(0,t); g.gain.linearRampToValueAtTime(.08,t+.25); g.gain.setValueAtTime(.08,t+3.4); g.gain.linearRampToValueAtTime(0,t+4.2); o.connect(f); f.connect(g); g.connect(AC.destination); o.start(t); o.stop(t+4.3); }catch(e){} }
function vivoSVG(){ return `<svg viewBox="0 0 320 150" role="img" aria-label="Un vivo, flûte nasale en bambou"><rect x="40" y="66" width="240" height="18" rx="9" fill="#D9C27A" stroke="#8A7A3B" stroke-width="2"/>${[90,150,210].map(x=>`<rect x="${x}" y="64" width="5" height="22" fill="#B59E52"/>`).join('')}${[120,180,230].map(x=>`<circle cx="${x}" cy="75" r="3.6" fill="#5C4A1E"/>`).join('')}<ellipse cx="44" cy="75" rx="5" ry="8" fill="#5C4A1E"/><path d="M60 92 q20 10 40 0 q20 10 40 0" stroke="#3B8C58" stroke-width="2" fill="none"/></svg>`; }
function vivoCard(){ const V=vivoGet(), today=dayKey(Date.now()), u=uupaGet(), mut=(SYNC_URL?friends.filter(f=>isMutual(f.code)):[]);
  if(!vivoReady()) return '';
  if(!V.ofe) return `<div class="card flat"><h3>????</h3><p class="small muted">Un quatrième instrument se cache. On ne le fabrique quʼavec quelque chose quʼon ne plante pas. Indice : là où lʼeau chante, pose ce qui te pèse.</p></div>`;
  if(!V.made) return `<div class="card flat"><div class="insfig">${vivoSVG()}</div><h3>Le vivo</h3><p class="small muted">La flûte nasale, en bambou : on souffle par le nez, doucement. Le plus discret des instruments.</p><div class="inscost"><span class="ok">ʻofe (bambou) : 1 / 1</span><span class="${feathers>=3?'ok':'no'}">plumes : ${Math.min(feathers,3)} / 3</span></div><button class="btn sm primary" id="vvMake">Fabriquer</button></div>`;
  const used=V.day===today;
  return `<div class="card flat"><div class="insfig">${vivoSVG()}</div><h3>Le vivo ✓</h3><p class="small muted">Une fois par jour, un seul souffle, au choix :</p>${used?`<p class="small"><b>${V.retry===today?'Une seconde chance tʼattend dans les jeux de la cour.':'Le ʻūʻupa est venu aujourdʼhui.'}</b> Le vivo se repose jusquʼà demain.</p>`:`<div class="bkpick" style="display:grid;gap:8px"><button class="btn" id="vvRetry" style="display:block;width:100%;text-align:left"><b>Une seconde chance</b><br><span class="small muted">Aujourdʼhui, ton prochain essai raté dans les jeux de la cour ne compte pas : tu le retentes.</span></button><button class="btn" id="vvUupa" style="display:block;width:100%;text-align:left"><b>Appeler le ʻūʻupa</b><br><span class="small muted">Le pigeon vert de Tahiti et Moʻorea vient près de ton manu pour la journée.</span></button></div>`}
    ${u.day===today && u.gave!==today && mut.length?`<div class="card flat"><div class="eyebrow">Offrir le ʻūʻupa</div><p class="small muted">Tu peux lʼenvoyer chez un cœur lié : il reste chez lui aujourdʼhui, et repart de chez toi.</p><div class="row" id="vvFr">${mut.map(f=>`<button class="btn sm" data-f="${f.code}">${esc(f.name||fmtCode(f.code))}</button>`).join('')}</div></div>`:''}</div>`; }
function vivoWire(){ const mk=$('#vvMake'); if(mk) mk.onclick=()=>{ if(feathers<3){ toast('Il manque des plumes'); return; } feathers-=3; store.set('feathers',feathers); renderFeathers(); const V=vivoGet(); V.made=true; store.set('vivo',V); vivoSound(); openInstr(); setTimeout(()=>toast('Le vivo est prêt. Écoute…'),300); };
  const rt=$('#vvRetry'); if(rt) rt.onclick=()=>{ const V=vivoGet(), k=dayKey(Date.now()); V.day=k; V.retry=k; store.set('vivo',V); vivoSound(); closeSheet(); say('Le vivo a soufflé. Aujourdʼhui, un essai raté dans la cour ne compte pas : tu pourras le retenter.'); };
  const up=$('#vvUupa'); if(up) up.onclick=()=>{ const V=vivoGet(), k=dayKey(Date.now()); V.day=k; V.retry=''; store.set('vivo',V); store.set('uupa',{day:k, from:'', gave:''}); vivoSound(); closeSheet(); setTimeout(()=>{ uupaRender(); say('Écoute… Le ʻūʻupa a répondu ! Le pigeon vert ne vit quʼà Tahiti et à Moʻorea. Il reste avec nous aujourdʼhui.'); },1800); };
  const fr=$('#vvFr'); if(fr) fr.addEventListener('click', e=>{ const b=e.target.closest('[data-f]'); if(!b) return; const code=b.dataset.f, f=friends.find(x=>x.code===code), nm=f?(f.name||fmtCode(code)):''; sendGesture(code,'uupa',nm); const u=uupaGet(); u.gave=dayKey(Date.now()); u.day=''; store.set('uupa',u); uupaRender(); closeSheet(); toast('Le ʻūʻupa sʼenvole vers '+nm); }); }
{ const _oi=openInstr; openInstr=function(){ const r=_oi.apply(this,arguments); try{ const h=vivoCard(); if(h){ const st=sheetInner.querySelector('.stack'); if(st){ st.insertAdjacentHTML('beforeend',h); vivoWire(); } } }catch(e){} return r; };
  const _pd=placeDone; placeDone=function(){ const r=_pd.apply(this,arguments); try{ if(curPlace==='vai' && vivoReady()){ const V=vivoGet(); if(!V.ofe){ V.ofe=true; store.set('vivo',V); setTimeout(()=>toast('Trouvé : un morceau de ʻofe (bambou)'),2400); setTimeout(function w(n){ n=n||0; if(n>12) return; if(!visitFree() || bubbleEl.classList.contains('show') || !$('#sheet').hidden){ setTimeout(()=>w(n+1),5000); return; } say('Au bord de la rivière, un morceau de ʻofe, le bambou… Avec ça, on peut faire une flûte. Va voir lʼatelier des instruments.'); },3000); } } }catch(e){} return r; };
  const _ae=bkAttemptEnd; bkAttemptEnd=function(ok,msg){ try{ const V=vivoGet(), k=dayKey(Date.now()); if(!ok && V.retry===k && !BK.ending && BK.i>=1){ V.retry='used'; store.set('vivo',V); BK.ending=true; const tx=$('#bkTxt'); if(tx) tx.textContent=msg+' Mais le vivo souffle : cet essai ne compte pas. Recommence !'; vivoSound(); BK.tm=setTimeout(()=>{ BK.ending=false; const t2=$('#bkTxt'); if(t2) t2.textContent=SP[BK.k].tip; if(BK.game) BK.game.next(); },2000); return; } }catch(e){} return _ae.apply(this,arguments); }; }
setTimeout(uupaRender,400); setInterval(uupaRender,60000);

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
