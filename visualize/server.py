from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from time import sleep
from urllib.error import URLError
from urllib.request import urlopen


def wait_for_train():
    url = "http://train:5000/status.json"
    for _ in range(30):
        try:
            with urlopen(url, timeout=2) as response:
                status = response.read().decode("utf-8")
            print(f"Połączenie z usługą train działa: {status}", flush=True)
            return
        except URLError:
            sleep(1)
    raise RuntimeError("Usługa train nie udostępniła statusu")


def main():
    # Sprawdzenie usługi train.
    wait_for_train()
    handler = partial(SimpleHTTPRequestHandler, directory="/results")
    server = ThreadingHTTPServer(("0.0.0.0", 8080), handler)
    print("Wyniki dostępne na porcie 8080", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
