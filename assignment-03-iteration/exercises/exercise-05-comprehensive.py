"""
Assignment 3 - Exercise 5: Comprehensive Challenge
Difficulty: 🔴 Expert

TODO: Create a complete inventory management system.

This is a comprehensive exercise combining all iteration concepts:
- For loops and while loops
- Nested loops for data processing
- Loop control (break, continue)
- Menu-driven interface
- Input validation
- List manipulation

INVENTORY MANAGEMENT SYSTEM
============================

Create a program that manages a store inventory with the following features:

MENU OPTIONS:
1. Add new product
2. Update product quantity
3. View all products
4. Search for product
5. Generate inventory report
6. Remove out-of-stock items
7. Calculate total inventory value
8. Exit

DATA STRUCTURE:
- Store products as a list of lists
- Each product: [name, quantity, price]
- Example: ["Laptop", 5, 899.99]

REQUIREMENTS:
-------------
1. ADD NEW PRODUCT:
   - Ask for product name, quantity, and price
   - Validate: quantity >= 0, price > 0
   - Check if product already exists (case-insensitive)
   - If exists, ask if user wants to update instead

2. UPDATE PRODUCT QUANTITY:
   - Display all products with numbers
   - Ask which product to update
   - Ask for new quantity (can add or replace)
   - Validate input

3. VIEW ALL PRODUCTS:
   - Display in table format
   - Show: Number, Name, Quantity, Price, Total Value
   - Sort by name

4. SEARCH FOR PRODUCT:
   - Ask for search term
   - Display all matching products (partial match)
   - Case-insensitive search

5. GENERATE INVENTORY REPORT:
   - Total number of products
   - Total number of items in stock
   - Total inventory value
   - Most expensive product
   - Product with highest quantity
   - Products below reorder level (< 5 units)

6. REMOVE OUT-OF-STOCK ITEMS:
   - Find products with quantity = 0
   - Ask for confirmation
   - Remove from inventory

7. CALCULATE TOTAL INVENTORY VALUE:
   - Sum of (quantity × price) for all products

8. EXIT:
   - Display summary
   - Ask for confirmation

Example Output:
--------------
=== INVENTORY MANAGEMENT SYSTEM ===
1. Add new product
2. Update product quantity
3. View all products
4. Search for product
5. Generate inventory report
6. Remove out-of-stock items
7. Calculate total inventory value
8. Exit

Enter choice (1-8): 1
Enter product name: Laptop
Enter quantity: 5
Enter price: 899.99
Product added successfully!

Enter choice (1-8): 1
Enter product name: Mouse
Enter quantity: 20
Enter price: 19.99
Product added successfully!

Enter choice (1-8): 3
=== ALL PRODUCTS ===
No. | Name         | Quantity | Price    | Total Value
----|--------------|----------|----------|------------
1   | Laptop       | 5        | $899.99  | $4,499.95
2   | Mouse        | 20       | $19.99   | $399.80
----|--------------|----------|----------|------------
Total Products: 2                Total Value: $4,899.75

Enter choice (1-8): 5
=== INVENTORY REPORT ===
Total Products: 2
Total Items in Stock: 25
Total Inventory Value: $4,899.75
Most Expensive: Laptop ($899.99)
Highest Quantity: Mouse (20 units)
Products Below Reorder Level: None

Enter choice (1-8): 8
Are you sure you want to exit? (yes/no): yes
Thank you for using the Inventory Management System!
"""

# TODO: Initialize inventory list


# TODO: Define menu display function


# TODO: Define add product function


# TODO: Define update quantity function


# TODO: Define view all products function


# TODO: Define search product function


# TODO: Define generate report function


# TODO: Define remove out-of-stock function


# TODO: Define calculate total value function


# TODO: Main program loop with menu


# TODO: Handle each menu option


# TODO: Validate all inputs


# TODO: Exit with confirmation
