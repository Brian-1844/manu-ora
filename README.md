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

## Faʻaʻapu (le jardin)

Six emplacements. On plante une graine, elle pousse avec le temps réel (appli ouverte ou non), puis on récolte. Rien ne meurt : un fruit mûr attend.

| Plante | Mûre en | Vaut |
|---|---|---|
| tiare | 1 jour | 5 plumes |
| ʻaute | 2 jours | 8 plumes |
| meiʻa (banane) | 3 jours | 12 plumes |
| vī (mangue) | 5 jours | 20 plumes |
| ʻuru | 7 jours | 30 plumes |

- **Graines :** 2 tiare et 1 ʻaute au départ ; une graine à chaque journée complète ; une graine reçue avec chaque fruit offert par un ami.
- **Récolte :** « Échanger » contre des plumes, ou « Offrir » à un ami lié. L'ami reçoit les plumes et une graine ; celui qui offre récupère une graine.
- Le jardin est enregistré sur le téléphone ; seuls les cadeaux passent par Firebase.

### Coffre et atelier

À la récolte, « Mettre au coffre » range la fleur ou le fruit. Le coffre s'ouvre depuis le bouton à côté des plumes. Dans l'atelier, on choisit les quantités de chaque ingrédient et on mélange : le dosage décide du résultat. Un mélange inconnu ne fait rien perdre.

| Création | Recette | Temps | Vaut | Aura (1 jour) |
|---|---|---|---|---|
| Hei tiare | 5 tiare | tout de suite | 30 | turquoise · la paix |
| Hei ʻārearea | 3 tiare + 2 ʻaute | tout de suite | 35 | rose · la tendresse |
| Salade de fruits | 1 meiʻa + 1 vī + 1 coco | tout de suite | 50 | orange · la joie |
| Poʻe meiʻa | 2 meiʻa + 1 coco | tout de suite | 40 | jaune · la gratitude |
| Monoï tiare | 3 tiare + 1 coco | 3 jours | 40 | dorée · le soin de soi |
| Monoï ʻaute (secrète) | 2 tiare + 1 ʻaute + 1 coco | 3 jours | 55 | rouge · le courage |
| Monoï ānuanua (secrète) | 3 tiare + 1 ʻaute + 1 vī + 1 coco | 4 jours | 90 | arc-en-ciel · l'espoir |

Les recettes secrètes apparaissent comme « ??? » avec un indice dans le carnet, jusqu'à ce qu'on les trouve. Chaque création peut être utilisée (aura sur son manu ; les monoï ouvrent en plus « Un moment pour toi »), offerte à un ami lié (l'aura va à son manu) ou échangée contre des plumes. Le haʻari (cocotier) mûrit en 4 jours ; une graine au départ, puis une tous les 7 jours.

### Étoile de confiance

Quand quelqu'un choisit un ami comme personne de confiance, son manu lui porte une étoile qui brille en haut de l'écran de veille. En la touchant, l'ami lit ce que cela veut dire et peut la garder ou la rendre. S'il la rend, la personne est prévenue et peut choisir quelqu'un d'autre.

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

**Accord et coupure du lien.** Entrer le code d'un ami envoie une *demande*. L'ami la voit dans « Cœurs liés » et choisit Accepter ou Refuser. Tant qu'il n'a pas accepté, personne ne voit le cœur de l'autre. Chacun peut « Couper le lien » à tout moment ; la personne coupée ne peut plus envoyer de demande, sauf si on entre soi-même son code. En cas d'abus, « Changer mon code » rend l'ancien code inutilisable. Limite : ces protections sont appliquées par l'application ; la base de test reste lisible par quelqu'un qui connaît un code et sait interroger Firebase directement.

**Prévenir une personne de confiance.** Dans « Cœurs liés », on peut désigner jusqu'à deux amis liés comme personnes de confiance. Sur l'écran d'aide (idées noires), un bouton propose alors « Oui, préviens … ». Rien n'est envoyé automatiquement : c'est toujours la personne qui appuie. L'ami voit arriver le manu avec « … a besoin de toi » et un écran de conseils (appeler, écouter, prévenir un adulte, le 15). Le message ne mentionne ni suicide ni dépression. Il n'est vu qu'à l'ouverture de Manu Ora : pour une urgence, il faut appeler. À faire relire par un·e psychologue avant diffusion.

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
