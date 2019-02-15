from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point #added while trying to solve code blow-up
from .models import Shop

longitude = 10.391764
latitude = 63.379053

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = "shops"
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    template_name = "shops/index.html"

#home = Home.as_view()