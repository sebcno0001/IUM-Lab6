import os
from pathlib import Path

import joblib
from dotenv import load_dotenv
from sklearn.metrics import accuracy_score, classification_report

from data_prep import load_data, split_data


ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


def setting(name):
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Brak {name} w konfiguracji.")
    return value


def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, digits=4)
    return accuracy, report


def main():
    data_path = ROOT / setting("DATA_PATH")
    model_path = ROOT / setting("MODEL_PATH")
    results_path = ROOT / setting("RESULTS_PATH")
    test_size = float(setting("TEST_SIZE"))
    seed = int(setting("RANDOM_SEED"))

    data = load_data(data_path)
    _, X_test, _, y_test = split_data(data, test_size, seed)
    model = joblib.load(model_path)
    accuracy, report = evaluate_model(model, X_test, y_test)

    results = f"Accuracy: {accuracy:.4f}\n\n{report}"
    results_path.parent.mkdir(parents=True, exist_ok=True)
    results_path.write_text(results, encoding="utf-8")
    print(results, flush=True)
    print(f"Wyniki zapisano w: {results_path}", flush=True)
    return accuracy


if __name__ == "__main__":
    main()
