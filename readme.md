# Menu
| Endpoint                   | Role                    | Method                   | Purpose                                                       |
|----------------------------|-------------------------|--------------------------|---------------------------------------------------------------|
| /api/menu-items            | Customer, delivery crew | GET                      | Lists all menu items. Return a 200 – Ok HTTP status code      |
| /api/menu-items            | Customer, delivery crew | POST, PUT, PATCH, DELETE | Denies access and returns 403 – Unauthorized HTTP status code |
| /api/menu-items/{menuItem} | Customer, delivery crew | GET                      | Lists single menu item                                        |
| /api/menu-items/{menuItem} | Customer, delivery crew | POST, PUT, PATCH, DELETE | Returns 403 - Unauthorized                                    |
| /api/menu-items            | Manager                 | GET                      | Lists all menu items                                          |
| /api/menu-items            | Manager                 | POST                     | Creates a new menu item and returns 201 - Created             |
| /api/menu-items/{menuItem} | Manager                 | GET                      | Creates a new menu item and returns 201 - Created             |
| /api/menu-items/{menuItem} | Manager                 | PUT, PATCH               | Updates single menu item                                      |
| /api/menu-items/{menuItem} | Manager                 | DELETE                   | Deletes menu item                                             |