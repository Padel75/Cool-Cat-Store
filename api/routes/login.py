from flask import request, session, jsonify
from domain.services.user_service import UserService
from api.exceptions.missingParameterException import MissingParameterException
from . import login_bp

@login_bp.route("/login", methods=['POST'])
def login():
    login_infos = request.get_json()
    for key in ["username", "password"]:
        if key not in login_infos:
            raise MissingParameterException(f"{key} est manquant")
    username = login_infos["username"]
    password = login_infos["password"]

    user_sevice = UserService()
    user_sevice.validate_user_password(username, password)

    user_id = user_sevice.get_user_id(username)
    session['logged_in'] = True
    session['id'] = user_id

    response = {
        "user_id": user_id
    }
    return jsonify(response), 200
