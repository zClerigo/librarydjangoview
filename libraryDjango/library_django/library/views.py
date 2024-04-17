from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "home.html"
    
class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = "checkout.html"

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