from django.urls import path
from eventapp import views

urlpatterns = [
    path('', views.index, name="event"),
    path('events/find', views.getevent , name="getevent"),
]
