from flask import request, session, jsonify, Response
from . import add_to_cart_bp
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@add_to_cart_bp.route("/add_to_cart/<customer_id>/<product_id>", methods=["POST"])
def add_to_cart(customer_id: str, product_id: str) -> (Response, int):
    quantity = request.get_json()["quantity"]
    customer_id: int = int(customer_id)
    product_id: int = int(product_id)

    __validate_user_id(customer_id)
    __validate_product_id(product_id)
    __validate_user_is_logged_in(customer_id)

    database: ProductDatabase = ProductDatabase()
    cart_id: int = database.add_product_to_cart(product_id, customer_id, quantity)
    response: dict[str, int] = {
        "user_id": customer_id,
        "product_id": product_id,
        "cart_id": cart_id,
    }
    return jsonify(response), 201


def __validate_user_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user: tuple = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return


def __validate_product_id(product_id: int) -> None:
    database: ProductDatabase = ProductDatabase()
    product: tuple = database.get_product(product_id)
    if product is None:
        raise InvalidParameterException("Le ID du produit est invalide")
    return


def __validate_user_is_logged_in(user_id: int) -> None:
    if session.get("id") != user_id:
        raise InvalidParameterException(
            "Vous devez vous connecter pour ajouter un produit au panier"
        )
    return
