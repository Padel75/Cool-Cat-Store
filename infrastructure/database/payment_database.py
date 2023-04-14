from typing import Any, List, Dict

from domain.models.payment_system import PaymentSystem
from infrastructure.database.database import Database


class PaymentDatabase(Database):
    def create_payment_system(self, payment_system: PaymentSystem) -> int:
        customer_id: int = payment_system.get_customer_id()
        number: int = payment_system.get_number()
        date: str = payment_system.get_expiration_date()
        cvv: int = payment_system.get_cvv()
        type_system: str = payment_system.get_type()

        payment_id: int = self.__add_payment_system(
            customer_id, type_system, number, date, cvv
        )

        return payment_id

    def get_payment_systems(self, customer_id: int) -> list[dict[str, Any]] | None:
        query: str = f"SELECT payment_system_id FROM customer_own_payment_system WHERE customer_id = {customer_id}"
        payment_systems: list = self.select_all_query(query)

        if payment_systems is None:
            return None

        payment_systems_dto: list[dict[str, Any]] = []
        for payment_system in payment_systems:
            payment_systems_dto.append(self.get_payment_system(payment_system[0]))

        return payment_systems_dto

    def __add_payment_system(
        self, customer_id: int, number: int, date: str, cvv: int, payment_type: str
    ) -> int:
        query: str = "INSERT INTO payment_systems (payment_type, number, expiration_date, cvv) VALUES (%s, %s, %s, %s)"
        values: tuple = (payment_type, number, date, cvv)
        payment_id: int = self.insert_query(query, values)

        query: str = "INSERT INTO customers_has_payment_systems (customer_id, payment_system_id) VALUES (%s, %s)"
        values: tuple = (customer_id, payment_id)

        return payment_id

    def get_payment_system(self, payment_id: int) -> dict[str, Any] | None:
        query: str = "SELECT * FROM payment_systems WHERE id = %s"
        values: tuple = (payment_id,)
        payment: tuple = self.select_one_query(query, values)

        if payment is None:
            return None

        payment_dto: dict[str, Any] = {
            "id": payment[0],
            "type": payment[1],
            "number": payment[2],
            "expiration_date": payment[3],
            "cvv": payment[4],
        }
        return payment_dto
