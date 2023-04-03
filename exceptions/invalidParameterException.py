class InvalidParameterException(Exception):
    """Exception raised for invalid parameters."""

    status_code: int = 400

    def __init__(self, message: str) -> None:
        self.message: str = message
