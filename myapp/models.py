# from django.db import models
# from django.contrib.auth.models import User


from django.contrib.auth.models import User
from django.db import models

class Car(models.Model):
    
    title = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    model_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    body_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.title
    

class FavoriteCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.car.title}"
    








    # ye filter ka kaam change h
from django.shortcuts import render
from .models import Car

# Landing Page
def se_project(request):
    # Fetch unique values for the filters
    car_conditions = ['New Car', 'Used Car']  # You can extend this if needed.
    brands = Car.objects.values_list('brand_name', flat=True).distinct()
    models = Car.objects.values_list('car_model', flat=True).distinct()
    years = Car.objects.values_list('model_year', flat=True).distinct()
    mileages = Car.objects.values_list('mileage', flat=True).distinct()
    prices = Car.objects.values_list('price', flat=True).distinct()
    body_types = Car.objects.values_list('body_type', flat=True).distinct()

    context = {
        'car_conditions': car_conditions,
        'brands': brands,
        'models': models,
        'years': years,
        'mileages': mileages,
        'prices': prices,
        'body_types': body_types,
    }

    return render(request, 'se_project.html', context)