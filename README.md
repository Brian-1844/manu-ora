# Manu Ora

Ton manu, tes émotions. Un compagnon-oiseau polynésien qui se promène sur l'écran, demande comment tu vas, et propose de petites actions pour prendre soin de soi : respirer avec la vague, appeler son ama, trois māuruuru, démêler le upe'a. Les émotions se nomment en reo tahiti et en français, et se situent dans le tino (le corps).

**Prototype** : ce n'est pas un soin médical. En cas d'idées noires, l'appli renvoie vers SOS Suicide Polynésie, le 3114 et le 15.

## Lancer le site

Tout tient dans `index.html` (pas de serveur, pas de compte). Les données restent dans le téléphone (localStorage).

- En ligne : https://brian-1844.github.io/manu-ora/
- Sur téléphone : ouvrir le lien, puis « Ajouter à l'écran d'accueil ». L'appli fonctionne ensuite hors ligne (service worker).

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | l'application complète (HTML, CSS, JS) |
| `manifest.webmanifest` | installation sur l'écran d'accueil |
| `sw.js` | cache hors ligne |
| `icon.svg` | icône |

## À faire avant de la donner à de vrais utilisateurs

1. Faire valider le vocabulaire tahitien et les libellés « Reo » par des locuteurs (Fare Vāna'a).
2. Vérifier par téléphone les numéros d'aide (SOS Suicide Polynésie, 3114 depuis le fenua) et les mettre à jour chaque année.
3. Faire relire le mode « idées noires » par un·e psychologue.
4. Co-concevoir avec des jeunes et des matahiapo (anciens) : histoires, motifs, parures.

## Idées pour la suite

- Versions pa'umotu, marquisienne, australe.
- Petites histoires à choix ('a'amu) pour apprendre à reconnaître les émotions chez les autres.
- Mode école / groupe de jeunes, en lien avec le label « École en santé ».
