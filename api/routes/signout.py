from flask import render_template, request, jsonify, session, Response
from . import signout_bp


@signout_bp.route("/signout", methods=["DELETE"])
def signout() -> Response:
    user_signed_out_id = session.get("id")
    session.clear()
    response = {"user_id": user_signed_out_id}

    return jsonify(response)
