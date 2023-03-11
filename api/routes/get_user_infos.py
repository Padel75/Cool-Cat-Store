from flask import request, session, jsonify

from infrastructure.database.database import Database
from infrastructure.database.user_database import UserDatabase
from . import get_user_infos_bp


@get_user_infos_bp.route("/get_user_infos/<user_id>", methods=["GET"])
def get_user_infos(user_id):
    user_database: UserDatabase = UserDatabase()

    customer = user_database.get_user("customers", user_id)
    if customer is not None:
        return jsonify(customer), 200

    vendor = user_database.get_user("vendors", user_id)
    if vendor is not None:
        return jsonify(vendor), 200

    admin = user_database.get_user("admins", user_id)
    if admin is not None:
        return jsonify(admin), 200

    return jsonify({"error": "User not found"}), 404
