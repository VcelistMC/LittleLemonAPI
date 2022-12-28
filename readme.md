# Menu
| Endpoint                   | Role                    | Method                   | Purpose                                                       |
|----------------------------|-------------------------|--------------------------|---------------------------------------------------------------|
| `/api/menu`            | Customer, delivery crew, Manager | GET                      | Lists all menu items. Return a 200 – Ok HTTP status code      |
| `/api/menu`            | Customer, delivery crew | POST, PUT, PATCH, DELETE | Denies access and returns 403 – Unauthorized HTTP status code |
| `/api/menu/{itemId}` | Customer, delivery crew, Manager | GET                      | Lists single menu item                                        |
| `/api/menu/{itemId}` | Customer, delivery crew | POST, PUT, PATCH, DELETE | Returns 403 - Unauthorized                                    |
| `/api/menu`            | Manager                 | POST                     | Creates a new menu item and returns 201 - Created             |
| `/api/menu/{itemId}` | Manager                 | PUT, PATCH               | Updates single menu item                                      |
| `/api/menu/{itemId}` | Manager                 | DELETE                   | Deletes menu item                                             |

# Groups

| Endpoint                                 | Role    | Method | Purpose                                                                                                                                                |                 |
|------------------------------------------|---------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| `/api/groups/manager/users`                | Manager | GET    | Returns all managers                                                                                                                                   |                 |
| `/api/groups/manager/users`                | Manager | POST   | Assigns the user in the payload to the manager group and returns 201-Created                                                                           |                 |
| `/api/groups/manager/users/{userId}`       | Manager | DELETE | Removes this particular user from the manager group and returns 200 – Success if everything is okay. If the user is not found, returns 404 – Not found |                 |
| `/api/groups/delivery-crew/users`          | Manager | GET    | Returns all delivery crew                                                                                                                              |                 |
| `/api/groups/delivery-crew/users`          | Manager | POST   | Assigns the user in the payload to delivery crew group and returns 201-Created HTTP                                                                    |                 |
| `/api/groups/delivery-crew/users/{userId}` | Manager | DELETE | Removes this user from the manager group and returns 200 – Success if everything is okay. If the user is not found, returns                            | 404 – Not found |

# Cart
| Endpoint | Role | Method | Purpose |
|---|---|---|---|
| `cart/` | Manager | GET | List all carts |
| `cart/me` | ALL | GET | get cart for current user |
| `cart/me/items` | ALL | GET, POST | lists all items or adds an item to current user cart |
| `cart/me/items/{itemId}` | ALL | GET, DELETE, PATCH | gets, patches or deletes an item from current user cart |
| `cart/{cartId}` | Manager | GET | get cart of cart id |
| `cart/{cartId}/items` | Manager | POST | adds an item to user cart |
| `cart/{cartId}/items/{itemId}` | Manager | GET, DELETE, PATCH | gets, patches or deletes an item from user cart | cart |                                       |

# Orders
| Endpoint | Role | Method | Purpose |
|---|---|---|---|
| `/api/orders` | Manager | GET | Returns all orders with order items by all users |
| `/api/orders` | Delivery crew | GET | Returns all orders with order items assigned to the delivery crew |
| `/api/orders/{orderId}` | Manager | PATCH, DELETE | Assign a delevery crew or optionally change the status of the order, allowed values are `PENDING` or `DELIVERED` or deletes the order |
| `/api/orders/{orderId}` | Delivery crew | PATCH | A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order. |
| `/api/orders/me` | ALL | GET, POST | Returns all orders with order items created by the current user or creates a new order with all items in the current user cart and empties it |
| `/api/orders/me/{orderId}` | ALL | GET, DELETE | Returns all items for this order id. |