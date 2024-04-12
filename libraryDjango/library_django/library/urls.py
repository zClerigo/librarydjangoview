from django.urls import path

from . import views

app_name = "movies"

urlpatterns = [
    path("home/", views.HomePageView.as_view(), name="home")
]