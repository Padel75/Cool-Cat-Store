class Product:
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        category_id: int,
        vendor_id: int,
    ) -> None:
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.category_id: int = category_id
        self.vendor_id: int = vendor_id

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def get_category_id(self) -> int:
        return self.category_id

    def get_vendor_id(self) -> int:
        return self.vendor_id
