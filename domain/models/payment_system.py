from exceptions.invalidParameterException import InvalidParameterException


class PaymentSystem:
    def __init__(
        self, customer_id: int, type: str, number: int, expiration_date: str, cvv: int
    ):
        self.__validate(type, number, expiration_date, cvv)

        self.type: str = type
        self.number: int = number
        self.expiration_date: str = expiration_date
        self.cvv: int = cvv

    def get_type(self) -> str:
        return self.type

    def get_number(self) -> int:
        return self.number

    def get_expiration_date(self) -> str:
        return self.expiration_date

    def get_cvv(self) -> int:
        return self.cvv

    def __validate_type(self, type: str) -> None:
        if type not in ["Visa", "Mastercard", "American Express"]:
            raise InvalidParameterException("Le type de carte de crédit est invalide")
        return

    def __validate_number(self, number: int) -> None:
        if len(str(number)) != 16:
            raise InvalidParameterException("Le numéro de carte de crédit est invalide")
        return

    def __validate_expiration_date(self, date: str) -> None:
        if len(date) != 5:
            raise InvalidParameterException("La date d'expiration est invalide")
        return

    def __validate_cvv(self, cvv: int) -> None:
        if len(str(cvv)) != 3:
            raise InvalidParameterException("Le CVV est invalide")
        return

    def __validate(
        self, type: str, number: int, expiration_date: str, cvv: int
    ) -> None:
        self.__validate_type(type)
        self.__validate_number(number)
        self.__validate_expiration_date(expiration_date)
        self.__validate_cvv(cvv)
        return
