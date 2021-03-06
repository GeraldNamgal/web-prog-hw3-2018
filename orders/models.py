from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Item(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priceSmall = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    priceLarge = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return f'{self.name} ({self.category}): ${self.priceSmall} - ${self.priceLarge}'

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customers')
    orderNumber = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.customer.username}: is on his/her {self.orderNumber} order'

class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    orderNumber = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}: is on its {self.orderNumber} order'

class Order(models.Model):
    customerID = models.IntegerField()
    customerName = models.CharField(max_length=64)
    orderNumberCust = models.IntegerField()
    orderNumberRest = models.IntegerField(null=True, blank=True)
    itemID = models.IntegerField()
    itemName = models.CharField(max_length=64)
    itemCategory = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    size = models.CharField(max_length=16, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=11, decimal_places=2, default=0.00)
    dateTime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    complete = models.BooleanField(default=False)

class PizzaOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True, related_name='pizzaOrders')
    toppings = models.ManyToManyField(Topping)

class SubOrder(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True, related_name='subOrders')
    extraCheese = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    greenPeppers = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)
