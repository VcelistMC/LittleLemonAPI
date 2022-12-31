from .OwnOrderViews import OwnOrdersGetCreateView, OwnOrderSingleOperations
from .OtherOrderViews import AllOrdersView, OrdersSingleOpsView

own_orders_get_create_view = OwnOrdersGetCreateView.as_view()
own_orders_single_ops = OwnOrderSingleOperations.as_view()

all_orders_view = AllOrdersView.as_view()
orders_single_ops_view = OrdersSingleOpsView.as_view()