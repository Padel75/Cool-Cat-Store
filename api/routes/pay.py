from flask import request, jsonify, Response
from flask_jwt_extended import jwt_required, get_current_user
from . import pay_bp

from infrastructure.database.payment_database import PaymentDatabase
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@pay_bp.route("/pay", methods=["POST"])
@jwt_required()
def pay() -> (Response, int):
    product_database: ProductDatabase = ProductDatabase()
    payment_database: PaymentDatabase = PaymentDatabase()

    customer_id: int = get_current_user()
    __validate_customer_id(customer_id)

    cart_id: int = product_database.get_cart_id(customer_id)

    is_paid = payment_database.pay(cart_id, customer_id)

    if is_paid:
        response: dict[str, int] = {
            "user_id": customer_id,
            "cart_id": cart_id,
        }
        return jsonify(response), 201
    else:
        response: dict[str, int] = {
            "user_id": customer_id,
            "cart_id": cart_id,
        }
        return jsonify(response), 400


def __validate_customer_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user: dict = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return
