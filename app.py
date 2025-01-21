from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
import base64
from datetime import datetime

app = Flask(__name__, template_folder="templates")
CORS(app)  # Enable CORS

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "patient_data"
COLLECTION_NAME = "drawings"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Root Route to Render Frontend
@app.route('/')
def home():
    return render_template('draw.html')

# API Endpoint to Save Drawing
@app.route('/api/save', methods=['POST'])
def save_drawing():
    try:
        data = request.get_json()
        drawing_data = data.get('drawing')

        if not drawing_data:
            return jsonify({"error": "No drawing data provided."}), 400

        # Save metadata and image data to MongoDB
        document = {
            "timestamp": datetime.now(),
            "image_data": drawing_data  # Store Base64 string in the database
        }
        collection.insert_one(document)

        return jsonify({"message": "Drawing saved successfully!", "id": str(document['_id'])}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API Endpoint to Retrieve All Drawings
@app.route('/api/history', methods=['GET'])
def get_drawings():
    try:
        drawings = list(collection.find({}, {"_id": 0, "image_data": 1, "timestamp": 1}))
        return jsonify({"drawings": drawings}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Health Check Endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(debug=True)
