# Patch — La route (ville) et Te pō, la soirée

Dépend de `dock-patch`.

## La route (en ville)
- Bouton « La route : le code, à vélo ou en scooter » dans la feuille de la ville, et icône dans la colonne.
- On choisit vélo ou scooter (« à partir de 14 ans, avec le BSR »), puis 5 situations tirées parmi 13 : feu orange, STOP, piéton engagé, casque attaché, passager en trop (scooter) ou sur le porte-bagages (vélo), téléphone, camion qui tourne (angle mort), rond-point, nuit sans lumière (vélo), pluie, écouteurs.
- 9 secondes pour choisir (barre qui diminue) ; si on hésite trop : « dans le doute, on ralentit et on s'arrête ».
- Après le choix : le véhicule repart, s'arrête à la ligne, ou un « ! » montre le quasi-accident (jamais d'image d'accident). Une phrase explique la règle.
- **Volontairement : uniquement des réflexes de sécurité, aucun montant d'amende, aucun chiffre légal.** L'écran d'accueil le dit : « pour les règles exactes, c'est le code de la route de la Polynésie et ton auto-école qui font foi ».

## Te pō, la soirée (nouveau lieu)
- Toujours disponible dans « Lieux » ; décor de nuit (guirlande, enceintes, piste).
- « Garder l'œil » : 5 situations, dont 4 tirées parmi : verre tendu par un inconnu, verre laissé sur la table, cachet proposé, amie qui titube après un seul verre, inconnu qui veut la raccompagner ; et toujours « on s'organise avant : quelqu'un reste clair, on rentre ensemble ».
- Fin : trois réflexes (verre vu servir ou fermé ; verre laissé = laissé ; on arrive et on repart ensemble), « demander de l'aide n'est pas une honte », et un bouton qui ouvre l'Aide de l'appli. **Aucun numéro ajouté** : on renvoie à l'Aide existante (numéros encore à vérifier).
- Aucune substance nommée, aucune image de drogue ou de malaise grave.

## Clés et activités
Activités `route` et `soiree` (plume via `award`, comme les autres lieux). Lieu `po`.

## À valider
- **DTT ou auto-école** : les 13 situations et leurs phrases (le code de la route de Polynésie diffère du code national, par ex. sur le BSR) ; le rond-point en particulier.
- **Prévention (addictions / soumission chimique)** : les situations de la soirée et leurs réponses, reprises des conseils des forces de l'ordre (police.be, Gendarmerie).
- Locuteur : « Te pō » pour la soirée.

## Testé
`node test_route.js [fichier]` : vélo et scooter, bonnes et mauvaises réponses, hésitation trop longue ; soirée complète, ouverture de l'Aide. Navigateur sans écran, jamais un vrai téléphone.
