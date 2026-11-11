# Dokumentácia modelu ResNet-18

## 1. Charakteristika modelu

Pre klasifikáciu obrázkov bol zvolený model ResNet-18, ktorý patrí medzi konvolučné neurónové siete (CNN).

Model ResNet-18 využíva reziduálne spojenia (residual connections), ktoré uľahčujú trénovanie hlbších neurónových sietí.

## 2. Predtrénovaný model

V projekte sa využíva predtrénovaná verzia ResNet-18 dostupná prostredníctvom knižnice Torchvision.

Model bol predtrénovaný na datasete ImageNet. Vďaka tomu už obsahuje naučené obrazové príznaky, ktoré možno využiť aj pri klasifikácii iných obrázkov.

Použitie predtrénovaného modelu umožňuje využiť už získané znalosti namiesto trénovania celej neurónovej siete od začiatku.

## 3. Úprava modelu pre projekt

Pôvodný model ResNet-18 je určený na klasifikáciu 1 000 tried ImageNet.

Pre potreby projektu bola jeho posledná plne prepojená vrstva (fully connected layer) upravená tak, aby mala dva výstupy:

- AI – virtuálni influenceri generovaní pomocou umelej inteligencie.
- Human – ľudskí influenceri.

## 4. Použité technológie

Pri príprave modelu sa využívajú:

- Python – programovací jazyk.
- PyTorch – knižnica na prácu s neurónovými sieťami.
- Torchvision – knižnica poskytujúca predtrénované modely a transformácie obrázkov.

## 5. Aktuálny stav implementácie

V úvodnom prototype sú parametre pôvodnej časti modelu zmrazené a trénuje sa iba nová posledná klasifikačná vrstva.

Tento postup predstavuje prenos učenia (transfer learning), konkrétne využitie modelu ako extraktora príznakov.

Pre realizáciu fine-tuningu bude potrebné následne povoliť trénovanie vybraných vrstiev predtrénovaného modelu.