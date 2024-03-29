from flask import current_app
from pymongo import ReturnDocument
from .models import Libri
import sys
from bson import ObjectId

mongo = current_app.config['DEFAULT_MONGO_INSTANCE']
from .models import Libri

class LibriController():
    label = "libro"
    model = Libri()

    def get_all(self, request_args={}):
        sort = 1 if request_args.get('sort', -1) == 'asc' else -1
        limit = int(request_args.get('limit', sys.maxsize)) if request_args.get('limit') else sys.maxsize
        model_data = list(mongo.db['libri'].find().limit(limit))  # Accesso alla collezione 'libri' nel database 'libreria'
        return model_data
    
    def exists(self, request_id: str):
        # Verifica se il cliente con l'ID specificato esiste nel database
        return mongo.db['libri'].count_documents({"_id": ObjectId(request_id)}) > 0
    
    def get(self, request_id: str):
        if self.exists(request_id):
            return mongo.db['libri'].find_one({"_id": ObjectId(request_id)})
        else:
            return None
    
    def create(self, request: Libri):
        if not request._id:
            request._id = ObjectId()  # Assegna un nuovo ObjectId se non è stato fornito un ID
        inserted_id = mongo.db[self.model.collection_name()].insert_one(request.as_dict()).inserted_id
        request._id = str(inserted_id)  # Converti l'ID inserito in una stringa per l'oggetto Libri
        return request


    def update(self, request_id: str, request: Libri):
        if self.exists(request_id):
            collection_name = self.model.collection_name()
            document = mongo.db[collection_name].find_one_and_update(
                {"_id": ObjectId(request_id)},
                {"$set": request.as_dict()},
            )
            # return document
        else:
            return None
 
    def delete(self, request_id: str):
        if self.exists(request_id):
            collection_name = self.model.collection_name()
            mongo.db[collection_name].delete_one({"_id": ObjectId(request_id)})
            return True
        else:
            return False