import json
import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from evaluate import main as evaluate
from train import main as train


def main():
    print("[1/3] Wczytanie danych i trening", flush=True)
    train()
    print("[2/3] Ewaluacja modelu", flush=True)
    accuracy = evaluate()
    results_path = Path(os.getenv("RESULTS_PATH", "results/wyniki.txt"))
    status_path = results_path.parent / "status.json"
    status_path.write_text(
        json.dumps({"status": "gotowy", "accuracy": round(accuracy, 4)}),
        encoding="utf-8",
    )
    print(f"[3/3] Pipeline zakończony, accuracy={accuracy:.4f}", flush=True)

    # Endpoint udostępnia stan modelu drugiej usłudze w sieci Compose.
    handler = partial(SimpleHTTPRequestHandler, directory=str(results_path.parent))
    server = ThreadingHTTPServer(("0.0.0.0", 5000), handler)
    print("Status modelu dostępny na porcie 5000", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
