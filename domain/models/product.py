class Product:
    def __init__(
        self,
        name: str,
        size: str,
        price: float,
        category: int,
        seller_id: int,
    ) -> None:
        self.name: str = name
        self.size: str = size
        self.price: float = price
        self.category: int = category
        self.seller_id: int = seller_id

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> str:
        return self.size

    def get_price(self) -> float:
        return self.price

    def get_category(self) -> int:
        return self.category

    def get_seller_id(self) -> int:
        return self.seller_id
