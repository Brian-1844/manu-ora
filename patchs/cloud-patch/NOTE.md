# Le petit nuage — à intégrer dans la session en cours (v91 ou plus)

Cette fonction a été écrite dans l'ancienne session, sur la version 83. Elle n'est PAS dans la version 91.
Ne pas utiliser les fichiers manu-ora-site-v84.zip ni manu-ora-handover-v84.zip : ils sont plus anciens que la v91.

## Pour l'intégrer
1. `python3 cloud_patch.py /home/claude/manu-ora-site/index.html /home/claude/manu-ora.html`
   (vérifié : s'applique proprement sur l'aperçu v91, syntaxe correcte, le nuage apparaît et se touche).
2. Monter `APP_V` et le cache de `sw.js`, `node --check`, tester, zipper, publier.
3. Ajouter au README la section ci-dessous.

## Ce que fait le patch
- Un petit nuage clair au-dessus du manu, environ 70 secondes, après qu'une émotion difficile est nommée sur la ronde. Il s'efface seul.
- Jamais pour le point « idées noires », jamais partagé, ne grossit pas.
- Touché : « Il passera tout seul, et je reste dessous avec toi » + respirer / parler à quelqu'un / laisse-le / ne plus montrer de nuage.
- Respiration ou surf terminés pendant qu'il est là : un rayon de soleil le remplace quelques secondes.
- Case à cocher dans « Mon manu » (carte de croissance) pour le remettre ou l'enlever.
- Correctif inclus : la bulle de parole invisible ne bloque plus les touchers (`.bubble` en `pointer-events:none` sauf `.show`). Sans lui, le nuage ne peut pas être touché.

## Section README

## Le petit nuage (version NN)

Quand l'utilisateur nomme une émotion difficile sur la ronde, un petit nuage clair apparaît au-dessus du manu pendant environ une minute, puis s'efface tout seul. Il n'apparaît jamais sans que l'utilisateur ait nommé l'émotion, jamais pour le point « idées noires » (qui mène directement à l'aide), il ne grossit pas, ne dure pas, et les cœurs liés ne le voient pas.

Si on le touche, le manu dit : « Il passera tout seul, et je reste dessous avec toi », avec quatre choix : respirer, parler à quelqu'un, « laisse-le, ça va », ou « ne plus montrer de nuage » (réglage conservé). Si l'on termine une respiration ou un surf pendant qu'il est là, un rayon de soleil le remplace quelques secondes.

Pourquoi si court : nommer une émotion aide à la calmer, et la voir « à côté de soi » aide les adolescents à prendre du recul ; mais garder son humeur sous les yeux trop longtemps peut nourrir la rumination. À faire relire par un·e psychologue.

