from django.urls import path
from .views import (
    AffectationListView, CreateAffectationView, UpdateAffectationView, DeleteAffectationView, AffectationDetailsView,
    CollaborateurListView, CreateCollaborateurView, UpdateCollaborateurView, DeleteCollaborateurView, CollaborateurDetailsView, IdleCollaborateursView,
    FonctionListView, CreateFonctionView, UpdateFonctionView, DeleteFonctionView, FonctionDetailsView,
    RestaurantListView, CreateRestaurantView, UpdateRestaurantView, DeleteRestaurantView, RestaurantDetailsView,
)


urlpatterns = [
    # Affectations
    path("affectation/all", AffectationListView.as_view(), name="affectation-list"),
    path("affectation/new", CreateAffectationView.as_view(), name="affectation-new"),
    path("affectation/<int:pk>/detail/", AffectationDetailsView.as_view(), name="affectation-details"),
    path("affectation/<int:pk>/edit/", UpdateAffectationView.as_view(), name="affectation-update"),
    path("affectation/<int:pk>/delete/", DeleteAffectationView.as_view(), name="affectation-delete"),

    # Collaborateurs
    path("collaborateur/all", CollaborateurListView.as_view(), name="collaborateur-list"),
    path("collaborateur/new", CreateCollaborateurView.as_view(), name="collaborateur-new"),
    path("collaborateur/<int:pk>/details/", CollaborateurDetailsView.as_view(), name="collaborateur-details"),
    path("collaborateur/<int:pk>/edit/", UpdateCollaborateurView.as_view(), name="collaborateur-update"),
    path("collaborateur/<int:pk>/delete/", DeleteCollaborateurView.as_view(), name="collaborateur-delete"),
    path("collaborateur/idle/", IdleCollaborateursView.as_view(), name="collaborateur-idle"),

    # Fonctions
    path("fonction/all", FonctionListView.as_view(), name="fonction-list"),
    path("fonction/new", CreateFonctionView.as_view(), name="fonction-new"),
    path("fonction/<int:pk>/details/", FonctionDetailsView.as_view(), name="fonction-details"),
    path("fonction/<int:pk>/edit/", UpdateFonctionView.as_view(), name="fonction-update"),
    path("fonction/<int:pk>/delete/", DeleteFonctionView.as_view(), name="fonction-delete"),

    # Restaurants
    path("restaurant/all", RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurant/new", CreateRestaurantView.as_view(), name="restaurant-new"),
    path("restaurant/<int:pk>/details/", RestaurantDetailsView.as_view(), name="restaurant-details"),
    path("restaurant/<int:pk>/edit/", UpdateRestaurantView.as_view(), name="restaurant-update"),
    path("restaurant/<int:pk>/delete/", DeleteRestaurantView.as_view(), name="restaurant-delete"),
]