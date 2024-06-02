from marshmallow import fields
from schemas import ma

# Define the Customer schema
class UserSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    role = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

    # class Meta:
    #     fields = ("id", "name", "email", "phone", "username")

# Create instances of the schema
user_input_schema = UserSchema()
user_output_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(many=True, exclude=["password"])
user_login_schema = UserSchema(only=["username", "password"])