from rest_framework.serializers import ModelSerializer
from .models import Category, MenuItem

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'