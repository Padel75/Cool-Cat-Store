from typing import Any

import mysql.connector
from mysql.connector.cursor import MySQLCursor

from infrastructure.database.database import Database
from domain.models.customer import Customer
from domain.models.vendor import Vendor
from exceptions.invalidParameterException import InvalidParameterException


class UserDatabase(Database):
    def create_customer(self, customer: Customer) -> int:
        first_name: str = customer.get_first_name()
        last_name: str = customer.get_last_name()
        username: str = customer.get_username()
        password: str = customer.get_password()
        address: str = customer.get_address()
        phone_number: str = customer.get_phone_number()
        email: str = customer.get_email()

        human_id: int = self.__add_human(username, password)
        user_id: int = self.__add_customer(
            first_name, last_name, address, phone_number, email, human_id
        )
        self.__add_cart(user_id)

        return user_id

    def create_vendor(self, vendor: Vendor) -> int:
        name: str = vendor.get_name()
        description: str = vendor.get_description()
        username: str = vendor.get_username()
        password: str = vendor.get_password()
        address: str = vendor.get_address()
        phone_number: str = vendor.get_phone_number()
        email: str = vendor.get_email()

        human_id: int = self.__add_human(username, password)
        user_id: int = self.__add_vendor(
            name, description, address, phone_number, email, human_id
        )
        return user_id

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

    def get_user(self, type: str, user_id: int) -> tuple | None:
        query: str = f"SELECT * FROM {type} WHERE id = %s"
        values: tuple = (user_id,)
        user: tuple = self.select_one_query(query, values)

        if user is None:
            return None

        return user

    def __add_human(self, username: str, password: str) -> int:
        query: str = "INSERT INTO humans (username, password) VALUES (%s, %s)"
        values: tuple = (username, password)

        return self.insert_query(query, values)

    def __add_customer(
        self,
        first_name: str,
        last_name: str,
        address: str,
        phone_number: str,
        email: str,
        human_id: int,
    ) -> int:
        query: str = (
            "INSERT INTO customers (first_name, last_name, address, phone_number, email, id) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        values: tuple = (first_name, last_name, address, phone_number, email, human_id)

        return self.__insert_user(query, values, human_id)

    def __add_vendor(
        self,
        name: str,
        description: str,
        address: str,
        phone_number: str,
        email: str,
        human_id: int,
    ) -> int:
        query: str = (
            "INSERT INTO vendors (name, description, address, phone_number, email, id) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        values: tuple = (name, description, address, phone_number, email, human_id)

        return self.__insert_user(query, values, human_id)

    def __insert_user(self, query: str, values: tuple, human_id: int) -> int:
        try:
            user_id: int = self.insert_query(query, values)
        except mysql.connector.Error as err:
            self.__delete_human(human_id)
            if "phone_number_invalid" in str(err):
                raise InvalidParameterException(
                    "Numéro de téléphone doit avoir le format 418-123-4567"
                )
            elif "email_invalid" in str(err):
                raise InvalidParameterException("Email est invalide")
            raise InvalidParameterException(err)
        return user_id

    def __delete_human(self, human_id: int) -> None:
        cursor: MySQLCursor = self.connection.cursor()
        query: str = "DELETE FROM humans WHERE id = %s"
        cursor.execute(query, (human_id,))

        query: str = "ALTER TABLE humans AUTO_INCREMENT = %s"
        auto_increment_value: int = human_id - 1 if human_id > 1 else 1

        cursor.execute(query, (auto_increment_value,))
        self.connection.commit()
        cursor.close()

        return

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
