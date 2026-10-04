# Manu Ora

Ton manu, tes émotions. Un compagnon-oiseau polynésien qui se promène sur l'écran, demande comment tu vas, et propose de petites actions pour prendre soin de soi : respirer avec la vague, appeler son ama, trois māuruuru, démêler le upe'a. Les émotions se nomment en reo tahiti et en français, et se situent dans le tino (le corps).

**Prototype** : ce n'est pas un soin médical. En cas d'idées noires, l'appli renvoie vers SOS Suicide Polynésie, le 3114 et le 15.

## Comment ça marche

**Mode veille (écran par défaut).** Le manu se repose dans un coin de l'écran (choix du coin dans « Mon manu »). En haut à gauche, un petit cœur se remplit des couleurs de la journée ; en haut à droite, « ≡ » ouvre tout Manu Ora (point complet, mots, personnalisation, aide).

- **Touche deux fois** le manu (ou l'écran) : une ronde de couleurs apparaît, une par émotion, en reo tahiti. Touche une couleur : elle s'ajoute au cœur. Le point noir « idées noires » ouvre directement l'aide.
- **Touche une fois** : petit menu (point complet, respirer, ukulele, mon cœur).
- **Caresse-le** lentement avec le doigt : il ferme les yeux et t'invite à respirer.
- **De temps en temps** (toutes les 2 h sans nouvelle, et 12 s après l'ouverture si rien n'a été noté depuis 2 h), le manu vole au centre de l'écran et demande « E aha tō 'oe huru ? ».
- **Le cœur** : touche-le pour voir la journée heure par heure, les 7 derniers jours, et les cœurs liés.

**Limite importante.** Une application web ne peut pas s'afficher *par-dessus* les autres applis du téléphone. Le manu vit donc dans Manu Ora, pas sur l'écran d'accueil ni sur WhatsApp. Pour cela, il faudrait une vraie application Android (permission « Afficher par-dessus d'autres applis ») ; iPhone ne le permet pas du tout.

## Plumes et boutique

Tout est enregistré sur le téléphone (pas de compte, pas d'e-mail, pas de mot de passe). Si la personne efface les données du navigateur ou change de téléphone, les plumes repartent de zéro.

| Pour gagner | Plumes |
|---|---|
| Journée complète : une couleur dans le cœur + une activité | 10 |
| Chaque activité (respirer, caresser, ukulele, point complet), 3 par jour au plus | 1 |
| Tous les 7 jours d'utilisation (au total, pas forcément d'affilée) | 20 de plus |
| Premier cœur lié avec un ami | 10 |

| Pour débloquer | Prix |
|---|---|
| Couleur de plumage (3 gratuites) | 10 |
| Tātau | 30 |
| Parure : hei, pāpale, 'aute, lunettes, pūpū, poe, pāreu (tiare gratuite) | 50 |
| Animation : 'ori, salto | 100 |
| Animal : honu | 150 |

Respirer, faire le point et l'aide ne sont jamais verrouillés.

**Veille.** Le manu dort dans son coin (yeux fermés, « z »). Un appui long permet de le prendre et de le poser n'importe où ; il réagit et garde cette place.

## Lier son cœur à un ami (optionnel)

Le partage des couleurs demande un tout petit serveur. Version gratuite avec Firebase :

1. Sur https://console.firebase.google.com, créer un projet (ex. `manu-ora`).
2. Menu « Realtime Database » → Créer une base → choisir une région → démarrer en **mode test**.
3. Copier l'URL de la base (elle ressemble à `https://manu-ora-default-rtdb.europe-west1.firebasedatabase.app`).
4. Dans `index.html`, chercher la ligne `const SYNC_URL = '';` et coller l'URL entre les guillemets. Envoyer le fichier sur GitHub.
5. Onglet « Règles » de la base, remplacer par :

```json
{ "rules": { "hearts": { "$code": { ".read": true, ".write": true, ".validate": "newData.hasChildren(['day','updated'])" } }, "visits": { "$to": { ".read": true, "$from": { ".write": true, ".validate": "newData.hasChildren(['g','t'])" } } } } }
```

**Rencontre des manu.** Quand deux personnes ont chacune entré le code de l'autre et coché « Partager », un bouton « Envoyer un signe » apparaît (salut, câlin, fleur de tiare, air de ukulele). Le manu de l'ami vient alors en visite sur l'écran de l'autre, avec son apparence et la couleur de son cœur du jour. Pas de messages écrits : uniquement ces gestes.

Ensuite, dans l'appli : cœur → « Cœurs liés » → cocher « Partager », donner son code à l'ami, et entrer le sien. Seules les couleurs du jour sont partagées (jamais les notes), sous un code aléatoire sans nom ni téléphone. C'est un prototype : pour une vraie mise en service, prévoir des règles d'accès plus strictes.

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
