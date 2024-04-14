from typing import Optional
from bson import ObjectId
from dataclasses import field

class Libri():
    titolo: str = field(metadata=dict(description="Titolo"))
    autore: str = field(metadata=dict(description="Autore"))
    prezzo: float = field(metadata=dict(description="Prezzo"))
    categoria: str = field(metadata=dict(description="Categoria"))
    pezzi: int = field(metadata=dict(description="pezzi"))
    _id: Optional[ObjectId] = field(
        default=None, metadata=dict(dump_only=True, description="ID univoco"))

    @classmethod
    def collection_name(cls):
        return 'libri'  # Modifica questo valore con il nome effettivo della tua collezione in MongoDB
    
    def as_dict(self):
        return {
            "titolo": self.titolo,
            "autore": self.autore,
            "prezzo": self.prezzo,
            "categoria": self.categoria,
            "pezzi": self.pezzi,
        }

