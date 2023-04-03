from typing import Dict, Any

from infrastructure.database.database import Database
from domain.models.product import Product


class ProductDatabase(Database):
    def create_product(self, product: Product) -> int:
        name: str = product.get_name()
        description: str = product.get_description()
        price: float = product.get_price()
        category_id: int = product.get_category_id()
        seller_id: int = product.get_seller_id()

        product_id: int = self.__add_product(
            name, description, price, category_id, seller_id
        )

        return product_id

    def add_product_to_cart(
        self, product_id: int, customer_id: int, quantity: int
    ) -> int:
        cart_id: int = self.__get_cart_id(customer_id)
        query: str = "REPLACE INTO carts_contains_products (cart_id, product_id, quantity) VALUES (%s, %s, %s)"
        values: tuple = (cart_id, product_id, quantity)

        self.insert_query(query, values)

        return cart_id

    def get_product(self, product_id: int) -> dict[str, Any] | None:
        query: str = "SELECT * FROM products WHERE id = %s"
        values: tuple = (product_id,)
        product: tuple = self.select_one_query(query, values)

        if product is None:
            return None

        product_dto: dict[str, Any] = {
            "id": product[0],
            "name": product[1],
            "description": product[2],
            "price": product[3],
            "category": product[4],
        }
        return product_dto

    def __add_product(
        self,
        name: str,
        description: str,
        price: float,
        category_id: int,
        seller_id: int,
    ) -> int:
        query: str = (
            "INSERT INTO products (name, description, price, category_id) "
            "VALUES (%s, %s, %s, %s)"
        )
        values: tuple = (name, description, price, category_id)
        product_id: int = self.insert_query(query, values)

        query: str = (
            "INSERT INTO sellers_adds_products (product_id, seller_id) "
            "VALUES (%s, %s)"
        )
        values: tuple = (product_id, seller_id)
        self.insert_query(query, values)

        return product_id

    def get_products(self) -> list:
        query: str = "SELECT * FROM products"
        product_list: list = self.__create_products_dto(query)

        return product_list

    def get_products_filtered(self, search_filter: str) -> list:
        query: str = f"SELECT * FROM products WHERE name LIKE %{search_filter}% OR description LIKE %{search_filter}%"
        product_list: list = self.__create_products_dto(query)

        return product_list

    def __create_products_dto(self, query: str) -> list:
        products: list = self.select_all_query(query)
        product_list: list = []

        for product in products:
            product_dto: dict[str, Any] = {
                "id": product[0],
                "name": product[1],
                "description": product[2],
                "price": product[3],
                "category": product[4],
            }
            product_list.append(product_dto)

        return product_list

    def get_seller_products_id(self, seller_id: int) -> list:
        query: str = f"SELECT product_id FROM sellers_adds_products WHERE seller_id = {seller_id}"
        products: list = self.select_all_query(query)

        return products

    def __get_cart_id(self, customer_id: int) -> int | None:
        query: str = "SELECT cart_id FROM customers_own_carts WHERE customer_id = %s"
        values: tuple = (customer_id,)
        cart_id: tuple = self.select_one_query(query, values)

        if cart_id is None:
            return None

        return cart_id[0]

    def get_cart(self, cart_id: int) -> list:
        query: str = f"SELECT product_id, quantity FROM carts_contains_products c where c.cart_id = {cart_id}"
        cart: list = self.select_all_query(query)

        return cart
