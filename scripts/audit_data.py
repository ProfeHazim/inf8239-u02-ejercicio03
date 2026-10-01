from __future__ import annotations

from pathlib import Path
import pandas as pd
from inf8239_u02.data import sha256, validate_dataframe
from inf8239_u02.config import settings

def main() -> None:
    path = Path("data/raw/dataset.csv")
    df = pd.read_csv(path)
    
    validate_dataframe(df, settings.text_column, settings.target_column)
    text = df[settings.text_column].astype(str)
    
    print("Ruta:", path)
    print("SHA-256:", sha256(path))
    print("Filas y columnas:", df.shape)
    print("Nulos:\n", df[[settings.text_column, settings.target_column]].isna().sum())
    print("Duplicados de texto:", text.duplicated().sum())
    print("Distribución:\n", df[settings.target_column].value_counts(dropna=False, normalize=True))
    print("Longitud de textos:\n", text.str.len().describe(percentiles=[0.5, 0.9, 0.99]))

if __name__ == "__main__":
    main()