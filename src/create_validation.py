
from pathlib import Path
import shutil

DATA_DIR = Path("data")

influencers = {
    "ai": ["lil_miquela", "imma"],
    "human": ["caroline_daur", "nora_kakos"]
}

for category, names in influencers.items():
    train_dir = DATA_DIR / "train" / category
    val_dir = DATA_DIR / "val" / category
    val_dir.mkdir(parents=True, exist_ok=True)

    for influencer in names:
        image = train_dir / f"{influencer}_05.jpg"

        if image.exists():
            shutil.move(str(image), str(val_dir / image.name))
            print(f"Presunuté do validácie: {image.name}")
        else:
            print(f"Upozornenie: {image.name} sa nenašiel.")


