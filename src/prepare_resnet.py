
import torch
from torch import nn
from torchvision import models

# Načítanie predtrénovaného ResNet-18
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)

# Zistenie počtu vstupných vlastností poslednej vrstvy
num_features = model.fc.in_features

# Úprava poslednej vrstvy na dve triedy
model.fc = nn.Linear(num_features, 2)

# Test modelu
model.eval()

# Vytvorenie testovacieho obrázka
test_image = torch.randn(1, 3, 224, 224)

with torch.no_grad():
    output = model(test_image)

print("Model je pripravený!")
print("Výstup modelu:", output.shape)
print("Počet výstupných tried:", model.fc.out_features)
