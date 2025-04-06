from django.contrib.auth.models import User
from ufc_users.models import Restaurant, Ratings,Sale
from django.utils import timezone 
from django.db import connection
from django.db.models import Sum

from pprint import pprint

def run():
    # chinese = Restaurant.TypeChoices.CHINESE
    # indian = Restaurant.TypeChoices.INDIAN
    # mexican = Restaurant.TypeChoices.MEXICAN
    # check_types = [chinese,indian,mexican]

    sales = Restaurant.objects.prefetch_related("sales", "ratings").filter(ratings__ratings=5)\
                .annotate(total = Sum("sales__income"))
    print(sales.values())
    # pprint(connection.queries)




