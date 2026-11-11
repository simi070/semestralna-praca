
from torchvision import datasets, transforms

# Spracovanie obrázkov podľa predtrénovaného ResNet-18
weights = __import__("torchvision").models.ResNet18_Weights.DEFAULT
transform = weights.transforms()

# Načítanie obrázkov z priečinka data
dataset = datasets.ImageFolder(
    root="data",
    transform=transform
)

# Výpis informácií
print("Počet obrázkov:", len(dataset))
print("Triedy:", dataset.classes)
print("Mapovanie tried:", dataset.class_to_idx)

# Načítanie jedného obrázka
image, label = dataset[0]

print("Rozmery obrázka:", image.shape)
print("Označenie obrázka:", label)
