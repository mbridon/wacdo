from django.forms import ModelForm
from .models import Restaurant


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ["name", "address", "post_code", "city"]

    def save(self, args, **kwargs):
        restaurant = super().save(*args, **kwargs)
        print(self.cleaned_data)
        print(restaurant)
        #password = self.cleaned_data['password']
        #user.set_password(password)
        #user.is_staff = True
        #user.save()
        #return user