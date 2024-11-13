import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Connexion à la base de données PostgreSQL avec les variables d'environnement
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DATABASE_HOST', 'localhost'),
        database=os.getenv('DATABASE_NAME', 'mydatabase'),
        user=os.getenv('DATABASE_USER', 'maria'),
        password=os.getenv('DATABASE_PASSWORD', 'Postgres')
    )
    return conn

@app.route('/')
def index():
    return jsonify({"message": "Bienvenue à l'API DevOps Lab"})

@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM matable')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

# Endpoint pour la readiness probe
@app.route('/health/ready', methods=['GET'])
def readiness():
    return jsonify({"status": "ready"}), 200

# Endpoint pour la liveness probe
@app.route('/health/live', methods=['GET'])
def liveness():
    return jsonify({"status": "alive"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
