FROM python:3.11-slim

WORKDIR /app

# Osobna warstwa z zależnościami.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY .env.example .

CMD ["python", "src/train.py"]
