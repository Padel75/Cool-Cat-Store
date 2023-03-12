from flask import request, session, jsonify
from . import get_cart_bp
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@get_cart_bp.route("/get_cart/<customer_id>", methods=["GET"])
def get_cart(customer_id):
    customer_id = int(customer_id)
    __validate_user_id(customer_id)
    __validate_user_is_logged_in(customer_id)
    database = ProductDatabase()
    cart = database.get_cart(customer_id)
    response = {"user_id": customer_id, "cart": cart}
    return jsonify(response), 200


def __validate_user_id(user_id: int) -> None:
    database = UserDatabase()
    user = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return


def __validate_user_is_logged_in(user_id: int) -> None:
    if session.get("id") != user_id:
        raise InvalidParameterException(
            "Vous devez vous connecter pour obtenir un panier"
        )
    return
