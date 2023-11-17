from application.ecommerce import Product, ShoppingCart

def main():
    # Créez quelques produits
    laptop = Product(name='Laptop', price=1000)
    phone = Product(name='Phone', price=500)
    tablet = Product(name='Tablet', price=300)

    # Initialisez un panier d'achat
    cart = ShoppingCart()

    # Ajoutez des articles au panier
    cart.add_item(laptop, quantity=2)
    cart.add_item(phone, quantity=1)
    cart.add_item(tablet, quantity=3)

    # Affichez le contenu du panier
    print("Contenu du panier :")
    for item in cart.items:
        print(f"{item['product'].name} - Quantité : {item['quantity']}")

    # Calculez et affichez le total
    total = cart.calculate_total()
    print(f"Total du panier : {total}")

if __name__ == "__main__":
    main()
