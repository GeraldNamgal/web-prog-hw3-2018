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
    # Get item's objects from database
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    context = {
        'item': item
    }

    # Get toppings (for pizza items)
    toppings = Topping.objects.all()
    context['toppings'] = toppings

    # Get number of toppings according to item (for pizza items)
    if item.name == '1 topping' or item.name == '1 item':
        context['toppingLimit'] = 1
    if item.name == '2 toppings' or item.name == '2 items':
        context['toppingLimit'] = 2
    if item.name == '3 toppings' or item.name == '3 items':
        context['toppingLimit'] = 3

    # TODO: What to do for special pizza?

    # Decide which item details page to render (pizza, or sub, etc.)
    if item.category.name == "Regular Pizza" or item.category.name == "Sicilian Pizza":
        return render(request, "orders/itemDetailsPizza.html", context)
    if item.category.name == "Subs":
        return render(request, "orders/itemDetailsSub.html", context)
    else:
        return render(request, "orders/itemDetails.html", context)

def addToCart(request, itemID):
    # Get item's corresponding object from database that user selected
    try:
        item = Item.objects.get(id=itemID)
    except Item.DoesNotExist:
        raise Http404("Item does not exist.")

    # Get size and quantity user selected
    size = request.POST.get('itemSize')
    quantity = request.POST.get('quantity')

    # If user selected a pizza, get toppings selected (i.e., checkbox'd)
    toppings = []
    toppingObjects = Topping.objects.all()
    if item.category.name == "Sicilian Pizza" or item.category.name == "Regular Pizza":
        # Iterate through user's form; if a topping is selected, add it to 'toppings' list
        for object in toppingObjects:
            if request.POST.get(object.name) == 'yes':
                toppings.append(object.name)

    # Check that user selected appropriate amount of toppings if chose a pizza
    if item.name == '1 topping' or item.name == '1 item':
        if len(toppings) is not 1:
            return render(request, 'orders/errorDetails.html', \
                {'message': 'Please check exactly 1 topping/item.', \
                'itemID': itemID
            })
    if item.name == '2 toppings' or item.name == '2 items':
        if len(toppings) is not 2:
            return render(request, 'orders/errorDetails.html', \
                {'message': 'Please check exactly 2 toppings/items.', \
                'itemID': itemID
            })
    if item.name == '3 toppings' or item.name == '3 items':
        if len(toppings) is not 3:
            return render(request, 'orders/errorDetails.html', \
                {'message': 'Please check exactly 3 toppings/items.', \
                'itemID': itemID
            })

    # If user selected a sub, get extra options selected (if any)
    subExtras = {}
    subExtras['mushrooms'] = request.POST.get('mushrooms')
    subExtras['greenPeppers'] = request.POST.get('greenPeppers')
    subExtras['onions'] = request.POST.get('onions')
    subExtras['extraCheese'] = request.POST.get('extraCheese')

    # Add item to cart
    cart = Cart(request)
    cart.add(item, size, quantity, toppings, subExtras)

    # Return user to the menu
    return HttpResponseRedirect(reverse("index"))

def removeFromCart(request, selectionID):
    # Remove item from cart
    cart = Cart(request)
    cart.remove(selectionID)

    # Return user to cart page
    return HttpResponseRedirect(reverse("cartContents"))

def cartContents(request):
    cart = Cart(request)

    # TODO: Create tuple list; each tuple like (user's selection, selection's toppings (if any), selection's extras)
    cartItems = []
    for selection in cart.selections:
        cartItems.append((selection, cart.getToppings(selection.pk)))

    context = {
        'cart': cart,
        'cartItems': cartItems
    }

    return render(request, 'orders/cart.html', context)
