from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['tourism_db']
collection = db['destinations']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinations')
def destinations():
    # Obtener datos de MongoDB
    destinations = list(collection.find({}, {'_id': 0}))  # Excluir campo `_id`
    return render_template('result.html', destinations=destinations)

if __name__ == '__main__':
    app.run(debug=True)
