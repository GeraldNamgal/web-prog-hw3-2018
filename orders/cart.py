from decimal import Decimal
from .models import Item, Customer, Order

# TODO: Try cart without 'object'
class Cart(object):
    def __init__(self, request):
        # Get customer's shopping cart (rows in Order with customer's current number of orders)
        self.customer = Customer.objects.get(pk=request.user.id)
        self.selections = Order.objects.filter(customerID=self.customer.pk, orderNumber=self.customer.orderNumber)

    def add(self, item, size, quantity):
        # Determine pricing
        if size == 'Small':
            price = item.priceSmall
        else:
            price = item.priceLarge

        # If item only has one size, change size name to 'Regular'
        if item.priceSmall is None:
            size = 'Regular'

        # TODO: Don't need? (maybe in update method):
        # # Add item to cart or update it if it's already in the cart
        # if self.selections.filter(itemID=item.pk, size=size).exists():
        #     # TODO: Account for small and large sizes?
        #     selection = self.selections.get(itemID=item.pk, size=size)
        #     selection.quantity = quantity
        #     selection.subtotal = Decimal(quantity) * price
        #
        # else:

        selection = Order(customerID=self.customer.pk, orderNumber=self.customer.orderNumber, \
            itemID=item.pk, price=price, size=size, quantity=quantity, itemName=item.name, \
            itemCategory=item.category, subtotal=(Decimal(quantity) * price))

        # Save the selection changes
        selection.save()

    def remove(self, selectionID):
        # If item is in cart, delete it
        if self.selections.filter(pk=selectionID).exists():
            self.selections.get(pk=selectionID).delete()

    def getTotalPrice(self):
        return sum(selection.subtotal for selection in self.selections)

    def getNumItems(self):
        return sum(selection.quantity for selection in self.selections)
