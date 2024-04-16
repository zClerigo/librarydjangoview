from django.urls import path

from . import views

app_name = "movies"

urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("addbook/", views.AddBookView.as_view(), name="addbook")
]