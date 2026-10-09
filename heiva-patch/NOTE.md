# Patch — Le pāuma (cerf-volant) et Te Heiva

Dépend de `jeu-patch` (moteur canvas) et `dock-patch` (icônes). Le script refuse de s'appliquer sans eux.

## Le pāuma (plage)
- Bouton « Le pāuma, le cerf-volant » dans la feuille de la plage, et icône Pāuma dans la colonne.
- On appuie pour tendre la ligne, on relâche pour donner du mou. Trop serrée trop longtemps : elle casse. Trop lâche : le pāuma tombe. Une jauge à droite montre la tension et la zone verte.
- Le vent change par rafales qu'on voit venir dans les cocotiers ; son nom s'affiche (maraʻamu, maoaʻe… si le patch du ciel est là).
- Niveaux : Brise (45 s), Alizé (60 s, après 3 jours), Rafales (75 s, après 7 jours). Clé `kiteDays`. Activité `pauma` dans le journal.
- Une pancarte sur la plage : « Pāuma : jamais près des fils électriques ».
- La phrase de fin : « Ni trop serré, ni trop lâche. Ça marche aussi avec ce qu'on tient dans sa tête. »

## Te Heiva
- **S'ouvre quand les 5 airs de ukulélé (hors duos) sont connus.** Le manu l'annonce une fois. Un lieu de plus dans « Lieux », toujours de nuit.
- **Le feu, en sécurité** : c'est **tonton (un adulte) qui l'allume** (« Demander à tonton d'allumer le feu ») ; un cercle de pierres sur le sable, près de l'eau, et un seau d'eau de mer. La première fois, tonton dit : « Un feu, on le fait avec un adulte, sur le sable, loin des arbres, et on l'éteint avec de l'eau avant de partir. » « Fin de soirée : éteindre le feu » (seau d'eau + sable). Si un feu d'un autre soir n'a pas été éteint, on doit d'abord l'éteindre avant d'en rallumer un.
- Danser (le manu joue un air connu, les invités dansent), le bar à jus.
- **Inviter des cœurs liés** (`g:'heiva'`) : l'ami accepte (`g:'heivaOk'`), son manu apparaît autour du feu **avec sa vraie apparence**, et le tien chez lui, **pour la soirée** (jusqu'au lendemain). Un ami qui n'a pas encore débloqué le Heiva peut venir ce soir-là grâce à l'invitation. 4 invités affichés au plus.
- **Prévention, de façon indirecte, sans aucun mot sur les drogues ni l'alcool :**
  - la carte du « Bar du Heiva » : jus d'ananas, jus de pamplemousse, eau de coco, lait de coco au miel — « C'est tout, et c'est déjà beaucoup. » Ce sont les seules boissons qui existent dans la fête ;
  - une pancarte en bois avec un manu et un coco : « Ici, les seuls qui planent, ce sont les manu. »
- Clés : `heiva` ({lit, circle, guestDay, seen, juice}), `hvDay`.

## À valider
- **Professionnel de la prévention (addictions)** : les deux pancartes, et l'absence volontaire de message explicite.
- **Conseiller culturel** : la représentation du Heiva (fête nationale avec une forte charge culturelle) ; ici c'est une petite fête sur la plage « façon Heiva », pas le concours.
- Locuteur : pāuma, ʻori, tōʻere.

## Testé
`node test_heiva.js <fichier avec SYNC_URL factice>` : pāuma tenu jusqu'au bout et ligne cassée ; Heiva fermé puis ouvert ; feu, bar, invitation ; l'amie qui n'a pas les airs vient quand même ; son manu apparaît avec sa couleur ; le lendemain le feu s'éteint et les invités repartent. Navigateur sans écran, base simulée ; pas de vrai téléphone, son non vérifié.
