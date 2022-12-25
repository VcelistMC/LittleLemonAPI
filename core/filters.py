from django.db.models.query import QuerySet
import unittest

class BaseFilter:
    # the query set that will filter through
    queryset = None

    # a key value dict of required query params
    required_params = None

    # a key value dict of extra query params
    extra_params = None

    # private property that conatains a dict of sucessfully parsed params
    _parsed_params = {}

    _hasError = False

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

    def _get_required_params(self):
        if self.required_params is None: return dict()

        assert type(self.required_params) is dict, "required_params must be of type dict<str: str>"

        return self.required_params

    def _get_extra_params(self):
        if self.extra_params is None: return dict()

        assert type(self.extra_params) is dict, "extra_params must be of type dict<str: str>"

        return self.extra_params

    def _get_from_request(self, kwargs, serialized_property, required):
        value_from_req = kwargs.get(serialized_property, None)
        if required:
            assert value_from_req is not None, f'{serialized_property} is required'
        
        return value_from_req
        
    def parse_params(self, kwargs):
        req_params = self._get_required_params()
        parsed_params = {}
        
        for db_property, serialized_property in req_params.items():
            val = self._get_from_request(kwargs, serialized_property, True)
            parsed_params[db_property] = val
        
        extra_params = self._get_extra_params()
        for db_property, serialized_property in extra_params.items():
            val = self._get_from_request(kwargs, serialized_property, False)
            if val is None: continue

            parsed_params[db_property] = val

        self._parsed_params = parsed_params
        return parsed_params


    def filter(self, kwargs):
        self._hasError = False
        queryset = self.get_queryset()
        parsed_params = self.parse_params(kwargs)

        return queryset.filter(**parsed_params)

    

