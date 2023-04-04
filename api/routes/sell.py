from flask import request, jsonify, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from domain.models.product import Product
from . import sell_bp
from domain.factories.product_factory import ProductFactory
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.missingParameterException import MissingParameterException
from exceptions.invalidParameterException import InvalidParameterException


@sell_bp.route("/sell", methods=["POST"])
@jwt_required()
def sell() -> (Response, int):
    seller_id: int = get_jwt_identity()
    sell_infos: dict = request.get_json()

    for key in ["name", "description", "price", "category_id"]:
        if key not in sell_infos:
            raise MissingParameterException(f"{key} est manquant")

    __validate_seller_id(seller_id)

    product_infos: dict[str, str | int] = {
        "name": sell_infos["name"],
        "description": sell_infos["description"],
        "price": sell_infos["price"],
        "category_id": sell_infos["category_id"],
        "seller_id": seller_id,
    }

    product_factory: ProductFactory = ProductFactory()
    product: Product = product_factory.create_product(product_infos)
    database: ProductDatabase = ProductDatabase()
    product_id: int = database.create_product(product)

    response: dict[str, int] = {"product_id": product_id}

    return jsonify(response), 201


def __validate_seller_id(seller_id: int) -> None:
    database: UserDatabase = UserDatabase()
    seller: tuple = database.get_user("sellers", seller_id)

    if seller is None:
        raise InvalidParameterException("Le ID du vendeur est invalide")
    return
