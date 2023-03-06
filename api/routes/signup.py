from flask import request, jsonify
from . import signup_bp
from domain.services.user_service import UserService
from domain.models.customer import Customer
from api.exceptions.missingParameterException import MissingParameterException

@signup_bp.route("/signup", methods=['POST'])
def signup():

    signup_infos = request.get_json()

    for key in ["username", "password", "first_name", "last_name", "address", "phone_number", "email"]:
        if key not in signup_infos:
            raise MissingParameterException(f"{key} est manquant")

    #Reste à voir les validations à faire ici
    username = signup_infos["username"]
    password = signup_infos["password"]
    first_name = signup_infos["first_name"]
    last_name = signup_infos["last_name"]
    address = signup_infos["address"]
    phone_number = signup_infos["phone_number"]
    email = signup_infos["email"]
    customer = Customer(username, password, first_name, last_name, address, phone_number, email)

    user_service = UserService()
    user_id = user_service.create_customer(customer)

    response = {
        "user_id": user_id
    }

    return jsonify(response), 201


