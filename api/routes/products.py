from flask import jsonify, Response
from . import products_bp
from infrastructure.database.product_database import ProductDatabase
from exceptions.invalidParameterException import InvalidParameterException


@products_bp.route("/products", methods=["GET"])
def get_products() -> (Response, int):
    database: ProductDatabase = ProductDatabase()
    products: list = database.get_products()

    return jsonify(products), 200


@products_bp.route("/products/<product_id>", methods=["GET"])
def get_product(product_id: str) -> (Response, int):
    product_id: int = int(product_id)
    database: ProductDatabase = ProductDatabase()
    product: tuple = database.get_product(product_id)

    if product is None:
        raise InvalidParameterException("Le ID du produit est invalide")

    return jsonify(product), 200
