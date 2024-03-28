from marshmallow_dataclass import class_schema
from .models import Libri

LibriSchema = class_schema(Libri)
