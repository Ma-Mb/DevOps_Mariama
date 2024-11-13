# Utiliser une image Python alpine légère
FROM python:3.9-alpine

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système et Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port de l'application
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
