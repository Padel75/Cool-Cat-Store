from flask import jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import get_cart_bp
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@get_cart_bp.route("/cart", methods=["GET"])
@jwt_required()
def get_cart() -> (Response, int):
    customer_id: int = get_jwt_identity()
    __validate_user_id(customer_id)

    database: ProductDatabase = ProductDatabase()
    cart: list = database.get_cart(customer_id)
    response: dict[str, list] = {"user_id": customer_id, "cart": []}

    for product in cart:
        response["cart"].append(
            {"product": database.get_product(product[0]), "quantity": product[1]}
        )

    return jsonify(response), 200


def __validate_user_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user: tuple = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return
