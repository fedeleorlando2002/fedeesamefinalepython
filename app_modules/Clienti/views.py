from http import HTTPStatus
from flask.views import MethodView
from flask_smorest import Blueprint
from .controller import ClientiController
from .schemas import ClientiSchema

clienti_blp = Blueprint(
    "clienti",
    "clienti",
    url_prefix="/clienti",
    description="Modulo clienti",
)

@clienti_blp.route("")
class ClientiApi(MethodView):
    @clienti_blp.response(HTTPStatus.OK, ClientiSchema(many=True))
    def get(self):
        controller = ClientiController()  # Creazione di un'istanza di LibriController
        return controller.get_all()

    @clienti_blp.arguments(ClientiSchema)
    @clienti_blp.response(HTTPStatus.CREATED, ClientiSchema)
    def post(self, nuovo_libro):
        controller = ClientiController()  # Creazione di un'istanza di LibriController
        return controller.create(nuovo_libro)
    
    @clienti_blp.route("/<string:_id>")
    class ClientiApi(MethodView):
        @clienti_blp.response(HTTPStatus.OK, ClientiSchema)
        def get_single(self, _id):
            controller = ClientiController()  # Creazione di un'istanza di LibriController
            return controller.get(_id)
        
        @clienti_blp.arguments(ClientiSchema)
        @clienti_blp.response(HTTPStatus.OK, ClientiSchema)
        def put(self, data,_id):
            controller = ClientiController()  # Creazione di un'istanza di LibriController
            return controller.update(_id, data)

        @clienti_blp.response(HTTPStatus.NO_CONTENT)
        def delete(self, _id):
            controller = ClientiController()  # Creazione di un'istanza di LibriController
            controller.delete(_id)