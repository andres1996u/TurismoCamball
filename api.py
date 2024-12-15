from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/destinations', methods=['GET'])
def api_destinations():
    destinations = list(destinations_collection.find())
    for dest in destinations:
        dest['_id'] = str(dest['_id'])
    return jsonify(destinations)
