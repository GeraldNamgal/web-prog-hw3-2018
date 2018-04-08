from django.contrib import admin

from .models import Topping
from .models import PizzaRegular
from .models import PizzaSicilian
from .models import Sub
from .models import Steak
from .models import SteakAndCheese
from .models import Pasta
from .models import Salad
from .models import DinnerPlatter

admin.site.register(Topping)
admin.site.register(PizzaRegular)
admin.site.register(PizzaSicilian)
admin.site.register(Sub)
admin.site.register(Steak)
admin.site.register(SteakAndCheese)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
