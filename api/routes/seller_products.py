from flask import jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import seller_products_bp
from infrastructure.database.product_database import ProductDatabase
from exceptions.invalidParameterException import InvalidParameterException


@seller_products_bp.route("/seller/products", methods=["GET"])
@jwt_required
def get_seller_products() -> tuple[Response, int]:
    seller_id: int = get_jwt_identity()
    database: ProductDatabase = ProductDatabase()
    products_id: list = database.get_seller_products_id(seller_id)

    seller_products: list = [
        database.get_product(product_id[0]) for product_id in products_id
    ]

    return jsonify(seller_products), 200
