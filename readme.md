# Little Lemon Restraunt REST API

A restraunt api made in django as a captstone project for the REST APIs course from the META backend specialization

## Installation
You can either use pipenv to install the required packages by running
```
pip install requirements.txt
```
or you can use pip by running
```
pipenv install
```
then start the virtual enviroment by using
```
pipenv shell
```

Finally, start the project by running
```
python manage.py runserver
```

## Usage
The baseurl for all the endpoints is `{hostUrl}/api`

### Menu
| Endpoint | Role | Method | Purpose |
|---|---|---|---|
| `/menu` | Customer, delivery crew, Manager | GET | Lists all menu items. Return a 200 – Ok HTTP status code |
| `/menu` | Customer, delivery crew | POST, PUT, PATCH, DELETE | Denies access and returns 403 – Unauthorized HTTP status code |
| `/menu/{itemId}` | Customer, delivery crew, Manager | GET | Lists single menu item |
| `/menu/{itemId}` | Customer, delivery crew | POST, PUT, PATCH, DELETE | Returns 403 - Unauthorized |
| `/menu` | Manager | POST | Creates a new menu item and returns 201 - Created |
| `/menu/{itemId}` | Manager | PUT, PATCH | Updates single menu item |
| `/menu/{itemId}` | Manager | DELETE | Deletes menu item |                                             

### Groups

| Endpoint | Role | Method | Purpose |
|---|---|---|---|
| `/api/groups/manager/users` | Manager | GET | Returns all managers |
| `/api/groups/manager/users` | Manager | POST | Assigns the user in the payload to the manager group and returns 201-Created |
| `/api/groups/manager/users/{userId}` | Manager | DELETE | Removes this particular user from the manager group and returns 200 – Success if everything is okay. If the user is not found, returns 404 – Not found |
| `/api/groups/delivery-crew/users` | Manager | GET | Returns all delivery crew |
| `/api/groups/delivery-crew/users` | Manager | POST | Assigns the user in the payload to delivery crew group and returns 201-Created HTTP |
| `/api/groups/delivery-crew/users/{userId}` | Manager | DELETE | Removes this user from the manager group and returns 200 – Success if everything is okay. If the user is not found |
                          
### Cart
| Endpoint | Role | Method | Purpose |
|---|---|---|---|
| `/cart/` | Manager | GET | List all carts |
| `/cart/me` | ALL | GET | get cart for current user |
| `/cart/me/items` | ALL | GET, POST | lists all items or adds an item to current user cart |
| `/cart/me/items/{itemId}` | ALL | GET, DELETE, PATCH | gets, patches or deletes an item from current user cart |
| `/cart/{cartId}` | Manager | GET | get cart of cart id |
| `/cart/{cartId}/items` | Manager | POST | adds an item to user cart |
| `/cart/{cartId}/items/{itemId}` | Manager | GET, DELETE, PATCH | gets, patches or deletes an item from user cart | cart |                                       |

### Orders
| Endpoint | Role | Method | Purpose |
|---|---|---|---|
| `/orders` | Manager | GET | Returns all orders with order items by all users |
| `/orders` | Delivery crew | GET | Returns all orders with order items assigned to the delivery crew |
| `/orders/{orderId}` | Manager | PATCH, DELETE | Assign a delevery crew or optionally change the status of the order, allowed values are `PENDING` or `DELIVERED` or deletes the order |
| `/orders/{orderId}` | Delivery crew | PATCH | A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order. |
| `/orders/me` | ALL | GET, POST | Returns all orders with order items created by the current user or creates a new order with all items in the current user cart and empties it |
| `/orders/me/{orderId}` | ALL | GET, DELETE | Returns all items for this order id. |