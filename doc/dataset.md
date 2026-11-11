# Dokumentácia datasetu

## 1. Charakteristika datasetu

Pre praktickú časť projektu bol vytvorený vlastný obrazový dataset určený na rozlišovanie medzi virtuálnymi influencermi generovanými pomocou umelej inteligencie a ľudskými tvorcami obsahu.

Dataset obsahuje celkovo 30 fotografií rozdelených do dvoch tried:

- AI – fotografie virtuálnych influencerov.
- Human – fotografie ľudských influencerov.

Každá trieda obsahuje 15 fotografií.

## 2. Zloženie datasetu

Dataset obsahuje fotografie šiestich influencerov.

### Virtuálni influenceri (AI)

- Lil Miquela – 5 fotografií.
- Imma – 5 fotografií.
- Shudu – 5 fotografií.

### Ľudskí influenceri (Human)

- Caroline Daur – 5 fotografií.
- Nora Kakos – 5 fotografií.
- Ivana Gáborík – 5 fotografií.

## 3. Technické vlastnosti obrázkov

Obrázky sú uložené vo formáte JPEG.

Pri príprave datasetu bola vykonaná kontrola:

- čitateľnosti obrázkov,
- poškodených súborov,
- presných duplicít,
- rozmerov obrázkov,
- farebného režimu.

Obrázky sú vo farebnom režime RGB.

Pred vstupom do modelu ResNet-18 sa upravujú podľa predvolených transformácií predtrénovaných váh modelu vrátane zmeny rozmerov a normalizácie.

## 4. Rozdelenie datasetu

Dataset bol rozdelený podľa identity influencerov, nie náhodným rozdelením jednotlivých fotografií.

### Tréningová množina (Train)

- AI: Lil Miquela a Imma – 8 fotografií.
- Human: Caroline Daur a Nora Kakos – 8 fotografií.

Spolu: 16 fotografií.

### Validačná množina (Validation)

- AI: Lil Miquela a Imma – 2 fotografie.
- Human: Caroline Daur a Nora Kakos – 2 fotografie.

Spolu: 4 fotografie.

### Testovacia množina (Test)

- AI: Shudu – 5 fotografií.
- Human: Ivana Gáborík – 5 fotografií.

Spolu: 10 fotografií.

Testovacia množina obsahuje fotografie influencerov, ktorí sa nenachádzali v tréningovej ani validačnej množine.

## 5. Preprocessing

Pred spracovaním modelom ResNet-18 sa obrázky upravujú pomocou transformácií definovaných v predtrénovaných váhach modelu.

Výsledkom je obrazový tenzor s rozmermi:

- 3 farebné kanály (RGB),
- výška 224 pixelov,
- šírka 224 pixelov.

## 6. Obmedzenia datasetu

Dataset obsahuje iba 30 fotografií a šesť influencerov.

Takýto rozsah predstavuje významné obmedzenie pri trénovaní a vyhodnocovaní modelu.

Testovacia množina obsahuje iba jedného nevideného influencera z každej triedy. Výsledky preto nemožno považovať za dostatočný dôkaz všeobecnej schopnosti modelu rozlišovať AI-generovaných a ľudských tvorcov.

Pri ďalšej realizácii projektu bude potrebné zvážiť rozšírenie datasetu.

## 7. Evidencia zdrojov

Názvy obrázkov, mená influencerov a odkazy na pôvodné príspevky sú zaznamenané v súbore:

`prehľad_datasetov_s_evidenciou.xlsx`

Zdrojové odkazy a podmienky použitia obrázkov je potrebné overiť pred ich ďalším použitím alebo zverejnením.
