from flask import request, session, jsonify, Response

from exceptions.invalidParameterException import InvalidParameterException
from infrastructure.database.database import Database
from infrastructure.database.user_database import UserDatabase
from . import get_user_infos_bp


@get_user_infos_bp.route("/user_infos/<user_id>", methods=["GET"])
def get_user_infos(user_id: str) -> (Response, int):
    user_id: int = int(user_id)
    user_database: UserDatabase = UserDatabase()

    customer: tuple = user_database.get_user("customers", user_id)
    if customer is not None:
        return jsonify(customer), 200

    vendor: tuple = user_database.get_user("vendors", user_id)
    if vendor is not None:
        return jsonify(vendor), 200

    admin: tuple = user_database.get_user("admins", user_id)
    if admin is not None:
        return jsonify(admin), 200

    raise InvalidParameterException("Le ID de l'utilisateur est invalide")
