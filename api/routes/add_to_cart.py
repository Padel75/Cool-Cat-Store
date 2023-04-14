from flask import request, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import add_to_cart_bp
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@add_to_cart_bp.route("/add_to_cart/<product_id>", methods=["POST"])
@jwt_required()
def add_to_cart(product_id: str) -> (Response, int):
    quantity: str = request.get_json()["quantity"]
    product_id: int = int(product_id)
    customer_id: int = get_jwt_identity()

    __validate_customer_id(customer_id)
    __validate_product_id(product_id)

    database: ProductDatabase = ProductDatabase()
    cart_id: int = database.add_product_to_cart(product_id, customer_id, quantity)
    response: dict[str, int] = {
        "user_id": customer_id,
        "product_id": product_id,
        "cart_id": cart_id,
    }
    return jsonify(response), 201


def __validate_customer_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user: dict = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return


def __validate_product_id(product_id: int) -> None:
    database: ProductDatabase = ProductDatabase()
    product: tuple = database.get_product(product_id)
    if product is None:
        raise InvalidParameterException("Le ID du produit est invalide")
    return
