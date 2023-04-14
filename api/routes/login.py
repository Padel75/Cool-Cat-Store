from flask import request, jsonify, Response
import bcrypt
from flask_jwt_extended import create_access_token
from . import login_bp
from infrastructure.database.user_database import UserDatabase
from exceptions.missingParameterException import MissingParameterException
from exceptions.invalidParameterException import InvalidParameterException


@login_bp.route("/login", methods=["POST"])
def login() -> (Response, int):
    login_infos = request.get_json()

    for key in ["username", "password"]:
        if key not in login_infos:
            raise MissingParameterException(f"{key} est manquant")

    username = login_infos["username"]
    password = login_infos["password"]

    __validate_user_password(username, password)

    database: UserDatabase = UserDatabase()
    user_id: int = database.get_user_id(username)
    identity: dict = {
        "id": user_id,
        "username": username,
        "password": password,
    }
    token = create_access_token(identity=identity)
    role: str = database.get_user_role(user_id)

    response: Response = jsonify({"access_token": token, "role": role})
    return response, 200


def __validate_user_password(username: str, password: str) -> None:
    database: UserDatabase = UserDatabase()
    encrypted_password: str = database.get_user_password(username)

    if encrypted_password is None:
        raise InvalidParameterException("username est invalide")

    is_password_valid: bool = bcrypt.checkpw(
        password.encode("utf-8"), encrypted_password.encode("utf-8")
    )
    if not is_password_valid:
        raise InvalidParameterException("password est invalide")

    return
