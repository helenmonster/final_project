from django.urls import path

from . import views

urlpatterns = [
        path('map/',views.map, name = 'map'),
        path('sightings/', views.sightings, name = 'sightings'),
        path('sightings/<squirrel_id>/',views.id, name = 'id'),
        path('sightings/add/',views.add, name = 'add'),
        #path('stats/', views.stats, name = 'stats'),
]
