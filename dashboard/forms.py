from django.forms import DateField, ModelForm, TextInput

from .models import Affectation, Collaborateur, Fonction, Restaurant


class AffectationForm(ModelForm):
    class Meta:
        model = Affectation
        fields = ["collaborateur", "restaurant", "fonction", "debut", "end"]

    debut = DateField(widget=TextInput(attrs={'class': 'form-control', 'type': 'date'}))
    end = DateField(widget=TextInput(attrs={'class': 'form-control', 'type':'date'}), required=False)


class CollaborateurForm(ModelForm):
    class Meta:
        model = Collaborateur
        fields = ["nom", "prenom", "email", "date_premiere_embauche", "is_admin", "password"]

    date_premiere_embauche = DateField(widget=TextInput(attrs={'class': 'form-control', 'type':'date'}))
    end = DateField(widget=TextInput(attrs={'class': 'form-control', 'type':'date'}), required=False)


class FonctionForm(ModelForm):
    class Meta:
        model = Fonction
        fields = ["poste"]


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ["name", "address", "post_code", "city"]