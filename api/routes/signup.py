from flask import request, jsonify, Response
import secrets
from domain.models.customer import Customer
from domain.models.seller import Seller
from . import signup_bp
from domain.factories.user_factory import UserFactory
from infrastructure.database.user_database import UserDatabase
from exceptions.missingParameterException import MissingParameterException


@signup_bp.route("/signup/customer", methods=["POST"])
def signup_customer() -> (Response, int):
    signup_infos = request.get_json()

    for key in [
        "username",
        "password",
        "first_name",
        "last_name",
        "address",
        "phone_number",
        "email",
    ]:
        if key not in signup_infos:
            raise MissingParameterException(f"{key} est manquant")

    customer_infos = {
        "username": signup_infos["username"],
        "password": signup_infos["password"],
        "first_name": signup_infos["first_name"],
        "last_name": signup_infos["last_name"],
        "address": signup_infos["address"],
        "phone_number": signup_infos["phone_number"],
        "email": signup_infos["email"],
    }

    user_factory: UserFactory = UserFactory()
    customer: Customer = user_factory.create_customer(customer_infos)
    database: UserDatabase = UserDatabase()
    user_id: int = secrets.randbits(16)
    while database.get_user("humans", user_id) is not None:
        user_id = secrets.randbits(16)
    database.create_customer(customer, user_id)

    response: dict[str, int] = {"user_id": user_id}

    return jsonify(response), 201


@signup_bp.route("/signup/seller", methods=["POST"])
def signup_seller() -> (Response, int):
    signup_infos = request.get_json()

    for key in [
        "username",
        "password",
        "name",
        "description",
        "address",
        "phone_number",
        "email",
    ]:
        if key not in signup_infos:
            raise MissingParameterException(f"{key} est manquant")

    seller_infos = {
        "username": signup_infos["username"],
        "password": signup_infos["password"],
        "name": signup_infos["name"],
        "description": signup_infos["description"],
        "address": signup_infos["address"],
        "phone_number": signup_infos["phone_number"],
        "email": signup_infos["email"],
    }

    user_factory: UserFactory = UserFactory()
    seller: Seller = user_factory.create_seller(seller_infos)
    database: UserDatabase = UserDatabase()
    user_id: int = secrets.randbits(16)
    while database.get_user("humans", user_id) is not None:
        user_id = secrets.randbits(16)
    database.create_seller(seller, user_id)

    response: dict[str, int] = {"user_id": user_id}

    return jsonify(response), 201
