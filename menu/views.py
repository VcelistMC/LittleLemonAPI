from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from menu.filters import MenuItemFilter
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from core.permissions import ReadOnlyForNonManager
from rest_framework.response import Response

class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyForNonManager]


class CategorySingleOperations(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyForNonManager]
    

class MenuListCreate(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyForNonManager]

    def get(self, request, *args, **kwargs):
        filter = MenuItemFilter()
        items = filter.filter(request.query_params)
        srialized_items = MenuItemSerializer(items, many=True)
        return Response(srialized_items.data)



class MenuSingleOperations(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [ReadOnlyForNonManager]

categoryViewSet = CategoryListCreate.as_view()
categorySingleOperations = CategorySingleOperations.as_view()
menuViewSet = MenuListCreate.as_view()
menuSingleOperations = MenuSingleOperations.as_view()
