
class InvalidParameterException(Exception):
    """Exception raised for invalid parameters."""
    status_code = 400
    def __init__(self, message: str):
        self.message = message
