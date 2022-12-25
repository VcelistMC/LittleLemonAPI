from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, MenuItem
from .serializers import CategorySerializer
from core.permissions import ReadOnlyForNonManager
from rest_framework.permissions import IsAuthenticated

class CategoryListCreate(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ReadOnlyForNonManager]


class CategorySingleOperations(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ReadOnlyForNonManager]
    
categoryViewSet = CategoryListCreate.as_view()
categorySingleOperations = CategorySingleOperations.as_view()
