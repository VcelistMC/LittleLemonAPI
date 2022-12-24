from django.urls import include, path
from . import views


urlpatterns = [
    path('<str:group>/users', views.users_of_group)
]
