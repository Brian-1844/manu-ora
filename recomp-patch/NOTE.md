# Patch — Récompenses des nouvelles activités

Dépend de `jeu-patch`, `heiva-patch`, `route-patch`. Une récompense par vraie étape, une seule fois, jamais de pression : rien ne se perd si on s'arrête. Les objets vont au coffre (on peut les « utiliser » pour l'aura, les offrir, les échanger), comme les autres objets de l'appli. Ils ne sont pas dessinés sur le manu.

| Activité | Récompense | Quand |
|---|---|---|
| Tirs au but | Foulard du tupa (aura « le cran ») | 3 buts de suite, une fois |
| Basket | Ballon dédicacé (« la persévérance ») | 20 paniers au total |
| Ping-pong | Raquette de corail (« le bon moment ») | un échange réussi au 5e essai, la balle la plus rapide |
| Pāuma | graine de fara, puis Pāuma de fara (« tenir sans serrer ») | 3 jours, puis 7 jours de pāuma |
| La route | Casque du manu (« la prudence ») | 5/5 à vélo **et** 5/5 en scooter |
| Garder l'œil | Hei de nuit (« veiller sur les autres ») | avoir vu les 6 situations (pas « gagner ») |
| Heiva | graine de tipanie ; Pāreu du Heiva (« la fête partagée ») | premier feu ; premier ami venu danser (ou première fois chez un ami) |
| Heiva, bar | recette secrète « Jus du Heiva » (ananas + orange) dans le livre | après avoir goûté les 4 jus |

Clés : `rw` (récompenses déjà données), `bkBaskets`, `rt5`, `poSeen`, `hvJuices`.

Testé : `node test_recomp.js [fichier]`, chaque récompense déclenchée et une seule fois. Navigateur sans écran uniquement.
