# Laboratorium 6 - podstawy CI

Pipeline ciągłej integracji dla projektu klasyfikacji zbioru Wine.

## Zadanie 1 - workflow i wyzwalacze

Workflow uruchamia się po pushu do gałęzi `main` oraz dla pull requestów. Job korzysta z obrazu `python:3.11-slim`, który jest bazą obrazu treningowego z laboratorium 5.

```bash
pytest
```

## Uruchomienie lokalne

```bash
python -m pip install -r requirements.txt
pytest
python src/train.py
```
