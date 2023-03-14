from flask import jsonify

from . import products_filtered_bp
from infrastructure.database.product_database import ProductDatabase


@products_filtered_bp.route("/product_filtered/<search_filter>", methods=["GET"])
def get_products_filtered(search_filter: str):
    database: ProductDatabase = ProductDatabase()
    products: list = database.get_products_filtered(search_filter)

    return jsonify(products), 200
