from infrastructure.database.database import Database


class PaymentDatabase(Database):
    def create_payment_system(self, payment_system: PaymentSystem) -> int:
        name: str = payment_system.get_name()
        image_src: str = payment_system.get_image_src()
        payment_system_id: int = self.__add_payment_system(name, image_src)
        return payment_system_id
