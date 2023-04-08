class Product:
    def __init__(
        self,
        name: str,
        size: str,
        image_src: str,
        price: float,
        category: str,
        seller_id: int,
    ) -> None:
        self.name: str = name
        self.size: str = size
        self.image_src: str = image_src
        self.price: float = price
        self.category: str = category
        self.seller_id: int = seller_id

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> str:
        return self.size

    def get_image_src(self) -> str:
        return self.image_src

    def get_price(self) -> float:
        return self.price

    def get_category(self) -> str:
        return self.category

    def get_seller_id(self) -> int:
        return self.seller_id
