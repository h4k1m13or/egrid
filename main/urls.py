from django.conf.urls import url
from django.urls import include, path

from main import views

app_nale = 'main'
urlpatterns = [
    path('', views.index, name="index"),
    path('maps/', views.maps, name="maps")

]
