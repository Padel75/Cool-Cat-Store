from flask import request, jsonify, Response
from flask_jwt_extended import get_current_user, jwt_required
from . import add_payment_system_bp

from domain.models.payment_system import PaymentSystem
from domain.factories.payment_system_factory import PaymentSystemFactory

from infrastructure.database.payment_database import PaymentDatabase
from infrastructure.database.user_database import UserDatabase
from exceptions.invalidParameterException import InvalidParameterException


@add_payment_system_bp.route("/add_payment_system", methods=["POST"])
@jwt_required()
def add_payment_system() -> (Response, int):
    payment_infos = request.get_json()

    customer_id: int = get_current_user()
    __validate_customer_id(customer_id)
    payment_infos["customer_id"] = customer_id

    factory: PaymentSystemFactory = PaymentSystemFactory()
    payment_system: PaymentSystem = factory.create_payment_system(payment_infos)

    database: PaymentDatabase = PaymentDatabase()
    payment_id: int = database.create_payment_system(payment_system)
    return jsonify({"payment_id": payment_id}), 201


def __validate_customer_id(user_id: int) -> None:
    database: UserDatabase = UserDatabase()
    user: dict = database.get_user("customers", user_id)
    if user is None:
        raise InvalidParameterException("Le ID du client est invalide")
    return
