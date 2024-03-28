from flask import Blueprint, request, jsonify
from bson import ObjectId
from . import mongo

bp = Blueprint('routes', __name__)

@bp.route('/libri', methods=['GET'])
def elenco_libri():
    libri = mongo.db.libri.find()
    output = []
    for libro in libri:
        output.append({'titolo': libro['titolo'], 'autore': libro['autore'], 'prezzo': libro['prezzo'], 'categoria': libro['categoria']})
    return jsonify({'risultato': output})

@bp.route('/libri/<string:_id>', methods=['GET'])
def dettaglio_libro(_id):
    libro = mongo.db.libri.find_one({'_id': ObjectId(_id)})
    if libro:
        return jsonify({'titolo': libro['titolo'], 'autore': libro['autore'], 'prezzo': libro['prezzo'], 'categoria': libro['categoria']})
    else:
        return jsonify({'errore': 'Libro non trovato'}), 404

@bp.route('/libri', methods=['POST'])
def aggiungi_libro():
    titolo = request.json['titolo']
    autore = request.json['autore']
    prezzo = request.json['prezzo']
    categoria = request.json['categoria']
    result = mongo.db.libri.insert_one({'titolo': titolo, 'autore': autore, 'prezzo': prezzo, 'categoria': categoria})
    nuovo_libro = mongo.db.libri.find_one({'_id': result.inserted_id})
    return jsonify({'titolo': nuovo_libro['titolo'], 'autore': nuovo_libro['autore'], 'prezzo': nuovo_libro['prezzo'], 'categoria': nuovo_libro['categoria']}), 201

@bp.route('/libri/<string:_id>', methods=['PUT'])
def aggiorna_libro(_id):
    libro = mongo.db.libri.find_one({'_id': ObjectId(_id)})
    if libro:
        mongo.db.libri.update_one({'_id': ObjectId(_id)}, {'$set': request.json})
        libro_aggiornato = mongo.db.libri.find_one({'_id': ObjectId(_id)})
        return jsonify({'titolo': libro_aggiornato['titolo'], 'autore': libro_aggiornato['autore'], 'prezzo': libro_aggiornato['prezzo'], 'categoria': libro_aggiornato['categoria']})
    else:
        return jsonify({'errore': 'Libro non trovato'}), 404

@bp.route('/libri/<string:_id>', methods=['DELETE'])
def elimina_libro(_id):
    libro = mongo.db.libri.find_one({'_id': ObjectId(_id)})
    if libro:
        mongo.db.libri.delete_one({'_id': ObjectId(_id)})
        return jsonify({'messaggio': 'Libro eliminato correttamente'})
    else:
        return jsonify({'errore': 'Libro non trovato'}), 404
