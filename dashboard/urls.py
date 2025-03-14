from django.urls import path
from .views import (
    CollaborateurListView, CreateCollaborateurView, UpdateCollaborateurView, DeleteCollaborateurView,
    FonctionListView, CreateFonctionView, UpdateFonctionView, DeleteFonctionView,
    RestaurantListView, CreateRestaurantView, UpdateRestaurantView, DeleteRestaurantView,
)


urlpatterns = [
    # Collaborateurs
    path("collaborateur/all", CollaborateurListView.as_view(), name="collaborateur-list"),
    path("collaborateur/new", CreateCollaborateurView.as_view(), name="collaborateur-new"),
    path("collaborateur/<int:pk>/", UpdateCollaborateurView.as_view(), name="collaborateur-update"),
    path("collaborateur/<int:pk>/delete/", DeleteCollaborateurView.as_view(), name="collaborateur-delete"),

    # Fonctions
    path("fonction/all", FonctionListView.as_view(), name="fonction-list"),
    path("fonction/new", CreateFonctionView.as_view(), name="fonction-new"),
    path("fonction/<int:pk>/", UpdateFonctionView.as_view(), name="fonction-update"),
    path("fonction/<int:pk>/delete/", DeleteFonctionView.as_view(), name="fonction-delete"),

    # Restaurants
    path("restaurant/all", RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurant/new", CreateRestaurantView.as_view(), name="restaurant-new"),
    path("restaurant/<int:pk>/", UpdateRestaurantView.as_view(), name="restaurant-update"),
    path("restaurant/<int:pk>/delete/", DeleteRestaurantView.as_view(), name="restaurant-delete"),
]