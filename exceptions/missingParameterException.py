class MissingParameterException(Exception):
    """Exception raised for missing parameters."""

    status_code = 400

    def __init__(self, message: str):
        self.message = message
