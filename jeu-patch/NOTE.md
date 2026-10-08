# Patch — Les jeux de la cour (école) : basket, tirs au but, ping-pong

Remplace `manu-ora-basket-patch.zip` (ne pas appliquer les deux). Base : v91 ou plus récent.

## Appliquer
    python3 jeu_patch.py <site>/index.html <manu-ora.html>
Chaque remplacement est vérifié (`assert count==1`) : si une ancre a changé, le script s'arrête sans rien écrire. Puis `node --check` sur le JS extrait, monter le numéro de version et le cache du service worker.

## Ce que ça ajoute
Bouton « Jouer dans la cour : basket, foot, ping-pong » dans la feuille du lieu **école** (`curPlace==='haapii'`) → choix de 3 jeux, 5 essais chacun.

| Jeu | Mécanique | Ce que le jeu apprend |
|---|---|---|
| Panier de basket | jauge qui va et vient, tirer au milieu | un tir raté ne dit rien du suivant |
| Tirs au but | le tupa garde le but et change de place ; tirer là où il n'est pas (poteaux aux extrémités) | regarder avant d'agir |
| Ping-pong | le manu envoie la balle, la renvoyer après le rebond (ni trop tôt, ni trop tard) ; chaque balle va un peu plus vite | répondre au bon moment |

- 1 plume par jour au maximum, tous jeux confondus ; la journée compte dans `placeDays.haapii`.
- **À deux, en équipe, sans classement** : après la partie, envoi du score à un cœur lié (`g:'jeu'`, `p:'b3'|'f3'|'p3'`). L'ami joue le même jeu quand il veut ; la réponse (`g:'jeuOk'`, `p:'f3:4'`) additionne : « À vous deux : 7 sur 10 ». Bouton « Lui dire bien joué » (`g:'bravo'`).
- Pas de match, pas de gagnant, pas de tableau. Le ping-pong n'est pas un échange en direct entre deux téléphones (les liens ne le permettent pas) : chacun joue ses 5 balles avec son manu.
- Mouvement réduit (`RM`) : les ballons ne volent pas (basket, foot). Au ping-pong la balle bouge quand même, c'est le jeu lui-même.

## Clés
`bkDay`, `bkOut` (invitations en attente, par code), `placeDays`. Règles Firebase inchangées (`g`, `p` ≤ 12 caractères).

## Testé
`node test_jeux.js b|f|p` : deux utilisateurs simulés, navigateur sans écran, base simulée, pour les trois jeux. Jamais testé sur un vrai téléphone (le ressenti du rythme au doigt est à régler là) ni sur le vrai Firebase.

## README (à ajouter)
> **Les jeux de la cour** — à l'école : panier de basket, tirs au but, ping-pong. Cinq essais, seul ou avec un cœur lié. À deux, les scores s'additionnent : ce n'est pas un match, c'est une équipe.
