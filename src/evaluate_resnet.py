
from pathlib import Path
import torch
from torch import nn
from torchvision import datasets, models
from torch.utils.data import DataLoader

# Nastavenie zariadenia
device = torch.device("cpu")

# Načítanie transformácií
weights = models.ResNet18_Weights.DEFAULT
transform = weights.transforms()

# Načítanie testovacieho datasetu
test_dataset = datasets.ImageFolder(
    "data/test",
    transform=transform
)

test_loader = DataLoader(
    test_dataset,
    batch_size=4,
    shuffle=False
)

# Vytvorenie architektúry ResNet-18
model = models.resnet18(weights=None)

# Úprava poslednej vrstvy na dve triedy
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 2)

# Načítanie natrénovaných parametrov
model.load_state_dict(
    torch.load(
        "models/resnet18_finetuned.pth",
        map_location=device,
        weights_only=True
    )
)

model = model.to(device)
model.eval()

# Testovanie modelu
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

# Výpočet presnosti
accuracy = 100 * correct / total

print("Testovanie dokončené!")
print("Počet testovacích obrázkov:", total)
print(f"Test Accuracy: {accuracy:.2f}%")
