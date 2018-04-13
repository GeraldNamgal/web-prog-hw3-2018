from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("register", views.register, name="register"),
    path("<str:className>/<int:itemID>", views.orderDetail, name="orderDetail"),
    path("addToCart/<str:className>/<int:itemID>", views.addToCart, name="addToCart")
]
