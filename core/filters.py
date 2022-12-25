from django.db.models.query import QuerySet

class BaseFilter:
    """
    A helper class designed to make adding query parameters easier

    The `queryset` is the query set of item we will filter through

    The `params` variable takes a dict object that has a string `db_lookup_field` which will be used to look 
    up properties in the database and `query_parameter_name` which is the name of the query parameter that'll have the value of the query parameter
    we want to filter at
    ```
    param = {
        "db_lookup_field": "query_parameter_name"
    }
    ```
    Example, To add support for filtering a `MenuItem` by category or name

    ```
    class MenuItemFilter(BaseFilter):
        queryset = MenuItem.objects.all()
        params = {
            "category__title": "category",
            "title__icontains": "title"
        }
    # then you would simply create an instance and call the .filter() function and 
    # pass it the query_params dict from the request object

    class SomeView(SomeAPIView):
        def get(self, request, *args, **kwargs):
            filter = MenuItemFilter()
            items = filter.filter(request.query_params)
            srialized_items = MenuItemSerializer(items, many=True)
            return Response(srialized_items.data)
    ```

    """
    # the query set that will filter through
    queryset = None

    # a key value dict of extra query params
    params = None

    # private property that conatains a dict of sucessfully parsed params
    _parsed_params = {}

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset


    def _get_params(self):
        if self.params is None: return dict()

        assert type(self.params) is dict, "params must be of type dict<str: str>"

        return self.params

    def _get_from_request(self, kwargs, serialized_property):

        return kwargs.get(serialized_property, None)
        
    def parse_params(self, kwargs):
        parsed_params = {}
        
        params = self._get_params()
        for db_property, serialized_property in params.items():
            val = self._get_from_request(kwargs, serialized_property)
            if val is None: continue

            parsed_params[db_property] = val

        self._parsed_params = parsed_params
        return parsed_params


    def filter(self, kwargs):
        queryset = self.get_queryset()
        parsed_params = self.parse_params(kwargs)

        return queryset.filter(**parsed_params)

    

