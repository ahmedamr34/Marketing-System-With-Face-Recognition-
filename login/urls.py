from django.urls import path
from . import views


urlpatterns = [
   path('' , views.login_view, name="login"),
   path('logout_View' , views.logout_View, name="logout"),
]