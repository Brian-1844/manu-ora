# Patch "le faʻaʻapu, suite" : une petite image pour chaque chose du coffre et chaque graine,
# « Laisser mûrir encore » (très mûr = récolte double), une première pousse rapide, une carte « Le temps du faʻaʻapu »,
# et le secret de lʼaube de la tiare ʻāpetahi (faʻaʻapu partagé). Dépend de tous les patchs précédents.
# Usage : python3 jardin_patch.py <site>/index.html <manu-ora.html>
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    assert 'function openChest(' in s and 'function renderSharedGarden(' in s and 'function carryRender(' in s, 'appliquer les patchs précédents avant'
    rep(".pepes{position:absolute;",""".ico{width:20px;height:20px;vertical-align:-5px;margin-right:3px;flex:none;display:inline-block}
.icoB{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;flex:none;border:2px solid var(--surface);box-shadow:0 0 8px var(--au,#ccc);background:color-mix(in srgb,var(--au,#ccc) 24%,var(--surface))}
.icoB .ico{width:26px;height:26px;margin:0;vertical-align:0}
.plot.vr>svg:first-child{filter:drop-shadow(0 0 7px #F2C94C) saturate(1.2)}
.apDawn{border-radius:18px;overflow:hidden;background:linear-gradient(#2B3B6B,#E88B6A 62%,#F6D58E)}
.apDawn svg{display:block;width:100%;height:auto}
.apDawn .pt{transform-box:fill-box;transform-origin:50% 100%;transform:rotate(var(--r)) scaleY(.25);animation:apOpen 2.6s 0.6s cubic-bezier(.3,1.4,.5,1) forwards}
@keyframes apOpen{to{transform:rotate(var(--r)) scaleY(1)}}
.apDawn .sun{animation:apSun 4s ease-out forwards}@keyframes apSun{from{transform:translateY(18px)}to{transform:translateY(0)}}
@media (prefers-reduced-motion:reduce){.apDawn .pt{animation:none;transform:rotate(var(--r))}.apDawn .sun{animation:none}}
.pepes{position:absolute;""")

    # coffre : une image à côté de chaque récolte et de chaque création
    rep("""const stock=ING.map(k=>`<span class="feather">${ingName(k)} ×""","""const stock=ING.map(k=>`<span class="feather">${/^\?/.test(ingName(k))?'':icoSVG(k)}${ingName(k)} ×""")
    rep("""<span class="auradot" style="background:${it.aura==='rainbow'?'conic-gradient(#E4583F,#F2C94C,#3B8C58,#5B6FB8,#E4583F)':it.aura}"></span>""",
        """<span class="icoB" style="--au:${it.aura==='rainbow'?'#B58AD8':it.aura}${it.aura==='rainbow'?';background:conic-gradient(#E4583F55,#F2C94C55,#3B8C5855,#5B6FB855,#E4583F55)':''}">${icoSVG(id,1)}</span>""")
    rep("""<div class="mixrow"><span>${ingName(k)} <span""","""<div class="mixrow"><span>${/^\?/.test(ingName(k))?'':icoSVG(k)}${ingName(k)} <span""")
    # graines
    rep(""":`<span class="feather">${PLANTS[k].name} ×${garden.seeds[k]||0}</span>`).join('');""",""":`<span class="feather">${icoSVG(k)}${PLANTS[k].name} ×${garden.seeds[k]||0}</span>`).join('');""")

    # très mûr
    rep("""return `<div class="plot">${plantSVG(pl?pl.p:null,st)}""","""return `<div class="plot${pl&&st===3&&vrState(pl)===2?' vr':''}">${plantSVG(pl?pl.p:null,st)}""")
    rep("""else body=`<b>${PLANTS[pl.p].name}</b><span class="small" style="color:var(--fern);font-weight:700">Mûr !</span>""",
        """else body=`<b>${PLANTS[pl.p].name}</b>${vrTag(pl,i)}""")
    rep("""    else if(d.wed!==undefined){ vanWed(+d.wed); }""","""    else if(d.vr!==undefined){ const pl=garden.plots[+d.vr]; if(pl && plotStage(pl)===3 && !pl.slow){ pl.slow=Date.now(); saveGarden(); openGarden(); toast('On le laisse mûrir encore : très mûr dans '+vrLeft(pl)); } }
    else if(d.wed!==undefined){ vanWed(+d.wed); }""")
    rep("""const w=PLANTS[pl.p].worth; feathers+=w;""","""const w=PLANTS[pl.p].worth*(vrState(pl)===2?2:1); feathers+=w;""")
    rep("""gotAdd(pl.p); garden.store[pl.p]=(garden.store[pl.p]||0)+1; garden.plots[i]=null;""","""gotAdd(pl.p); garden.store[pl.p]=(garden.store[pl.p]||0)+1; if(vrState(pl)===2){ garden.store[pl.p]++; setTimeout(()=>toast('Très mûr : 2 au coffre !'),1800); } garden.plots[i]=null;""")

    rep("""<button class="btn sm" data-sell="${i}">Échanger · ${PLANTS[pl.p].worth} plumes</button>""","""<button class="btn sm" data-sell="${i}">Échanger · ${PLANTS[pl.p].worth*(vrState(pl)===2?2:1)} plumes</button>""")
    # première pousse rapide
    rep("""garden.plots[GSEL.i]=moonPlot(k); GSEL=null; saveGarden(); openGarden(); toast(ms||(""","""const gi=GSEL.i; garden.plots[gi]=moonPlot(k); GSEL=null; const fg=firstGrow(gi); saveGarden(); openGarden(); toast(fg||ms||(""")
    # carte du temps
    rep("""    ${skCard()}
    ${moonCard()}""","""    ${timeCard()}
    ${skCard()}
    ${moonCard()}""")

    new = r"""/* ---------- le faʻaʻapu, suite : images, très mûr, première pousse, aube de lʼʻāpetahi ---------- */
const ICO=(function(){
  const fl=(pc,cc,a)=>{ a=a||'#0000'; let o=''; for(let k=0;k<5;k++) o+=`<ellipse cx="12" cy="6.6" rx="3.7" ry="5.4" fill="${pc}" stroke="${a}" stroke-width=".6" transform="rotate(${k*72} 12 12)"/>`; return o+`<circle cx="12" cy="12" r="2.4" fill="${cc}"/>`; };
  const hib=(pc,cc)=>{ let o=''; for(let k=0;k<5;k++) o+=`<path d="M12 12 q-6 -4 -3 -9.5 q3 -1.5 5.5 1.5 q2 4 -2.5 8z" fill="${pc}" transform="rotate(${k*72} 12 12)"/>`; return o+`<path d="M12 12 l5 -6" stroke="${cc}" stroke-width="1.3" stroke-linecap="round"/><circle cx="17.2" cy="5.8" r="1.2" fill="#F2C94C"/>`; };
  const hei=(c1,c2)=>{ let o='<circle cx="12" cy="12" r="7.5" fill="none" stroke="#3B8C58" stroke-width="1.6"/>'; for(let k=0;k<9;k++){ const t=k*40*Math.PI/180; o+=`<circle cx="${(12+7.5*Math.cos(t)).toFixed(1)}" cy="${(12+7.5*Math.sin(t)).toFixed(1)}" r="2.7" fill="${k%2?c2:c1}" stroke="#0002" stroke-width=".4"/>`; } return o; };
  const bottle=(c)=>`<rect x="9.5" y="2" width="5" height="3" rx="1" fill="#A8743A"/><path d="M10 5 h4 v2.5 q4 2 4 6 v6.5 q0 2 -2 2 h-8 q-2 0 -2 -2 v-6.5 q0 -4 4 -6z" fill="#FFFFFFB0" stroke="#7A9AA8" stroke-width=".8"/><path d="M6.3 13 h11.4 v6.8 q0 1.6 -1.6 1.6 h-8.2 q-1.6 0 -1.6 -1.6z" fill="${c}"/>`;
  const glass=(c)=>`<path d="M6 5 h12 l-1.6 15.5 q-.2 1.5 -1.7 1.5 h-5.4 q-1.5 0 -1.7 -1.5z" fill="#FFFFFFA0" stroke="#7A9AA8" stroke-width=".8"/><path d="M6.8 10 h10.4 l-1.1 10.4 q-.1 1 -1.1 1 h-6 q-1 0 -1.1 -1z" fill="${c}"/><path d="M14 2 l-1.5 12" stroke="#E4583F" stroke-width="1.3" stroke-linecap="round"/><circle cx="17" cy="6" r="2.2" fill="#F2C94C"/>`;
  const dish=(c)=>`<ellipse cx="12" cy="16" rx="10" ry="4" fill="#3B8C58"/><ellipse cx="12" cy="13.5" rx="7" ry="4.5" fill="${c}"/><ellipse cx="10" cy="12" rx="2.5" ry="1" fill="#FFFFFF60"/>`;
  const bowl=(c,dots)=>`<path d="M3 11 h18 q-1 9 -9 9 q-8 0 -9 -9z" fill="#A8743A"/><ellipse cx="12" cy="11" rx="9" ry="2.6" fill="${c}"/>${(dots||[]).map((d,k)=>`<circle cx="${7+k*3.4}" cy="${9.8+(k%2)}" r="1.9" fill="${d}"/>`).join('')}`;
  const cloth=(c,m)=>`<path d="M4 4 q8 -2 16 0 v15 q-8 3 -16 0z" fill="${c}"/><path d="M4 9 q8 -2 16 0" stroke="#0002" stroke-width="1" fill="none"/>${m===false?'':`<g transform="translate(12 13) scale(.32) translate(-12 -12)">${hib('#FFFFFFD0','#FFFFFFD0')}</g>`}`;
  const hat=(c)=>`<ellipse cx="12" cy="16" rx="10.5" ry="3.6" fill="#D9BE7A" stroke="#9A7A3B" stroke-width=".7"/><path d="M6.5 15 q0 -8 5.5 -8 q5.5 0 5.5 8z" fill="#D9BE7A" stroke="#9A7A3B" stroke-width=".7"/><path d="M6.6 13.6 h10.8" stroke="#3B8C58" stroke-width="1.6"/><circle cx="8.5" cy="13" r="2.4" fill="${c}"/><circle cx="8.5" cy="13" r=".9" fill="#F2C94C"/>`;
  const pearls=(round)=>round?(()=>{ let o=''; for(let k=0;k<10;k++){ const t=k*36*Math.PI/180; o+=`<circle cx="${(12+7*Math.cos(t)).toFixed(1)}" cy="${(12+7*Math.sin(t)).toFixed(1)}" r="1.9" fill="${k%3?'#E8EEF0':'#5E6E78'}" stroke="#9FB3BC" stroke-width=".4"/>`; } return o; })():`<path d="M3 4 q9 14 18 0" stroke="#9FB3BC" stroke-width=".8" fill="none"/>${[[5,7],[7.5,10],[10,12],[14,12],[16.5,10],[19,7]].map(q=>`<circle cx="${q[0]}" cy="${q[1]}" r="1.6" fill="#E8EEF0" stroke="#9FB3BC" stroke-width=".4"/>`).join('')}<circle cx="12" cy="16.5" r="3.2" fill="#3E4E5A"/><circle cx="11" cy="15.4" r="1" fill="#FFFFFF90"/>`;
  const leaf=(c,d)=>`<path d="M12 22 q-9 -8 -2 -19 q9 6 2 19z" fill="${c}"/><path d="M12 22 q-1 -10 -2 -19" stroke="${d||'#1F6B3F'}" stroke-width=".9" fill="none"/>`;
  const o={
    tiare:fl('#FFFFFF','#F2C94C','#D8D2C0'), aute:hib('#E4583F','#B8322A'), tipanie:fl('#FFFDF5','#F2C94C','#E8D9A0'), tipax:fl('#F7A8C4','#F2C94C'), autex:hib('#F28CB1','#E4583F'),
    apetahi:(()=>{ let o=''; [-70,-35,0,35,70].forEach(a=>o+=`<ellipse cx="12" cy="9" rx="2.6" ry="6.2" fill="#FFFFFF" stroke="#D8D2C0" stroke-width=".6" transform="rotate(${a} 12 16)"/>`); return o+'<path d="M12 16 v6" stroke="#3B8C58" stroke-width="1.4"/>'; })(),
    meia:`<path d="M5 6 q2 13 15 13 q-2 -2 -1 -3 q-10 -1 -11.5 -11z" fill="#F2C94C" stroke="#B8902A" stroke-width=".7"/><path d="M5 6 l-1.5 -2" stroke="#6E5A2A" stroke-width="1.6" stroke-linecap="round"/>`,
    painapo:`<path d="M12 9 l-4 -6 l3 3 l1 -5 l1 5 l3 -3z" fill="#3B8C58"/><ellipse cx="12" cy="15" rx="5.5" ry="7" fill="#F2B632"/><path d="M8 11 l8 8 M16 11 l-8 8 M7.5 15 l4 -5 M16.5 15 l-4 -5" stroke="#B8802A" stroke-width=".7"/>`,
    iita:`<path d="M12 2 q7 3 7 12 q0 8 -7 8 q-7 0 -7 -8 q0 -9 7 -12z" fill="#F08A2B"/><path d="M12 2 q4 2 5 6 q-5 -1 -5 -6z" fill="#6E9A3E"/>`,
    vi:`<ellipse cx="12" cy="13" rx="6.5" ry="8" fill="#D9C24A"/><ellipse cx="10" cy="10" rx="2" ry="3" fill="#FFFFFF50"/><path d="M12 5 q2 -3 5 -2" stroke="#3B8C58" stroke-width="1.5" fill="none"/>`,
    vix:`<ellipse cx="12" cy="13" rx="6.5" ry="8" fill="#D9C24A"/><ellipse cx="14" cy="15" rx="4" ry="5" fill="#E4583F80"/><path d="M12 5 q2 -3 5 -2" stroke="#3B8C58" stroke-width="1.5" fill="none"/>`,
    anani:`<circle cx="12" cy="13" r="7.5" fill="#F08A2B"/><circle cx="9.5" cy="10.5" r="2" fill="#FFFFFF40"/><path d="M12 6 q2 -4 6 -3 q-2 4 -6 3z" fill="#3B8C58"/>`,
    taro:`<path d="M12 9 q7 1 6 8 q-1 5 -6 5 q-5 0 -6 -5 q-1 -7 6 -8z" fill="#7A5A6E"/><path d="M8 14 q4 1 8 0 M8.5 18 q3.5 1 7 0" stroke="#5A3A4E" stroke-width=".8" fill="none"/><path d="M12 9 v-6 M12 4 q-5 -1 -7 2 M12 4 q5 -1 7 2" stroke="#3B8C58" stroke-width="1.6" fill="none" stroke-linecap="round"/>`,
    uru:`<circle cx="12" cy="13" r="8" fill="#8FBF4A"/>${[[9,10],[13,9],[16,12],[10,14],[14,15],[11,18],[15,18]].map(q=>`<circle cx="${q[0]}" cy="${q[1]}" r="1.6" fill="none" stroke="#5E8A2A" stroke-width=".7"/>`).join('')}<path d="M12 5 v-3" stroke="#6B4423" stroke-width="1.5"/>`,
    haari:`<circle cx="12" cy="13" r="8.5" fill="#8A5A2B"/><path d="M5 10 q7 -4 14 0" stroke="#6B4423" stroke-width=".8" fill="none"/><circle cx="9.5" cy="10" r="1.3" fill="#3B2A1A"/><circle cx="14.5" cy="10" r="1.3" fill="#3B2A1A"/><circle cx="12" cy="13.5" r="1.3" fill="#3B2A1A"/>`,
    vanira:`<path d="M5 21 q2 -10 13 -18" stroke="#3B2A1A" stroke-width="2.6" fill="none" stroke-linecap="round"/><path d="M7 21 q3 -9 13 -16" stroke="#5C4A1E" stroke-width="1.4" fill="none" stroke-linecap="round"/><g transform="translate(14 11) scale(.4) translate(-12 -12)">${fl('#F4EBB0','#E2C24A')}</g>`,
    nono:`<path d="M12 3 q6 2 6 10 q0 8 -6 8 q-6 0 -6 -8 q0 -8 6 -10z" fill="#E8E6C0" stroke="#B8B68A" stroke-width=".7"/>${[[10,8],[14,9],[9,12],[13,13],[16,14],[10,16],[14,17]].map(q=>`<circle cx="${q[0]}" cy="${q[1]}" r=".9" fill="#8A8A5A"/>`).join('')}`,
    metua:`<path d="M12 22 q1 -10 -3 -19" stroke="#2F6B3F" stroke-width="1.2" fill="none"/>${[4,7,10,13,16].map((y,k)=>`<path d="M${(9.6+k*.5).toFixed(1)} ${y} q-5 0 -6 2 M${(9.8+k*.5).toFixed(1)} ${y} q5 -1 7 1" stroke="#3B8C58" stroke-width="2.2" fill="none" stroke-linecap="round"/>`).join('')}`,
    tamanu:`<circle cx="12" cy="13" r="7" fill="#7FA84A"/><circle cx="10" cy="11" r="2" fill="#FFFFFF40"/><path d="M12 6 q1 -3 4 -3" stroke="#3B8C58" stroke-width="1.4" fill="none"/>`,
    vavai:`<circle cx="9" cy="10" r="4.5" fill="#FFFFFF" stroke="#DDD" stroke-width=".6"/><circle cx="15" cy="10" r="4.5" fill="#FFFFFF" stroke="#DDD" stroke-width=".6"/><circle cx="12" cy="14" r="4.5" fill="#FFFFFF" stroke="#DDD" stroke-width=".6"/><path d="M8 18 l4 4 l4 -4" fill="#8A6A3B"/>`,
    fara:`<path d="M5 22 q2 -12 14 -20" stroke="#3B8C58" stroke-width="3.4" fill="none" stroke-linecap="round"/><path d="M5 22 q2 -12 14 -20" stroke="#8FD08A" stroke-width=".8" fill="none"/><path d="M9 22 q4 -10 11 -14" stroke="#2F7A48" stroke-width="2.6" fill="none" stroke-linecap="round"/>`,
    rea:`<path d="M4 15 q2 -5 7 -3 q3 -4 7 -1 q3 1 2 5 q-1 4 -6 3 q-3 3 -7 1 q-4 -1 -3 -5z" fill="#E8902A"/><path d="M8 14 h2 M14 13 h2 M11 17 h2" stroke="#B8602A" stroke-width=".8"/><circle cx="16" cy="9" r="1.8" fill="#F2B632"/>`,
    meli:`<rect x="6" y="8" width="12" height="13" rx="3" fill="#F2B632" stroke="#B8802A" stroke-width=".8"/><rect x="5.5" y="5" width="13" height="3.6" rx="1.2" fill="#A8743A"/><path d="M9 12 h6 v3 h-6z" fill="#FFFFFF80"/>`,
    fei:`<path d="M12 21 v-17" stroke="#6E5A2A" stroke-width="1.6"/>${[[8,9],[16,9],[7.5,13],[16.5,13],[9,17],[15,17]].map(q=>`<ellipse cx="${q[0]}" cy="${q[1]}" rx="2.2" ry="3.4" fill="#E4583F" stroke="#A8322A" stroke-width=".5"/>`).join('')}`,
    mati:`<path d="M12 3 v8 M12 7 q-5 0 -6 4 M12 7 q5 0 6 4" stroke="#3B8C58" stroke-width="1.2" fill="none"/>${[[6,13],[9,15],[12,13],[15,15],[18,13],[8,18],[12,18],[16,18]].map(q=>`<circle cx="${q[0]}" cy="${q[1]}" r="2" fill="#C8302A"/>`).join('')}`,
    tou:`<path d="M12 22 q-10 -9 -3 -19 q11 6 3 19z" fill="#2F6B3F"/><path d="M12 22 q-2 -10 -3 -19 M10.6 14 l-4 -3 M10 9 l-3 -2 M11.2 17 l4 -3 M10.5 11 l4 -3" stroke="#8FBF6A" stroke-width=".8" fill="none"/>`,
    tiairi:`<circle cx="9" cy="12" r="4.4" fill="#C8B89A" stroke="#8A7A5A" stroke-width=".7"/><circle cx="15" cy="12" r="4.4" fill="#BBA987" stroke="#8A7A5A" stroke-width=".7"/><circle cx="12" cy="17" r="4.4" fill="#D4C6A8" stroke="#8A7A5A" stroke-width=".7"/>`,
    hei:hei('#FFFFFF','#F2C94C'), heiarea:hei('#FFFFFF','#E4583F'), heitipa:hei('#FFFDF5','#F7D86A'), heiapetahi:hei('#FFFFFF','#F7C8DA'), heipiti:hei('#E4583F','#F2C94C'), heix:hei('#F28CB1','#FFFFFF'), heimaire:hei('#3B8C58','#8FD08A'), heipo:hei('#9FE3C8','#2B3B6B'),
    monoi:bottle('#F6E7A8'), monoiaute:bottle('#F2A08A'), monoianu:bottle('#B58AD8'), monoivan:bottle('#E8D08A'), tamanuhuile:bottle('#7FA84A'),
    jus:glass('#F2A23A'), paipiti:glass('#F2C94C'), nonojus:glass('#D8D2A0'), jusheiva:glass('#F08A2B'), laitmeli:`<path d="M3 11 q0 10 9 10 q9 0 9 -10z" fill="#8A5A2B"/><ellipse cx="12" cy="11" rx="9" ry="2.6" fill="#FFFDF5"/><path d="M15 3 q2 3 0 5 q-2 -2 0 -5z" fill="#F2B632"/>`,
    'i:poe':dish('#F2C94C'), poetaro:dish('#8A5A8E'), poepiti:dish('#F2A23A'), salade:bowl('#F6E7A8',['#F2C94C','#E4583F','#F08A2B','#3B8C58']), feicoco:bowl('#FFFDF5',['#E4583F','#E4583F','#F08A2B']),
    compost:`<path d="M6 7 q6 -3 12 0 l2 13 q-8 3 -16 0z" fill="#8A6A3B"/><path d="M6 7 q6 2 12 0" stroke="#5C3A1E" stroke-width="1" fill="none"/><path d="M10 12 q2 -4 4 0 q-2 3 -4 0z" fill="#6E9A3E"/>`,
    pareuura:cloth('#C8302A'), pareurea:cloth('#F2B632'), pareuahi:cloth('#F08A5A'), pareuvare:cloth('#7A5AB8'), pareuheiva:cloth('#E4583F'),
    peue:`<rect x="3" y="5" width="18" height="14" rx="1.5" fill="#D9BE7A" stroke="#9A7A3B" stroke-width=".7"/>${[6,9,12,15,18].map(x=>`<path d="M${x} 5 v14" stroke="#9A7A3B" stroke-width=".7"/>`).join('')}${[8,11,14,17].map(y=>`<path d="M3 ${y} h18" stroke="#B8985A" stroke-width=".6"/>`).join('')}`,
    tifaifai:`<rect x="3" y="3" width="18" height="18" rx="1.5" fill="#FFFDF5" stroke="#C8302A" stroke-width="1"/><g transform="translate(12 12) scale(.62) translate(-12 -12)">${hib('#C8302A','#C8302A')}</g>`,
    taupooaute:hat('#E4583F'), taupootipa:hat('#FFFDF5'), taupoo:hat('#FFFFFF'),
    ete:`<path d="M4 10 h16 l-2 10 h-12z" fill="#D9BE7A" stroke="#9A7A3B" stroke-width=".7"/><path d="M7 10 q5 -9 10 0" stroke="#9A7A3B" stroke-width="1.4" fill="none"/>${[7,10,13,16].map(x=>`<path d="M${x} 10 l-.4 10" stroke="#9A7A3B" stroke-width=".6"/>`).join('')}<path d="M4.4 14 h15.2" stroke="#9A7A3B" stroke-width=".6"/>`,
    collierpoe:pearls(false), braceletpoe:pearls(true),
    melivanira:`<rect x="5" y="8" width="11" height="13" rx="3" fill="#F2B632" stroke="#B8802A" stroke-width=".8"/><rect x="4.5" y="5" width="12" height="3.6" rx="1.2" fill="#A8743A"/><path d="M17 21 q1 -9 4 -17" stroke="#3B2A1A" stroke-width="2" fill="none" stroke-linecap="round"/>`,
    niutoru:`<circle cx="12" cy="12" r="8.5" fill="#8A5A2B"/><circle cx="9" cy="10" r="1.8" fill="#3B2A1A"/><circle cx="15" cy="10" r="1.8" fill="#3B2A1A"/><circle cx="12" cy="14.5" r="1.8" fill="#3B2A1A"/><path d="M4 7 l2 1 M20 7 l-2 1 M12 2 v2" stroke="#F2C94C" stroke-width="1.2" stroke-linecap="round"/>`,
    foulard:`<path d="M3 6 h18 l-9 13z" fill="#E4583F"/><path d="M6 6 l6 9 l6 -9" stroke="#FFFFFF90" stroke-width=".8" fill="none"/><path d="M3 6 l-1 4 M21 6 l1 4" stroke="#E4583F" stroke-width="1.4"/>`,
    ballon:`<circle cx="12" cy="12" r="8.5" fill="#F08A2B"/><path d="M3.5 12 h17 M12 3.5 v17 M6 6 q4 6 0 12 M18 6 q-4 6 0 12" stroke="#5C3A1E" stroke-width=".9" fill="none"/>`,
    raquette:`<circle cx="10" cy="10" r="7" fill="#F28CB1" stroke="#C8607E" stroke-width=".8"/><path d="M14.5 14.5 l6 6" stroke="#8A5A2B" stroke-width="3" stroke-linecap="round"/><circle cx="19" cy="5" r="2" fill="#FFFFFF" stroke="#CCC" stroke-width=".5"/>`,
    paumafara:`<path d="M12 2 l7 8 l-7 10 l-7 -10z" fill="#D9BE7A" stroke="#9A7A3B" stroke-width=".8"/><path d="M12 2 v18 M5 10 h14" stroke="#9A7A3B" stroke-width=".6"/><path d="M12 20 q-3 2 0 3 q3 1 0 1" stroke="#E4583F" stroke-width="1" fill="none"/>`,
    casque:`<path d="M3.5 16 q0 -11 8.5 -11 q8.5 0 8.5 11z" fill="#2F80D8"/><path d="M3 16 h18 v2 h-18z" fill="#1F5FA8"/><path d="M8 7 q4 -2 8 0 M12 5 v11" stroke="#FFFFFF80" stroke-width="1" fill="none"/>`,
    _:''};
  o.poe=`<circle cx="12" cy="12" r="7" fill="#4E5E68"/><circle cx="9.5" cy="9.5" r="2.4" fill="#FFFFFF70"/><circle cx="14" cy="15" r="2" fill="#7FA8B8" opacity=".5"/>`;
  o.dessinapetahi=`<rect x="3" y="3" width="18" height="18" rx="1" fill="#FFFDF5" stroke="#C9B890" stroke-width=".8"/><g transform="translate(12 11) scale(.6) translate(-12 -12)">${o.apetahi}</g><path d="M5 19 h14" stroke="#C9B890" stroke-width=".6"/>`;
  o.ahia=`<path d="M12 6 q7 -2 7 7 q0 8 -7 8 q-7 0 -7 -8 q0 -9 7 -7z" fill="#C8302A"/><circle cx="9.5" cy="10" r="1.8" fill="#FFFFFF50"/><path d="M12 6 q0 -3 3 -4" stroke="#3B8C58" stroke-width="1.4" fill="none"/>`;
  return o; })();
function icoSVG(id,isItem){ const it=isItem?ITEMS[id]:null; let b=(isItem&&ICO['i:'+id])||ICO[id];
  if(!b){ const c=(it&&it.aura&&it.aura!=='rainbow')?it.aura:'#9FB3BC'; b=`<circle cx="12" cy="12" r="6" fill="${c}"/><circle cx="10" cy="10" r="2" fill="#FFFFFF60"/>`; }
  return `<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">${b}</svg>`; }

/* très mûr : on laisse un fruit mûr sur la plante, il devient très mûr, la récolte compte double. Rien ne pourrit. */
function vrDur(pl){ return Math.max(12*36e5, PLANTS[pl.p].days*864e5*.5); }
function vrState(pl){ if(!pl || !pl.slow) return 0; return Date.now()-pl.slow>=vrDur(pl) ? 2 : 1; }
function vrLeft(pl){ const ms=pl.slow+vrDur(pl)-Date.now(); const h=Math.max(1,Math.ceil(ms/36e5)); return h>=24 ? `${Math.floor(h/24)} j ${h%24} h` : `${h} h`; }
function vrTag(pl,i){ const v=vrState(pl), ok='<span class="small" style="color:var(--fern);font-weight:700">Mûr !</span>';
  if(v===2) return `<span class="small" style="color:#B8802A;font-weight:800">Très mûr ! Récolte ×2</span>`;
  if(v===1) return ok+`<span class="small muted">Très mûr dans ${vrLeft(pl)} (tu peux quand même récolter maintenant)</span>`;
  if(pl.p==='metua' || pl.p==='vanira') return ok;
  return ok+`<button class="btn sm ghost" data-vr="${i}">Laisser mûrir encore · ${vrLeft({p:pl.p, slow:Date.now()})} · ×2</button>`; }

/* la toute première graine plantée pousse vite : on voit tout de suite que ça marche */
function firstGrow(i){ try{ if(store.get('firstGrow',false)) return ''; store.set('firstGrow',true); if(Array.isArray(garden.got) && garden.got.length) return ''; const pl=garden.plots[i]; if(!pl || !PLANTS[pl.p]) return ''; const d=PLANTS[pl.p].days*864e5; pl.t=Math.min(pl.t, Date.now()-d+2*36e5); return 'Ta première graine ! La terre neuve est généreuse : mûre dans 2 h.'; }catch(e){ return ''; } }

function timeCard(){ let ins=false; try{ const O=insGet(); ins=!!(O.uke||O.toere||O.pahu); }catch(e){}
  return `<details class="card flat"><summary class="eyebrow" style="cursor:pointer">Le temps du faʻaʻapu</summary><p class="small muted" style="margin-top:8px">Chaque plante a son temps, de 1 jour (la tiare) à 10 jours (le tāmanu). Rien ne meurt, rien ne pourrit : tes récoltes tʼattendent.</p>
    <p class="small"><b>Pour aller plus vite :</b> un sac de compost (−1 jour), planter une bonne nuit de lune, ${ins?'jouer dʼun instrument au faʻaʻapu, une fois par jour':'la musique (un atelier se cache quelque part)'}… et quelques secrets à trouver.</p>
    <p class="small"><b>Pour aller plus lentement :</b> sur un fruit mûr, « Laisser mûrir encore ». Il devient <b>très mûr</b> et sa récolte compte double, au coffre ou en plumes.</p></details>`; }

/* le secret de lʼaube : une tiare ʻāpetahi mûre, dans un faʻaʻapu partagé, regardée au lever du jour */
ITEMS.dessinapetahi={name:'Dessin de la tiare ʻāpetahi', un:'un dessin de la tiare ʻāpetahi', worth:50, aura:'#F7C8DA', mood:'lʼémerveillement', need:{}, days:0, hint:'Dessiné à lʼaube, devant une ʻāpetahi mûre qui sʼouvre.', hid:'Une ʻāpetahi mûre, au bon moment…', shared:true};
function apDawnNow(){ const h=new Date().getHours(); return h>=5 && h<8; }
function apCrack(){ try{ AC = AC || new (window.AudioContext||window.webkitAudioContext)(); if(AC.state!=='running') AC.resume(); const t=AC.currentTime+.05; [0,.09,.15].forEach((dt,k)=>{ const n=Math.floor(AC.sampleRate*.03), buf=AC.createBuffer(1,n,AC.sampleRate), d=buf.getChannelData(0); for(let i=0;i<n;i++) d[i]=(Math.random()*2-1)*Math.pow(1-i/n,4); const s=AC.createBufferSource(), f=AC.createBiquadFilter(), g=AC.createGain(); s.buffer=buf; f.type='highpass'; f.frequency.value=2500+k*800; g.gain.value=.25; s.connect(f); f.connect(g); g.connect(AC.destination); s.start(t+dt); }); }catch(e){} }
function apDawnSVG(){ let p=''; [-64,-32,0,32,64].forEach(a=>p+=`<ellipse class="pt" style="--r:${a}deg" cx="160" cy="92" rx="11" ry="26" fill="#FFFFFF" stroke="#E8DCC8" stroke-width="1.2"/>`);
  return `<svg viewBox="0 0 320 170" role="img" aria-label="Le soleil se lève sur le Temehani, une tiare ʻāpetahi sʼouvre"><circle class="sun" cx="250" cy="120" r="26" fill="#FFE7A0"/><path d="M0 128 q60 -34 120 -20 q50 -26 110 -6 q50 -12 90 4 v64 h-320z" fill="#3E5A4A"/><path d="M0 150 q80 -14 160 -6 q80 -10 160 0 v26 h-320z" fill="#2F4A3A"/><g transform="translate(0 30)">${p}<path d="M160 118 v26" stroke="#3B8C58" stroke-width="3"/><path d="M160 136 q-18 -4 -26 6 M160 132 q18 -4 26 6" stroke="#3B8C58" stroke-width="5" fill="none" stroke-linecap="round"/></g></svg>`; }
{ const _rs=renderSharedGarden; renderSharedGarden=function(code,d){ const r=_rs.apply(this,arguments); try{
    if(d && d.p==='apetahi' && SPLANTS.apetahi){ const days=sgDays(d); if(days.length>=SPLANTS.apetahi.days){ const key=pairKey(code)+':'+(days[0]||''); const seen=store.get('apDawn',{})||{}; const card=sheetInner.querySelector('.card');
      let h=''; if(seen[key]) h=`<p class="small muted">Tu lʼas vue sʼouvrir à lʼaube. Ce souvenir-là est à toi.</p>`;
      else if(apDawnNow()) h=`<div class="card"><div class="eyebrow">Cʼest lʼaube</div><p class="small">Chut… La tiare ʻāpetahi est sur le point de sʼouvrir.</p><button class="btn primary" id="apDawnGo">Regarder</button></div>`;
      else h=`<p class="small muted">Les anciens de Raʻiātea disent que lʼʻāpetahi sʼouvre au lever du jour, avec un tout petit bruit…</p>`;
      if(card) card.insertAdjacentHTML('beforebegin',h); const b=$('#apDawnGo'); if(b) b.onclick=()=>apDawnOpen(code,key); } }
  }catch(e){} return r; }; }
function apDawnOpen(code,key){ const seen=store.get('apDawn',{})||{}; if(seen[key]) return; seen[key]=dayKey(Date.now()); store.set('apDawn',seen);
  openSheet(`<div class="head"><div><div class="eyebrow">Le secret de lʼaube</div><h2>La tiare ʻāpetahi</h2></div><button class="x" id="sx" aria-label="Fermer">×</button></div>
    <div class="apDawn">${apDawnSVG()}</div>
    <p id="apTx" class="small muted" style="margin-top:10px">Écoute bien…</p>
    <div id="apMore" hidden><p class="small">Dans la vraie vie, elle ne fleurit que sur le mont Temehani, à Raʻiātea, et nulle part ailleurs. On ne la cueille pas : elle est protégée. Alors on la regarde… et on la dessine.</p>
    <p class="small"><b>Ton manu a dessiné la tiare ʻāpetahi.</b> Le dessin est dans ton coffre.</p><button class="btn primary" id="apOk">Māuruuru</button></div>`);
  $('#sx').onclick=closeSheet; setTimeout(apCrack,1400); setTimeout(()=>{ const t=$('#apTx'); if(t) t.innerHTML='<b>Crac…</b> Tu lʼas entendue ? Elle vient de sʼouvrir.'; },1700);
  try{ garden.items.dessinapetahi=(garden.items.dessinapetahi||0)+1; learn('dessinapetahi'); saveGarden(); chestBadge(); }catch(e){}
  setTimeout(()=>{ const m=$('#apMore'); if(m) m.hidden=false; const o=$('#apOk'); if(o) o.onclick=()=>openSharedGarden(code); },3400); }

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
