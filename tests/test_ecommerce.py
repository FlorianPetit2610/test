import unittest
from application.ecommerce import Product, ShoppingCart

class TestEcommerce(unittest.TestCase):
    def test_add_item(self):
        product = Product(name='Laptop', price=1000)
        cart = ShoppingCart()

        cart.add_item(product, quantity=2)

        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0]['product'], product)
        self.assertEqual(cart.items[0]['quantity'], 2)

    def test_calculate_total(self):
        product1 = Product(name='Phone', price=500)
        product2 = Product(name='Tablet', price=300)
        cart = ShoppingCart()

        cart.add_item(product1, quantity=2)
        cart.add_item(product2, quantity=1)

        total = cart.calculate_total()

        self.assertEqual(total, 1300)

if __name__ == '__main__':
    unittest.main()
