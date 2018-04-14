from decimal import Decimal
from .models import Item

# TODO: Try cart without 'object'
class Cart(object):
    def __init__(self, request):
        # Store the current session so it's accessible to other methods
        self.session = request.session
        # Retrieve a cart from session
        cart = self.session.get('cart')
        # If no cart exists in session, create one and store it in session
        if not cart:
            # Create the cart (a dictionary, will use item ID's as keys)
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, item, quantity):
        # Must convert item ID to JSON format, i.e., a string
        itemID = str(item.id)
        # Add item to cart or update it if it's already in the cart
        if itemID not in self.cart:
            # Must add item price to cart in JSON format, i.e., a string
            self.cart[itemID] = {'quantity': quantity, 'price': str(item.price)}
        else:
            self.cart[itemID]['quantity'] = quantity
        # Save the cart to session
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, item):
        # Must convert item ID to JSON format, i.e., a string
        itemID = str(item.id)
        if itemID in self.cart:
            del self.cart[itemID]
            # Save the cart to session
            self.session['cart'] = self.cart
            self.session.modified = True

    def __iter__(self):
        # Get cart dictionary's keys
        product_ids = self.cart.keys()
        # Access corresponding item instances in database
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Empty cart and save to session
        self.session['cart'] = {}
        self.session.modified = True
