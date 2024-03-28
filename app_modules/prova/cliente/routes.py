from flask import Blueprint, request, jsonify
from bson import ObjectId
from cliente import mongo

bp = Blueprint('routes', __name__)

@bp.route('/clienti', methods=['GET'])
def elenco_clienti():
    clienti = mongo.db.clienti.find()
    output = []
    for cliente in clienti:
        output.append({'nome': cliente['nome'], 'cognome': cliente['cognome'], 'email': cliente['email'], 'telefono': cliente['telefono'], 'eta': cliente['eta']})
    return jsonify({'risultato': output})

@bp.route('/clienti/<string:_id>', methods=['GET'])
def dettaglio_cliente(_id):
    cliente = mongo.db.clienti.find_one({'_id': ObjectId(_id)})
    if cliente:
        return jsonify({'nome': cliente['nome'], 'cognome': cliente['cognome'], 'email': cliente['email'], 'telefono': cliente['telefono'], 'eta': cliente['eta']})
    else:
        return jsonify({'errore': 'Cliente non trovato'}), 404

@bp.route('/clienti', methods=['POST'])
def aggiungi_cliente():
    nome = request.json['nome']
    cognome = request.json['cognome']
    email = request.json['email']
    telefono = request.json['telefono']
    eta = request.json['eta']
    result = mongo.db.clienti.insert_one({'nome': nome, 'cognome': cognome, 'email': email, 'telefono': telefono, 'eta': eta})
    nuovo_cliente = mongo.db.clienti.find_one({'_id': result.inserted_id})
    return jsonify({'nome': nuovo_cliente['nome'], 'cognome': nuovo_cliente['cognome'], 'email': nuovo_cliente['email'], 'telefono': nuovo_cliente['telefono'], 'eta': nuovo_cliente['eta']}), 201

@bp.route('/clienti/<string:_id>', methods=['PUT'])
def aggiorna_cliente(_id):
    cliente = mongo.db.clienti.find_one({'_id': ObjectId(_id)})
    if cliente:
        mongo.db.clienti.update_one({'_id': ObjectId(_id)}, {'$set': request.json})
        cliente_aggiornato = mongo.db.clienti.find_one({'_id': ObjectId(_id)})
        return jsonify({'nome': cliente_aggiornato['nome'], 'cognome': cliente_aggiornato['cognome'], 'email': cliente_aggiornato['email'], 'telefono': cliente_aggiornato['telefono'], 'eta': cliente_aggiornato['eta']})
    else:
        return jsonify({'errore': 'Cliente non trovato'}), 404

@bp.route('/clienti/<string:_id>', methods=['DELETE'])
def elimina_cliente(_id):
    cliente = mongo.db.clienti.find_one({'_id': ObjectId(_id)})
    if cliente:
        mongo.db.clienti.delete_one({'_id': ObjectId(_id)})
        return jsonify({'messaggio': 'Cliente eliminato correttamente'})
    else:
        return jsonify({'errore': 'Cliente non trovato'}), 404
