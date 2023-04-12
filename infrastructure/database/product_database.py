from typing import Dict, Any

from infrastructure.database.database import Database
from infrastructure.database.user_database import UserDatabase
from domain.models.product import Product


class ProductDatabase(Database):
    def create_product(self, product: Product) -> int:
        name: str = product.get_name()
        size: str = product.get_size()
        image_src: str = product.get_image_src()
        price: float = product.get_price()
        category: str = product.get_category()
        seller_id: int = product.get_seller_id()

        product_id: int = self.__add_product(
            name, size, image_src, price, category, seller_id
        )

        return product_id

    def add_product_to_cart(
        self, product_id: int, customer_id: int, quantity: int
    ) -> int:
        cart_id: int = self.__get_cart_id(customer_id)
        query: str = "REPLACE INTO carts_contains_products (cart_id, product_id, quantity) VALUES (%s, %s, %s)"
        values: tuple = (cart_id, product_id, quantity)
        self.insert_query(query, values)
        if quantity == 0:
            self.__remove_product_from_cart(cart_id, product_id)
        return cart_id

    def get_product(self, product_id: int) -> dict[str, Any] | None:
        query: str = "SELECT * FROM products WHERE id = %s"
        values: tuple = (product_id,)
        product: tuple = self.select_one_query(query, values)

        if product is None:
            return None

        user_database: UserDatabase = UserDatabase()
        sellerId: int = self.get_product_seller_id(product[0])
        sellerName: tuple = user_database.get_user("sellers", sellerId)["name"]
        product_dto: dict[str, Any] = {
            "id": product[0],
            "name": product[1],
            "size": product[2],
            "image": product[3],
            "price": product[4],
            "category": product[5],
            "sellerId": sellerId,
            "sellerName": sellerName
        }
        return product_dto

    def __add_product(
        self,
        name: str,
        size: str,
        image_src: str,
        price: float,
        category: str,
        seller_id: int,
    ) -> int:
        query: str = (
            "INSERT INTO products (name, size, image_src, price, category) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        values: tuple = (name, size, image_src, price, category)
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
        user_database: UserDatabase = UserDatabase()

        for product in products:
            sellerId: int = self.get_product_seller_id(product[0])
            sellerName: tuple = user_database.get_user("sellers", sellerId)["name"]
            product_dto: dict[str, Any] = {
                "id": product[0],
                "name": product[1],
                "size": product[2],
                "image": product[3],
                "price": product[4],
                "category": product[5],
                "sellerId": sellerId,
                "sellerName": sellerName
            }
            product_list.append(product_dto)

        return product_list

    def get_seller_products_id(self, seller_id: int) -> list:
        query: str = f"SELECT product_id FROM sellers_adds_products WHERE seller_id = {seller_id}"
        products: list = self.select_all_query(query)

        return products

    def get_product_seller_id(self, product_id: int) -> int:
        query: str = f"SELECT seller_id FROM sellers_adds_products WHERE product_id = %s"
        values: tuple = (product_id,)
        seller_id: tuple = self.select_one_query(query, values)

        return seller_id[0]

    def __get_cart_id(self, customer_id: int) -> int | None:
        query: str = "SELECT cart_id FROM customers_own_carts WHERE customer_id = %s"
        values: tuple = (customer_id,)
        cart_id: tuple = self.select_one_query(query, values)

        if cart_id is None:
            return None

        return cart_id[0]

    def get_cart(self, customer_id: int) -> list:
        query: str = f"SELECT product_id, quantity FROM carts_contains_products cart, customers_own_carts c" \
                     f" where c.customer_id = {customer_id} and c.cart_id = cart.cart_id"
        cart: list = self.select_all_query(query)

        return cart

    def get_cart_total_cost(self, customer_id: int) -> float:
        query: str = f"SELECT total_cost FROM carts cart, customers_own_carts c" \
                     f" where c.customer_id = %s and c.cart_id = cart.id"
        values: tuple = (customer_id,)
        total_cost: tuple = self.select_one_query(query, values)
        return total_cost[0]

    def __remove_product_from_cart(self, cart_id: int, product_id: int):
        query: str = "DELETE FROM carts_contains_products WHERE cart_id = %s AND product_id = %s"
        values: tuple = (cart_id, product_id)
        self.insert_query(query, values)
