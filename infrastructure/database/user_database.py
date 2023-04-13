import mysql.connector
from mysql.connector.cursor import MySQLCursor

from infrastructure.database.database import Database
from domain.models.customer import Customer
from domain.models.seller import Seller
from exceptions.invalidParameterException import InvalidParameterException


class UserDatabase(Database):
    def create_customer(self, customer: Customer) -> None:
        first_name: str = customer.get_first_name()
        last_name: str = customer.get_last_name()
        username: str = customer.get_username()
        password: str = customer.get_password()
        address: str = customer.get_address()
        phone_number: str = customer.get_phone_number()
        email: str = customer.get_email()

        self.__add_human(username, password)
        self.__add_customer(first_name, last_name, address, phone_number, email)
        # self.__add_cart(user_id) # faire ca dans la bd? TODO

        return

    def create_seller(self, seller: Seller) -> None:
        name: str = seller.get_name()
        description: str = seller.get_description()
        username: str = seller.get_username()
        password: str = seller.get_password()
        address: str = seller.get_address()
        phone_number: str = seller.get_phone_number()
        email: str = seller.get_email()

        self.__add_human(username, password)
        self.__add_seller(name, description, address, phone_number, email)
        return

    def get_user_password(self, username: str) -> str | None:
        query: str = "SELECT password FROM humans WHERE username = %s"
        values: tuple = (username,)
        password: tuple = self.select_one_query(query, values)

        if password is None:
            return None

        return password[0]

    def get_user_id(self, username: str) -> int | None:
        query: str = "SELECT id FROM humans WHERE username = %s"
        values: tuple = (username,)
        user_id: tuple = self.select_one_query(query, values)

        if user_id is None:
            return None

        return user_id[0]

    def get_user(self, type: str, user_id: int) -> dict | None:
        query: str = f"SELECT * FROM {type} WHERE id = %s"
        values: tuple = (user_id,)
        user: tuple = self.select_one_query(query, values)

        if user is None:
            return None

        user_dto: dict[str, str] = self.__get_user_dto(type, user)
        return user_dto

    def __get_user_dto(self, type: str, user: tuple) -> dict[str, str]:
        user_dto: dict[str, str] = {}
        if type == "customers":
            user_dto: dict[str, str] = {
                "id": user[0],
                "first_name": user[1],
                "last_name": user[2],
                "address": user[3],
                "phone_number": user[4],
                "email": user[5],
            }
        elif type == "sellers":
            user_dto: dict[str, str] = {
                "id": user[0],
                "name": user[1],
                "description": user[2],
                "address": user[3],
                "phone_number": user[4],
                "email": user[5],
            }
        elif type == "admins":
            user_dto: dict[str, str] = {
                "id": user[0],
                "name": user[1],
            }
        return user_dto

    def __add_human(self, username: str, password: str) -> None:
        query: str = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        values: tuple = (username, password)
        self.insert_query(query, values)
        return

    def __add_customer(
        self,
        first_name: str,
        last_name: str,
        address: str,
        phone_number: str,
        email: str,
    ) -> None:
        query: str = (
            "INSERT INTO customers (id, first_name, last_name, address, phone_number, email) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        values: tuple = (first_name, last_name, address, phone_number, email)
        self.__insert_user(query, values)
        return

    def __add_seller(
        self,
        name: str,
        description: str,
        address: str,
        phone_number: str,
        email: str,
    ) -> None:
        query: str = (
            "INSERT INTO sellers (id, name, description, address, phone_number, email) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        values: tuple = (name, description, address, phone_number, email)
        self.__insert_user(query, values)
        return

    def __insert_user(self, query: str, values: tuple) -> None:
        try:
            self.insert_human_query(query, values)
        except mysql.connector.Error as err:
            if "phone_number_invalid" in str(err):
                raise InvalidParameterException(
                    "Numéro de téléphone doit avoir le format 418-123-4567"
                )
            elif "email_invalid" in str(err):
                raise InvalidParameterException("Email est invalide")
            raise InvalidParameterException(err)
        return

    def __insert_human(self, values: tuple) -> None:
        query: str = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        self.insert_query(query, values)

    def __add_cart(self, customer_id: int) -> None:
        query: str = "INSERT INTO carts (total_cost) VALUES (%s)"
        values: tuple = (0,)
        cart_id: int = self.insert_query(query, values)

        query: str = (
            "INSERT INTO customers_own_carts (customer_id, cart_id) VALUES (%s, %s)"
        )
        values: tuple = (customer_id, cart_id)
        self.insert_query(query, values)

        return

    def get_user_role(self, user_id: int) -> str | None:
        if self.__is_admin(user_id):
            return "admin"
        elif self.__is_seller(user_id):
            return "seller"
        elif self.__is_customer(user_id):
            return "customer"
        else:
            return None

    def __is_admin(self, user_id: int) -> bool:
        query: str = "SELECT id FROM admins WHERE id = %s"
        values: tuple = (user_id,)
        result: tuple = self.select_one_query(query, values)
        return result is not None

    def __is_seller(self, user_id: int) -> bool:
        query: str = "SELECT id FROM sellers WHERE id = %s"
        values: tuple = (user_id,)
        result: tuple = self.select_one_query(query, values)
        return result is not None

    def __is_customer(self, user_id: int) -> bool:
        query: str = "SELECT id FROM customers WHERE id = %s"
        values: tuple = (user_id,)
        result: tuple = self.select_one_query(query, values)
        return result is not None
