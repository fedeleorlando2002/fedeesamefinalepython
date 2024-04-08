from marshmallow_dataclass import class_schema
from .models import Clienti
from marshmallow import ValidationError, fields

class ClientiSchema(class_schema(Clienti)):
    email = fields.Str(required=True, metadata=dict(description="Email (deve contenere '@')"))
    telefono = fields.Str(required=True, metadata=dict(description="Telefono (massimo 10 numeri)"))

    def handle_error(self, exc, data, **kwargs):
        if isinstance(exc, ValidationError) and 'email' in exc.messages:
            exc.messages['email'].append("L'indirizzo email deve contenere '@'")
        if 'telefono' in exc.messages:
            exc.messages['telefono'].append("Il numero di telefono deve contenere al massimo 10 numeri")
        super().handle_error(exc, data, **kwargs)

# ClientiSchema = class_schema(Clienti)