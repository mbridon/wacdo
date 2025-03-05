from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Collaborator, Restaurant, Job
from .forms import CollaboratorForm, RestaurantForm


class CollaboratorListView(LoginRequiredMixin, ListView):
    model = Collaborator
    template_name = "collaborators/collaborator_list.html"
    context_object_name = "collaborators"


class CreateCollaboratorView(LoginRequiredMixin, CreateView):
    model = Collaborator
    form_class = CollaboratorForm
    template_name = "collaborators/collaborator_form.html"
    success_url = reverse_lazy("collaborator-list")


class UpdateCollaboratorView(LoginRequiredMixin, UpdateView):
    model = Collaborator
    form_class = CollaboratorForm
    template_name = "collaborators/collaborator_form.html"
    success_url = reverse_lazy("collaborator-list")


class DeleteCollaboratorView(LoginRequiredMixin, DeleteView):
    model = Collaborator
    template_name = "collaborators/collaborator_confirm_delete.html"
    success_url = reverse_lazy("collaborator-list")


class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant
    template_name = "restaurants/restaurant_list.html"
    context_object_name = "restaurants"


class CreateRestaurantView(LoginRequiredMixin, CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = "restaurants/restaurant_form.html"
    success_url = reverse_lazy("restaurant-list")


class UpdateRestaurantView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = "restaurants/restaurant_form.html"
    success_url = reverse_lazy("restaurant-list")


class DeleteRestaurantView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    template_name = "restaurants/restaurant_confirm_delete.html"
    success_url = reverse_lazy("restaurant-list")