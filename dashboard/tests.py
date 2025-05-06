import datetime

from django.contrib.auth import SESSION_KEY
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from dashboard.models import Collaborateur, Fonction, Restaurant, Affectation


# Testing the models
class CollaborateurTestCase(TestCase):
    def setUp(self):
        Collaborateur.objects.create(prenom="foo", nom="bar", email="bla@bla.com",
            date_premiere_embauche=datetime.datetime.now(datetime.UTC), is_admin=False, password="bla")

    def test_collaborateur(self):
        foo = Collaborateur.objects.get(prenom="foo")
        self.assertEqual(foo.nom, "bar")


class FonctionTestCase(TestCase):
    def setUp(self):
        Fonction.objects.create(poste="poste1")

    def test_fonction(self):
        fonction = Fonction.objects.get(poste="poste1")

        self.assertEqual(fonction.poste, "poste1")


class RestaurantTestCase(TestCase):
    def setUp(self):
        Restaurant.objects.create(name="resto1", address="address1", post_code="post_code1", city="city1")

    def test_restaurant(self):
        resto = Restaurant.objects.get(name="resto1")
        self.assertEqual(resto.address, "address1")
        self.assertEqual(resto.post_code, "post_code1")
        self.assertEqual(resto.city, "city1")


class AffectationTestCase(TestCase):
    def setUp(self):
        self.date_premiere_embauche = datetime.datetime.now(datetime.UTC)

        collaborateur = Collaborateur.objects.create(prenom="foo", nom="bar", email="bla@bla.com",
            date_premiere_embauche=self.date_premiere_embauche, is_admin=False, password="bla")
        fonction = Fonction.objects.create(poste="poste1")
        restaurant = Restaurant.objects.create(name="resto1", address="address1", post_code="post_code1", city="city1")
        self.affectation = Affectation.objects.create(collaborateur=collaborateur, fonction=fonction, restaurant=restaurant, debut=datetime.datetime.now(tz=datetime.UTC))

    def test_affectation(self):
        self.assertEqual(self.affectation.collaborateur.prenom, "foo")
        self.assertEqual(self.affectation.collaborateur.nom, "bar")
        self.assertEqual(self.affectation.collaborateur.email, "bla@bla.com")
        self.assertEqual(self.affectation.collaborateur.date_premiere_embauche, self.date_premiere_embauche)
        self.assertEqual(self.affectation.collaborateur.is_admin, False)
        self.assertEqual(self.affectation.collaborateur.password, "bla")

        self.assertEqual(self.affectation.fonction.poste, "poste1")

        self.assertEqual(self.affectation.restaurant.name, "resto1")
        self.assertEqual(self.affectation.restaurant.address, "address1")
        self.assertEqual(self.affectation.restaurant.post_code, "post_code1")
        self.assertEqual(self.affectation.restaurant.city, "city1")

# Functional tests for the UX
class FonctionalUXTestCase(TestCase):
    def setUp(self):
        self.credentials = {
            "username": "test",
            "email": "test@test.com",
            "password": "T35t",
        }
        User.objects.create_user(**self.credentials)
        # Doesn't seem to work? 🤔
        #self.assertEqual(str(self.client.session[SESSION_KEY]), str(self.user.id))
        self.client = Client()

    def login(self):
        return self.client.login(**self.credentials)

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_register(self):
        response = self.client.post("/users/register", self.credentials)

    def test_login(self):
        r = self.login()
        response = self.client.post("/users/login/", **self.credentials, follow=True)
        self.assertTrue(response.context["user"].is_active)

    def test_list_collaborateurs(self):
        self.login()

        response = self.client.get("/dashboard/collaborateur/all")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<a href=\"/dashboard/collaborateur/new\" class=\"btn btn-primary\">")

    def test_create_collaborateur(self):
        self.login()

        response = self.client.post("/dashboard/collaborateur/new", {
            "nom": "nom1",
            "prenom": "prenom1",
            "email": "email1",
            "date_premiere_embauche": datetime.datetime.now(tz=datetime.UTC),
            "is_admin": False,
            "password": "N0m.Pr3n0m",
        })
        self.assertEqual(Collaborateur.objects.filter(email="email1").count(), 1)