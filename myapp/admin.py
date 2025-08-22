# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import UserProfile

# admin.site.register(UserProfile)


# Remove this line if UserProfile is not in models.py
# from .models import UserProfile

from django.contrib import admin 
from .models import Car, FavoriteCar

admin.site.register(Car)
admin.site.register(FavoriteCar)
