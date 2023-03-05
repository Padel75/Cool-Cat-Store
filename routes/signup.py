from flask import render_template, request, jsonify
from . import signup_bp
from database import Database
from exceptions.missingParameterException import MissingParameterException

@signup_bp.route("/signup", methods=['POST'])
def signup():

    database = Database()

    signup_infos = request.get_json()

    for key in ["username", "password", "first_name", "last_name", "address", "phone_number", "email"]:
        if key not in signup_infos:
            raise MissingParameterException(key)

    #Reste à voir les validations à faire ici

    user_info = {
        "username": signup_infos["username"],
        "password": signup_infos["password"], #Peut-être à sécuriser
        "first_name": signup_infos["first_name"],
        "last_name": signup_infos["last_name"],
        "address": signup_infos["address"],
        "phone_number": signup_infos["phone_number"],
        "email": signup_infos["email"]
    }

    user_id = database.create_customer(user_info)

    response = {
        "user_id": user_id
    }

    return jsonify(response), 201


