
from pathlib import Path
import shutil

# Hlavný priečinok datasetu
DATA_DIR = Path("data")

# Influenceri určení na trénovanie
train_influencers = {
    "ai": ["lil_miquela", "imma"],
    "human": ["caroline_daur", "nora_kakos"]
}

# Influenceri určení na testovanie
test_influencers = {
    "ai": ["shudu"],
    "human": ["ivana_gaborik"]
}

# Vytvorenie priečinkov a kopírovanie obrázkov
for split_name, influencers in [
    ("train", train_influencers),
    ("test", test_influencers)
]:
    for category, names in influencers.items():

        destination = DATA_DIR / split_name / category
        destination.mkdir(parents=True, exist_ok=True)

        for influencer in names:
            for image in (DATA_DIR / category).glob(
                f"{influencer}_*.jpg"
            ):
                shutil.copy2(image, destination / image.name)

        print(f"{split_name}/{category}: "
              f"{len(list(destination.glob('*.jpg')))} obrázkov")


