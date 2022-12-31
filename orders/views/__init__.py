from .OwnOrderViews import OwnOrdersGetCreateView, OwnOrderSingleOperations
from .OtherOrderViews import AllOrdersView

own_orders_get_create_view = OwnOrdersGetCreateView.as_view()
own_orders_single_ops = OwnOrderSingleOperations.as_view()

all_orders_view = AllOrdersView.as_view()