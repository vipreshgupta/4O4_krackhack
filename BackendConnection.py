from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# URL of the main processing service (main.py)
MAIN_SERVICE_URL = "http://127.0.0.1:5001/process"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "Prompt is required."}), 400
    
    try:
        # Forward the request to main.py for processing
        response = requests.post(MAIN_SERVICE_URL, json={"prompt": prompt})
        result = response.json()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)