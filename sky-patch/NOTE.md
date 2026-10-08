# Patch — Les quatre pierres, le passage, Te reva (le monde du ciel) : nuages et vents

Dépend du patch décors (`scene-patch`, pour savoir qu'un décor est complet). S'accorde avec `dock-patch` s'il est présent (icônes Ciel / Nuages / Vents). Partie 1 et 2 sur 4 : restent « l'île vue d'en haut » et le fare (avec l'aide d'un cœur lié).

## Ce que ça ajoute
- **Une pierre par décor complet** (toutes les étapes du décor atteintes) : rivière verte, plage bleue, ville rouge, école dorée. Le manu l'annonce (« je ne sais pas à quoi elle sert, je la garde »). Dans la feuille « Les lieux du jour », une carte « Pierres trouvées » n'apparaît qu'après la première pierre et ne montre que celles trouvées : **surprise complète**, aucun emplacement vide, aucune allusion au ciel.
- **Le passage** : à la quatrième pierre, une animation unique (les pierres montent, un anneau s'ouvre sur le ciel, « Te reva »). On touche pour entrer. Ensuite Te reva est un lieu comme les autres (bouton Lieux, feuille des lieux).
- **Te reva, le décor** : au-dessus des nuages, l'île et son lagon vus d'en haut. Il grandit aussi : un ānuanua (arc-en-ciel) quand les 5 nuages sont reconnus, un pāuma (cerf-volant) quand les 4 vents sont connus.
- **Les nuages** : 3 par séance parmi 5 (cumulus, cumulonimbus, cirrus, stratus, nuage de la montagne). Une question « qu'annonce-t-il ? », l'explication, puis le lien avec ce qu'on ressent (« un nuage noir n'est pas tout le ciel »).
- **Les vents** : une rose des vents avec l'île au centre (maraʻamu, toʻerau, maoaʻe, hupe), puis « quel vent souffle en moi aujourd'hui ? » avec un conseil simple. Aucun vent n'est « mauvais ».
- Récompenses : 1 plume par jour dans Te reva ; +5 plumes une seule fois pour les nuages, +5 pour les vents.

## Pour essayer sans attendre des semaines
Ouvrir l'appli avec `?ciel=1` à la fin de l'adresse : les quatre pierres sont données et le passage s'ouvre. (À retirer ou garder secret avant publication, au choix.)

## Clés
`stones`, `portal`, `reva` ({clouds, winds}), `skyC`, `skyW`, `revaDay`.

## À valider — important
- **Noms tahitiens** : `Te reva` pour ce monde, `maraʻamu` (sud-est), `toʻerau` (nord), `maoaʻe` (est), `hupe` (brise de montagne la nuit), `ānuanua`, `pāuma`. Je n'ai trouvé en ligne qu'une source ancienne et incomplète pour les directions des vents ; elles reposent sur l'usage courant et **doivent être confirmées par un locuteur** (les directions varient selon les îles et les familles). L'écran des vents affiche d'ailleurs « en cours de vérification ».
- **Météo** : explications volontairement simples ; à relire par un enseignant ou Météo-France Polynésie si possible.
- **Psychologue** : les phrases qui relient nuages/vents aux émotions.

## Testé
`node test_sky.js <fichier>` : pierres, carte, passage, décor, 2 tours de nuages, vents, récompenses, rechargement. Navigateur sans écran uniquement.

README : > **Un secret** — quelque chose attend ceux qui font grandir les quatre décors. (Ne pas en dire plus dans le README public.)
