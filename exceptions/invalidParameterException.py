
class InvalidParameterException(Exception):
    """Exception raised for invalid parameters."""
    status_code = 400
    def __init__(self, invalid_parameter: str):
        self.message = invalid_parameter + " est invalide."
