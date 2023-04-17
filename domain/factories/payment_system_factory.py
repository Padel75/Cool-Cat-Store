from datetime import datetime

from domain.models.payment_system import PaymentSystem
import bcrypt

from exceptions.invalidParameterException import InvalidParameterException


class PaymentSystemFactory:
    def create_payment_system(self, payment_system_infos: {}) -> PaymentSystem:
        customer_id = payment_system_infos["customer_id"]
        payment_type = payment_system_infos["payment_type"]
        number = payment_system_infos["number"]
        expiration_date = payment_system_infos["expiration_date"]
        cvv = payment_system_infos["cvv"]

        self.__validate(payment_type, number, expiration_date, cvv)

        payment_system: PaymentSystem = PaymentSystem(
            customer_id,
            payment_type,
            number,
            expiration_date,
            cvv,
        )

        return payment_system

    def __validate_payment_type(self, payment_type: str) -> None:
        if payment_type not in ["VISA", "MASTERCARD", "AMEX"]:
            raise InvalidParameterException("Le type de carte de crédit est invalide")
        return

    def __validate_number(self, number: int) -> None:
        if len(str(number)) != 16:
            raise InvalidParameterException("Le numéro de carte de crédit est invalide")
        return

    def __validate_expiration_date(self, date: str) -> None:
        """Format: YYYY-MM-DD"""
        try:
            expiration_date: datetime = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise InvalidParameterException("La date d'expiration est invalide")
        if expiration_date < datetime.now():
            raise InvalidParameterException("La date d'expiration est invalide")
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
