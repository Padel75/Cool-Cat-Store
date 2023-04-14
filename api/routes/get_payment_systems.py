from flask import request, jsonify, Response
from flask_jwt_extended import get_jwt_identity

from infrastructure.database.payment_database import PaymentDatabase
from . import get_payment_systems_bp
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@get_payment_systems_bp.route("/get_payment_systems/", methods=["GET"])
def get_payment_system() -> (Response, int):
    customer_id: int = get_jwt_identity()
    __validate_customer_id(customer_id)

    database: PaymentDatabase = PaymentDatabase()
    payment_systems: list = database.get_payment_systems(customer_id)

    return jsonify(payment_systems), 200


def __validate_customer_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user: dict = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return
