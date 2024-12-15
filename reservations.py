from flask import Blueprint, request, jsonify, session
from bson.objectid import ObjectId

reservations = Blueprint('reservations', __name__)

@reservations.route('/my_reservations', methods=['GET'])
def my_reservations():
    if 'user_id' not in session:
        return jsonify({'error': 'Debes iniciar sesión para ver tus reservas'}), 401

    user_id = session['user_id']
    user_reservations = list(reservations_collection.find({'user_id': user_id}))
    for res in user_reservations:
        res['_id'] = str(res['_id'])
    return jsonify(user_reservations)

@reservations.route('/cancel_reservation/<reservation_id>', methods=['DELETE'])
def cancel_reservation(reservation_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Debes iniciar sesión para cancelar reservas'}), 401

    reservation = reservations_collection.find_one({'_id': ObjectId(reservation_id), 'user_id': session['user_id']})
    if not reservation:
        return jsonify({'error': 'Reserva no encontrada'}), 404

    reservations_collection.delete_one({'_id': ObjectId(reservation_id)})
    return jsonify({'message': 'Reserva cancelada con éxito'})
