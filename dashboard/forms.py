from django.forms import ModelForm
from .models import Restaurant


class NewRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ["name", "address", "post_code", "city"]