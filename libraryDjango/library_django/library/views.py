from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import model_to_dict
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
import json

from .models import Book
from .forms import BookForm

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

class AddBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(
            self.request, messages.SUCCESS,
            'Book "{book_name}" has been added'.format(
                book_name=self.object.name))
        return response

    def get_success_url(self):
        return reverse_lazy("library:book_detail", args=[self.object.id])
    
class HomeView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_data = Book.objects.filter(checked_out=True)
        book_list = [{'name': book.name, 'author': book.author, 'checkout_date': book.checkout_date.strftime('%Y-%m-%d')} for book in book_data]
        books_json = json.dumps(book_list)
        context["book_list"] = books_json
        print("context", context)
        return context

class CheckoutView(LoginRequiredMixin, UpdateView):
    template_name = 'checkout.html'
    model = Book
    fields = ['checked_out'] 
    success_url = reverse_lazy('home') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_data = Book.objects.all()
        books_json = serialize('json', book_data, fields=('name', 'author', 'checkout_date'))
        context["book_list"] = books_json
        return context


    def get_object(self, queryset=None):
        return None

    def form_valid(self, form):
        selected_books = form.cleaned_data.get('selectedBooks', [])
        for book_id in selected_books:
            book = Book.objects.get(pk=book_id)
            book.checked_out = not book.checked_out 
            book.save()

        return super().form_valid(form)

class CoreLoginView(LoginView):
    template_name = "core/login.html"
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        auth_login(self.request, user)
        if user_need_to_go_to_otp:
            return redirect('otp_url')
        else:
            return else_where
# @login_required
# def test_view(request):
#     return render(request, "core/test.html")  