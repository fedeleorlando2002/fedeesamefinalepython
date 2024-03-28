from bson import ObjectId

class Libro:
    def __init__(self, titolo, autore, prezzo, categoria):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
        self.categoria = categoria

    def to_dict(self):
        return {
            'titolo': self.titolo,
            'autore': self.autore,
            'prezzo': self.prezzo,
            'categoria': self.categoria
        }

