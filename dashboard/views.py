from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import RestaurantForm
from .models import Restaurant


class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant

    def all(self, request):
        restaurants = Restaurant.objects.all()

        return HttpResponse(restaurants)


class CreateRestaurantView(LoginRequiredMixin, CreateView):
    model = Restaurant
    template_name = "restaurant_form.html"
    form_class = RestaurantForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect("restaurant-list")

        else:
            print("Invalid form")
            print(form.errors)

            return render(request, self.template_name, {"form": form, "error": "Données incorrectes"})


class UpdateRestaurantView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = ["name", "address", "post_code", "city"]


class DeleteRestaurantView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy("restaurant-list")