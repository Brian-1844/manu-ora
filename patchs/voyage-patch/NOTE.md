# Patch — Te reva, suite et fin : l'île vue d'en haut, le fare, le grand vol

Dépend de `sky-patch` (le script refuse de s'appliquer sans lui).

## 1. L'île vue d'en haut (après les nuages et les vents)
Carte de l'île avec 8 noms à toucher : mouʻa, faʻa, tahatai, tairoto, aʻau, ava, motu, moana. Chacun a une phrase de géographie et une phrase « pour le cœur » (le récif = les limites, la passe = garder une ouverture, l'océan = le vrai monde). Les 8 connus : une pirogue sur le lagon du décor, +5 plumes, et le fare devient possible.

## 2. Le fare (après l'île)
4 étapes, **une par jour**, payées avec les récoltes du faʻaʻapu : poteaux (2 ʻuru, le repas du chantier), charpente (2 cocos, la corde), toit (3 fara), natte et accueil (1 fara + 1 tiare). Chaque étape a une phrase (les bases, les liens, le toit qui laisse au sec, le lieu sûr).
**Coup de main d'un cœur lié** : « Demander un coup de main » envoie `g:'fareAsk'`. L'ami reçoit « X bâtit quelque chose et aurait besoin de bras » (sans rien révéler du ciel) ; s'il accepte (`g:'fareAid'`), l'étape suivante est offerte et son prénom reste inscrit : « Bâti avec Hina ». Un ami dont la version n'a pas ce patch ne comprendra pas la demande.
Fare fini : +10 plumes, un petit fare sur l'île du décor.

## 3. Le grand vol (quand tout Te reva est complet : nuages, vents, île, fare)
Décisions de Brian appliquées :
- **Jamais automatique.** Le manu propose (« J'ai quelque chose à te proposer. Rien ne presse. ») au plus une fois par semaine ; « Pas encore » est possible à chaque écran, rien n'est perdu. L'entrée reste aussi dans le menu de Te reva.
- **Il attend si ça ne va pas** : aucune proposition si 3 jours différents avec une émotion difficile dans les 7 derniers jours.
- **Rétrospective d'abord** (uniquement avec ce qui est sur le téléphone) : nombre de jours et bande de couleurs, émotions nommées, trois coquillages au hasard, plantes, pierres, cœurs liés, fare, le manu au début / en chemin / aujourd'hui.
- **La constellation** : animation, puis « Te fetiʻa o <nom> » visible chaque nuit dans le ciel de l'utilisateur. **Dans le ciel des cœurs liés seulement avec consentement** (case décochée par défaut, modifiable ensuite dans « Les étoiles de … » ; le retrait est immédiat).
- **Le manu peut revenir** : bouton « Appeler <nom> » à l'écran ; il redescend aussitôt. On peut le laisser remonter ou le rappeler autant qu'on veut. Tout le reste de l'appli reste ouvert.
- Après le grand vol, la question automatique du matin (`askRing(true)`) n'apparaît plus : c'est l'utilisateur qui vient. Les autres messages spontanés du manu (coucher, etc.) ne sont **pas** coupés.
- Dernier écran, « L'aventure du vrai monde » : trois invitations concrètes (quelqu'un, un lieu, un geste) et le rappel du bouton Aide.

## Clés
`skyI`, `fare` ({n, day, help, gift}), `fareOut`, `cst` ({done, share, up, day}), `cstAsk`. Le regard publié (`cfg`) reçoit `star:true` si consentement (booléen, accepté par les règles Firebase actuelles).

## À valider — le plus sensible de toute l'appli
- **Psychologue, avant toute publication** : le grand vol (risque de lecture « mon manu est mort / m'a quitté »), ses textes, le seuil d'attente (3 jours difficiles sur 7), l'arrêt de la question du matin.
- **Locuteur de reo tahiti** : `Te fetiʻa o …`, `te pou`, `te tahuhu`, `te tāpoʻi`, `te peʻue`, les 8 noms de l'île.
- **Conseiller culturel** : la construction du fare (matériaux, étapes), les étoiles qui « guident ».

## Limites connues
- Pendant que le manu est dans ses étoiles, il n'est plus à l'écran : on ne peut plus le toucher deux fois pour dire comment on se sent tant qu'on ne l'a pas rappelé. Le texte d'aide en bas de l'écran le dit encore.
- Au plus 3 constellations d'amis affichées.

## Testé
`node test_voyage.js <fichier avec SYNC_URL factice>` : deux utilisateurs simulés, de l'île jusqu'au ciel de l'ami. Navigateur sans écran, base simulée ; jamais sur un vrai téléphone ni le vrai Firebase.
