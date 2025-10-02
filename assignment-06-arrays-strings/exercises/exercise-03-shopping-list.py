"""
Assignment 6 - Exercise 3: Shopping List Manager
Difficulty: 🟡 Intermediate

TODO: Create a shopping list manager with add, remove, search, and display features.

Requirements:
1. Add items to list
2. Remove items from list
3. Display list in alphabetical order
4. Find items containing specific text
5. Optional: Calculate total if prices are included
"""

# Shopping list will be a list of dictionaries
# Each item: {'name': str, 'quantity': int, 'price': float (optional)}


# ==================== FUNCTION 1: Add Item ====================
def add_item(shopping_list, item_name, quantity=1, price=None):
    """
    Add an item to the shopping list.
    
    Requirements:
    - If item already exists, increase quantity
    - Otherwise, add new item
    - Return True if successful
    
    Parameters:
    - shopping_list: list of item dictionaries
    - item_name: string
    - quantity: integer (default 1)
    - price: float or None
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Remove Item ====================
def remove_item(shopping_list, item_name):
    """
    Remove an item from the shopping list.
    
    Requirements:
    - Find and remove item by name (case-insensitive)
    - Return True if found and removed
    - Return False if not found
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Find Items ====================
def find_items(shopping_list, search_term):
    """
    Find all items containing the search term.
    
    Requirements:
    - Case-insensitive search
    - Partial match
    - Return list of matching items
    
    Example:
    Items: ['apple', 'pineapple', 'banana']
    search_term: 'apple'
    Returns: ['apple', 'pineapple']
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Display List ====================
def display_list(shopping_list, sort=True):
    """
    Display the shopping list in a formatted manner.
    
    Format:
    === SHOPPING LIST ===
    1. Apples x2 - $3.50
    2. Bananas x5 - $6.25
    3. Milk x1
    -------------------
    Total Items: 3
    Total Cost: $9.75 (if prices available)
    
    Parameters:
    - shopping_list: list of items
    - sort: boolean, whether to sort alphabetically
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Calculate Total ====================
def calculate_total(shopping_list):
    """
    Calculate total cost of items with prices.
    
    Returns: float (total cost)
    Note: Only includes items that have prices
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Update Quantity ====================
def update_quantity(shopping_list, item_name, new_quantity):
    """
    Update the quantity of an existing item.
    
    Requirements:
    - Find item by name (case-insensitive)
    - Update quantity
    - If quantity is 0, remove the item
    - Return True if successful, False if not found
    """
    # TODO: Implement this function
    pass


# ==================== MAIN PROGRAM ====================
def main():
    """
    Interactive shopping list manager.
    
    Menu:
    1. Add item
    2. Remove item
    3. Update quantity
    4. Search items
    5. Display list
    6. Clear list
    7. Exit
    """
    shopping_list = []
    
    print("=== Shopping List Manager ===\n")
    
    # TODO: Implement menu loop
    # TODO: Handle each option
    # TODO: Validate inputs
    
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    # Test with sample data
    test_list = []
    
    print("Testing Shopping List Manager:\n")
    
    print("Test 1: Adding items")
    # add_item(test_list, "Apples", 2, 3.50)
    # add_item(test_list, "Bananas", 5, 6.25)
    # add_item(test_list, "Milk", 1)
    # display_list(test_list)
    
    print("\nTest 2: Searching")
    # results = find_items(test_list, "apple")
    # print(f"  Items containing 'apple': {results}")
    
    print("\nTest 3: Updating quantity")
    # update_quantity(test_list, "Apples", 5)
    # display_list(test_list)
    
    print("\nTest 4: Removing item")
    # remove_item(test_list, "Bananas")
    # display_list(test_list)
    
    print("\nTo run interactive program:")
    print("  Uncomment: main()")
    # main()
