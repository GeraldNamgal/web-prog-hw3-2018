from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.apps import apps
from .cart import Cart

# Import models
from .models import Item, Topping, Customer, Order, Category

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
    regularPizzas = Item.objects.filter(category=Category.objects.get(name="Regular Pizza"))
    context['regularPizzas'] = regularPizzas
    sicilianPizzas = Item.objects.filter(category=Category.objects.get(name="Sicilian Pizza"))
    context['sicilianPizzas'] = sicilianPizzas
    subs = Item.objects.filter(category=Category.objects.get(name="Subs"))
    context['subs'] = subs
    pastas = Item.objects.filter(category=Category.objects.get(name="Pasta"))
    context['pastas'] = pastas
    salads = Item.objects.filter(category=Category.objects.get(name="Salads"))
    context['salads'] = salads
    dinnerPlatters = Item.objects.filter(category=Category.objects.get(name="Dinner Platters"))
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
        # Error check user input
        username = request.POST["username"]
        if username == "":
            return render(request, "orders/register.html", {"message": "Must enter a username."})
        if User.objects.filter(username=username).exists():
            return render(request, "orders/register.html", {"message": "Username already exists."})

        # Process user input
        else:
            firstName = request.POST["firstName"]
            lastName = request.POST["lastName"]
            email = request.POST["emailAddress"]
            password = request.POST["password"]

            # Save user in database
            user = User.objects.create_user(username, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()

            # Save user in Customer table
            customer = Customer(customer=user)
            customer.save()

            return HttpResponseRedirect(reverse("index"))

def logoutView(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})

def itemDetails(request, itemID):
    # Get item's object
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    context = {
        'item': item
    }

    return render(request, "orders/itemDetails.html", context)

def saveToCart(request, itemID):
    # Get user's choices
    size = request.POST.get('itemSize')
    quantity = request.POST.get('quantity')

    # Get item's object
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    # Add item to cart
    cart = Cart(request)
    cart.add(item, size, quantity)

    # Return user to the menu
    return HttpResponseRedirect(reverse("index"))

def removeFromCart(request, size, itemID):
    # Get item's object
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    # Remove item from cart
    cart = Cart(request)
    cart.remove(size, item)

    # Return user to cart page
    return HttpResponseRedirect(reverse("cartContents"))

def cartContents(request):
    cart = Cart(request)

    context = {
        'cart': cart
    }

    return render(request, 'orders/cart.html', context)
