# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import UserProfile
# from .models import Car

from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
