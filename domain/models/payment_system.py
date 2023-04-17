from datetime import datetime

from exceptions.invalidParameterException import InvalidParameterException


class PaymentSystem:
    def __init__(
        self,
        customer_id: int,
        payment_type: str,
        number: int,
        expiration_date: str,
        cvv: int,
    ):
        self.__validate(payment_type, number, expiration_date, cvv)
        self.customer_id: int = customer_id
        self.payment_type: str = payment_type
        self.number: int = number
        self.expiration_date: str = expiration_date
        self.cvv: int = cvv

    def get_payment_type(self) -> str:
        return self.payment_type

    def get_number(self) -> int:
        return self.number

    def get_expiration_date(self) -> str:
        return self.expiration_date

    def get_cvv(self) -> int:
        return self.cvv

    def get_customer_id(self) -> int:
        return self.customer_id

    def __validate_payment_type(self, payment_type: str) -> None:
        if payment_type not in ["Visa", "Mastercard", "American Express"]:
            raise InvalidParameterException("Le type de carte de crédit est invalide")
        return

    def __validate_number(self, number: int) -> None:
        if len(str(number)) != 16:
            raise InvalidParameterException("Le numéro de carte de crédit est invalide")
        return

    def __validate_expiration_date(self, date: str) -> None:
        """Format: YYYY-MM-DD"""
        if len(date) != 10:
            if date[4] != "-" or date[7] != "-":
                raise InvalidParameterException(
                    "La date d'expiration est invalide. Format: YYYY-MM-DD"
                )
            if int(date[5:7]) > 12:
                raise InvalidParameterException(
                    "La date d'expiration est invalide. Format: YYYY-MM-DD"
                )
            if int(date[8:10]) > 31:
                raise InvalidParameterException(
                    "La date d'expiration est invalide. Format: YYYY-MM-DD"
                )
            if int(date[0:4]) < datetime.now().year:
                raise InvalidParameterException(
                    "La date d'expiration est invalide. Format: YYYY-MM-DD"
                )
        return

    def __validate_cvv(self, cvv: int) -> None:
        if len(str(cvv)) != 3:
            raise InvalidParameterException("Le CVV est invalide")
        return

    def __validate(
        self, type: str, number: int, expiration_date: str, cvv: int
    ) -> None:
        self.__validate_payment_type(type)
        self.__validate_number(number)
        self.__validate_expiration_date(expiration_date)
        self.__validate_cvv(cvv)
        return
