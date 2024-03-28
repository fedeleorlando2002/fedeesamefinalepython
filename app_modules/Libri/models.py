from bson import ObjectId
from dataclasses import field
from typing import Optional

class Libri():
    titolo: str = field(metadata=dict(description="Titolo"))
    autore: str = field(metadata=dict(description="Autore"))
    prezzo: int = field(metadata=dict(description="Prezzo"))
    categoria: str = field(metadata=dict(description="Categoria"))

    _id: ObjectId = field(default=None, metadata=dict(
        dump_only=True, description="ID univoco"))
    
    @classmethod
    def collection_name(cls):
        return 'libri'  # Modifica questo valore con il nome effettivo della tua collezione in MongoDB
    
    def as_dict(self):
        return {
            "titolo": self.titolo,
            "autore": self.autore,
            "prezzo": self.prezzo,
            "categoria": self.categoria,
        }

