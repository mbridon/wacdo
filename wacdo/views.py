from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template = "home.html"

    def get(self, request):
        return render(request, self.template)