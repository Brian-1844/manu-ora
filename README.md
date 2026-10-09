# Manu Tere

A voyaging bird that takes visitors around the islands of French Polynesia. It plays in English, French, Japanese or Chinese, with Reo Māʻohi words throughout, and is a sister app to Manu Ora.

**Prototype, version 0.11.** Four islands (Tahiti, Moʻorea, Porapora / Bora Bora, Tahaʻa), a star-navigation voyage between them, fifteen activities, six legends, a faʻaʻapu with four crafts, a passport and a word list.

## Put it online (GitHub Pages)

1. On GitHub, create a new public repository named `manu-tere`.
2. Use **Add file › Upload files** to upload every file from this folder: `index.html`, `sw.js`, `manifest.webmanifest`, `icon.svg`, `icon-192.png`, `icon-512.png` and `README.md`. Then click **Commit**.
3. Open **Settings › Pages**. Under Source, choose **Deploy from a branch**, then branch `main`, folder `/ (root)`, and click **Save**.
4. After a minute or two the app is live at `https://brian-1844.github.io/manu-tere/`.

`sw.js` lets the installed app open without a connection. It always fetches the newest page first, so an update shows after a reload. When you publish a new version, change `VERSION` at the top of `sw.js`.

## What's inside

- **Languages:** English, Français, 日本語 and 中文 (simplified). The language is chosen on the welcome screen, and can be changed at any time with the globe button at the top. On first launch the app picks the phone's language if it is one of these four. Reo Māʻohi words always stay in Reo Māʻohi; their meanings are translated. The translations live in `19-i18n-data.js` (in the build, inside `index.html`); anything not yet translated shows in English.

- **Arrival:** after the welcome screen, a twin-engine long-haul jet (drawn after the Boeing 787-9 profile, with an original Manu Tere livery) approaches Faʻaʻā at sunset. It lowers its landing gear, flares, touches down with tyre smoke and rolls out past the control tower to the terminal. A Skip button jumps straight to Tahiti.

| Island | Activities |
|---|---|
| Tahiti | Te mātete (Papeete market, words for fruit), Faʻaheʻe (catch a wave at Teahupoʻo), ʻOri Tahiti (tap with the tōʻere), Faarumai (walk to the three waterfalls of Tiarei, then the legend of Faʻuai and Ivi), Arahoho (the blowhole: tap when a big wave hits) |
| Moʻorea | Te tairoto (lagoon friends, look but don't touch), Painapo (pick Queen pineapples at the turning stage), Te toʻa (clean a coral nursery, hang fragments, plant grown corals on the reef), Rotui (sort pineapples and fill juice bottles at the factory below Mount Rotui) |
| Porapora | Hoe vaʻa (outrigger race around Otemanu), Fāfā piti (approach a manta gently), Te mau fetiʻa (stars over Matira) |
| Tahaʻa | Vānira (hand-pollinate vanilla flowers before they close), Te vānira (dry the pods in the sun a few hours a day, then massage them; gives cured vanilla pods), Ahimāʻa (build an earth oven with a family on a motu: fire, hot stones, banana leaves, parcels, leaves, wet sacks, sand, wait, open) |

- **Tahiti scene, alive:** an animated waterfall in the Faarumai mountains (falling water, ripples in the pool, rising mist, ferns), and a coast road where *le truck* (pereʻoʻo mataʻeinaʻa) drives past with passengers, music and market goods on the roof. Tap the truck to stop it and read its story: wooden cabin, side benches, no fixed stops (raise your arm), a bell to get off, its replacement by buses, and the Tere Faʻaʻati truck tour each January. You can ring the bell, and the bird learns two words.
- **Papeete and Lake Vaihiria:** the Tahiti scene shows the cathedral (yellow façade, red steeple, maroon arched windows) beside the two-storey market hall, and a small lake in the mountains. Tap the round “i” markers for the cathedral and Lake Vaihiria. The legend of Hina and the eel is now set at Lake Vaihiria, with a marbled freshwater eel.
- **Voyages:** the bird sails a *pahi*, a double canoe with a crab-claw sail woven from pandanus, a deck platform with a small shelter, and a steering paddle. The day crossing to Moʻorea follows the sun.
  - **Star path:** on night voyages, a guide star is used while it is low, then the navigator picks the next star rising or setting at the same point of the horizon. Westward, Matariʻi is followed by Pīpiri mā; eastward, ʻAna-mua is followed by Te Matau a Māui. Pick the wrong star and the bird warns that you would miss the island. This is simplified: in reality these stars are not all low on the same night.
  - **Signs of land:** on long crossings, while the island is still out of sight, three signs appear: a cloud that stays piled up over the hidden island, noddy terns flying home at dawn (rarely more than about 65 km from land), and the green glow of a lagoon reflected under the clouds.
- **Market fruit:** redrawn with shading and detail: a banana bunch, a mango, an ʻuru, a coconut, a fish and a tiare.
- **Rewards:** finishing all the activities on an island unlocks an item for the bird: a hei (Tahiti), a pāreu (Moʻorea), sunglasses (Porapora), a vanilla flower (Tahaʻa).
- **Faʻaʻapu (garden):** six plots, with plants ready in a few minutes so a visitor can harvest during a stay. The real moon speeds up growth while it is waxing. The real season does too: Matariʻi i niʻa, the season of abundance from 20 November, gives more fruit, and the fruit in season each month (ʻuru, mango, pineapple, tiare) grows twice as fast. Food can be "tasted" for a tip on where to try it. Shells wash up on the beaches, and a pearl line in the lagoon opens after Porapora.
- **Kitchen (in the faʻaʻapu, after the Tahaʻa oven):** cook your harvest in your own ahimāʻa: ʻuru, taro with coconut milk, fēʻī, and poʻe vānira (plantain poʻe scented with Tahaʻa vanilla). Ingredients are used only when the oven is opened. Serve the dishes to your manu for a fact about each. Fēʻī and taro can now be planted.
- **Crafts:** a sun-printed pāreu (cotton and a plant dye), a woven tāupoʻo (pandanus, over-and-under weaving), a hei poe (pearls and shells) and a tapa (beat ʻuru bark with the ʻiʻe, then print motifs). The bird wears what you make, and every craft says where to see the real thing.
- **Te raʻi (the star button at the top):** the night sky of the fenua, as in Manu Ora. Tap a star to learn its Reo name and story, play "find the star", and see tonight's moon with its Tahitian night name. Learning all 11 gives the bird a cloak of stars.
- **Surf:** a banded, illustrated wave with a curling lip, a tube, crest foam and whitewash. Catch the swell at the right moment, then ride the pocket by pumping, without getting too close to the lip or too far out on the shoulder.
- **ʻĀʻai (legends):** Hina and the eel (Tahiti), Pai and the pierced mountain (Moʻorea), ʻOro and the rainbow (Porapora), and two garden legends: Ruataʻata and the ʻuru, and Hina in the moon. Each legend gives seeds or materials.
- **Keeping your voyage:** progress is saved on the phone only (localStorage); there are no accounts and nothing is sent anywhere. The welcome screen and **My manu › Save and restore** offer:
  - **Install on my phone:** a real install button on Android and desktop Chrome; on iPhone, instructions for Share › Add to Home Screen.
  - **Backup code:** copy a code (or save it as a file) and paste it back on any phone to restore everything. A reminder appears once a day after real progress if no backup was made in three days.
  - The app also asks the browser to keep its storage (`navigator.storage.persist`).
- **Chemise (island shirt):** dye the cotton, choose two motifs (tiare, ʻaute, ʻuru leaf, ʻautī leaf, fern, honu, niho, waves), a print colour and size, then sew it. Flower motifs use a flower from the basket. The bird wears the shirt.

## Before a public launch

- Have the French, Japanese and Chinese texts reviewed by native speakers, especially the legends and the pronunciation guides (Japanese uses katakana; Chinese keeps the Latin guide).

- Have native speakers check every Reo word, the pronunciation hints and the short phrases. The words are kept together in the `W` list at the top of the script.
- Add recordings by native speakers if you want sound for the words. The computer voice has been removed, so for now the words are written only, with a pronunciation guide.
- Check the travel information (ferry and flight times) with the operators, and add partner links (for example Tahiti Tourisme) if a partnership happens.
- Show sacred places such as Taputapuātea, which is planned for Raiatea, with the guardians' agreement.
- The Arahoho blowhole has been closed at times for cliff safety work: check its status with the Service du Tourisme before promoting a visit.
- Have the legends checked by a storyteller or the Maison de la Culture. Each legend exists in several versions, and the app says which version it follows.
