from flask import render_template, request, jsonify
from . import signup_bp

@signup_bp.route("/signup", methods=['POST'])
def signup():
    response = {
        "status": 200
    }

    return jsonify(response)


