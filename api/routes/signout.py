from flask import jsonify, Response, current_app
from flask_jwt_extended import (
    get_jwt,
    jwt_required,
)

from . import signout_bp


@signout_bp.route("/signout", methods=["DELETE"])
@jwt_required()
def signout() -> (Response, int):
    token_revoked = get_jwt()["jti"]
    token_manager = current_app.config["TOKEN_MANAGER"]
    token_manager.add_token_to_blocklist(token_revoked)

    response: Response = jsonify({"msg": "User successfully signed out"})
    return response, 200
