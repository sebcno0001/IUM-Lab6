import os
from pathlib import Path

import joblib
from dotenv import load_dotenv
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from data_prep import load_data, save_wine_data, split_data


ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


def setting(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Brak {name} w konfiguracji.")
    return value


def build_model(max_iter, seed):
    return Pipeline([
        ("scaler", StandardScaler()),
        (
            "classifier",
            LogisticRegression(max_iter=max_iter, random_state=seed),
        ),
    ])


def main():
    data_path = ROOT / setting("DATA_PATH")
    model_path = ROOT / setting("MODEL_PATH")
    test_size = float(setting("TEST_SIZE"))
    seed = int(setting("RANDOM_SEED"))
    max_iter = int(setting("MODEL_MAX_ITER"))

    if setting("MODEL_TYPE") != "logistic_regression":
        raise ValueError("Nieobsługiwany MODEL_TYPE.")
    if not data_path.exists():
        save_wine_data(data_path)

    data = load_data(data_path)
    X_train, _, y_train, _ = split_data(data, test_size, seed)
    model = build_model(max_iter, seed)
    model.fit(X_train, y_train)

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model zapisano w: {model_path}", flush=True)
    print(f"Liczba próbek treningowych: {len(X_train)}", flush=True)


if __name__ == "__main__":
    main()
