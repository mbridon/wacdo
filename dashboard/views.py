from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Affectation, Collaborateur, Fonction, Restaurant
from .forms import AffectationForm, CollaborateurForm, FonctionForm, RestaurantForm, RestaurantDetailsForm


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

    def post(self, request):
        search_term = request.POST["q"]
        results = Restaurant.objects.all().filter(name__icontains=search_term)
        if results.count() == 1:
            restaurant_pk = results.first().pk
            return redirect(f"/dashboard/restaurant/{restaurant_pk}")

        elif not results.exists():
            raise Http404(f"No such restaurant: {search_term}")

        return HttpResponse(results)


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


class RestaurantDetailsView(LoginRequiredMixin, DetailView):
    model = Restaurant
    template_name = "restaurants/restaurant_details.html"
    form_class = RestaurantDetailsForm


class AffectationListView(LoginRequiredMixin, ListView):
    model = Affectation
    template_name = "affectations/affectation_list.html"
    context_object_name = "affectations"


class CreateAffectationView(LoginRequiredMixin, CreateView):
    model = Affectation
    form_class = AffectationForm
    template_name = "affectations/affectation_form.html"
    success_url = reverse_lazy("affectation-list")


class UpdateAffectationView(LoginRequiredMixin, UpdateView):
    model = Affectation
    form_class = AffectationForm
    template_name = "affectations/affectation_form.html"
    success_url = reverse_lazy("affectation-list")
    context_object_name = "affectation"


class DeleteAffectationView(LoginRequiredMixin, DeleteView):
    model = Affectation
    form_class = AffectationForm
    template_name = "affectations/affectation_form.html"
    success_url = reverse_lazy("affectation-list")
