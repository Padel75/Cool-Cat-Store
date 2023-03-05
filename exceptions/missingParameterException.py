
class MissingParameterException(Exception):
    """Exception raised for missing parameters."""
    status_code = 400
    def __init__(self, missing_parameter: str):
        self.message = missing_parameter + " est manquant."
