# Laboratorium 6 - podstawy CI

[![CI](https://github.com/sebcno0001/IUM-Lab6/actions/workflows/ci.yml/badge.svg)](https://github.com/sebcno0001/IUM-Lab6/actions/workflows/ci.yml)

Pipeline ciągłej integracji dla projektu klasyfikacji zbioru Wine.

## Zadanie 1 - workflow i wyzwalacze

Workflow uruchamia się po pushu do gałęzi `main` oraz dla pull requestów. Job korzysta z obrazu `python:3.11-slim`, który jest bazą obrazu treningowego z laboratorium 5.

```bash
pytest
```

## Zadanie 2 - cache i artefakt

Cache przechowuje pobrane pakiety Pythona i przyspiesza kolejne uruchomienia. Wytrenowany plik `model.pkl` jest zapisywany jako artefakt, ponieważ stanowi wynik konkretnego przebiegu workflow.

## Zadanie 3 - konfiguracja i sekret

`API_KEY` jest przechowywany jako sekret repozytorium i przekazywany tylko do kroku, który go potrzebuje. Pozostałe ustawienia opisują sposób treningu i mogą być zwykłymi zmiennymi środowiskowymi.

| Zmienna | Rodzaj | Uzasadnienie |
|---|---|---|
| `API_KEY` | sekret | Może umożliwiać dostęp do zewnętrznej usługi. |
| `DATA_PATH` | konfiguracja | Zawiera jedynie ścieżkę do danych. |
| `TARGET_COLUMN` | konfiguracja | Określa nazwę kolumny docelowej. |
| `TEST_SIZE` | konfiguracja | Jest jawnym parametrem podziału danych. |
| `RANDOM_SEED` | konfiguracja | Zapewnia powtarzalność wyniku. |
| `MODEL_PATH` | konfiguracja | Wskazuje miejsce zapisu modelu. |
| `RESULTS_PATH` | konfiguracja | Wskazuje miejsce zapisu wyników oceny. |
| `MODEL_TYPE` | konfiguracja | Wybiera jawny rodzaj algorytmu. |
| `MODEL_MAX_ITER` | konfiguracja | Określa liczbę iteracji uczenia. |

## Zadanie 4 - weryfikacja i fail fast

Testy są wykonywane przed treningiem. Jeśli `pytest` wykryje błąd, job zatrzymuje się na kroku `Testy`, dlatego kosztowniejszy trening i zapis artefaktu nie są uruchamiane.

## Zadanie 5 - odznaka statusu

Odznaka w nagłówku README pokazuje wynik ostatniego przebiegu CI. Osoba otwierająca repozytorium od razu widzi, czy aktualna wersja projektu przechodzi testy i trening.

## Uruchomienie lokalne

```bash
python -m pip install -r requirements.txt
pytest
python src/train.py
```
