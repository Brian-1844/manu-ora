# Manu Ora — tous les nouveaux patchs en un seul zip (base v91 ou plus)

Ce zip remplace tous les zips envoyés séparément (nuage, décors-anguilles, basket / jeux de la cour, lieux-bienvenue). Ne pas appliquer deux fois.

## Appliquer
    python3 apply_all.py <site>/index.html <manu-ora.html>
Le script travaille sur une copie : si une ancre a changé depuis v91, il s'arrête et laisse le fichier intact, en nommant le patch en cause. Ensuite : `node --check` sur le JS extrait, monter le numéro de version, le cache du service worker, et ajouter les lignes README de chaque NOTE.md.

## Contenu (lire le NOTE.md de chaque dossier)
1. `cloud-patch/` — petit nuage court après une émotion difficile + correctif de la bulle qui bloquait les appuis.
2. `scene-patch/` — anguilles redessinées ; décors qui évoluent (plage, rivière, ville, école) ; Vespa, truck, petite voiture en ville.
3. `jeu-patch/` — jeux de la cour à l'école : basket, tirs au but, ping-pong, seul ou à deux en équipe.
6. `moo-patch/` — le moʻo, troisième animal (5 jours de calme) ; la tortue grandit ; un trait par animal.
7. `sky-patch/` — les quatre pierres, le passage et Te reva, le monde du ciel (nuages, vents). Dépend de `scene-patch`.
8. `voyage-patch/` — suite de Te reva : l'île vue d'en haut, le fare (avec l'aide d'un cœur lié), le grand vol (rétrospective, constellation). Dépend de `sky-patch`.
5. `bee-patch/` — l'abeille ne suit le manu que quand le miel est prêt à récolter.
4. `dock-patch/` — bouton « Lieux » et icônes d'activités à l'écran ; écran de bienvenue avec Commencer / Installer.

## Vérifié
Les huit patchs appliqués ensemble sur la copie v91 : syntaxe correcte, tests `dock-patch/test_dock.js` et `jeu-patch/test_jeux.js` réussis sur la version combinée. Navigateur sans écran et base simulée uniquement : jamais sur un vrai téléphone ni le vrai Firebase.

