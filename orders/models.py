from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

    def toClassName(self):
        return self.__class__.__name__

class ClassName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

    def toClassName(self):
        return self.__class__.__name__

class Item(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    priceSmall = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    priceLarge = models.DecimalField(max_digits=4, decimal_places=2)
    subclass = models.ForeignKey(ClassName, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.category}): ${self.priceSmall} - ${self.priceLarge}, \
            has subclass "{self.subclass}"'

    def toClassName(self):
        return self.__class__.__name__

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

    def toClassName(self):
        return self.__class__.__name__

class PizzaRegular(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True, related_name='regularPizzas')
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.item.name} ({self.item.category}): ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class PizzaSicilian(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True, related_name='sicilianPizzas')
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.item.name} ({self.item.category}): ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Sub(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True, related_name='subs')
    xtraCheese = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    greenPeppers = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item.name} ({self.item.category}): ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Pasta(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True, related_name='pastas')

    def __str__(self):
        return f'{self.item.name} ({self.item.category}): ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Salad(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True, related_name='salads')

    def __str__(self):
        return f'{self.item.name} ({self.item.category}): ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class DinnerPlatter(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True, related_name='dinnerPlatters')

    def __str__(self):
        return f'{self.item.name} ({self.item.category}): ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customerID = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="customers")
    date = models.DateField(null=True)
    itemID = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name="orderedItems")
    quantity = models.IntegerField(null=True)
