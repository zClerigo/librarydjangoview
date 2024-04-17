from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import model_to_dict

from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    
class BookDetailView(DetailView):
    model = Book

class AddBookView(CreateView):
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

class CheckoutView(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_list = list(Book.objects.all().values())
        context["book_list"] = book_list
        print("context", context)
        return context
    
    def post(self, request):
        selected_ids = request.POST.getlist('selectedIds[]') 
        for book_id in selected_ids:
            book = Book.objects.get(id=book_id)
            book.checked_out = not book.checked_out
            book.save()
    
    def get(self, request):
        return render(request, 'checkout.html')

# @login_required
# def test_view(request):
#     return render(request, "core/test.html")  