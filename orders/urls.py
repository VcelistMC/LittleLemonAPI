from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_orders_view),
    path('<int:orderId>', views.orders_single_ops_view),
    path('me', views.own_orders_get_create_view),
    path('me/<int:orderId>', views.own_orders_single_ops),
]
