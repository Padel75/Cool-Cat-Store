from flask import render_template, request, session, redirect, url_for, jsonify
from database import Database
from exceptions.missingParameterException import MissingParameterException
from exceptions.invalidParameterException import InvalidParameterException
from . import login_bp

@login_bp.route("/login", methods=['POST'])
def login():
    database = Database()
    login_infos = request.get_json()
    for key in ["username", "password"]:
        if key not in login_infos:
            raise MissingParameterException(key)
    username = login_infos["username"]
    password = login_infos["password"]

    if not __check_credentials(username, password):
        raise InvalidParameterException("username ou password")

    user_id = database.get_user_id(username)
    session['logged_in'] = True
    session['id'] = user_id

    response = {
        "user_id": user_id
    }
    return jsonify(response), 200

def __check_credentials(username, password):
    database = Database()
    validPassword = database.get_user_password(username)
    if validPassword is None:
        return False
    return validPassword == password #À sécuriser


