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