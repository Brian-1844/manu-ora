# jardin-patch — le faʻaʻapu, suite (v104)

- **Images** : chaque récolte et chaque graine (`ICO`, `icoSVG(id,isItem)`) et chaque création du coffre (pastille teintée de son aura). La plante secrète reste sans image tant quʼelle est secrète. `ICO['i:poe']` = le poʻe (le plat), `ICO.poe` = la perle.
- **Très mûr** : sur un fruit mûr, « Laisser mûrir encore » (`pl.slow`). Au bout de la moitié de son temps de pousse (12 h minimum), il est très mûr : halo doré, récolte ×2 au coffre ou en plumes. On peut récolter avant, normalement. Rien ne pourrit. Pas pour le metuapuaʻa ni la vānira.
- **Première pousse** : la toute première graine plantée (si rien nʼa jamais été récolté) est mûre en 2 h (`firstGrow`).
- **Carte « Le temps du faʻaʻapu »** (repliée) : ce qui accélère (compost, lune, musique) et ce qui ralentit (très mûr). Les autres secrets ne sont pas dévoilés.
- **Le secret de lʼaube** : dans un faʻaʻapu partagé, une tiare ʻāpetahi mûre regardée entre 5 h et 8 h sʼouvre (animation, petit « crac »). Message : elle ne fleurit que sur le Temehani et on ne la cueille pas. Récompense : « Dessin de la tiare ʻāpetahi » au coffre, une fois par plantation (`apDawn`). Le reste de la journée, un indice discret.
- Test : `test_jardin.js` (navigateur sans écran seulement).
- À valider : le récit de lʼʻāpetahi (sʼouvre à lʼaube avec un léger bruit, protégée, Temehani) avec un conseiller culturel de Raʻiātea.
