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
9. `heiva-patch/` — le pāuma (cerf-volant) sur la plage et Te Heiva (feu, danse, bar à jus, cœurs liés autour du feu). Dépend de `jeu-patch` et `dock-patch`.
10. `route-patch/` — la route (code de la route, vélo ou scooter) en ville, et Te pō, la soirée (garder l'œil sur son verre et sur ses amis). Dépend de `dock-patch`.
11. `recomp-patch/` — les récompenses des nouvelles activités (foulard, ballon, raquette, pāuma de fara, casque, hei de nuit, pāreu du Heiva, recette du jus). Dépend de `jeu-patch`, `heiva-patch`, `route-patch`.
12. `instr-patch/` — l'atelier des instruments (la musique du faʻaʻapu : une fois par jour, un seul instrument) (ʻukulele, tōʻere, pahu) fabriqués avec le bois et les cocos du faʻaʻapu, décorés, qui font pousser fleurs, arbres ou fruits.
13. `vivo-patch/` — le vivo, flûte nasale cachée : une seconde chance dans les jeux, ou le ʻūʻupa (pigeon vert) pour la journée, à garder ou à offrir.
14. `vaa-patch/` — le vaʻa : jeu de rythme à la plage, coup léger / coup fort, trois niveaux. Dépend de `jeu-patch` et `dock-patch`.
15. `porter-patch/` — le manu porte l'instrument choisi sur le dos (avec sa finition), en cordelette tressée ou dans un étui en fara (2 fara, une fois). Dépend de `instr-patch`.
5. `bee-patch/` — l'abeille ne suit le manu que quand le miel est prêt à récolter.
4. `dock-patch/` — bouton « Lieux » et icônes d'activités à l'écran ; écran de bienvenue avec Commencer / Installer.

## Vérifié
Les quinze patchs appliqués ensemble sur la copie v91 : syntaxe correcte, tests `dock-patch/test_dock.js` et `jeu-patch/test_jeux.js` réussis sur la version combinée. Navigateur sans écran et base simulée uniquement : jamais sur un vrai téléphone ni le vrai Firebase.

