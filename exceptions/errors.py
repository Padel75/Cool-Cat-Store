"""Application error handlers."""
from flask import jsonify
from . import errors_bp


@errors_bp.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code if hasattr(error, "status_code") else 500
    success = False
    response = {
        "success": success,
        "error": {"type": error.__class__.__name__, "message": message},
    }

    return jsonify(response), status_code
