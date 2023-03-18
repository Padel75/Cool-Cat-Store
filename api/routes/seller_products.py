from typing import Tuple

from flask import jsonify, Response
from . import seller_products_bp
from infrastructure.database.product_database import ProductDatabase
from exceptions.invalidParameterException import InvalidParameterException


@seller_products_bp.route("/seller/<seller_id>/products", methods=["GET"])
def get_seller_products(seller_id: str) -> tuple[Response, int]:
    database: ProductDatabase = ProductDatabase()
    products_id: list = database.get_seller_products_id(int(seller_id))

    seller_products: list = [
        database.get_product(product_id[0]) for product_id in products_id
    ]

    return jsonify(seller_products), 200
