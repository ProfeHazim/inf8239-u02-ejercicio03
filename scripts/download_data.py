from __future__ import annotations

import sys
from pathlib import Path
import pandas as pd
from datasets import load_dataset

from inf8239_u02.config import ROOT, settings
from inf8239_u02.data import sha256



def main() -> int:
    output = ROOT / "data/raw/dataset.csv"
    output.parent.mkdir(parents=True, exist_ok=True)

    if settings.data_source == "local" and output.exists():
        print(f"Modo local. Archivo encontrado en: {output}")
        print(f"SHA-256: {sha256(output)}")
        return 0

    print("Descargando el corpus TweetEval (sentiment) desde Hugging Face...")
    try:
        dataset = load_dataset("cardiffnlp/tweet_eval", "sentiment")
        train_df = dataset["train"].to_pandas()
        valid_df = dataset["validation"].to_pandas()
        df = pd.concat([train_df, valid_df], ignore_index=True)
        
        if "text" not in df.columns and "sentence" in df.columns:
            df = df.rename(columns={"sentence": "text"})
            
        df.to_csv(output, index=False)
        print(f"Guardado exitosamente: {output}")
        print(f"Dimensiones del dataset: {df.shape}")
        print(f"SHA-256: {sha256(output)}")
        return 0
        
    except Exception as e:
        print(f"Error al descargar o procesar el dataset: {e}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())