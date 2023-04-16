from flask import request, jsonify, Response
from flask_jwt_extended import get_jwt_identity

from domain.models.payment_system import PaymentSystem
from infrastructure.database.payment_database import PaymentDatabase
from . import add_payment_system_bp
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@add_payment_system_bp.route("/add_payment_system", methods=["POST"])
def add_payment_system() -> (Response, int):
    payment_infos = request.get_json()

    customer_id: int = get_jwt_identity()
    __validate_customer_id(customer_id)

    type: str = payment_infos["type"]
    number: int = payment_infos["number"]
    expiration_date: str = payment_infos["expiration_date"]
    cvv: int = payment_infos["cvv"]

    payment_system: PaymentSystem = PaymentSystem(
        customer_id, type, number, expiration_date, cvv
    )

    database: PaymentDatabase = PaymentDatabase()


def __validate_customer_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user: dict = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return
