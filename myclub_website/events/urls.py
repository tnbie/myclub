from django.urls import path
from . import views

urlpatterns = [
    # Path Converters #
    
    # int: numbers
    # str: strings
    # path: whole urls
    # slug: hyphen and underscores_stuff
    # UUID: identifier for the
    
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events, name="list-events")
]