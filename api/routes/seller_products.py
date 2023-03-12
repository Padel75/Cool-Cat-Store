from typing import Tuple

from flask import jsonify, Response
from . import seller_products_bp
from infrastructure.database.product_database import ProductDatabase
from exceptions.invalidParameterException import InvalidParameterException


@seller_products_bp.route("/seller/<seller_id>/products", methods=["GET"])
def get_seller_products(seller_id: str) -> tuple[Response, int]:
    database: ProductDatabase = ProductDatabase()
    products: list = database.get_products()
    products_id: list = database.get_seller_products_id(seller_id)
    seller_products: list = [
        product for product in products if product["id"] in products_id
    ]
    return jsonify(seller_products), 200
