# Patch "le petit nuage" — a appliquer sur la version en cours (v91 ou plus), sur les DEUX fichiers.
# Usage : python3 cloud_patch.py /home/claude/manu-ora-site/index.html /home/claude/manu-ora.html
# Ensuite : monter APP_V et le cache de sw.js, node --check, tester, ajouter la section README (voir NOTE.md).
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    rep(".pepes{position:absolute;",""".mcloud{position:absolute;left:50%;top:-40px;width:58px;height:34px;margin-left:-29px;border:0;background:none;padding:8px;box-sizing:content-box;cursor:pointer;pointer-events:auto;opacity:0;transition:opacity 1.6s ease;-webkit-tap-highlight-color:transparent}
.mcloud.on{opacity:.92}.mcloud svg{width:100%;height:100%;display:block;animation:cloudDrift 7s ease-in-out infinite alternate}
.mcloud.sun svg{animation:none}
@keyframes cloudDrift{from{transform:translateX(-5px)}to{transform:translateX(5px)}}
@media (prefers-reduced-motion:reduce){.mcloud svg{animation:none}.mcloud{transition:none}}
.pepes{position:absolute;""")
    rep("store.set('calmDay',dayKey(Date.now())); crabRender();","store.set('calmDay',dayKey(Date.now())); crabRender(); cloudSun();")
    rep("store.set('calmDay',k); crabRender();","store.set('calmDay',k); crabRender(); cloudSun();")
    rep("if(m.indexOf('love:')===0){ loveBtn(m.slice(5)); return; }","if(m.indexOf('cloud:')===0){ cloudBtn(m.slice(6)); return; } if(m.indexOf('love:')===0){ loveBtn(m.slice(5)); return; }")
    new = r"""/* ---------- le petit nuage : une émotion difficile a été entendue, et elle passe ---------- */
let CLOUD={t:0};
const CLOUD_MS=70000;
function cloudSVG(sun){ return sun ? '<svg viewBox="0 0 58 34" aria-hidden="true"><g stroke="#F2C94C" stroke-width="2.4" stroke-linecap="round"><path d="M29 2v5M12 8l4 4M46 8l-4 4M5 22h5M48 22h5"/></g><circle cx="29" cy="22" r="10" fill="#FFE08A"/><path d="M14 30 a7 7 0 0 1 6 -11 a9 9 0 0 1 17 1 a6 6 0 0 1 5 10z" fill="#fff" opacity=".75"/></svg>' : '<svg viewBox="0 0 58 34" aria-hidden="true"><path d="M10 30 a9 9 0 0 1 4 -17 a12 12 0 0 1 23 -2 a9.5 9.5 0 0 1 11 19z" fill="#DDE5E8" stroke="#B9C7CC" stroke-width="1.2"/><path d="M16 22 a7 7 0 0 1 7 -6" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" opacity=".8"/></svg>'; }
function cloudEl(){ return birdEl.querySelector('.mcloud'); }
function cloudHide(){ clearTimeout(CLOUD.t); const c=cloudEl(); if(!c) return; c.classList.remove('on'); setTimeout(()=>{ try{ c.remove(); }catch(e){} },1700); }
function cloudShow(id){ try{ if(store.get('noCloud',false) || id==='__dark') return; const e=EMO.find(x=>x.id===id); if(!e || e.cat==='ok') return; let c=cloudEl(); if(c) c.remove();
    c=document.createElement('button'); c.className='mcloud'; c.setAttribute('aria-label','Un petit nuage'); c.innerHTML=cloudSVG(false); birdEl.appendChild(c);
    ['pointerdown','pointerup','click','dblclick'].forEach(ev=>c.addEventListener(ev, x=>{ x.stopPropagation(); if(ev==='click') cloudTap(); }));
    requestAnimationFrame(()=>requestAnimationFrame(()=>c.classList.add('on'))); clearTimeout(CLOUD.t); CLOUD.t=setTimeout(cloudHide, CLOUD_MS); }catch(e){} }
function cloudTap(){ const c=cloudEl(); if(!c || c.classList.contains('sun')) return; clearTimeout(CLOUD.t); CLOUD.t=setTimeout(cloudHide, 40000);
  sayHTML(`Il y a un petit nuage aujourdʼhui. Il passera tout seul, et je reste dessous avec toi.<div class="mini"><button data-m="breathe">Respirer</button><button data-m="heart">Parler à quelquʼun</button><button data-m="cloud:ok">Laisse-le, ça va</button><button data-m="cloud:off">Ne plus montrer de nuage</button></div>`, 30000); }
function cloudBtn(k){ bubbleEl.classList.remove('show'); if(k==='off'){ store.set('noCloud',true); cloudHide(); toast('Dʼaccord : plus de nuage. Tu peux le remettre dans « Mon manu ».'); } else { clearTimeout(CLOUD.t); CLOUD.t=setTimeout(cloudHide, 8000); } }
function cloudSun(){ try{ const c=cloudEl(); if(!c || c.classList.contains('sun')) return; clearTimeout(CLOUD.t); c.classList.add('sun'); c.innerHTML=cloudSVG(true); CLOUD.t=setTimeout(cloudHide, 6000); }catch(e){} }
const _pickRing1=pickRing;
pickRing=function(id){ _pickRing1(id); cloudShow(id); };

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    # option pour remettre / enlever le nuage, dans la carte de croissance ("Mon manu")
    rep("  const fb=$('#futureNote'); if(fb) fb.onclick=openFutureNote; }","  const fb=$('#futureNote'); if(fb) fb.onclick=openFutureNote;\n  try{ el.insertAdjacentHTML('beforeend', `<label class=\"small\" style=\"display:flex;gap:8px;align-items:center;margin-top:10px\"><input type=\"checkbox\" id=\"cloudOpt\" ${store.get('noCloud',false)?'':'checked'}> Montrer un petit nuage quand je nomme une émotion difficile</label>`); $('#cloudOpt').onchange=e=>store.set('noCloud',!e.target.checked); }catch(e){} }")
    # correctif : la bulle invisible ne doit plus bloquer les touchers
    a="pointer-events:auto;opacity:0;transform:translateY(6px);transition:opacity .25s,transform .25s}"
    assert s.count(a)==1,(path,'bubble'); s=s.replace(a,a.replace("pointer-events:auto","pointer-events:none"))
    b=".bubble.show{opacity:1;"
    assert s.count(b)==1,(path,'bubble.show'); s=s.replace(b,".bubble.show{pointer-events:auto;opacity:1;")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
