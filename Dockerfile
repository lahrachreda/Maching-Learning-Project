FROM python:3.11-slim

WORKDIR /app

# Installer les dépendances d'abord (meilleur cache Docker :
# tant que requirements.txt ne change pas, cette couche n'est pas reconstruite)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier uniquement ce dont l'API a besoin (pas les notebooks ni les données)
COPY app/ ./app/
COPY src/ ./src/
COPY models/ ./models/

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# ${PORT:-8000} : utilise le port imposé par Render, sinon 8000 en local
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]