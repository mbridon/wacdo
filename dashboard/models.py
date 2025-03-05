from django import forms
from django.db import models


class Collaborator(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    date_first_hire = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_admin = models.BooleanField()
    password = models.CharField(max_length=60)


class Restaurant(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField(max_length=600)
    post_code = models.CharField(max_length=5)
    city = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Job(models.Model):
    post = models.CharField(max_length=30)


class Affectation(models.Model):
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    begin = models.DateTimeField(auto_now=False, auto_now_add=False)
    end = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)