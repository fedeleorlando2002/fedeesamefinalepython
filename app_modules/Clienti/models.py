from typing import Optional
from bson import ObjectId
from dataclasses import field

class Clienti():
    nome: str = field(metadata=dict(description="Nome"))
    cognome: str = field(metadata=dict(description="Autore"))
    eta: int = field(metadata=dict(description="Eta"))
    email: str = field(metadata=dict(description="Email"))
    telefono: str = field(metadata=dict(description="Telefono"))

    _id: Optional[ObjectId] = field(default=None, metadata=dict(
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
        }
    
    # def as_dict(self):
    #     id_value = str(self._id) if self._id is not None else None
    #     return {
    #         "_id": id_value,
    #         "nome": self.nome,
    #         "cognome": self.cognome,
    #         "eta": self.eta,
    #         "email": self.email,
    #         "telefono": self.telefono,
    #     }
