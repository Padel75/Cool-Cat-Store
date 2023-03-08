from infrastructure.database.database import Database
from domain.models.product import Product


class ProductDatabase(Database):
    def create_product(self, product: Product) -> int:
        name = product.get_name()
        description = product.get_description()
        price = product.get_price()
        category_id = product.get_category_id()
        vendor_id = product.get_vendor_id()

        product_id = self.__add_product(name, description, price, category_id, vendor_id)
        return product_id

    def add_product_to_cart(self, product_id: int, customer_id: int, quantity: int) -> int:
        cart_id = self.__get_cart_id(customer_id)
        query = "INSERT INTO carts_contains_products (cart_id, product_id, quantity) VALUES (%s, %s, %s)"
        values = (cart_id, product_id, quantity)
        self.insert_query(query, values)
        return cart_id

    def get_product(self, product_id: int) -> tuple:
        query = "SELECT * FROM products WHERE id = %s"
        values = (product_id,)
        product = self.select_one_query(query, values)
        if product is None:
            return None
        return product

    def __add_product(self, name: str, description: str, price: float, category_id: int, vendor_id: int) -> int:
        query = "INSERT INTO products (name, description, price, category_id) " \
                "VALUES (%s, %s, %s, %s)"
        values = (name, description, price, category_id)
        product_id = self.insert_query(query, values)

        query = "INSERT INTO vendors_adds_products (product_id, vendor_id) " \
                "VALUES (%s, %s)"
        values = (product_id, vendor_id)
        self.insert_query(query, values)
        return product_id

    def __get_cart_id(self, customer_id: int) -> int:
        query = "SELECT cart_id FROM customers_own_carts WHERE customer_id = %s"
        values = (customer_id,)
        cart_id = self.select_one_query(query, values)
        if cart_id is None:
            return None
        return cart_id[0]