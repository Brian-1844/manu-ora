# Patch "lieux et activités à portée de doigt + écran de bienvenue" — à appliquer sur v91 ou plus, sur les DEUX fichiers.
# Usage : python3 dock_patch.py <site>/index.html <manu-ora.html>
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    rep(".pepes{position:absolute;",""".qdock{position:absolute;left:10px;top:calc(64px + env(safe-area-inset-top,0px));display:flex;flex-direction:column;gap:7px;align-items:flex-start;z-index:2}
.qdock.right{left:auto;right:10px;align-items:flex-end}
.qdk{border:0;background:transparent;padding:0;display:flex;flex-direction:column;align-items:center;gap:2px;width:58px;cursor:pointer;color:#16303B;font-family:var(--display)}
.qdk i{width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,.93);border:1.5px solid var(--line);display:grid;place-items:center;box-shadow:0 2px 6px rgba(16,48,59,.14);position:relative}
.qdk i svg{width:28px;height:28px}
.qdk span{font-size:.66rem;font-weight:700;line-height:1.1;text-align:center;background:rgba(255,255,255,.86);border-radius:8px;padding:1px 5px;max-width:64px}
.qdk.place i{border-color:var(--lagoon);border-width:2px}
.qdk.lock i{opacity:.6}.qdk.lock i::after{content:'🔒';position:absolute;right:-5px;bottom:-4px;font-size:.72rem}
.qdk:active i{transform:scale(.94)}
.qplaces{position:absolute;left:72px;top:0;display:flex;flex-wrap:wrap;width:max-content;max-width:calc(100vw - 84px);gap:4px;background:rgba(255,255,255,.96);border:1.5px solid var(--line);border-radius:18px;padding:8px 6px 6px;box-shadow:0 6px 18px rgba(16,48,59,.2)}
.qdock.right .qplaces{left:auto;right:72px}
.qplaces .qdk{width:52px}.qplaces .qdk i{width:42px;height:42px;box-shadow:none}.qplaces .qdk span{background:transparent;font-size:.62rem}
.qplaces .qdk.on i{border-color:var(--lagoon);border-width:2.5px;background:#E3F2F1}
@media (max-height:720px){.qdock{gap:3px;top:calc(56px + env(safe-area-inset-top,0px))}.qdk{width:52px}.qdk i{width:36px;height:36px}.qdk i svg{width:22px;height:22px}.qdk span{font-size:.6rem;padding:0 4px}}
.wel0{text-align:center}.wel0 .wprev{margin:6px auto}.wel0 h2{font-size:1.5rem}
.pepes{position:absolute;""")
    rep("function openWelcome(step){ step=step||1;","function openWelcome(step){ if(step===undefined){ openWelcome0(); return; } step=step||1;")
    new = r"""/* ---------- lieux et activités à portée de doigt, écran de bienvenue ---------- */
const QI={
 none:'<rect x="4" y="4" width="20" height="20" rx="6" fill="#E3F2F1" stroke="#8FB7B7" stroke-width="1.6" stroke-dasharray="3 2.4"/>',
 vai:'<path d="M2 21 L10 7 L15 15 L19 10 L26 21Z" fill="#6FAE7B"/><path d="M10 7 l-2.2 3.8 2.2 -1 2 1.4z" fill="#fff"/><path d="M2 23.5 q3 -2.4 6 0 t6 0 t6 0 t6 0" fill="none" stroke="#2F8FB0" stroke-width="2.2" stroke-linecap="round"/>',
 tai:'<circle cx="20" cy="8" r="4.5" fill="#F6C544"/><path d="M2 17 q3 -3 6 0 t6 0 t6 0 t6 0 V26 H2Z" fill="#4DB6C9"/><path d="M2 22 q3 -2 6 0 t6 0 t6 0 t6 0 V26 H2Z" fill="#F1DDB0"/>',
 oire:'<rect x="3" y="11" width="7" height="14" fill="#E8A66B"/><rect x="11" y="5" width="7" height="20" fill="#7FB2C9"/><rect x="19" y="13" width="6" height="12" fill="#E48A8A"/><path d="M5 14h3M5 18h3M13 9h3M13 13h3M13 17h3M21 16h2M21 20h2" stroke="#fff" stroke-width="1.6"/>',
 haapii:'<path d="M3 13 L14 5 L25 13Z" fill="#C8402F"/><rect x="5" y="13" width="18" height="12" fill="#FFF3D6" stroke="#C99A6B" stroke-width="1"/><rect x="12" y="18" width="4" height="7" fill="#8E5A2B"/><rect x="7" y="16" width="3" height="3" fill="#7FB2C9"/><rect x="18" y="16" width="3" height="3" fill="#7FB2C9"/>',
 souci:'<path d="M5 12 Q13 2 24 9 Q16 20 5 12Z" fill="#F0A23A"/><path d="M6 12 L21 10" stroke="#B5731E" stroke-width="1.2"/><path d="M2 21 q3 -2.4 6 0 t6 0 t6 0 t6 0" fill="none" stroke="#2F8FB0" stroke-width="2.2" stroke-linecap="round"/>',
 eel:'<path d="M4 20 q5 -9 10 -3 t10 -6" fill="none" stroke="#4B5F3A" stroke-width="4.2" stroke-linecap="round"/><circle cx="23.2" cy="10.6" r="1" fill="#fff"/>',
 meal:'<path d="M4 14 h20 q-1 9 -10 9 t-10 -9z" fill="#B98552"/><path d="M9 11 q1 -3 0 -5 M14 11 q1 -3 0 -5 M19 11 q1 -3 0 -5" stroke="#8FA7A7" stroke-width="1.6" fill="none" stroke-linecap="round"/>',
 hike:'<path d="M2 24 L13 6 L26 24Z" fill="#6FAE7B"/><path d="M13 24 q-3 -5 1 -8 t-1 -8" fill="none" stroke="#F1DDB0" stroke-width="2" stroke-dasharray="2.4 2"/><path d="M13 6 V1.5 l5 2 -5 2" fill="#C8402F" stroke="#C8402F" stroke-width="1"/>',
 shell:'<path d="M4 23 Q2 6 14 4 Q26 6 24 23 Q14 27 4 23Z" fill="#FAD4DE" stroke="#C99A6B" stroke-width="1.3"/><path d="M14 5 V24 M9 7 L10.5 24 M19 7 L17.5 24" stroke="#C99A6B" stroke-width="1" fill="none"/>',
 surf:'<path d="M2 21 q5 -12 14 -10 q-4 3 -2 7 q4 -1 12 3 V26 H2Z" fill="#4DB6C9"/><path d="M17 4 q6 6 3 15 q-7 -6 -3 -15z" fill="#F6C544" stroke="#B5731E" stroke-width="1"/>',
 dol:'<path d="M3 18 q8 -13 20 -6 l3 -3 -1 5 q-2 6 -9 5 l-3 3 0 -4 q-5 0 -10 0z" fill="#6C8FA8"/><circle cx="20" cy="13" r=".9" fill="#fff"/>',
 non:'<path d="M4 5 h20 v13 h-10 l-6 5 v-5 h-4z" fill="#fff" stroke="#16303B" stroke-width="1.5" stroke-linejoin="round"/><text x="14" y="15.2" text-anchor="middle" font-size="7.5" font-weight="800" fill="#C8402F" font-family="sans-serif">NON</text>',
 mkt:'<path d="M3 11 L5 5 H23 L25 11Z" fill="#C8402F"/><path d="M8.5 5 L7.5 11 M14 5 V11 M19.5 5 L20.5 11" stroke="#fff" stroke-width="1.6"/><rect x="5" y="11" width="18" height="13" fill="#FFF3D6" stroke="#C99A6B" stroke-width="1"/><circle cx="10" cy="19" r="2.4" fill="#F0A23A"/><circle cx="15" cy="19" r="2.4" fill="#6FAE7B"/><circle cx="20" cy="19" r="2.4" fill="#F6C544"/>',
 dur:'<path d="M14 24 C3 16 3 6 9 6 q3.4 0 5 3.4 Q15.6 6 19 6 c6 0 6 10 -5 18z" fill="#E48A8A"/><path d="M9 13 l10 4" stroke="#FFF3D6" stroke-width="4" stroke-linecap="round"/>',
 cour:'<circle cx="10" cy="13" r="7" fill="#F6C544" stroke="#B5731E" stroke-width="1"/><circle cx="19" cy="15" r="7" fill="#7FB2C9" stroke="#3B6F86" stroke-width="1"/><path d="M7 15 q3 2.6 6 0" stroke="#7A4A12" stroke-width="1.3" fill="none"/><path d="M16 18.5 q3 -2.4 6 0" stroke="#1F4658" stroke-width="1.3" fill="none"/>',
 jeux:'<circle cx="14" cy="14" r="10" fill="#F08A2B" stroke="#8A4A12" stroke-width="1.2"/><path d="M4 14 h20 M14 4 v20 M7 7 q7 7 0 14 M21 7 q-7 7 0 14" stroke="#8A4A12" stroke-width="1" fill="none"/>'
};
const QPL={none:'Simple', vai:'Rivière', tai:'Plage', oire:'Ville', haapii:'École'};
function qIco(k){ return `<i><svg viewBox="0 0 28 28" aria-hidden="true">${QI[k]||''}</svg></i>`; }
function qActs(){ const F=n=>typeof window[n]==='function'; const main={k:'', l:'', t:PLACES[curPlace]?PLACES[curPlace].a:'', go:()=>{ PL={i:0}; placeAct(); }}; let a=[];
  if(curPlace==='vai'){ a=[Object.assign(main,{k:'souci',l:'Souci'})]; if(F('openEels')) a.push({k:'eel',l:'Anguilles',t:'Nourrir les anguilles',go:()=>openEels()}); if(F('openEelMeal')&&F('emOk')) a.push({k:'meal',l:'Repas',t:'Le repas des anguilles',lock:!emOk(),go:()=>openEelMeal()}); if(F('openHike')) a.push({k:'hike',l:'Sentier',t:'Le sentier de la montagne',lock:!hikeOpen(),go:()=>{ if(hikeOpen()) openHike(); else toast('Le sentier se découvre en nourrissant les anguilles deux jours différents'); }}); }
  else if(curPlace==='tai'){ a=[Object.assign(main,{k:'shell',l:'Coquillages'})]; if(F('openSurf')) a.push({k:'surf',l:'Surf',t:'Apprendre à surfer sur ses émotions',go:()=>openSurf()}); if(F('openPetA')&&F('paOk')) a.push({k:'dol',l:'Dauphin',t:'Le dauphin',lock:!paOk('dol'),go:()=>openPetA('dol')}); }
  else if(curPlace==='oire'){ a=[Object.assign(main,{k:'non',l:'Dire non'})]; if(F('openMarket')) a.push({k:'mkt',l:'Marché',t:'Te mātete : le marché de Papeete',go:()=>openMarket()}); }
  else if(curPlace==='haapii'){ a=[Object.assign(main,{k:'dur',l:'Coup dur'})]; if(F('openYard')) a.push({k:'cour',l:'La cour',t:'La cour : derrière les apparences',go:()=>openYard()}); if(F('openYardGames')) a.push({k:'jeux',l:'Jeux',t:'Jouer dans la cour : basket, foot, ping-pong',go:()=>openYardGames()}); }
  return a; }
let QDOCK={open:false, acts:[]};
function dockRender(){ const q=$('#quiet'); if(!q) return; let d=$('#qDock'); if(!d){ d=document.createElement('div'); d.id='qDock'; d.className='qdock'; q.appendChild(d);
    d.addEventListener('click', e=>{ const b=e.target.closest('button'); if(!b) return; e.stopPropagation();
      if(b.id==='qPlace'){ QDOCK.open=!QDOCK.open; dockRender(); return; }
      if(b.dataset.pl!==undefined){ const k=b.dataset.pl; QDOCK.open=false; if(k!=='none'){ if(cfg.night==='on'){ cfg.night='auto'; store.set('cfg',cfg); renderNight(); } } setPlace(k); if(k!=='none' && isNight()) toast('Il fait nuit : le décor reviendra au matin. Les activités restent ouvertes.'); return; }
      if(b.dataset.a!==undefined){ const x=QDOCK.acts[+b.dataset.a]; if(x){ QDOCK.open=false; x.go(); } } });
    document.addEventListener('click', e=>{ if(QDOCK.open && !e.target.closest('#qDock')){ QDOCK.open=false; dockRender(); } }); }
  d.classList.remove('right');
  if(store.get('noDock',false)){ d.innerHTML=''; return; }
  QDOCK.acts = curPlace!=='none' ? qActs() : [];
  d.innerHTML=`<button class="qdk place" id="qPlace" aria-expanded="${QDOCK.open}" aria-label="Changer de lieu. Lieu actuel : ${curPlace==='none'?'écran simple':PLACES[curPlace].s}">${qIco(curPlace)}<span>${curPlace==='none'?'Lieux':QPL[curPlace]}</span></button>`
    +(QDOCK.open?`<div class="qplaces" role="group" aria-label="Choisir un lieu">${['none'].concat(Object.keys(PLACES)).map(k=>`<button class="qdk ${curPlace===k?'on':''}" data-pl="${k}" aria-label="${k==='none'?'Écran simple':PLACES[k].s}">${qIco(k)}<span>${QPL[k]||PLACES[k].n}</span></button>`).join('')}</div>`:'')
    +QDOCK.acts.map((x,i)=>`<button class="qdk ${x.lock?'lock':''}" data-a="${i}" aria-label="${esc(x.t)}${x.lock?' (à découvrir)':''}">${qIco(x.k)}<span>${x.l}</span></button>`).join('');
  try{ const raw=_homePoint0(), r=d.getBoundingClientRect(); if(raw.x < r.right+4 && r.bottom+8+BH > innerHeight-96) d.classList.add('right'); if(QUIET && B.state==='idle' && !B.asking && !RING.open){ const hm=homePoint(); if(Math.hypot(hm.x-B.x,hm.y-B.y)>4) goHome(); } }catch(e){} }
const _homePoint0=homePoint; homePoint=function(){ const p=_homePoint0.apply(this,arguments); try{ const d=$('#qDock'); if(!d || !QUIET || d.classList.contains('right') || !d.children.length) return p; const r=d.getBoundingClientRect(); if(p.x < r.right+4 && p.y < r.bottom+6 && p.y+BH > r.top) p.y=Math.min(innerHeight-BH-90, r.bottom+8); }catch(e){} return p; };
{ const _rp=renderPlace; renderPlace=function(){ _rp.apply(this,arguments); try{ dockRender(); }catch(e){} }; const _cs=closeSheet; closeSheet=function(){ const r=_cs.apply(this,arguments); try{ dockRender(); }catch(e){} return r; }; }
setTimeout(()=>{ try{ dockRender(); }catch(e){} },0);
function welSteps(){ const ua=navigator.userAgent||''; return /iPhone|iPad|iPod/.test(ua) ? ['Ouvre cette page dans <b>Safari</b>.','Touche <b>Partager</b> (le carré avec une flèche vers le haut).','Choisis <b>« Sur lʼécran dʼaccueil »</b>, puis <b>Ajouter</b>.'] : /Android/.test(ua) ? ['Touche le menu <b>⋮</b> en haut à droite du navigateur.','Choisis <b>« Ajouter à lʼécran dʼaccueil »</b> ou <b>« Installer lʼapplication »</b>.'] : ['Dans la barre dʼadresse, clique sur lʼicône <b>Installer</b>.','Sinon : menu du navigateur → <b>« Installer Manu Ora »</b>.']; }
function openWelcome0(){ const inst = CAN_INSTALL && !STANDALONE;
  openSheet(`<div class="wel0"><div class="eyebrow">ʻIa ora na · Maeva</div><h2>Bienvenue dans Manu Ora</h2><div class="wprev">${birdSVG(cfg,'w0')}</div>
    <p>Un petit oiseau qui tʼaccompagne pour mettre des mots et des couleurs sur ce que tu ressens. Un peu chaque jour, à ton rythme.</p>
    <p class="small muted">Sans compte, sans mot de passe. Tout reste sur ton téléphone.</p></div>
    <button class="btn primary" id="w0Go">Commencer</button>
    ${inst?`<button class="btn" id="w0Inst">Installer lʼappli sur mon écran dʼaccueil</button><div id="w0How" hidden><div class="stack">${welSteps().map((t,i)=>`<div class="card flat"><p class="small"><b>${i+1}.</b> ${t}</p></div>`).join('')}</div><p class="small muted">Tu peux aussi le faire plus tard, depuis lʼaccueil.</p></div>`:''}`);
  $('#w0Go').onclick=()=>openWelcome(1);
  const b=$('#w0Inst'); if(b) b.onclick=()=>{ if(deferredInstall){ const p=deferredInstall; p.prompt(); p.userChoice.then(r=>{ if(r && r.outcome==='accepted'){ hideInstall(); setInstall(false); b.hidden=true; } deferredInstall=null; }).catch(()=>{}); return; } const h=$('#w0How'); h.hidden=!h.hidden; if(!h.hidden) h.scrollIntoView({block:'nearest'}); }; }

"""
    rep("/* ---------- boot ---------- */", new+"/* ---------- boot ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
