from django.urls import include, path
from . import views


urlpatterns = [
    path('<str:group>/users', views.GetCreateUserGroups.as_view()),
    path('<str:group>/users/<int:userId>', views.DeleteUserFromGroup.as_view())
]
