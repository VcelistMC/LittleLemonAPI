from rest_framework.urls import path
from . import views

urlpatterns = [
    path('', views.list_create_cart_view),
    path('me', views.own_cart_view),
    path('me/items', views.own_cart_items_view)
]
