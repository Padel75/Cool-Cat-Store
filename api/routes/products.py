from flask import jsonify
from . import products_bp
from infrastructure.database.product_database import ProductDatabase
from exceptions.invalidParameterException import InvalidParameterException

@products_bp.route("/products", methods=['GET'])
def get_products():
    database = ProductDatabase()
    products = database.get_products()
    return jsonify(products), 200

@products_bp.route("/products/<product_id>", methods=['GET'])
def get_product(product_id):
    product_id = int(product_id)
    database = ProductDatabase()
    product = database.get_product(product_id)
    if product is None:
        raise InvalidParameterException("Le ID du produit est invalide")
    return jsonify(product), 200
