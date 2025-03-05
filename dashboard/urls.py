from django.urls import path
from .views import (
    CollaboratorListView, CreateCollaboratorView, UpdateCollaboratorView, DeleteCollaboratorView,
    RestaurantListView, CreateRestaurantView, UpdateRestaurantView, DeleteRestaurantView,
)


urlpatterns = [
    # Collaborators
    path("collaborator/all", CollaboratorListView.as_view(), name="collaborator-list"),
    path("collaborator/new", CreateCollaboratorView.as_view(), name="collaborator-new"),
    path("collaborator/<int:pk>/", UpdateCollaboratorView.as_view(), name="collaborator-update"),
    path("collaborator/<int:pk>/delete/", DeleteCollaboratorView.as_view(), name="collaborator-delete"),

    # Restaurants
    path("restaurant/all", RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurant/new", CreateRestaurantView.as_view(), name="restaurant-new"),
    path("restaurant/<int:pk>/", UpdateRestaurantView.as_view(), name="restaurant-update"),
    path("restaurant/<int:pk>/delete/", DeleteRestaurantView.as_view(), name="restaurant-delete"),
]