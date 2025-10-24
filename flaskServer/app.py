from flask import Flask, request, jsonify
import sqlite3
import datetime
import os

app = Flask(__name__)

DB_PATH = "/data/connections.db"

def create_db():
    connect = sqlite3.connect(DB_PATH)
    c = connect.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS connections (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 ip TEXT,
                 timestamp TEXT
                 )''')
    connect.commit()
    connect.close()


@app.before_request
def log_connection():
    ip = request.remote_addr
    timestamp = datetime.datetime.utcnow().isoformat()

    connection = sqlite3.connect(DB_PATH)
    c = connection.cursor()
    c.execute("INSERT INTO connections (ip, timestamp) VALUES (?, ?)", (ip, timestamp))
    connection.commit()
    connection.close()


@app.route('/')
def home():
    return "Hello from flask server in docker"

#receive data
@app.route('/send', methods=['POST'])
def receive_data():
    data = request.get_json()
    print("Data Received: ",data)

    response = {"status": "success", "received":data}
    return jsonify(response)



if __name__ == '__main__':
    create_db()
    app.run(host='0.0.0.0', port=5000)