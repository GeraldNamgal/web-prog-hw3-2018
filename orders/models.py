from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

    def toClassName(self):
        return self.__class__.__name__

class Item(models.Model):
    name = models.CharField(max_length=64)
    priceSmall = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    priceLarge = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}: ${self.priceSmall} - ${self.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class PizzaRegular(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.item.name}: ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class PizzaSicilian(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.item.name}: ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Sub(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)
    xtraCheese = models.BooleanField(default=False)
    mushrooms = models.BooleanField(default=False)
    greenPeppers = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item.name}: ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Pasta(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.item.name}: ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Salad(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.item.name}: ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class DinnerPlatter(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.item.name}: ${self.item.priceSmall} - ${self.item.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Customer(models.Model):
    username = models.CharField(max_length=64)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    emailAddress = models.CharField(max_length=64)

    def __str__(self):
	       return f'Username: {self.username} - First: {self.firstName} - Last: {self.lastName}'

class Order(models.Model):
    customerID = models.IntegerField()
    date = models.DateField()
    itemID = models.IntegerField()
