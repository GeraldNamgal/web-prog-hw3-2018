from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

# Import models
from .models import Topping
from .models import PizzaRegular
from .models import PizzaSicilian
from .models import Sub
from .models import Steak
from .models import SteakAndCheese
from .models import Pasta
from .models import Salad
from .models import DinnerPlatter

def index(request):
    # If user is not signed in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    # If user is signed in, get their info
    context = {
        'user': request.user
    }

    # Get menu items to display
    toppings = Topping.objects.all()
    context['toppings'] = toppings
    pizzaRegulars = PizzaRegular.objects.all()
    context['pizzaRegulars'] = pizzaRegulars
    pizzaSicilians = PizzaSicilian.objects.all()
    context['pizzaSicilians'] = pizzaSicilians
    subs = Sub.objects.all()
    context['subs'] = subs
    steak = Steak.objects.all()
    context['steak'] = steak
    steakAndCheese = SteakAndCheese.objects.all()
    context['steakAndCheese'] = steakAndCheese
    pastas = Pasta.objects.all()
    context['pastas'] = pastas
    salads = Salad.objects.all()
    context['salads'] = salads
    dinnerPlatters = DinnerPlatter.objects.all()
    context['dinnerPlatters'] = dinnerPlatters

    # Return index page
    return render(request, "orders/index.html", context)

def loginView(request):
    if request.method == 'GET':
        return render(request, "orders/login.html", {"message": None})

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})

def register(request):
    if request.method == 'GET':
        return render(request, "orders/register.html", {"message": None})

    if request.method == 'POST':
        username = request.POST["username"]
        if username == "":
            return render(request, "orders/register.html", {"message": "Must enter a username."})
        if User.objects.filter(username=username).exists():
            return render(request, "orders/register.html", {"message": "Username already exists."})
        else:
            firstName = request.POST["firstName"]
            lastName = request.POST["lastName"]
            email = request.POST["emailAddress"]
            password = request.POST["password"]
            user = User.objects.create_user(username, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            return HttpResponseRedirect(reverse("index"))

def logoutView(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})
