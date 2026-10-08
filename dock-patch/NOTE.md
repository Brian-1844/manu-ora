# Patch — Lieux et activités à portée de doigt + écran de bienvenue

Base : v91 ou plus récent. Indépendant des autres patchs (nuage, décors, jeux de la cour) ; ordre d'application libre.

## Appliquer
    python3 dock_patch.py <site>/index.html <manu-ora.html>
Remplacements vérifiés (`assert count==1`). Puis `node --check`, numéro de version, cache du service worker.

## Ce que ça ajoute
1. **Bouton « Lieux »** en haut à gauche de l'écran calme (icône du lieu actuel). Un appui ouvre 5 icônes : Simple, Rivière, Plage, Ville, École. Un appui change le décor tout de suite, sans passer par le menu. La feuille « Les lieux du jour » du menu reste inchangée.
2. **Icônes d'activités** sous ce bouton, selon le lieu :
   - Rivière : Souci, Anguilles, Repas (cadenas tant que non découvert), Sentier (cadenas)
   - Plage : Coquillages, Surf, Dauphin (cadenas)
   - Ville : Dire non, Marché
   - École : Coup dur, La cour, Jeux (seulement si le patch « jeux de la cour » est appliqué)
   Une activité verrouillée affiche le même message d'explication qu'avant. Une icône n'apparaît que si la fonction existe (`typeof window[...]`), donc le patch ne casse rien si une activité manque.
3. Si le manu est posé dans un coin gauche (`cfg.corner` en `…l`), la colonne passe à droite.
4. **Écran de bienvenue** au tout premier lancement, avant « Voici ton manu » : « Bienvenue dans Manu Ora », bouton **Commencer**, et bouton **Installer l'appli** (seulement si l'appli n'est pas déjà installée). Si le navigateur propose l'installation, la fenêtre native s'ouvre ; sinon les étapes s'affichent sous le bouton (iPhone, Android, ordinateur).

## À savoir
- Clé `noDock` (true) masque la colonne ; aucun réglage visible n'est encore prévu pour ça.
- Les icônes sont des dessins simples faits pour ce patch ; à revoir si un graphiste intervient.

## Testé
`node test_dock.js` : navigateur sans écran (390×800), premier lancement, changement de lieu, ouverture de chaque activité. Jamais testé sur un vrai téléphone ; la fenêtre native d'installation ne peut pas être testée sans vrai appareil.

## README (à ajouter)
> **Lieux et activités en un geste** — un bouton à l'écran change le décor, et chaque lieu montre ses activités en petites icônes.
