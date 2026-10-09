# Patch — Les jeux de la cour, version 2 : basket, tirs au but, ping-pong

Remplace entièrement la version 1 (jauge qui va et vient). Base : v91 ou plus récent. Les trois jeux sont dessinés et animés sur un `<canvas>` ; tout le reste de l'appli reste en SVG.

## Ce qui a changé, et pourquoi (d'après les jeux mobiles qui marchent)
- **Geste direct au lieu d'une jauge.** Basket : on glisse le doigt du ballon vers le panier, direction + longueur du geste = le tir (comme le basket de Messenger ou Flick Basketball). Penalty : on glisse jusqu'au coin visé, le ballon part là où le doigt s'arrête, un geste vif part plus vite. Ping-pong : la raquette suit le doigt.
- **Une vraie physique, lisible.** Gravité, rebond sur le cercle et la planche, filet qui bouge. Au ping-pong, l'angle de renvoi dépend de l'endroit où la balle touche la raquette (règle de Pong, 1972) et la balle accélère à chaque coup (+7 %).
- **Du retour visuel (« juice ») en petite dose** : écrasement de la raquette, secousse de 2–3 px, flash de 100 ms, 20 particules, texte flottant, arrêt d'image de 70 ms sur un panier. Tout est coupé si le téléphone demande moins d'animations.
- **Une difficulté qui bouge** : le panier change de place à chaque tir et se met à osciller après 3 réussites de suite ; le tupa (gardien) **penche vers le côté où il va plonger** (son « tell »), feinte parfois à partir du 3e tir, et plonge tard sur les tirs mous ; au ping-pong, chaque balle repart un peu plus vite que la précédente.
- **Le message de chaque jeu est dans la mécanique** : rater puis retirer (basket), regarder avant d'agir (le tell du tupa), répondre au bon moment (le rallye).

## Inchangé
Bouton « Jouer dans la cour » à l'école, 5 essais, 1 plume par jour au maximum, journée comptée dans `placeDays.haapii`, mode à deux coopératif (`g:'jeu'` / `'jeuOk'` / `'bravo'`, scores additionnés, pas de match ni de classement), clés `bkDay`, `bkOut`. Règles Firebase inchangées.
Correctif : le message « À vous deux : n sur 10 » réessaie jusqu'à ce que l'écran soit libre, au lieu d'être perdu si la visite de l'ami s'anime encore.

## Détails utiles
- Penalty : coins hauts (« lucarne ») et extrémités imbattables même si le tupa plonge du bon côté, mais au risque du poteau ou du dessus. Sauvegarde ≈ si le tir est dans sa zone (74 % de la moitié du but) et sous 72 % de la hauteur.
- Ping-pong : 5 renvois pour réussir l'échange ; le manu renvoie toujours (c'est coopératif) et vise des endroits variés.
- Basket : trajectoire pointillée pendant le geste (aide à viser) ; « Que du filet ! » si ni cercle ni planche.

## Testé
`node test_jeux.js b|f|p [fichier]` : deux utilisateurs simulés, gestes réels (souris/pointer) ou appels des mêmes fonctions que le doigt, mode à deux complet, fermeture en pleine partie. Navigateur sans écran et base simulée ; **jamais sur un vrai téléphone** : le ressenti du geste (longueur de glissement, vitesse) est à régler avec un vrai pouce, et les constantes sont au début de chaque jeu (`5.4` pour la force du basket, `.68-spd*.16` pour la vitesse du penalty, `1.07` pour l'accélération du ping-pong).

README : > **Les jeux de la cour** — à l'école : panier de basket, tirs au but, ping-pong. On glisse le doigt, on regarde, on recommence. Seul ou avec un cœur lié : à deux, les scores s'additionnent.
