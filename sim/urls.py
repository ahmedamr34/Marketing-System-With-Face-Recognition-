from django.urls import path
from . import views


urlpatterns = [
  path('' , views.sim_view, name="simulation"),
]