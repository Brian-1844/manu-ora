# Patch "le moʻo, troisième animal ; la tortue grandit ; un trait par animal" — base v91 ou plus.
# Usage : python3 moo_patch.py <site>/index.html <manu-ora.html>
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    rep("const ANIMAL={manu:'Manu (oiseau)', honu:'Honu (tortue)'};","const ANIMAL={manu:'Manu (oiseau)', honu:'Honu (tortue)', moo:'Moʻo (lézard)'};")
    rep("$('#optAnimal').innerHTML = Object.keys(ANIMAL).map(k=>optBtn('an:'+k,PRICE.an,k,ANIMAL[k],(cfg.animal||'manu')===k)).join('');",
        "$('#optAnimal').innerHTML = Object.keys(ANIMAL).map(k=>(k==='moo'&&!has('an:moo')) ? `<button class=\"lock\" data-k=\"moo\">${ANIMAL.moo}<span class=\"price\">${mooDays().length} / ${MOO_NEED} jours de calme</span></button>` : optBtn('an:'+k,PRICE.an,k,ANIMAL[k],(cfg.animal||'manu')===k)).join(''); try{ animalNote(); }catch(e){}")
    rep("if(b){ const k=b.dataset.k; tryUse('an:'+k,PRICE.an,ANIMAL[k],()=>{ cfg.animal=k; saveCfg(); }); } });",
        "if(b){ const k=b.dataset.k; if(k==='moo' && !has('an:moo')){ toast('Le moʻo vient quand tu as pris un moment de calme '+MOO_NEED+' jours différents (respirer avec la vague, par exemple). Tu en es à '+mooDays().length+'.'); return; } tryUse('an:'+k,PRICE.an,ANIMAL[k],()=>{ cfg.animal=k; saveCfg(); try{ animalNote(); }catch(e){} }); } });")
    rep("animal:c.animal==='honu'?'honu':'manu', season:","animal:(c.animal==='honu'||c.animal==='moo')?c.animal:'manu', season:")
    rep("""const clip = honu ? '<ellipse cx="52" cy="70" rx="32" ry="20"/>' :""","""const clip = c.animal==='moo' ? '<ellipse cx="50" cy="76" rx="27" ry="13"/>' : honu ? '<ellipse cx="52" cy="70" rx="32" ry="20"/>' :""")
    rep("  if(honu){\n    const skin = shade(c.body,.7), line = shade(c.body,.55);","  if(c.animal==='moo') return head + mooBody(c,id,L,A,nstars,tattoo,uke,wing);\n  if(honu){\n    const skin = shade(c.body,.7), line = shade(c.body,.55);")
    rep("""clip-path="url(#${id}-clip)"/>${nstars}${tattoo}${pareu}${A.body}</g>""","""clip-path="url(#${id}-clip)"/>${honuGrow(L,id,line,c)}${nstars}${tattoo}${pareu}${A.body}</g>""")
    new = r"""/* ---------- le moʻo (troisième animal), la carapace qui grandit, un trait par animal ---------- */
const MOO_NEED=5;
function mooDays(){ const a=store.get('calmDays',[]); return Array.isArray(a)?a:[]; }
function honuGrow(L,id,line,c){ const g=L.g, cp=`clip-path="url(#${id}-clip)"`; let h='';
  if(g>=2) h+=`<path d="M22 80 q4 5 8 1 q4 5 8 1 q4 5 8 1 q4 5 8 1 q4 5 8 1 q4 5 8 1 q4 5 8 1 q4 5 8 0" fill="none" stroke="${line}" stroke-width="1.3" ${cp}/>`;
  if(g>=3) h+=`<path d="M47 62 L57 62 L57 78 L47 78 Z" fill="none" stroke="${line}" stroke-width="1.1" opacity=".8" ${cp}/>`;
  if(g>=4) h+=`<path d="M28 60 L36 66 M28 82 L36 76 M76 60 L68 66 M76 82 L68 76" stroke="${line}" stroke-width="1.2" opacity=".8" ${cp}/>`;
  if(g>=5) h+=`<g fill="${shade(c.body,1.25)}" opacity=".55" ${cp}><circle cx="52" cy="58" r="2.6"/><circle cx="32" cy="70" r="2.4"/><circle cx="72" cy="70" r="2.4"/><circle cx="52" cy="82" r="2.2"/></g>`;
  if(g>=6) h+=`<ellipse cx="52" cy="70" rx="30.6" ry="18.6" fill="none" stroke="#F2C94C" stroke-width="1.6" opacity=".85"/>`;
  return h; }
function mooBody(c,id,L,A,nstars,tattoo,uke,dark){ const g=L.g, line=shade(c.body,.6), pad=shade(c.body,.7), cp=`clip-path="url(#${id}-clip)"`;
  const toes=(x,y)=>`<circle cx="${x-4}" cy="${y}" r="2.1" fill="${pad}"/><circle cx="${x}" cy="${y+1.6}" r="2.1" fill="${pad}"/><circle cx="${x+4}" cy="${y}" r="2.1" fill="${pad}"/>`;
  const spots = g>=3 ? `<g fill="${dark}" ${cp}>${[[36,68,3],[50,66,3.4],[64,69,2.8]].concat(g>=4?[[43,74,2.2],[58,75,2.2]]:[]).map(q=>`<circle cx="${q[0]}" cy="${q[1]}" r="${q[2]}"/>`).join('')}</g>` : '';
  const gold = g>=6 ? `<g fill="#F2C94C" ${cp}><circle cx="36" cy="68" r="1.1"/><circle cx="50" cy="66" r="1.3"/><circle cx="64" cy="69" r="1"/></g>` : '';
  const stripes = g>=5 ? `<path d="M13 62.5 L17.5 60.5 M9.5 54.5 L14.5 53 M8 47 L14 47.5" stroke="${dark}" stroke-width="1.8"/>` : '';
  const pareu = c.pareu ? `<rect x="18" y="77" width="72" height="20" fill="url(#${id}-pareu)" ${cp}/>` : '';
  return `
    <g class="tail"><g transform="translate(28 76) scale(${Math.max(.55,Math.min(1.3,L.tl))}) translate(-28 -76)"><path d="M44 66 L33 65 Q14 66 8 52 Q5 42 13 40 Q18.5 40 17.5 45 Q13.5 46 15 52 Q19 64 31 85 L42 86 Z" fill="${c.body}"/>${stripes}</g></g>
    <g class="legs"><g class="leg l1"><path d="M36 84 Q30 88 30 95" fill="none" stroke="${pad}" stroke-width="4.2" stroke-linecap="round"/>${toes(30,97)}</g><g class="leg l2"><path d="M66 84 Q72 88 72 95" fill="none" stroke="${pad}" stroke-width="4.2" stroke-linecap="round"/>${toes(72,97)}</g></g>
    <g class="body"><path d="M66 66 Q78 58 86 60 L88 74 Q78 80 68 84 Z" fill="${c.body}"/><ellipse cx="50" cy="76" rx="27" ry="13" fill="${c.body}"/><ellipse cx="52" cy="82" rx="20" ry="6.5" fill="${c.belly}" ${cp}/>${spots}${gold}${nstars}${tattoo}${pareu}${A.body}</g>
    ${uke}
    <g class="wing"><path d="M58 80 Q62 88 58 96" fill="none" stroke="${pad}" stroke-width="4.2" stroke-linecap="round"/>${toes(58,98)}</g>
    <g transform="translate(41.2 35.5) scale(.62)">${A.neck}</g>
    <g class="head"><g transform="translate(92 64) scale(${L.hs}) translate(-92 -64)"><path d="M78 64 Q79 52 92 52 Q106 53 108 63 Q107 73 93 75 Q79 75 78 64 Z" fill="${c.body}" stroke="${line}" stroke-width=".6"/><path d="M84 70 Q94 76 105 67" fill="none" stroke="#10303B" stroke-width="1.3" stroke-linecap="round"/><circle cx="105.5" cy="61" r=".8" fill="#10303B"/><circle cx="99" cy="67" r="2.6" fill="#F28CB1" opacity=".55"/><g class="eye" style="transform-origin:95px 59px"><circle cx="95" cy="59" r="${(L.er+.6).toFixed(1)}" fill="#F2C94C"/><ellipse cx="95.4" cy="59" rx="${(L.er*.42).toFixed(1)}" ry="${(L.er*.92).toFixed(1)}" fill="#10303B"/><circle cx="${(96.4).toFixed(1)}" cy="57.4" r="1.1" fill="#fff"/></g><g transform="translate(41.2 35.5) scale(.62)">${A.top}${A.eyes}</g></g></g>
  </svg>`; }
const ANIMAL_TRAIT={
  manu:['Le messager','Il vole jusquʼà tes cœurs liés pour porter tes signes. En grandissant : la crête, la queue, les ailes.'],
  honu:['La patience','Quand tu respires lentement avec elle, sa carapace brille doucement jusquʼau soir. En grandissant : les écailles de sa carapace se dessinent.'],
  moo:['Ce qui repousse','Le petit moʻo de la maison sait attendre sans bouger. Quand il perd sa queue, elle repousse : ça prend du temps, cʼest tout. En grandissant : sa queue sʼallonge et son dos se tachette.']};
function animalNote(){ const o=$('#optAnimal'); if(!o) return; let n=$('#animalNote'); if(!n){ n=document.createElement('p'); n.id='animalNote'; n.className='small muted'; n.style.marginTop='8px'; o.parentNode.appendChild(n); }
  const t=ANIMAL_TRAIT[cfg.animal||'manu']||ANIMAL_TRAIT.manu; n.innerHTML=`<b>${t[0]}.</b> ${t[1]} <span style="display:block;margin-top:4px">Aucun nʼest meilleur quʼun autre : ils grandissent tous au même rythme.</span>`; }
function mooTick(){ try{ const d=store.get('calmDay',''); if(!d) return; const a=mooDays(); if(!a.includes(d)){ a.push(d); store.set('calmDays',a.slice(-40)); }
    if(a.length>=MOO_NEED && !has('an:moo')){ OWN.add('an:moo'); store.set('owned',[...OWN]); setTimeout(function w(){ if(!visitFree() || bubbleEl.classList.contains('show') || !$('#sheet').hidden){ setTimeout(w,6000); return; } say('Un petit moʻo te regarde depuis quelques jours, sans bouger. Il veut bien rester. Tu le trouves dans « Mon manu », à Animal.'); },2500); } }catch(e){} }
{ const _cb=closeBreath; closeBreath=function(done){ const r=_cb.apply(this,arguments); try{ mooTick(); if(done && cfg.animal==='honu'){ const sh=store.get('shine',null); if(!sh || Date.now()>=sh.until){ const e=new Date(); e.setHours(23,59,0,0); store.set('shine',{until:e.getTime(), color:'#9FE3C8'}); applyShine(); } } }catch(e){} return r; };
  const _cs2=closeSheet; closeSheet=function(){ const r=_cs2.apply(this,arguments); mooTick(); return r; };
  const _pr2=pickRing; pickRing=function(id){ _pr2.apply(this,arguments); try{ if(cfg.animal!=='moo' || id==='__dark') return; const e=EMO.find(x=>x.id===id); if(!e || e.cat==='ok') return; const k=dayKey(Date.now()); if(store.get('mooSaid','')===k) return;
      setTimeout(function w(n){ n=n||0; if(n>20) return; if(!visitFree() || bubbleEl.classList.contains('show') || !$('#sheet').hidden || RING.open){ setTimeout(()=>w(n+1),8000); return; } store.set('mooSaid',k); say('Tu sais, quand je perds ma queue, elle repousse. Ça prend du temps, cʼest tout.'); },45000); }catch(e){} }; }
setTimeout(mooTick,1500); setInterval(mooTick,30000);

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
