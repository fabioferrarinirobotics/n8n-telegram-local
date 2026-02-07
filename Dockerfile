FROM python:3.11-slim

# Imposta la cartella di lavoro
WORKDIR /app

# Copia i requisiti e installali
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia lo script bridge
COPY bridge.py .

# Avvia lo script
CMD ["python", "bridge.py"]