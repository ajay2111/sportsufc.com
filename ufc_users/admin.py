from django.contrib import admin
from .models import Restaurant, Sale, Ratings

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Sale)
admin.site.register(Ratings)