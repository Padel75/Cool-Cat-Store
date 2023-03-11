from flask import request, session, jsonify
import bcrypt
from . import login_bp
from infrastructure.database.user_database import UserDatabase
from exceptions.missingParameterException import MissingParameterException
from exceptions.invalidParameterException import InvalidParameterException


@login_bp.route("/login", methods=["POST"])
def login():
    login_infos = request.get_json()
    for key in ["username", "password"]:
        if key not in login_infos:
            raise MissingParameterException(f"{key} est manquant")
    username = login_infos["username"]
    password = login_infos["password"]

    __validate_user_password(username, password)

    database = UserDatabase()
    user_id = database.get_user_id(username)
    session["logged_in"] = True
    session["id"] = user_id

    response = {"user_id": user_id}
    return jsonify(response), 200


def __validate_user_password(username: str, password: str) -> None:
    database = UserDatabase()
    encrypted_password = database.get_user_password(username)
    if encrypted_password is None:
        raise InvalidParameterException("username est invalide")

    is_password_valid = bcrypt.checkpw(
        password.encode("utf-8"), encrypted_password.encode("utf-8")
    )
    if not is_password_valid:
        raise InvalidParameterException("password est invalide")

    return
