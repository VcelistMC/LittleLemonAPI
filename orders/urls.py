from django.urls import path
from . import views
urlpatterns = [
    path('me', views.own_orders_get_create_view)
]
