from django.http import HttpResponse
from django.views.generic import ListView
from .models import Restaurant


class RestaurantListView(ListView):
    model = Restaurant

    def all(self, request):
        result = Restaurant.objects.all()

        return HttpResponse(result)