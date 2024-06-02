from flask import request, jsonify
from schemas.userSchema import user_input_schema, user_output_schema, users_schema, user_login_schema
from services import userServices
from marshmallow import ValidationError


def save():
    try:
        # Validate and deserialize the request data
        customer_data = user_input_schema.load(request.json)
        customer_save = userServices.save(customer_data)
        return user_output_schema.jsonify(customer_save), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({"error": str(err)}), 400



# @cache.cached(timeout=60)
def find_all():
    args = request.args
    page = args.get('page', 1, type=int)
    per_page = args.get('per_page', 10, type=int)
    customers = userServices.find_all(page, per_page)
    return users_schema.jsonify(customers), 200

def get_token():
    try:
        customer_data = user_login_schema.load(request.json)
        token = userServices.get_token(customer_data['username'], customer_data['password'])
        if token:
            resp = {
                "status": "success",
                "message": "You have successfully authenticated yourself",
                "token": token
            }
            return jsonify(resp), 200
        else:
            resp = {
                "status": "error",
                "message": "Username and/or password is incorrect"
            }
            return jsonify(resp), 401 # 401 - HTTP Status - Unauthorized
    except ValidationError as err:
        return jsonify(err.messages), 400
