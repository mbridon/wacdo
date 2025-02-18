from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import NewRestaurantForm
from .models import Restaurant


class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant

    def all(self, request):
        result = Restaurant.objects.all()

        return HttpResponse(result)


class CreateRestaurantView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ["name", "address", "post_code", "city"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdateRestaurantView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = ["name", "address", "post_code", "city"]


class DeleteRestaurantView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy("restaurant-list")