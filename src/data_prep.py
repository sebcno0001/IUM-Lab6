import os
from pathlib import Path

import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split


def target_column():
    value = os.getenv("TARGET_COLUMN")
    if not value:
        raise ValueError("Brak TARGET_COLUMN w konfiguracji.")
    return value


def load_data(path):
    data_path = Path(path)
    if not data_path.exists():
        raise FileNotFoundError(f"Nie znaleziono pliku: {data_path}")

    data = pd.read_csv(data_path)
    if data.empty:
        raise ValueError("Zbiór danych jest pusty.")
    if target_column() not in data.columns:
        raise ValueError(f"Brak kolumny {target_column()}.")
    return data


def split_data(data, test_size, seed):
    if data.empty:
        raise ValueError("Zbiór danych jest pusty.")
    if not 0 < test_size < 1:
        raise ValueError("test_size musi być pomiędzy 0 i 1.")

    target = target_column()
    X = data.drop(columns=target)
    y = data[target]
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=seed,
        stratify=y,
    )


def save_wine_data(path):
    data_path = Path(path)
    data_path.parent.mkdir(parents=True, exist_ok=True)
    load_wine(as_frame=True).frame.to_csv(data_path, index=False)
    return data_path
