class Product:
    def __init__(
        self,
        name: str,
        description: str,
        image_src: str,
        price: float,
        category_id: int,
        seller_id: int,
    ) -> None:
        self.name: str = name
        self.description: str = description
        self.image_src: str = image_src
        self.price: float = price
        self.category_id: int = category_id
        self.seller_id: int = seller_id

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_image_src(self) -> str:
        return self.image_src

    def get_price(self) -> float:
        return self.price

    def get_category_id(self) -> int:
        return self.category_id

    def get_seller_id(self) -> int:
        return self.seller_id
