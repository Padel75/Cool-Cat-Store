from flask import request, jsonify
from . import signup_bp
from domain.factories.user_factory import UserFactory
from infrastructure.database import Database
from api.exceptions.missingParameterException import MissingParameterException

@signup_bp.route("/signup", methods=['POST'])
def signup():

    signup_infos = request.get_json()

    for key in ["username", "password", "first_name", "last_name", "address", "phone_number", "email"]:
        if key not in signup_infos:
            raise MissingParameterException(f"{key} est manquant")

    customer_infos = {
        "username": signup_infos["username"],
        "password": signup_infos["password"],
        "first_name": signup_infos["first_name"],
        "last_name": signup_infos["last_name"],
        "address": signup_infos["address"],
        "phone_number": signup_infos["phone_number"],
        "email": signup_infos["email"]
    }

    user_factory = UserFactory()
    customer = user_factory.create_customer(customer_infos)
    database = Database()
    user_id = database.create_customer(customer)

    response = {
        "user_id": user_id
    }

    return jsonify(response), 201


