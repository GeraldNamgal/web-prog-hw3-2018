from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("register", views.register, name="register"),
    path("itemDetails/<int:itemID>", views.itemDetails, name="itemDetails"),
    path("addToCart/<int:itemID>", views.addToCart, name="addToCart"),
    path("removeFromCart/<int:itemID>", views.removeFromCart, name="removeFromCart")
]
