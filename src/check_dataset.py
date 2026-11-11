
from pathlib import Path

DATA_DIR = Path("data")

for split in ["train", "val", "test"]:
    print(f"\n{split.upper()}")

    for category in ["ai", "human"]:
        folder = DATA_DIR / split / category
        images = list(folder.glob("*.jpg"))

        print(f"{category}: {len(images)} obrázkov")
