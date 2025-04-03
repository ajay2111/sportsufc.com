from django.contrib.auth.models import User
from ufc_users.models import Restaurant, Ratings,Sale
from django.utils import timezone 
from django.db import connection

from pprint import pprint

def run():
    restaurant = Restaurant.objects.count()
    ratings = Ratings.objects.count()
    sale = Sale.objects.count()

    pprint(connection.queries)




