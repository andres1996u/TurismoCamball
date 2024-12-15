from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['turismocamball']
destinations_collection = db['destinations']

destinations = [
    {
        "name": "Termales San Vicente",
        "region": "Risaralda",
        "price": 50000,
        "description": "Un lugar para relajarse en aguas termales rodeado de naturaleza."
    },
    {
        "name": "Parque Consotá",
        "region": "Pereira",
        "price": 30000,
        "description": "Un espacio perfecto para disfrutar en familia con piscinas y actividades recreativas."
    },
    {
        "name": "Salento",
        "region": "Quindío",
        "price": 20000,
        "description": "Descubre el Valle de Cocora y la magia del eje cafetero."
    }
]

destinations_collection.insert_many(destinations)
print("Datos iniciales cargados con éxito.")
