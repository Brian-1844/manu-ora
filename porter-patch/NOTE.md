# Patch — Le manu porte son instrument sur le dos

Dépend de `instr-patch` (et utilise `vivo-patch` s'il est là).

- Dans l'atelier des instruments, chaque instrument fabriqué a un bouton « Porter sur le dos » / « Le poser ». Un seul instrument à la fois ; en choisir un autre le remplace.
- Le manu le porte en bandoulière (ʻukulele, tōʻere avec ses baguettes, pahu, vivo), avec sa finition : gravé (motif), nacré (perle, bois plus foncé). Il suit le manu dans ses vols et se tourne avec lui.
- **Deux façons de le porter** (choix en haut de l'atelier) : une **cordelette tressée** rouge et jaune, nouée autour de l'instrument avec un pompon ; ou un **étui tressé en fara** avec un bouton en coquillage (2 fara du coffre, une seule fois).
- Le choix est gardé (`cfg.carry`, `cfg.carryStyle`, `etuiMade`) et revient après rechargement.
- Limite : les amis ne le voient pas encore sur ton manu quand il leur rend visite (l'apparence partagée ne contient pas l'instrument).

Testé : `node test_porter.js [fichier]` : les 4 instruments portés tour à tour, poser, rechargement, redessin du manu. Navigateur sans écran.
