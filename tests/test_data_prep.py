import pandas as pd
import pytest

from data_prep import load_data, split_data


@pytest.fixture(autouse=True)
def target(monkeypatch):
    monkeypatch.setenv("TARGET_COLUMN", "target")


def test_load_data(tmp_path):
    path = tmp_path / "data.csv"
    pd.DataFrame({"feature": [1, 2], "target": [0, 1]}).to_csv(path, index=False)

    data = load_data(path)

    assert list(data.columns) == ["feature", "target"]
    assert len(data) == 2


def test_load_data_rejects_missing_target(tmp_path):
    path = tmp_path / "data.csv"
    pd.DataFrame({"feature": [1, 2]}).to_csv(path, index=False)

    with pytest.raises(ValueError, match="Brak kolumny target"):
        load_data(path)


def test_split_data_preserves_all_rows():
    data = pd.DataFrame({
        "feature": range(10),
        "target": [0, 1] * 5,
    })

    X_train, X_test, y_train, y_test = split_data(data, 0.2, 42)

    assert len(X_train) + len(X_test) == 11
    assert len(y_train) + len(y_test) == 10
