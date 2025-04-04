from django import forms
from django.db import models


class Collaborateur(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    date_premiere_embauche = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_admin = models.BooleanField()
    password = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField(max_length=600)
    post_code = models.CharField(max_length=5)
    city = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Fonction(models.Model):
    poste = models.CharField(max_length=30)

    def __str__(self):
        return self.poste


class Affectation(models.Model):
    collaborateur = models.ForeignKey(Collaborateur, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    fonction = models.ForeignKey(Fonction, on_delete=models.CASCADE)
    debut = models.DateTimeField(auto_now=False, auto_now_add=False)
    end = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return f"{self.collaborateur} - {self.restaurant} - {self.fonction} ({self.debut} à {self.end or 'en cours'})"