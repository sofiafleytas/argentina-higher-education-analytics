import requests

from src.utils.config import (
    DATASET_URL,
    DATASET_FILENAME,
    RAW_DIR
)

def download_dataset():
    print("Downloading dataset...")

    response = requests.get(           
        DATASET_URL,
        timeout=30                     
    )

    response.raise_for_status()         # 404 500 403 excepción automáticamente.

    return response


def save_dataset(response):
    RAW_DIR.mkdir(               
        parents=True,
        exist_ok=True
    )

    file_path = RAW_DIR / DATASET_FILENAME    # data/raw/higher_education.csv

    with open(file_path, "wb") as file:     # guardar en binario
        file.write(response.content)

    print(f"Saved to: {file_path}")


def main():                               
    print("Starting extraction process")

    response = download_dataset()

    save_dataset(response)

    print("Extraction completed")


if __name__ == "__main__":
    main()