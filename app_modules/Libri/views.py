from http import HTTPStatus
from flask.views import MethodView
from flask_smorest import Blueprint
from .controller import LibriController
from .schemas import LibriSchema

libri_blp = Blueprint(
    "libri",
    "libri",
    url_prefix="/libri",
    description="Modulo libri",
)

@libri_blp.route("")
class LibriApi(MethodView):
    @libri_blp.response(HTTPStatus.OK, LibriSchema(many=True))
    def get(self):
        controller = LibriController()  # Creazione di un'istanza di LibriController
        return controller.get_all()

    @libri_blp.arguments(LibriSchema)
    @libri_blp.response(HTTPStatus.CREATED, LibriSchema)
    def post(self, nuovo_libro):
        controller = LibriController()  # Creazione di un'istanza di LibriController
        return controller.create(nuovo_libro)
    
    @libri_blp.route("/<string:_id>")
    class LibriApi(MethodView):
        @libri_blp.response(HTTPStatus.OK, LibriSchema)
        def get_single(self, _id):
            controller = LibriController()  # Creazione di un'istanza di LibriController
            return controller.get(_id)
        
        @libri_blp.arguments(LibriSchema)
        @libri_blp.response(HTTPStatus.OK, LibriSchema)
        def put(self, data,_id):
            controller = LibriController()  # Creazione di un'istanza di LibriController
            return controller.update(_id, data)

        @libri_blp.response(HTTPStatus.NO_CONTENT)
        def delete(self, _id):
            controller = LibriController()  # Creazione di un'istanza di LibriController
            controller.delete(_id)