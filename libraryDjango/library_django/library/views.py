from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm

class HomePageView(ListView):
    model = Book
    
class CheckoutView(TemplateView):
    template_name = "checkout.html"
    
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

    # comment the following line to show the error about not having an
    # success_url
    def get_success_url(self):
        return reverse_lazy("library:book_detail", args=[self.object.id])
        # you can also use it this way with kwargs, just to let you know
        # but here we have only one argument, so no mistake can be done
        #return reverse_lazy("movies:actor_detail",
        #                    kwargs={'pk':self.object.id})


# @login_required
# def test_view(request):
#     return render(request, "core/test.html")  