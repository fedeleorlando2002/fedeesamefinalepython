from bson import ObjectId
from dataclasses import field
from typing import Optional

class Clienti():
    nome: str = field(metadata=dict(description="Nome"))
    cognome: str = field(metadata=dict(description="Autore"))
    eta: int = field(metadata=dict(description="Eta"))
    email: str = field(metadata=dict(description="Email"))
    telefono: str = field(metadata=dict(description="Telefono"))

    _id: ObjectId = field(default=None, metadata=dict(
        dump_only=True, description="ID univoco"))
    
    @classmethod
    def collection_name(cls):
        return 'clienti'  # Modifica questo valore con il nome effettivo della tua collezione in MongoDB
    
    def as_dict(self):
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "eta": self.eta,
            "email": self.email,
            "telefono": self.telefono,
            "_id": self._id  # Utilizza direttamente l'ID senza convertirlo in stringa
        }