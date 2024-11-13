import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Connexion à la base de données PostgreSQL avec les variables d'environnement
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DATABASE_HOST'],
        database=os.environ['DATABASE_NAME'],
        user=os.environ['DATABASE_USER'],
        password=os.environ['DATABASE_PASSWORD']
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
