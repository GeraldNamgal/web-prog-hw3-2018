from django.contrib import admin

from .models import Topping, PizzaRegular, PizzaSicilian, Sub, Steak, \
    SteakAndCheese, Pasta, Salad, DinnerPlatter

admin.site.register(Topping)
admin.site.register(PizzaRegular)
admin.site.register(PizzaSicilian)
admin.site.register(Sub)
admin.site.register(Steak)
admin.site.register(SteakAndCheese)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
