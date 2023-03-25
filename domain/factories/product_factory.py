from domain.models.product import Product


class ProductFactory:
    def create_product(self, product_infos: {}) -> Product:
        name = product_infos["name"]
        description = product_infos["description"]
        price = product_infos["price"]
        category_id = product_infos["category_id"]
        seller_id = product_infos["seller_id"]

        product: Product = Product(name, description, price, category_id, seller_id)
        return product
