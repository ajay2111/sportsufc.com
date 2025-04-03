from django.db import models
import string
import random
from django.contrib.auth.models import User

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.


class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

#restaurant
#user
#ratings

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = "IN", 'indian'
        CHINESE = "CH", 'chinese'
        ITALIAN = 'IT', 'italian'
        MEXICAN = "MX", 'mexican'
        GREEK = "GR", 'greek'
        FASTFOOD = "FF", 'fastfood'
        OTHER = 'OT', 'other'
    
    name = models.CharField(max_length=100)
    website = models.URLField(default="")
    date_opened = models.DateField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)


    def __str__(self):
        return self.name
    
class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ratings = models.PositiveSmallIntegerField()

    
class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()