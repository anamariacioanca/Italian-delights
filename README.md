# Italian-delights
Inventory - Cafe Management Application

Inventory is an application designed to assist cafe managers in simplifying inventory management, tracking products, and handling orders. It also provides daily and total sales reports. The application is divided into two main areas: Administration and Users. The Users area, in turn, is divided into two categories: Manager and Waiters, with users in these categories having differentiated access to the application's functionalities.

1. Administration Area
In the administration area, new users can be added, depending on their role (Manager or Waiter). The application can only be accessed by users added here. Additionally, in the administration area, you can add, modify, and delete ingredients, menus, orders, and sales reports. Deleting and modifying sales reports is only possible from the administration area.

2. Area Dedicated to Users
The application can be accessed only if the user has been added in the administration area. After login, the user will have access to the application's functionalities based on the permissions set in the administration area. For users in the Manager category, after logging in, they can add, modify, and delete ingredients, menu items, and orders. They can also view the sales report, both daily and total. For users in the Waiters category, after logging in, they can view ingredients, menu items, and the sales report. They can add, modify, and delete orders.

Technologies Used:
Python
Django
Docker
Bootstrap
