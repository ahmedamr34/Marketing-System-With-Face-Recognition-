from django.urls import path
from . import views


urlpatterns = [
  path('order/edit/<int:order_id>/' , views.edit_order, name="edit"),
  path('order/delete/<int:order_id>/' , views.delete_order, name="delete"),
]