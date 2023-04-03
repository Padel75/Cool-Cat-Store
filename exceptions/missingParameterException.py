class MissingParameterException(Exception):
    """Exception raised for missing parameters."""

    status_code: int = 400

    def __init__(self, message: str) -> None:
        self.message: str = message
