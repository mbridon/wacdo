from django.forms import ModelForm
from .models import Collaborator, Restaurant


class CollaboratorForm:
    class Meta:
        model = Collaborator
        fields = ["last_name", "first_name", "email", "date_first_hire", "is_admin", "password"]


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ["name", "address", "post_code", "city"]