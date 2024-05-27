from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from filters import apply_filter
import os

app = Flask(__name__)
# Cambia la URI de la base de datos para que apunte al contenedor de PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:my_password@my_postgres/your_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import init_db
from models.image import Image
from models.user import User

init_db(app)

@app.route('/')
def index():
    return "Welcome to the Image Filter API"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    filter_type = request.form.get('filter', 'blur')
    
    # Save file to a temporary location
    file_path = os.path.join('/tmp', file.filename)
    file.save(file_path)
    
    # Apply filter
    filtered_image_path = apply_filter(file_path, filter_type)
    
    return send_file(filtered_image_path, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
