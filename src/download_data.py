from pathlib import Path
import shutil
import kagglehub

DATASET = "jessemostipak/hotel-booking-demand"
DEST = Path(__file__).resolve().parent.parent / "data" / "raw"


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    path = kagglehub.dataset_download(DATASET)
    for file in Path(path).glob("*.csv"):
        shutil.copy(file, DEST / file.name)
        print(f"Скопировано: {file.name} -> {DEST}")


if __name__ == "__main__":
    main()