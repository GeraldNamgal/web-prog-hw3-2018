from django.contrib import admin

from .models import Item, Topping, PizzaRegular, PizzaSicilian, Sub, Pasta, Salad, \
    DinnerPlatter, Category, ClassName, Order

admin.site.register(Item)
admin.site.register(Topping)
admin.site.register(PizzaRegular)
admin.site.register(PizzaSicilian)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Category)
admin.site.register(ClassName)
admin.site.register(Order)
