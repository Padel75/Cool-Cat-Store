class Product:
    def __init__(self, name, description, price, category_id, vendor_id):
        self.name = name
        self.description = description
        self.price = price
        self.category_id = category_id
        self.vendor_id = vendor_id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_category_id(self):
        return self.category_id

    def get_vendor_id(self):
        return self.vendor_id
