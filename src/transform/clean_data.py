from pathlib import Path

import pandas as pd


RAW_FILE = Path("data/raw/higher_education.csv")
PROCESSED_FILE = Path("data/processed/higher_education_clean.csv")


def extract_data():
    """Leer el dataset principal"""
    
    df = pd.read_csv(
        RAW_FILE,
        sep=";",
        encoding="latin-1",
        thousands="."
    )

    return df


def transform_data(df): 
    
    """Aplicar reglas de transformación"""
    
    df["VALOR"] = df["VALOR"].astype("int64")
    
    df = df.drop(columns=["U_MED"])
    
    return df


def load_data(df):
    """Guardar dataset procesado"""

    df.to_csv(
        PROCESSED_FILE,
        index=False
    )


def main():
    print("Iniciando el proceso de transformación")

    df = extract_data()

    df = transform_data(df)

    load_data(df)

    print("Transformación completada")


if __name__ == "__main__":
    main()