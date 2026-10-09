# Patch — Le vaʻa : pagayer ensemble (plage)

Dépend de `jeu-patch` et `dock-patch`. Bouton « Le vaʻa : pagayer ensemble » dans la feuille de la plage, icône Vaʻa dans la colonne.

- Jeu de rythme : des ronds glissent vers un cercle ; on touche la piste quand un rond y passe. Un tambour (son de synthèse) joue chaque temps.
- **Petit rond bleu = coup léger** (touche brève, moins de 0,2 s). **Grand rond rouge « HOE » = coup fort** (on garde le doigt appuyé un instant, puis on lâche). Mauvaise force : le coup compte peu, avec un conseil.
- Précision : « Parfait » à ±0,09 s, « Bien » à ±0,24 s ; au-delà, raté. La pirogue accélère avec les bons coups ; une barre jaune montre l'avancée.
- **Trois niveaux** (on peut rejouer les niveaux déjà ouverts) : Le lagon (56 temps/min, un coup fort sur quatre), La passe (70, coups forts variés, après 3 jours de vaʻa), Le large (84, avec des contretemps, après 7 jours).
- Fin : « En rythme : n % » et la phrase « pas besoin d'être le plus fort : il faut être ensemble ». Activité `vaa` (plume via `award`). Clés : `vaaDays`, `vaaPick`.

Sur un vrai téléphone, la différence léger/fort est faite par la durée de l'appui (un téléphone ne mesure pas la force du doigt de façon fiable dans un navigateur).

À valider : « HOE » (pagaie) et le vocabulaire du vaʻa (locuteur, club de vaʻa).

Testé : `node test_vaa.js [fichier]` avec de vrais appuis souris : en rythme (≈75 % par le robot, le délai du navigateur de test compte), mauvaise force (12 %), rien (0 %), niveaux. Navigateur sans écran ; son non vérifié.
