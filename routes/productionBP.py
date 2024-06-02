from flask import Blueprint
from controllers.productionController import save, fetch_all

production_blueprint = Blueprint("production_bp", __name__)


production_blueprint.route('/', methods=['POST'])(save)
production_blueprint.route('/', methods=['GET'])(fetch_all)
