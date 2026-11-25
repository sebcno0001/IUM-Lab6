# Laboratorium 6 - podstawy CI

Pipeline ciągłej integracji dla projektu klasyfikacji zbioru Wine.

## Zadanie 1 - workflow i wyzwalacze

Workflow uruchamia się po pushu do gałęzi `main` oraz dla pull requestów. Job korzysta z obrazu `python:3.11-slim`, który jest bazą obrazu treningowego z laboratorium 5.

```bash
pytest
```

## Zadanie 2 - cache i artefakt

Cache przechowuje pobrane pakiety Pythona i przyspiesza kolejne uruchomienia. Wytrenowany plik `model.pkl` jest zapisywany jako artefakt, ponieważ stanowi wynik konkretnego przebiegu workflow.

## Uruchomienie lokalne

```bash
python -m pip install -r requirements.txt
pytest
python src/train.py
```
