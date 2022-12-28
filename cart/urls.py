from rest_framework.urls import path
from . import views

urlpatterns = [
    path('', views.list_create_cart_view),
    path('me', views.own_cart_view),
    path('me/items', views.own_cart_items_view),
    path('me/items/<int:pk>', views.own_cart_item_single_ops_view),
    path('<int:pk>', views.cart_single_ops_view),
    path('<int:cartId>/items', views.cart_items_view),
    path('<int:cartId>/items/<int:itemId>', views.cart_items_single_ops_view),
]
