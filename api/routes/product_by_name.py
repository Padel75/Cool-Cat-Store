from flask import jsonify

from exceptions.invalidParameterException import InvalidParameterException
from . import products_by_name_bp
from infrastructure.database.product_database import ProductDatabase


@products_by_name_bp.route("/product_by_name/<name>", methods=["GET"])
def get_products_by_name(name: str):
    database: ProductDatabase = ProductDatabase()
    products: list = database.get_products()
    product = [product for product in products if product["name"] == name][0]

    if product is None:
        raise InvalidParameterException("Le ID du produit est invalide")

    return jsonify(product), 200
