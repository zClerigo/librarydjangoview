from django.urls import path
from django.conf.urls import include
from . import views

app_name = "movies"

urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
]