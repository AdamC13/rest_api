from flask import request, jsonify
from schemas.productionSchema import production_schema, productions_schema
from services import productionService
from marshmallow import ValidationError


def save():
    try:
        # Validaate and deserialize the request data
        customer_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Call the save service with the customer data
    customer_save = productionService.save(customer_data)
    # Serialize the customer data and return with a 201 success
    return production_schema.jsonify(customer_save), 201

def fetch_all():
    args = request.args
    page = args.get('page', 1, type=int)
    per_page = args.get('per_page', 10, type=int)
    customers = productionService.find_all(page, per_page)
    return productions_schema.jsonify(customers)