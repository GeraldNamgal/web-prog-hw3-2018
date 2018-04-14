from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.apps import apps
from .cart import Cart
from .forms import ItemForm

# Import models
from .models import Item
from .models import Topping
from .models import PizzaRegular
from .models import PizzaSicilian
from .models import Sub
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
            # TODO: Add user to Customer table?
            return HttpResponseRedirect(reverse("index"))

def logoutView(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def itemDetails(request, itemID):
    # Get item object
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    # Get item's subclass object
    model = apps.get_model('orders', item.subclass.name)
    try:
        itemSub = model.objects.get(pk=itemID)
    except model.DoesNotExist:
        raise Http404("Item does not exist.")

    # TODO: remove (for debugging)
    print(f"Name of item is {itemSub.item.name}")
    print(f"id is {itemSub.pk}")

    # Add a form
    itemForm = ItemForm()
    context = {
        'itemSub': itemSub,
        'itemForm': itemForm
    }

    return render(request, "orders/itemDetails.html", context)

def addToCart(request, itemID):
    cart = Cart(request)

    # Get item object
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    # Get item's subclass object
    model = apps.get_model('orders', item.subclass.name)
    try:
        itemSub = model.objects.get(pk=itemID)
    except model.DoesNotExist:
        raise Http404("Item does not exist.")

    form = ItemForm()
    if form.is_valid():
        data = form.cleaned_data
        cart.add(item=itemSub, quantity=data['quantity'])

    return HttpResponseRedirect(reverse("index"))

def removeFromCart(request, itemID):
    cart = Cart(request)

    # Get item object
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    # Get item's subclass object
    model = apps.get_model('orders', item.subclass.name)
    try:
        itemSub = model.objects.get(pk=itemID)
    except model.DoesNotExist:
        raise Http404("Item does not exist.")

    cart.remove(itemSub)

    return HttpResponseRedirect(reverse("index"))

def cartContents(request):
    cart = Cart(request)
    return render(request, 'orders/cart.html', {'cart': cart})
