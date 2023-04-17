from datetime import datetime

from exceptions.invalidParameterException import InvalidParameterException


class PaymentSystem:
    def __init__(
        self,
        customer_id: int,
        payment_type: str,
        number: str,
        expiration_date: str,
        cvv: str,
    ):
        self.customer_id: int = customer_id
        self.payment_type: str = payment_type
        self.number: str = number
        self.expiration_date: str = expiration_date
        self.cvv: str = cvv

    def get_payment_type(self) -> str:
        return self.payment_type

    def get_number(self) -> str:
        return self.number

    def get_expiration_date(self) -> str:
        return self.expiration_date

    def get_cvv(self) -> str:
        return self.cvv

    def get_customer_id(self) -> int:
        return self.customer_id
