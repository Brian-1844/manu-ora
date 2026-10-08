# Patch — Le moʻo (troisième animal), la tortue qui grandit, un trait par animal

## Ce que ça ajoute
- **Moʻo (lézard)** dans « Mon manu » → Animal. Il ne s'achète pas : il vient après **5 jours différents de calme** (respirer avec la vague, surf calme, caresser un animal : tout ce qui écrit déjà `calmDay`). Le bouton verrouillé montre « n / 5 jours de calme ». Volontairement pas lié à la nuit, pour ne pas pousser à ouvrir l'appli tard.
- **Croissance** (mêmes 6 étapes pour les trois, aucun n'est « meilleur ») :
  - Manu : inchangé (crête, queue, ailes).
  - Honu : avant, elle grossissait seulement. Maintenant la carapace gagne un bord festonné (2), une écaille centrale (3), des écailles de coin (4), des taches claires (5), un liseré doré (6).
  - Moʻo : la queue s'allonge ; taches sur le dos (3-4), rayures sur la queue (5), points dorés (6).
- **Un trait par animal** (texte sous le choix de l'animal) :
  - Manu, le messager : rien de nouveau, c'est lui qui porte les signes.
  - Honu, la patience : après un exercice de souffle terminé, la carapace brille doucement jusqu'au soir (n'écrase pas un éclat déjà en cours).
  - Moʻo, ce qui repousse : après une émotion difficile, une seule fois par jour et environ 45 s plus tard, il dit : « Tu sais, quand je perds ma queue, elle repousse. Ça prend du temps, c'est tout. » Jamais sur le chemin « sombre » (`__dark`). **Aucune queue perdue à l'écran** : seulement des mots.
- Les accessoires (chapeau, fleur, hei, colliers, lunettes, tatouages, pāreu, nuit) se posent sur le moʻo.
- Les amis voient le moʻo si leur version a ce patch ; sinon ils voient un manu.

## Clés
`calmDays` (jours de calme, 40 max), `mooSaid` (jour de la dernière phrase), `owned` reçoit `an:moo`.

## À valider
- **Conseiller culturel** : le moʻo a un sens fort pour certaines familles (gardien, parfois craint). Il est présenté ici seulement comme le petit lézard de la maison.
- **Psychologue** : la phrase « elle repousse » après une émotion difficile.

## Testé
`node test_moo.js <fichier>` : déblocage au 5e jour, trait de la tortue, planche de dessin des 3 animaux × 6 étapes. Navigateur sans écran uniquement.

README : > **Trois animaux** — le manu, la honu et le moʻo grandissent au même rythme ; chacun a son trait : le messager, la patience, ce qui repousse.
