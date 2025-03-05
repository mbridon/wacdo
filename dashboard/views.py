import pprint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import RestaurantForm
from .models import Restaurant


class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant
    template_name = "restaurant_list.html"

    def get(self, request):
        restaurants = Restaurant.objects.all()
        # WTF: the template doesn't print the actual list :-/

        return HttpResponse(restaurants, self.template_name)


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
            return render(request, self.template_name, {"form": form, "error": str(form.errors)})


class UpdateRestaurantView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    template_name = "restaurant_form.html"
    form_class = RestaurantForm

    def get(self, request, pk):
        form = self.form_class()

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect("restaurant-list")

        else:
            return render(request, self.template_name, {"form": form, "error": str(form.errors)})


class DeleteRestaurantView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy("restaurant-list")

    def get(self, request, pk):
        restaurant = Restaurant.objects.get(pk=pk)

        return render(request, self.template_name, {"restaurant": restaurant})
