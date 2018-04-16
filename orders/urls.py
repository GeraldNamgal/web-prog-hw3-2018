from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("register", views.register, name="register"),
    path("itemDetails/<int:itemID>", views.itemDetails, name="itemDetails"),
    path("saveToCart/<int:itemID>", views.saveToCart, name="saveToCart"),
    path("removeFromCart/<str:size>/<int:itemID>", views.removeFromCart, name="removeFromCart"),
    path("cartContents", views.cartContents, name="cartContents")
]
