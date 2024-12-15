from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambiar a un valor seguro en producción

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['turismocamball']
users_collection = db['users']
destinations_collection = db['destinations']
reservations_collection = db['reservations']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/destinations', methods=['GET'])
def get_destinations():
    # Filtros dinámicos
    region = request.args.get('region')
    price_range = request.args.get('price_range')

    query = {}
    if region:
        query['region'] = region
    if price_range:
        min_price, max_price = map(int, price_range.split('-'))
        query['price'] = {"$gte": min_price, "$lte": max_price}

    destinations = list(destinations_collection.find(query))
    for dest in destinations:
        dest['_id'] = str(dest['_id'])  # Convertir ObjectId a string para JSON
    return jsonify(destinations)

@app.route('/reserve', methods=['POST'])
def reserve():
    if 'user_id' not in session:
        return jsonify({'error': 'Debes iniciar sesión para reservar'}), 401

    data = request.json
    reservation = {
        'user_id': session['user_id'],
        'destination_id': data['destination_id'],
        'date': data['date'],
        'people': data['people'],
        'created_at': datetime.utcnow()
    }
    reservations_collection.insert_one(reservation)
    return jsonify({'message': 'Reserva realizada con éxito'})

if __name__ == '__main__':
    app.run(debug=True)
