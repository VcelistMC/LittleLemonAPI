from core.filters import BaseFilter
from menu.models import MenuItem


class MenuItemFilter(BaseFilter):
    queryset = MenuItem.objects.all()
    params = {
        "category__title": "category",
        "title__icontains": "title"
    }