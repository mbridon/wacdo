from django.urls import path
from .views import RestaurantListView, CreateRestaurantView, UpdateRestaurantView, DeleteRestaurantView


urlpatterns = [
    path("restaurant/all", RestaurantListView.as_view(), name="restaurant-list"),
    path("restaurant/new", CreateRestaurantView.as_view(), name="restaurant-new"),
    path("restaurant/<int:pk>/", UpdateRestaurantView.as_view(), name="restaurant-update"),
    path("restaurant/<int:pk>/delete/", DeleteRestaurantView.as_view(), name="restaurant-delete"),
]