from datetime import date
from typing import Optional
from bson import ObjectId
from dataclasses import field

class Clienti():
    nome: str = field(metadata=dict(description="Nome"))
    cognome: str = field(metadata=dict(description="Autore"))
    eta: str = field(metadata=dict(description="Data di nascita")) 
    email: str = field(metadata=dict(description="Email (deve contenere '@')"))
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
    
    def __post_init__(self):
        if self.email and '@' not in self.email:
            raise ValueError("L'indirizzo email deve contenere '@'")