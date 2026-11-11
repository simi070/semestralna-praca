# Dokumentácia fine-tuningu ResNet-18

## 1. Cieľ implementácie

Cieľom praktickej časti je upraviť predtrénovaný model ResNet-18 tak, aby dokázal klasifikovať obrázky do dvoch kategórií:

- AI – virtuálni influenceri generovaní umelou inteligenciou.
- Human – ľudskí influenceri.

## 2. Použitý postup

Pri implementácii bol použitý čiastočný fine-tuning predtrénovaného modelu ResNet-18.

Väčšina pôvodných vrstiev modelu zostala zmrazená. Trénovanie bolo povolené pre:

- posledný konvolučný blok `layer4`,
- klasifikačnú vrstvu `fc`.

## 3. Nastavenie tréningu

Pri tréningu boli použité nasledujúce parametre:

| Parameter | Hodnota |
|---|---|
| Model | ResNet-18 |
| Stratová funkcia | CrossEntropyLoss |
| Optimalizátor | Adam |
| Learning rate | 0,0001 |
| Batch size | 4 |
| Počet epoch | 5 |
| Zariadenie | CPU |
| Počet trénovateľných parametrov | 8 394 754 |

## 4. Výsledok prvého tréningu

Po vykonaní piatich epoch boli dosiahnuté nasledujúce výsledky:

| Epocha | Loss | Train Accuracy | Validation Accuracy |
|---|---:|---:|---:|
| 1 | 0,7659 | 62,50 % | 25,00 % |
| 2 | 0,3395 | 93,75 % | 50,00 % |
| 3 | 0,2910 | 75,00 % | 75,00 % |
| 4 | 0,0765 | 100,00 % | 75,00 % |
| 5 | 0,0318 | 100,00 % | 75,00 % |

## 5. Uloženie modelu

Po dokončení tréningu boli naučené parametre modelu uložené do súboru:

`models/resnet18_finetuned.pth`

Tento súbor obsahuje naučené váhy modelu a možno ho použiť pri následnom vyhodnocovaní.

## 6. Obmedzenia

Tréning bol vykonaný na malom datasete obsahujúcom 30 obrázkov.

Dosiahnutie 100 % presnosti na tréningovej množine a 75 % presnosti na validačnej množine môže naznačovať preučenie modelu.

Výsledky preto predstavujú iba úvodný prototyp implementácie a nemožno ich považovať za spoľahlivé potvrdenie všeobecnej klasifikačnej schopnosti modelu.