from flask import request, session, jsonify, Response
from exceptions.invalidParameterException import InvalidParameterException
from infrastructure.database.user_database import UserDatabase
from . import get_user_infos_bp


@get_user_infos_bp.route("/seller/<seller_id>", methods=["GET"])
def get_public_seller(seller_id: int) -> (Response, int):
    user_database: UserDatabase = UserDatabase()
    seller: dict = user_database.get_user("sellers", seller_id)
    if seller is not None:
        response: dict = {
            "name": seller["name"],
            "description": seller["description"],
        }
        return jsonify(response), 200
    raise InvalidParameterException("Le ID du vendeur est invalide")
