from datetime import datetime
from typing import Any, List, Dict

from domain.models.payment_system import PaymentSystem
from infrastructure.database.database import Database


class PaymentDatabase(Database):
    def create_payment_system(self, payment_system: PaymentSystem) -> int:
        customer_id: int = payment_system.get_customer_id()
        number: int = payment_system.get_number()
        date: str = payment_system.get_expiration_date()
        cvv: int = payment_system.get_cvv()
        type_system: str = payment_system.get_payment_type()

        payment_id: int = self.__add_payment_system(
            customer_id, number, date, cvv, type_system
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
        self.insert_query(query, values)

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

    def pay(self, cart_id: int, customer_id: int) -> bool:
        query: str = (
            f"SELECT product_id, quantity FROM carts_contains_products cart, customers_own_carts c"
            f" where c.customer_id = {customer_id} and c.cart_id = cart.cart_id"
        )
        cart: list = self.select_all_query(query)

        if cart is None:
            return False

        invoice_id: int = self.__create_invoice(customer_id, 0)

        for product in cart:
            product_id: int = product[0]
            quantity: int = product[1]

            query: str = (
                "INSERT INTO invoice_contains_products (invoice_id, product_id, quantity)"
                " VALUES (%s, %s, %s)"
            )
            values: tuple = (invoice_id, product_id, quantity)
            self.insert_query(query, values)

        query: str = "DELETE FROM carts_contains_products WHERE cart_id = %s"
        values: tuple = (cart_id,)
        self.delete_query(query, values)

        query: str = "UPDATE carts SET total_cost = 0 WHERE id = %s"
        values: tuple = (cart_id,)
        self.update_query(query, values)

        return True

    def __create_invoice(self, customer_id: int, total_cost: float) -> int:
        query: str = (
            "INSERT INTO invoices (customer_id, total_cost, date) VALUES (%s, %s, %s)"
        )

        date_today = datetime.now()
        formatted_date = date_today.strftime("%Y-%m-%d")

        values: tuple = (customer_id, total_cost, formatted_date)
        invoice_id: int = self.insert_query(query, values)
        return invoice_id

    def get_invoices(self, customer_id: int) -> list[dict[str, Any]] | None:
        query: str = f"SELECT * FROM invoices WHERE customer_id = {customer_id}"
        invoices: list = self.select_all_query(query)

        if invoices is None:
            return None

        invoices_dto: list[dict[str, Any]] = []
        for invoice in invoices:
            invoices_dto.append(self.get_invoice(invoice[0]))

        return invoices_dto

    def get_invoice(self, invoice_id: int) -> dict[str, Any] | None:
        query: str = f"SELECT * FROM invoice_contains_products WHERE id = {invoice_id}"
        products: list = self.select_all_query(query)

        query: str = f"SELECT total_cost, date FROM invoices WHERE id = %s"
        values: tuple = (invoice_id,)
        invoice_data: float = self.select_one_query(query, values)[0]

        if products is None:
            return None

        invoice_dto = {
            "id": invoice_id,
            "total_cost": invoice_data[0],
            "date": invoice_data[1],
            "products": [],
        }

        for product in products:
            query: str = f"SELECT name, price FROM products WHERE id = {product[1]}"
            values: tuple = (product[1],)
            product_data: str = self.select_one_query(query, values)[0]

            product_dto: dict[str, Any] = {
                "id": product[1],
                "name": product_data[0],
                "quantity": product[2],
                "price": product_data[1],
            }

            invoice_dto["products"].append(product_dto)

        return invoice_dto
