from decimal import Decimal
from .models import Item, Customer, Order, Category, PizzaOrder, SubOrder, Topping

class Cart:
    def __init__(self, request):
        # Get customer's shopping cart (rows in Order with customer's current number of orders)
        self.customer = Customer.objects.get(pk=request.user.id)
        self.selections = Order.objects.filter(customerID=self.customer.pk, orderNumber=self.customer.orderNumber)

    def add(self, item, size, quantity, toppings, subExtras):
        # Determine pricing
        if size == 'Small':
            price = item.priceSmall
        else:
            price = item.priceLarge

        # If item only has one size, change size name to 'Regular'
        if item.priceSmall is None:
            size = 'Regular'

        # Calculate subtotal
        subtotal = Decimal(quantity) * price

        # If item is a sub, change subtotal for every extra selected
        if item.category.name == "Subs":
            if subExtras['mushrooms'] == 'yes':
                subtotal += Decimal(0.50) * Decimal(quantity)
            if subExtras['greenPeppers'] == 'yes':
                subtotal += Decimal(0.50) * Decimal(quantity)
            if subExtras['onions'] == 'yes':
                subtotal += Decimal(0.50) * Decimal(quantity)
            if subExtras['extraCheese'] == 'yes':
                subtotal += Decimal(0.50) * Decimal(quantity)

        # Save the selection to database
        selection = Order(customerID=self.customer.pk, orderNumber=self.customer.orderNumber, \
            itemID=item.pk, price=price, size=size, quantity=quantity, itemName=item.name, \
            itemCategory=item.category.name, subtotal=subtotal)
        selection.save()

        # If the item was a pizza, create a PizzaOrder object that inherits selection
        if item.category.name == 'Regular Pizza' or item.category.name == 'Sicilian Pizza':
            pizzaSelection = PizzaOrder(order=selection)
            pizzaSelection.save()
            for topping in toppings:
                pizzaSelection.toppings.add(Topping.objects.get(name=topping))
            pizzaSelection.save()

        # If the item was a sub, create a SubOrder object that inherits selection
        if item.category.name == 'Subs':
            subSelection = SubOrder(order=selection)
            subSelection.save()
            if subExtras['mushrooms'] == 'yes':
                subSelection.mushrooms = True
            if subExtras['greenPeppers'] == 'yes':
                subSelection.greenPeppers = True
            if subExtras['onions'] == 'yes':
                subSelection.onions = True
            if subExtras['extraCheese'] == 'yes':
                subSelection.extraCheese = True
            subSelection.save()

    # TODO: Make an update method?

    def remove(self, selectionID):
        # If item is in cart, delete it
        if self.selections.filter(pk=selectionID).exists():
            self.selections.get(pk=selectionID).delete()

    def getTotalPrice(self):
        return sum(selection.subtotal for selection in self.selections)

    def getNumItems(self):
        return sum(selection.quantity for selection in self.selections)

    # Returns toppings for one pizza
    def getToppings(self, orderID):
        toppings = []
        selection = self.selections.get(pk=orderID)
        if selection.itemCategory == 'Regular Pizza' or selection.itemCategory == 'Sicilian Pizza':
            pizzaOrder = PizzaOrder.objects.get(order=selection.pk)
            for topping in pizzaOrder.toppings.all():
                toppings.append(topping.name)
        return toppings

    # Returns extras for one sub
    def getExtras(self, orderID):
        extras = []
        selection = self.selections.get(pk=orderID)
        if selection.itemCategory == 'Subs':
            subOrder = SubOrder.objects.get(order=selection.pk)
            if subOrder.mushrooms == True:
                extras.append('Mushrooms')
            if subOrder.greenPeppers == True:
                extras.append('Green Peppers')
            if subOrder.onions == True:
                extras.append('Onions')
            if subOrder.extraCheese == True:
                extras.append('Extra Cheese')
        return extras
