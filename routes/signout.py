from flask import render_template, request, jsonify
from . import signout_bp

@signout_bp.route("/signout", methods=['POST'])
def signout():
    response = {
        "status": 200
    }

    return jsonify(response)