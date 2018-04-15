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

        # Set cart attribute
        self.cart = cart

    def add(self, itemSub, size, quantity):
        # Get price
        if size == 'small':
            price = itemSub.item.priceSmall
        else:
            price = itemSub.item.priceLarge

        # Get item ID (must convert item ID to JSON format, i.e., a string)
        itemID = str(itemSub.item.id)

        # Add item to cart or update it if it's already in the cart
        if itemID not in self.cart:
            # TODO: If item only has one size, remove size or make size value empty, i.e., ""
            # Must add item price to cart in JSON format, i.e., a string
            self.cart[itemID] = {'size': str(size), 'price': str(price), 'quantity': quantity, }
        else:
            # TODO: If item only has one size, remove size or make size value empty, i.e., ""
            self.cart[itemID]['size'] = str(size)
            self.cart[itemID]['price'] = str(price)
            self.cart[itemID]['quantity'] = quantity

        # Save the cart to session
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, item):
        # Get item ID (must convert item ID to JSON format, i.e., a string)
        itemID = str(item.id)

        # If item is in cart, delete it
        if itemID in self.cart:
            del self.cart[itemID]
            # Save the cart to session
            self.session['cart'] = self.cart
            self.session.modified = True

    def __iter__(self):
        # Get cart keys
        itemIDs = self.cart.keys()

        # Get corresponding item objects in database
        items = Item.objects.filter(id__in=itemIDs)

        # Add corresponding database item objects to cart
        for item in items:
            self.cart[str(item.id)]['item'] = item

        for item in self.cart.values():
            # Convert prices back to decimal
            item['price'] = Decimal(item['price'])
            # Add a total price to each item x quantity
            item['totalPrice'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Return the total number of items in the cart
        return sum(item['quantity'] for item in self.cart.values())

    def getTotalPrice(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # Empty cart and save to session
        self.session['cart'] = {}
        self.session.modified = True
