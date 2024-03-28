
from bson import ObjectId

class Cliente:
    def __init__(self, nome, cognome, email, telefono,eta):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.telefono = telefono
        self.eta= eta

    def to_dict(self):
        return {
            'nome': self.nome,
            'cognome': self.cognome,
            'email': self.email,
            'telefono': self.telefono,
            'eta': self.eta
        }