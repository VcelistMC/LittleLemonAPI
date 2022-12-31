from django.shortcuts import get_object_or_404

class MultipleLookUpFieldMixin(object):
    """
    Actual code http://www.django-rest-framework.org/api-guide/generic-views/#creating-custom-mixins\n
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    This mixin also allows using custom URL conf keywords
    The format of the lookup fields should be as follows 
    ```py
        {
            urlKeyword: dbKeyword,
            ...
        } 
    ```
    Example: To lookup an item by a userId and and orderId you would do something like this
    ```py
        lookup_fields = {
            'userId': 'customer__pk',
            'orderId': 'pk
        }
    """
    lookup_fields = {}
    

    def get_object(self):
        queryset = self.get_queryset()
        filter = {}
        for urlKeyword, dbKeyword in self.lookup_fields.items():
            try:
                filter[dbKeyword] = self.kwargs[urlKeyword]
            except Exception:
                raise Exception(f'Expected to find {urlKeyword}')
        
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

class FilterMixin(object):
    filter_fields = {}

    def filter_queryset(self, queryset):
        filters = {}
        for urlParam, dbParam in self.filter_fields.items():
            assert type(urlParam) is str, f'{urlParam} must be of type str'
            assert type(dbParam) is str, f'{dbParam} must be of type str'

            urlValue = self.request.GET.get(urlParam, None)
            if urlValue is None: continue

            filters[dbParam] = urlValue
        
        print(filters, self.filter_fields, self.request.GET)

        return queryset.filter(**filters)