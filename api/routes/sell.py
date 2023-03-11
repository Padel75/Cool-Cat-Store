from flask import request, session, jsonify
from . import sell_bp
from domain.factories.product_factory import ProductFactory
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.missingParameterException import MissingParameterException
from exceptions.invalidParameterException import InvalidParameterException


@sell_bp.route("/sell/<vendor_id>", methods=["POST"])
def sell(vendor_id):
    vendor_id = int(vendor_id)
    sell_infos = request.get_json()

    for key in ["name", "description", "price", "category_id"]:
        if key not in sell_infos:
            raise MissingParameterException(f"{key} est manquant")

    __validate_vendor_id(vendor_id)
    __validate_vendor_is_logged_in(vendor_id)

    product_infos = {
        "name": sell_infos["name"],
        "description": sell_infos["description"],
        "price": sell_infos["price"],
        "category_id": sell_infos["category_id"],
        "vendor_id": vendor_id,
    }

    product_factory = ProductFactory()
    product = product_factory.create_product(product_infos)
    database = ProductDatabase()
    product_id = database.create_product(product)

    response = {"product_id": product_id}

    return jsonify(response), 201


def __validate_vendor_id(vendor_id: int) -> None:
    database = UserDatabase()
    vendor = database.get_user("vendors", vendor_id)
    if vendor is None:
        raise InvalidParameterException("Le ID du vendeur est invalide")
    return


def __validate_vendor_is_logged_in(vendor_id: int) -> None:
    if session.get("id") != vendor_id:
        raise InvalidParameterException(
            "Vous devez vous connecter pour vendre un produit"
        )
    return
