from flask import jsonify, Response
from . import seller_products_bp
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@seller_products_bp.route("/seller/<seller_id>/products", methods=["GET"])
def get_seller_products(seller_id: int) -> tuple[Response, int]:
    __validate_seller_id(seller_id)
    database: ProductDatabase = ProductDatabase()
    products_id: list = database.get_seller_products_id(seller_id)

    seller_products: list = [
        database.get_product(product_id[0]) for product_id in products_id
    ]

    return jsonify(seller_products), 200


def __validate_seller_id(seller_id: int) -> None:
    database: UserDatabase = UserDatabase()
    seller: dict = database.get_user("sellers", seller_id)

    if seller is None:
        raise InvalidParameterException("Le ID du vendeur est invalide")
    return
