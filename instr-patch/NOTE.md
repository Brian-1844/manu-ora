# Patch — L'atelier des instruments

Base v91. Une carte « L'atelier des instruments » s'ajoute en bas du faʻaʻapu.

## Fabriquer (avec les récoltes du faʻaʻapu)
| Instrument | Matériaux | Fait pousser plus vite |
|---|---|---|
| ʻUkulele (une pièce de bois, 8 cordes) | 2 bois + 5 plumes (le fil de pêche des cordes) | les fleurs (tiare, ʻaute, tīpaniē, vānira, ʻāpetahi…) |
| Tōʻere (tronc creusé et fendu, deux baguettes) | 3 bois | les arbres (coco, ʻuru, tou, tāmanu, fara…) |
| Pahu (grand tambour, peau lacée à la bourre de coco) | 2 bois + 2 cocos + 5 plumes (la peau, par un artisan) | les fruits (meiʻa, vī, painapo, ʻānani…) |
« Bois » = du tou ou de l'ʻuru récolté. Il faut donc planter des arbres.

## Décorer (change la forme et la force)
Naturel (6 h de pousse en plus), Gravé de motifs de tatau (9 h, 3 plumes), Nacré, incrusté d'une perle (12 h, 1 perle du coffre). Une décoration achetée reste acquise ; on peut changer de l'une à l'autre.

## Jouer pour le faʻaʻapu
**Une fois par jour en tout**, avec un seul instrument au choix (les autres boutons attendent le lendemain). Le son est joué (ukulele : l'air choisi ; tōʻere et pahu : un rythme), et chaque plante de la bonne famille qui pousse encore gagne 6, 9 ou 12 h. Les plantes mûres ne sont pas touchées.

Clé : `instr` ({uke|toere|pahu: {fin, owned, day}}).

## À valider
Conseiller culturel / artisan : les descriptions (bois utilisés, peau du pahu, cordes en fil de pêche), à confirmer auprès du Service de l'artisanat traditionnel. Locuteur : tōʻere, pahu.

Testé : `node test_instr.js [fichier]` — fabrication refusée sans bois, fabrication des trois, décor nacré, tōʻere qui ne fait avancer que l'arbre, une fois par jour, pahu sur le fruit. Navigateur sans écran ; son non vérifié.
