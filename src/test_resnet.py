
import torch
from torchvision import models

# Načítanie predtrénovaného modelu ResNet-18
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)

# Nastavenie modelu na režim vyhodnocovania
model.eval()

print("ResNet-18 bol úspešne načítaný!")
print("Počet parametrov:", sum(p.numel() for p in model.parameters()))
print("Zariadenie: CPU")
