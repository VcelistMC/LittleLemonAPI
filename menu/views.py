from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.mixins import FilterMixin
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from core.permissions import ReadOnlyForNonManager
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyForNonManager]
    pagination_class = LimitOffsetPagination


class CategorySingleOperations(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyForNonManager]
    

class MenuListCreate(FilterMixin, ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyForNonManager]
    pagination_class = LimitOffsetPagination
    filter_fields = {
        "category": "category__title",
        "title": "title__icontains"
    }

class MenuSingleOperations(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyForNonManager]

categoryViewSet = CategoryListCreate.as_view()
categorySingleOperations = CategorySingleOperations.as_view()
menuViewSet = MenuListCreate.as_view()
menuSingleOperations = MenuSingleOperations.as_view()
