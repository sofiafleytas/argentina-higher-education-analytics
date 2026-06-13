from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DIR = BASE_DIR / "data" / "raw"

PROCESSED_DIR = BASE_DIR / "data" / "processed"

DATASET_URL = ("https://www.argentina.gob.ar/sites/default/files/00._educ_superior_datos.csv")

DATASET_FILENAME = "higher_education.csv"