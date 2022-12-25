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