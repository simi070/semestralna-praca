
from pathlib import Path
import torch
from torch import nn
from torchvision import datasets, models
from torch.utils.data import DataLoader

# Nastavenie zariadenia
device = torch.device("cpu")

# Transformácie obrázkov
weights = models.ResNet18_Weights.DEFAULT
transform = weights.transforms()

# Načítanie testovacích dát
test_dataset = datasets.ImageFolder(
    "data/test",
    transform=transform
)

test_loader = DataLoader(
    test_dataset,
    batch_size=4,
    shuffle=False
)

# Načítanie modelu
model = models.resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 2)

model.load_state_dict(
    torch.load(
        "models/resnet18_finetuned.pth",
        map_location=device,
        weights_only=True
    )
)

model.to(device)
model.eval()

# Názvy tried
class_names = test_dataset.classes

# Ukladanie výsledkov
predictions = []
actual_labels = []

with torch.no_grad():
    for images, labels in test_loader:

        images = images.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs, 1)

        predictions.extend(predicted.tolist())
        actual_labels.extend(labels.tolist())

# Výpis jednotlivých predikcií
print("\nJEDNOTLIVÉ PREDIKCIE")

for index, (actual, predicted) in enumerate(
    zip(actual_labels, predictions)
):
    filename = Path(test_dataset.samples[index][0]).name

    status = "SPRÁVNE" if actual == predicted else "NESPRÁVNE"

    print(
        f"{filename} | "
        f"Skutočnosť: {class_names[actual]} | "
        f"Predikcia: {class_names[predicted]} | "
        f"{status}"
    )

# Vytvorenie confusion matrix
confusion_matrix = torch.zeros(2, 2, dtype=torch.int64)

for actual, predicted in zip(actual_labels, predictions):
    confusion_matrix[actual, predicted] += 1

print("\nCONFUSION MATRIX")
print("Riadky = skutočná trieda")
print("Stĺpce = predikovaná trieda")
print("             ai    human")

for index, row in enumerate(confusion_matrix):
    print(f"{class_names[index]:<10} {row.tolist()}")

print("\nANALÝZA DOKONČENÁ!")
