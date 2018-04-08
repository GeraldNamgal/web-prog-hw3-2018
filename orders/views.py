from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

# TODO:
#from .models import Item

def index(request):
    # If user is not signed in
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    # If user is signed in, get their info
    context = {
        'user': request.user
    }

    # TODO: Get menu items to display
    #items = Item.objects.all()
    #context['items'] = items

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
