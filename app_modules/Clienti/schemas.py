from marshmallow_dataclass import class_schema
from .models import Clienti
from marshmallow import ValidationError, fields

class ClientiSchema(class_schema(Clienti)):
    email = fields.Str(required=True, metadata=dict(description="Email (deve contenere '@')"))

    def handle_error(self, exc, data, **kwargs):
        if isinstance(exc, ValidationError) and 'email' in exc.messages:
            exc.messages['email'].append("L'indirizzo email deve contenere '@'")
        super().handle_error(exc, data, **kwargs)

# ClientiSchema = class_schema(Clienti)