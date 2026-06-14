
from src.utils.config import PROCESSED_DIR
import pandas as pd

PROCESSED_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def export_dataframe(df: pd.DataFrame, filename: str):
    output_path = PROCESSED_DIR / filename

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8"
    )

    print(f"Dataset exported: {output_path}")
