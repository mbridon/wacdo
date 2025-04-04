from django.forms import DateInput, ModelForm, TextInput

from .models import Affectation, Collaborateur, Fonction, Restaurant


class AffectationForm(ModelForm):
    class Meta:
        model = Affectation
        fields = ["collaborateur", "restaurant", "fonction", "debut", "end"]
        widgets = {
            'debut': DateInput(attrs={'type': 'date'}),
            "end": DateInput(attrs={"type": "date", "required": False})
        }


class CollaborateurForm(ModelForm):
    class Meta:
        model = Collaborateur
        fields = ["nom", "prenom", "email", "date_premiere_embauche", "is_admin", "password"]
        widgets = {"date_premiere_embauche": DateInput(attrs={"type": "date"}),
                   "end": DateInput(attrs={"type": "date"})}


class FonctionForm(ModelForm):
    class Meta:
        model = Fonction
        fields = ["poste"]


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ["name", "address", "post_code", "city"]