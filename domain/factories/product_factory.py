from domain.models.product import Product


class ProductFactory:
    def create_product(self, product_infos: {}) -> Product:
        name = product_infos["name"]
        size = product_infos["size"]
        image_src = product_infos["image_src"]
        price = float(product_infos["price"])
        category = product_infos["category"]
        seller_id = product_infos["seller_id"]

        product: Product = Product(name, size, image_src, price, category, seller_id)

        return product
