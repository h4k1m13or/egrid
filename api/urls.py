from rest_framework import routers
from django.conf.urls import url
from django.urls import include, path

from api import views

router = routers.DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('plants/', views.PlantsList.as_view()),
    path('plants/<int:id>', views.PlantDetail.as_view()),
    path('states/', views.StatesList.as_view()),
    path('states/<int:id>', views.StateDetail.as_view()),
    path('', include(router.urls))

]
