from cart.views.OwnViews import OwnCartItemSingleOpsView, OwnCartItemsView, OwnCartView
from cart.views.OtherViews import AllCartsView, CartItemsSingleOpsView, CartItemsView, CartSingleOPsView


own_cart_view = OwnCartView.as_view()
own_cart_items_view = OwnCartItemsView.as_view()
own_cart_item_single_ops_view = OwnCartItemSingleOpsView.as_view()


list_create_cart_view = AllCartsView.as_view()
cart_single_ops_view = CartSingleOPsView.as_view()
cart_items_view = CartItemsView.as_view()
cart_items_single_ops_view = CartItemsSingleOpsView.as_view()
