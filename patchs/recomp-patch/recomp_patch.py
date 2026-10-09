# Patch "récompenses des nouvelles activités" (jeux de la cour, pāuma, la route, la soirée, le Heiva).
# Dépend de jeu-patch, heiva-patch, route-patch. Usage : python3 recomp_patch.py <site>/index.html <manu-ora.html>
import sys
for path in sys.argv[1:]:
    s=open(path,encoding='utf8').read()
    def rep(a,b,n=1):
        global s
        assert s.count(a)==n,(path,a[:70],s.count(a))
        s=s.replace(a,b)
    assert 'function bkAttemptEnd(' in s and 'function openHeiva(' in s and 'function rtStep(' in s, 'appliquer jeu-patch, heiva-patch et route-patch avant'
    new = r"""/* ---------- récompenses des nouvelles activités : une par vraie étape, jamais de pression ---------- */
Object.assign(ITEMS,{
  foulard:{name:'Foulard du tupa', un:'le foulard du tupa', worth:30, aura:'#E4583F', mood:'le cran', need:{}, days:0, hint:'Trois buts de suite, face au tupa.'},
  ballon:{name:'Ballon dédicacé', un:'un ballon dédicacé', worth:30, aura:'#F08A2B', mood:'la persévérance', need:{}, days:0, hint:'Vingt paniers, ratés compris entre eux.'},
  raquette:{name:'Raquette de corail', un:'une raquette de corail', worth:30, aura:'#F28CB1', mood:'le bon moment', need:{}, days:0, hint:'Un échange réussi avec la balle la plus rapide.'},
  paumafara:{name:'Pāuma de fara', un:'un pāuma de fara', worth:40, aura:'#F2C94C', mood:'tenir sans serrer', need:{}, days:0, hint:'Sept jours de pāuma.'},
  casque:{name:'Casque du manu', un:'le casque du manu', worth:40, aura:'#2F80D8', mood:'la prudence', need:{}, days:0, hint:'Cinq bons réflexes sur cinq, à vélo et en scooter.'},
  heipo:{name:'Hei de nuit', un:'un hei de nuit', worth:40, aura:'#9FE3C8', mood:'veiller sur les autres', need:{}, days:0, hint:'Avoir vu toutes les situations de la soirée.'},
  pareuheiva:{name:'Pāreu du Heiva', un:'un pāreu du Heiva', worth:50, aura:'#E4583F', mood:'la fête partagée', need:{}, days:0, hint:'Le premier cœur lié venu danser autour de ton feu.'},
  jusheiva:{name:'Jus du Heiva', un:'un jus du Heiva', worth:24, aura:'#F2A23A', mood:'la fête sans rien dʼautre', need:{painapo:1, anani:1}, days:0, hint:'Ce quʼon boit autour du feu, mélangé.', secret:true}});
function rwOnce(key){ const o=store.get('rw',{})||{}; if(o[key]) return false; o[key]=dayKey(Date.now()); store.set('rw',o); return true; }
function rwItem(id,msg){ try{ garden.items[id]=(garden.items[id]||0)+1; saveGarden(); try{ chestBadge(); }catch(e){} toast(ITEMS[id].name+' : au coffre'); if(msg) setTimeout(function w(n){ n=n||0; if(n>12) return; if(!visitFree() || bubbleEl.classList.contains('show') || !$('#sheet').hidden){ setTimeout(()=>w(n+1),5000); return; } say(msg); },1800); }catch(e){} }
function rwSeed(k,msg){ try{ garden.seeds[k]=(garden.seeds[k]||0)+1; saveGarden(); toast('Une graine de '+(PLANTS[k]?PLANTS[k].name:k)+' dans ton sac'); if(msg) setTimeout(()=>{ if(visitFree() && !bubbleEl.classList.contains('show')) say(msg); },1800); }catch(e){} }
{ const _ae=bkAttemptEnd; bkAttemptEnd=function(ok,msg){ const was=BK.ending; const r=_ae.apply(this,arguments); try{ if(was || BK.i<1) return r;
      if(BK.k==='f'){ BK.fRun = ok ? (BK.fRun||0)+1 : 0; if(BK.fRun>=3 && rwOnce('foulard')) rwItem('foulard','Trois buts de suite ! Le tupa tʼoffre son foulard. Il dit que tu lʼas bien regardé.'); }
      if(BK.k==='b' && ok){ const n=(store.get('bkBaskets',0)||0)+1; store.set('bkBaskets',n); if(n>=20 && rwOnce('ballon')) rwItem('ballon','Vingt paniers ! Et combien de ratés entre eux ? Peu importe : tu as continué. Voilà un ballon dédicacé.'); }
      if(BK.k==='p' && ok && BK.i===5 && rwOnce('raquette')) rwItem('raquette','Un échange complet avec la balle la plus rapide ! Une raquette de corail pour toi.'); }catch(e){} return r; }; }
function rwKite(){ try{ const n=kiteDays().length; if(n>=3 && rwOnce('fara')) rwSeed('fara','Trois jours de pāuma : voilà une graine de fara. Avec ses feuilles, on tresse les vrais cerfs-volants.'); if(n>=7 && rwOnce('paumafara')) rwItem('paumafara','Sept jours de pāuma ! Un pāuma de fara, rien que pour toi.'); }catch(e){} }
{ const _rs=rtStep; rtStep=function(){ const r=_rs.apply(this,arguments); try{ if(RTS.list && !RTS.list[RTS.i] && RTS.ok===5 && !RTS.rwDone){ RTS.rwDone=1; const o=store.get('rt5',{})||{}; o[RTS.v]=1; store.set('rt5',o); if(o.b && o.s && rwOnce('casque')) rwItem('casque','Cinq sur cinq à vélo, et cinq sur cinq en scooter ! Le casque du manu est à toi.'); } }catch(e){} return r; }; }
{ const _ps=poStep; poStep=function(){ const r=_ps.apply(this,arguments); try{ const sc=SOIRS.list&&SOIRS.list[SOIRS.i]; if(sc && SOIRS.pick!==null){ const seen=store.get('poSeen',[])||[]; if(!seen.includes(sc.id)){ seen.push(sc.id); store.set('poSeen',seen); } if(SOIR.every(x=>seen.includes(x.id)) && rwOnce('heipo')) rwItem('heipo','Tu as vu toutes les situations de la soirée. Ce hei de nuit, cʼest pour ceux qui veillent sur les autres.'); } }catch(e){} return r; }; }
{ const _oh=openHeiva; openHeiva=function(){ const r=_oh.apply(this,arguments); try{ const b=$('#hvLit'); if(b){ const f=b.onclick; b.onclick=function(){ f&&f.apply(this,arguments); if(rwOnce('tipanie')) rwSeed('tipanie','Une graine de tipanie : ses fleurs feront la guirlande du prochain Heiva.'); }; } const j=$('#hvBar'); if(j){ const g=j.onclick; j.onclick=function(){ g&&g.apply(this,arguments); const box=$('#hvJ'); if(box) box.addEventListener('click', e=>{ const t=e.target.closest('[data-j]'); if(!t) return; const set=store.get('hvJuices',[])||[]; if(!set.includes(t.dataset.j)){ set.push(t.dataset.j); store.set('hvJuices',set); } if(set.length>=4 && rwOnce('jusheiva')){ try{ if(!garden.known.includes('jusheiva')) garden.known.push('jusheiva'); saveGarden(); }catch(x){} setTimeout(()=>toast('Nouvelle recette dans le livre : le jus du Heiva (ananas + orange)'),1200); } }, true); }; } }catch(e){} return r; }; }
{ const _ha=hvArrive; hvArrive=function(v){ const r=_ha.apply(this,arguments); try{ if(rwOnce('pareuheiva')) rwItem('pareuheiva','Ton premier invité au Heiva ! Le pāreu du Heiva, pour les soirs de fête.'); }catch(e){} return r; };
  const _hb=hvBtn; hvBtn=function(a){ const r=_hb.apply(this,arguments); try{ if(a[1]==='go' && rwOnce('pareuheiva')) rwItem('pareuheiva','Ta première fois au Heiva dʼun ami ! Le pāreu du Heiva, pour les soirs de fête.'); }catch(e){} return r; };
  const _cs=closeSheet; closeSheet=function(){ const r=_cs.apply(this,arguments); setTimeout(rwKite,600); return r; }; }

"""
    rep("/* ---------- install button ---------- */", new+"/* ---------- install button ---------- */")
    open(path,'w',encoding='utf8').write(s)
    print('ok',path)
