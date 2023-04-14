from flask import request, session, jsonify, Response
from flask_jwt_extended import jwt_required, get_current_user
from exceptions.invalidParameterException import InvalidParameterException
from infrastructure.database.database import Database
from infrastructure.database.user_database import UserDatabase
from . import get_user_infos_bp


@get_user_infos_bp.route("/user_infos", methods=["GET"])
@jwt_required()
def get_user_infos() -> (Response, int):
    user_id: int = get_current_user()
    user_database: UserDatabase = UserDatabase()

    customer: dict = user_database.get_user("customers", user_id)
    if customer is not None:
        return jsonify(customer), 200

    seller: dict = user_database.get_user("sellers", user_id)
    if seller is not None:
        return jsonify(seller), 200

    admin: dict = user_database.get_user("admins", user_id)
    if admin is not None:
        return jsonify(admin), 200

    raise InvalidParameterException("Le ID de l'utilisateur est invalide")
