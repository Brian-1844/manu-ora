# Anguilles redessinées + décors qui grandissent — à intégrer dans la session en cours (v91 ou plus)

Écrit dans l'ancienne session, mais **développé et vérifié sur l'aperçu v91** (syntaxe correcte, aucun message d'erreur, rendu contrôlé sur captures). Non testé sur les fichiers du site de la session en cours, ni sur un vrai téléphone.

## Pour l'intégrer
1. `python3 scene_patch.py /home/claude/manu-ora-site/index.html /home/claude/manu-ora.html`
2. Monter `APP_V` et le cache de `sw.js`, `node --check`, tester (`test_scene.js` donne un exemple ; adapter le chemin du fichier), zipper, publier.
3. Ajouter au README la section ci-dessous.

## Ce que fait le patch
**Anguilles (elles ressemblaient à des vers).** D'après la description de l'anguille marbrée, *Anguilla marmorata* : corps plein, épais sur la première moitié puis effilé ; tête large et aplatie, mâchoire inférieure avancée ; petit œil ; nageoire pectorale arrondie bordée de jaune (l'« oreille » du puhi taria) ; longue nageoire dorsale ; marbrures sombres sur le dos, ventre clair. Ondulation qui se propage de la tête vers la queue.
- `eelSVG(c,d)` est remplacée (même signature : le bassin, le trou d'eau et le repas des anguilles en profitent sans autre changement). Nouvelle fonction `eelPath(...)`.
- Les petites anguilles du décor rivière (vues du dessus) ont un corps effilé, une tête plate et deux nageoires pectorales.

**Décors qui grandissent** (les quatre lieux), selon `surfDays`, `eelDays`, `hikeDone`, `placeDays`, `mktI`, `yardI`. Rien ne disparaît si l'on s'absente.
- Plage : une planche plantée dans le sable (1 jour de surf) ; la houle et deux dauphins qui sautent (3 jours) ; une baleine à l'horizon, avec son souffle (7 jours).
- Rivière : un sentier sur la montagne (2 jours auprès des anguilles) ; une seconde cascade et des fleurs sur les rives (3 jours) ; la vieille anguille et un arc-en-ciel dans la brume de la cascade (6 jours) ; un drapeau par montée faite ; un drapeau au sommet et un oiseau blanc qui tourne autour quand les trois montées sont faites.
- Ville, circulation : au départ, seule une **Vespa** passe dans la rue (le véhicule jaune et la voiture d'origine sont masqués). Le **vieux truck** à caisse en bois, chargé de passagers et de bagages sur le toit, arrive après 2 activités ; la **petite voiture** revient après 4.
- Ville (compteur : jours où l'activité « dire non » est terminée + scénarios du marché) : un étal de fruits et des fleurs aux balcons (1) ; des fanions au-dessus de la rue et une marchande de couronnes (3) ; une grande fresque peinte sur un mur (6).
- École (compteur : jours où une activité de l'école est terminée + scénarios de la cour) : un petit potager et des dessins à la craie (1) ; une banderole « Maeva · ʻIa ora na » et des fanions (3) ; une fresque sur le mur et deux oiseaux sur le toit (6).
- Pour la ville et l'école, les jours sont comptés à partir de l'installation du patch (`placeDays`, alimenté par une enveloppe de `placeDone`) ; les compteurs `mktI` et `yardI` existants sont repris.
- Une carte « Ce décor grandit avec toi » dans « Lieux du jour » (les étapes non atteintes s'affichent « ???? » avec leur condition).
- Un message quand le décor change (« La plage a changé : regarde le large »).
- Technique : `sceneInner`, `renderPlace`, `closeSheet` et `placeDone` sont enveloppées (pas réécrites) ; le décor se redessine quand la progression change.

## Section README

## Les quatre décors grandissent, les anguilles sont redessinées (version NN)

Les anguilles sont redessinées d'après l'anguille marbrée du fenua (corps effilé, tête plate, nageoire pectorale, marbrures).

Les décors se remplissent à mesure que l'on pratique : planche, houle, dauphins et baleine pour le surf ; sentier, seconde cascade, fleurs, vieille anguille et arc-en-ciel pour les anguilles ; drapeaux et oiseau du sommet pour les montées. La ville gagne un étal, des fleurs, des fanions, une marchande de couronnes puis une fresque ; l'école un potager, des dessins à la craie, une banderole, des fanions, une fresque et deux oiseaux. La liste est dans « Lieux du jour ». Rien ne disparaît si l'on s'absente.
