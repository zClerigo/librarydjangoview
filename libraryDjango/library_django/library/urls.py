from django.urls import path
from django.conf.urls import include
from . import views

app_name = "movies"

urlpatterns = [
    path("booklist/", views.BookListView.as_view(), name="booklist"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("addbook/", views.AddBookView.as_view(), name="addbook"),
    path("home/<int:pk>", views.BookDetailView.as_view(),
        name="book_detail"),
]