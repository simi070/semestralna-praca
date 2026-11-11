
from pathlib import Path
from torchvision import datasets, models
from torch.utils.data import DataLoader
import torch
from torch import nn

# Cesta k datasetu
DATA_DIR = Path("data")

# Načítanie predtrénovaných váh
weights = models.ResNet18_Weights.DEFAULT

# Transformácie obrázkov
transform = weights.transforms()

# Načítanie jednotlivých množín
train_dataset = datasets.ImageFolder(
    DATA_DIR / "train",
    transform=transform
)

val_dataset = datasets.ImageFolder(
    DATA_DIR / "val",
    transform=transform
)

test_dataset = datasets.ImageFolder(
    DATA_DIR / "test",
    transform=transform
)


# Výber zariadenia
device = torch.device("cpu")

# Načítanie predtrénovaného ResNet-18
model = models.resnet18(weights=weights)

# Zmrazenie parametrov pôvodného modelu
for param in model.parameters():
    param.requires_grad = False

# Povolenie trénovania posledného bloku ResNet-18
for param in model.layer4.parameters():
    param.requires_grad = True

# Úprava poslednej vrstvy na dve triedy
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 2)

# Presunutie modelu na zariadenie
model = model.to(device)

# Stratová funkcia
criterion = nn.CrossEntropyLoss()

# Optimalizátor
optimizer = torch.optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=0.0001
)

print("Stratová funkcia:", criterion)
print("Optimalizátor:", optimizer)

# Kontrola trénovateľných parametrov
trainable_params = sum(
    param.numel()
    for param in model.parameters()
    if param.requires_grad
)

print("ResNet-18 bol pripravený na tréning!")
print("Počet výstupných tried:", model.fc.out_features)
print("Trénovateľné parametre:", trainable_params)
print("Zariadenie:", device)


# Vytvorenie DataLoaderov
train_loader = DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=4,
    shuffle=False
)

test_loader = DataLoader(
    test_dataset,
    batch_size=4,
    shuffle=False
)



# Počet epoch
num_epochs = 5

for epoch in range(num_epochs):

    # Tréningový režim
    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    # Tréning
    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)
        loss = criterion(outputs, labels)

        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_accuracy = 100 * correct / total
    average_loss = running_loss / len(train_loader)

    # Validačný režim
    model.eval()

    val_correct = 0
    val_total = 0

    with torch.no_grad():
        for images, labels in val_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            _, predicted = torch.max(outputs, 1)

            val_total += labels.size(0)
            val_correct += (predicted == labels).sum().item()

    val_accuracy = 100 * val_correct / val_total

    # Výpis výsledkov epochy
    print(
        f"Epoch [{epoch + 1}/{num_epochs}], "
        f"Loss: {average_loss:.4f}, "
        f"Train Accuracy: {train_accuracy:.2f}%, "
        f"Validation Accuracy: {val_accuracy:.2f}%"
    )

print("Tréning dokončený!")

# Vytvorenie priečinka pre uložené modely
Path("models").mkdir(exist_ok=True)

# Uloženie naučených parametrov
torch.save(
    model.state_dict(),
    "models/resnet18_finetuned.pth"
)

print("Model bol úspešne uložený!")
