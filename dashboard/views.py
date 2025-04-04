from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Affectation, Collaborateur, Fonction, Restaurant
from .forms import AffectationForm, CollaborateurForm, FonctionForm, RestaurantForm


class CollaborateurListView(LoginRequiredMixin, ListView):
    model = Collaborateur
    template_name = "collaborateurs/collaborateur_list.html"
    context_object_name = "collaborateurs"


class CreateCollaborateurView(LoginRequiredMixin, CreateView):
    model = Collaborateur
    form_class = CollaborateurForm
    template_name = "collaborateurs/collaborateur_form.html"
    success_url = reverse_lazy("collaborateur-list")


class UpdateCollaborateurView(LoginRequiredMixin, UpdateView):
    model = Collaborateur
    form_class = CollaborateurForm
    template_name = "collaborateurs/collaborateur_form.html"
    success_url = reverse_lazy("collaborateur-list")


class DeleteCollaborateurView(LoginRequiredMixin, DeleteView):
    model = Collaborateur
    template_name = "collaborateurs/collaborateur_confirm_delete.html"
    success_url = reverse_lazy("collaborateur-list")


class FonctionListView(LoginRequiredMixin, ListView):
    model = Fonction
    template_name = "fonctions/fonction_list.html"
    context_object_name = "fonctions"


class CreateFonctionView(LoginRequiredMixin, CreateView):
    model = Fonction
    form_class = FonctionForm
    template_name = "fonctions/fonction_form.html"
    success_url = reverse_lazy("fonction-list")


class UpdateFonctionView(LoginRequiredMixin, UpdateView):
    model = Fonction
    form_class = FonctionForm
    template_name = "fonctions/fonction_form.html"
    success_url = reverse_lazy("fonction-list")


class DeleteFonctionView(LoginRequiredMixin, DeleteView):
    model = Fonction
    template_name = "fonctions/fonction_confirm_delete.html"
    success_url = reverse_lazy("fonction-list")


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


class AffectationListView(LoginRequiredMixin, ListView):
    model = Affectation
    template_name = "affectations/affectation_list.html"
    context_object_name = "affectations"


class CreateAffectationView(LoginRequiredMixin, CreateView):
    model = Affectation
    form_class = AffectationForm
    template_name = "affectations/affectation_form.html"
    success_url = reverse_lazy("affectation-list")


class UpdateAffectationView(LoginRequiredMixin, CreateView):
    model = Affectation
    form_class = AffectationForm
    template_name = "affectations/affectation_form.html"
    success_url = reverse_lazy("affectation-list")
    context_object_name = Affectation

    def get(self, request, pk):
        self.form = self.form_class(get_object_or_404(self.context_object_name.objects, pk=pk))
        return HttpResponse(self.form)


class DeleteAffectationView(LoginRequiredMixin, CreateView):
    model = Affectation
    form_class = AffectationForm
    template_name = "affectations/affectation_form.html"
    success_url = reverse_lazy("affectation-list")