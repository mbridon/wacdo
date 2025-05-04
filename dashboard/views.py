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

    def post(self, request):
        search_term = request.POST.get("q", "").strip()

        results = Collaborateur.objects.filter(nom__icontains=search_term) | \
                  Collaborateur.objects.filter(prenom__icontains=search_term) | \
                  Collaborateur.objects.filter(email__icontains=search_term)

        if results.count() == 1:
            return redirect("collaborateur-details", pk=results.first().pk)

        elif not results.exists():
            raise Http404(f"Aucun collaborateur trouvé pour : {search_term}")

        return render(request, self.template_name, {"collaborateurs": results})


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


class CollaborateurDetailsView(LoginRequiredMixin, DetailView):
    model = Collaborateur
    template_name = "collaborateurs/collaborateur_details.html"
    context_object_name = "collaborateur"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["affectations"] = self.object.affectation_set.select_related("fonction", "restaurant")
        return context


class IdleCollaborateursView(LoginRequiredMixin, ListView):
    model = Collaborateur
    template_name = "collaborateurs/collaborateur_idle.html"
    context_object_name = "collaborateurs"


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


class FonctionDetailsView(LoginRequiredMixin, DetailView):
    model = Fonction
    template_name = "fonctions/fonction_details.html"
    context_object_name = "fonction"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["affectations"] = self.object.affectation_set.select_related("collaborateur", "restaurant")
        return context


class RestaurantListView(LoginRequiredMixin, ListView):
    model = Restaurant
    template_name = "restaurants/restaurant_list.html"
    context_object_name = "restaurants"

    def post(self, request):
        search_term = request.POST.get("q", "").strip()
        results = Restaurant.objects.filter(name__icontains=search_term) | \
                  Restaurant.objects.filter(city__icontains=search_term) | \
                  Restaurant.objects.filter(post_code=search_term)

        if results.count() == 1:
            return redirect("restaurant-details", pk=results.first().pk)

        elif not results.exists():
            return render(request, self.template_name, {"restaurants": results, "search_term": search_term})

        return render(request, self.template_name, {"restaurants": results})


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
    context_object_name = "restaurant"

    def post(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)

        search_term = request.POST.get("q", "").strip()
        results = Affectation.objects.filter(restaurant=pk, fonction__poste__icontains=search_term) | \
                  Affectation.objects.filter(restaurant=pk, debut__icontains=search_term) | \
                  Affectation.objects.filter(restaurant=pk, end__icontains=search_term)

        if results.count() == 1:
            return redirect("affectation-details", pk=results.first().pk)

        elif not results.exists():
            return render(request, self.template_name, {"affectations": results, "pk": pk, "search_term": search_term})

        return render(request, self.template_name, {"affectations": results})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["affectations"] = self.object.affectation_set.select_related("collaborateur", "fonction")
        return context


class AffectationListView(LoginRequiredMixin, ListView):
    model = Affectation
    template_name = "affectations/affectation_list.html"
    context_object_name = "affectations"

    def post(self, request):
        search_term = request.POST.get("q", "").strip()
        results = Affectation.objects.filter(fonction__poste__icontains=search_term) | \
                  Affectation.objects.filter(debut__icontains=search_term) | \
                  Affectation.objects.filter(end__icontains=search_term) | \
                  Affectation.objects.filter(restaurant__city__icontains=search_term)

        if results.count() == 1:
            return redirect("affectation-details", pk=results.first().pk)

        elif not results.exists():
            raise Http404(f"Aucune affectation trouvée pour : {search_term}")

        return render(request, self.template_name, {"affectations": results})


# Assign an idle collaborator
# This needs to be an UpdateView so the form can be prefilled with at the very least the collaborator
class CreateAffectationView(LoginRequiredMixin, UpdateView):
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

class AffectationDetailsView(LoginRequiredMixin, DetailView):
    model = Affectation
    template_name = "affectations/affectation_details.html"
    context_object_name = "affectation"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context["affectation"] = self.object.affectation_set.select_related("collaborateur", "fonction", "restaurant")
        return context
