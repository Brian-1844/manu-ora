# Patch — Le vivo, la flûte nasale cachée

Dépend de `instr-patch` et `jeu-patch`.

- **Caché** : rien n'apparaît tant que l'ʻukulele, le tōʻere et le pahu ne sont pas fabriqués. Ensuite, une carte « ???? » dans l'atelier donne un indice : « là où l'eau chante, pose ce qui te pèse ».
- **Le ʻofe (bambou)** se trouve en faisant l'activité de la rivière (poser un souci) une fois les trois instruments faits. Puis on fabrique le vivo : 1 ʻofe + 3 plumes. Il joue un petit air doux (synthèse).
- **Un souffle par jour, au choix :**
  - *Une seconde chance* : le prochain essai raté du jour dans les jeux de la cour ne compte pas ; on le retente.
  - *Appeler le ʻūʻupa* : le pigeon vert (Ptilinopus purpuratus, qui ne vit qu'à Tahiti et Moʻorea) vole près du manu toute la journée.
- **Offrir le ʻūʻupa** à un cœur lié (`g:'uupa'`) : il quitte ton manu et va chez l'ami pour la journée.

Clés : `vivo` ({ofe, made, day, retry}), `uupa` ({day, from, gave}).

À valider : nom tahitien « ʻūʻupa » et son orthographe (locuteur), « vivo », le dessin du pigeon (vert, tête grise, calotte violette, ventre jaune pâle, d'après Wikipédia).

Testé : `node test_vivo.js [fichier]` (deux utilisateurs) : caché, indice, ʻofe, fabrication, essai raté non compté puis le suivant compté, ʻūʻupa appelé, offert, reçu chez l'amie. Navigateur sans écran ; son non vérifié.
