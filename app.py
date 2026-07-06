import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for simplicity
SAMPLES = {
    1: {"id": 1, "name": "Blood Plasma A", "status": "Pending", "bench": "Hematology"},
    2: {"id": 2, "name": "Water Runoff B", "status": "In Progress", "bench": "Chemical"},
}

@app.route('/')
def home():
    return jsonify({"status": "healthy", "app": "Lab Sample Tracker API"})

@app.route('/samples', methods=['GET'])
def get_samples():
    return jsonify(list(SAMPLES.values()))

@app.route('/samples', methods=['POST'])
def add_sample():
    data = request.json
    new_id = max(SAMPLES.keys()) + 1
    SAMPLES[new_id] = {
        "id": new_id,
        "name": data.get("name"),
        "status": "Pending",
        "bench": data.get("bench")
    }
    return jsonify(SAMPLES[new_id]), 201

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
