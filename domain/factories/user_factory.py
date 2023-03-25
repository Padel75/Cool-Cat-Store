from domain.models.customer import Customer
from domain.models.seller import Seller
import bcrypt


class UserFactory:
    def create_customer(self, customer_infos: {}) -> Customer:
        first_name = customer_infos["first_name"]
        last_name = customer_infos["last_name"]
        username = customer_infos["username"]
        password = customer_infos["password"]
        address = customer_infos["address"]
        phone_number = customer_infos["phone_number"]
        email = customer_infos["email"]

        encrypted_password: bytes = self.__encrypt_password(password)

        customer: Customer = Customer(
            username,
            encrypted_password,
            first_name,
            last_name,
            address,
            phone_number,
            email,
        )

        return customer

    def create_seller(self, seller_infos: {}) -> Seller:
        name = seller_infos["name"]
        description = seller_infos["description"]
        username = seller_infos["username"]
        password = seller_infos["password"]
        address = seller_infos["address"]
        phone_number = seller_infos["phone_number"]
        email = seller_infos["email"]

        encrypted_password: bytes = self.__encrypt_password(password)

        seller: Seller = Seller(
            username,
            str(encrypted_password),
            name,
            description,
            address,
            phone_number,
            email,
        )

        return seller

    def __encrypt_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        encrypted_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return encrypted_password
