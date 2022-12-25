from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.categoryViewSet),
    path('categories/<int:pk>', views.categorySingleOperations)
]
