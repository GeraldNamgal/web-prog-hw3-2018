from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

    def toClassName(self):
        return self.__class__.__name__

class PizzaRegular(models.Model):
    name = models.CharField(max_length=64)
    priceSmall = models.DecimalField(max_digits=4, decimal_places=2)
    priceLarge = models.DecimalField(max_digits=4, decimal_places=2)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.name}: ${self.priceSmall} - ${self.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class PizzaSicilian(models.Model):
    name = models.CharField(max_length=64)
    priceSmall = models.DecimalField(max_digits=4, decimal_places=2)
    priceLarge = models.DecimalField(max_digits=4, decimal_places=2)
    toppings = models.ManyToManyField(Topping, blank=True)

    def __str__(self):
        return f'{self.name}: ${self.priceSmall} - ${self.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Sub(models.Model):
    name = models.CharField(max_length=64)
    priceSmall = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    priceLarge = models.DecimalField(max_digits=4, decimal_places=2)
    xtraCheese = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: ${self.priceSmall} - ${self.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Steak(models.Model):
    sub = models.OneToOneField(Sub, on_delete=models.CASCADE, primary_key=True)
    mushrooms = models.BooleanField(default=False)
    greenPeppers = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sub.name}: ${self.sub.priceSmall} - ${self.sub.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class SteakAndCheese(models.Model):
    sub = models.OneToOneField(Sub, on_delete=models.CASCADE, primary_key=True)
    mushrooms = models.BooleanField(default=False)
    greenPeppers = models.BooleanField(default=False)
    onions = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sub.name}: ${self.sub.priceSmall} - ${self.sub.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}: ${self.price}'

    def toClassName(self):
        return self.__class__.__name__

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}: ${self.price}'

    def toClassName(self):
        return self.__class__.__name__

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    priceSmall = models.DecimalField(max_digits=4, decimal_places=2)
    priceLarge = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name}: ${self.priceSmall} - ${self.priceLarge}'

    def toClassName(self):
        return self.__class__.__name__

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
