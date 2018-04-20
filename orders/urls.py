from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginView, name="login"),
    path("logout", views.logoutView, name="logout"),
    path("register", views.register, name="register"),
    path("itemDetails/<int:itemID>", views.itemDetails, name="itemDetails"),
    path("addToCart/<int:itemID>", views.addToCart, name="addToCart"),
    path("removeFromCart/<int:selectionID>", views.removeFromCart, name="removeFromCart"),
    path("cartContents", views.cartContents, name="cartContents"),
    path("confirm", views.confirm, name="confirm"),
    path("checkout", views.checkout, name='checkout'),
    path("orders", views.orders, name='orders'),
    path("orderComplete", views.orderComplete, name='orderComplete'),
    path("myOrders", views.myOrders, name='myOrders')
]
