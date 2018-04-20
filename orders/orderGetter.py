from decimal import Decimal
from .models import Item, Order, Category, PizzaOrder, SubOrder, \
    Topping, Restaurant, User

class OrderGetter:
    def __init__(self, orderNumberRest):
        # Get all the orders (i.e., 'selections') with the order number 'orderNumberRest'
        self.selections = Order.objects.filter(orderNumberRest=orderNumberRest)

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
