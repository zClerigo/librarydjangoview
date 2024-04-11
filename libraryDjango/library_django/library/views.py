from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = "core/home.html"


# @login_required
# def test_view(request):
#     return render(request, "core/test.html")