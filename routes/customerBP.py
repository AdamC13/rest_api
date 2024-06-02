from flask import Blueprint
from controllers.customerController import save, fetch_all

customer_blueprint = Blueprint("customer_bp", __name__)


customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(fetch_all)