from django.urls import path
from . import views


urlpatterns = [
   path('' , views.aboutus_View, name="about"),
]