class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        for item in self.items:
            if item['product'] == product:
                item['quantity'] += quantity
                break
        else:
            self.items.append({'product': product, 'quantity': quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total
