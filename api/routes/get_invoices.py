from flask import jsonify, Response
from flask_jwt_extended import jwt_required, get_current_user

from infrastructure.database.payment_database import PaymentDatabase
from . import get_cart_bp, get_invoices_bp
from infrastructure.database.product_database import ProductDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@get_invoices_bp.route("/invoices", methods=["GET"])
@jwt_required()
def get_invoices() -> (Response, int):
    customer_id: int = get_current_user()
    __validate_user_id(customer_id)

    database: PaymentDatabase = PaymentDatabase()

    invoices: list = database.get_invoices(customer_id)

    response: dict[str, list] = {
        "user_id": customer_id,
        "invoices": [],
    }

    for invoice in invoices:
        response["invoices"].append(invoice)

    return jsonify(response), 200


def __validate_user_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return
