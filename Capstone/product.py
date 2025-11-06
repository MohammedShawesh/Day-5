class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_summary(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    def update_name(self,new_name):
        self.name = new_name
        print(f"Product ID {self.id} name updated to: {self.name}")
    def update_price(self,new_price):
        if new_price >= 0:
            self.price = new_price
            print(f"Product ID {self.id} price updated to: {self.price}")
        else:
            print(f"price cannot be negative!!")

class Inventory:
    def __init__(self):
        self.products = {}
    def add_product(self, product):
            if product.id in self.products:
                print(f"Product ID {product.id} already exists!!")
            else:
                self.products[product.id] = product
                print(f"Product '{product.name}' added to inventory!!")

    def update_stock(self, product_id,new_quantity):
        if product_id in self.products:
            if new_quantity >= 0:
                self.products[product_id].quantity = new_quantity
                print(f"Stock for product ID {product_id} updated to {new_quantity}.")
            else:
                print("Stock quantity cannot be negative.")
        else:
            print(f"Product with ID {product_id} not found.")

    def find_product_by_id(self, product_id):
        return self.products.get(product_id)

    def find_product_by_name(self, name):
        for product in self.products.values():
            if product.name.lower() == name.lower():
                return product
        return None

    def list_all_products(self):
        if not self.products:
            print("inventory is currently empty.")
        else:
            print("--- Inventory ---")
            for product in self.products.values():
                print(product.get_summary())
            print("-"*20)

class Electronics(Product):
    def __init__(self, id, name, price, quantity, warranty_period):
        super().__init__(id, name, price,quantity)
        self.warranty_period = warranty_period

    def get_summary(self):
        summary = super().get_summary()
        return f"{summary}, Warranty: {self.warranty_period} months"

class Clothing(Product):
        def __init__(self, id, name, price, quantity, size, color):
            super().__init__(id, name, price, quantity)
            self.size = size
            self.color = color
        def get_summary(self):
            summary = super().get_summary()
            return f"{summary}, Size: {self.size}, Color: {self.color}"
