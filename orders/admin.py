from django.contrib import admin

from .models import Item, Topping, Category, Customer, Order, PizzaOrder, SubOrder

admin.site.register(Item)
admin.site.register(Topping)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(PizzaOrder)
admin.site.register(SubOrder)
