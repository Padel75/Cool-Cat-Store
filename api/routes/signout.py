from flask import jsonify, Response, current_app
from flask_jwt_extended import (
    get_jwt,
    get_jwt_identity,
    jwt_required,
)

from . import signout_bp


@signout_bp.route("/signout", methods=["DELETE"])
@jwt_required()
def signout() -> Response:
    token_revoked = get_jwt()["jti"]
    token_manager = current_app.config["TOKEN_MANAGER"]
    token_manager.add_token_to_blocklist(token_revoked)

    user_signed_out_id = get_jwt_identity()
    response = {"user_id": user_signed_out_id}
    return jsonify(response), 200
