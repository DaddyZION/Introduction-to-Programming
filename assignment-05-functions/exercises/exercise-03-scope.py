"""
Assignment 5 - Exercise 3: Scope and Variables
Difficulty: 🟡 Intermediate

TODO: Practice understanding variable scope and lifetime.

This exercise explores local vs global scope and variable shadowing.
"""

# Global variables
counter = 0
app_name = "My Application"
settings = {"theme": "dark", "language": "en"}


# ==================== FUNCTION 1: Increment Counter ====================
def increment_counter():
    """
    Increment the global counter variable.
    
    Requirements:
    - Use the global keyword
    - Increment counter by 1
    - Return the new value
    
    Test: Call multiple times and observe counter value
    """
    # TODO: Implement this function using 'global' keyword
    pass


# ==================== FUNCTION 2: Local vs Global ====================
def demonstrate_scope():
    """
    Demonstrate the difference between local and global variables.
    
    Requirements:
    - Create a local variable with the same name as a global
    - Modify the local variable
    - Show that global variable is unchanged
    - Return both values as a tuple (local_value, global_value)
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Modify Settings ====================
def update_setting(key, value):
    """
    Update a value in the global settings dictionary.
    
    Requirements:
    - Modify the global settings dictionary
    - Add or update the key-value pair
    - Return True if successful
    
    Note: Dictionaries don't need 'global' keyword to modify contents
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Nested Function Scope ====================
def outer_function(x):
    """
    Demonstrate nested function scope.
    
    Requirements:
    - Create a local variable y = 10
    - Define an inner function that uses both x and y
    - Inner function should return x + y
    - Outer function returns the result of calling inner function
    
    Test Cases:
    - outer_function(5) → 15
    - outer_function(20) → 30
    """
    # TODO: Implement this function with nested inner function
    pass


# ==================== FUNCTION 5: Counter Generator ====================
def create_counter(start=0):
    """
    Create a counter function using closures.
    
    Requirements:
    - Initialize count variable with start value
    - Return a nested function that:
      * Increments count each time it's called
      * Returns the current count
    - Each counter should maintain its own state
    
    Example usage:
    counter1 = create_counter(0)
    counter2 = create_counter(100)
    print(counter1())  # 1
    print(counter1())  # 2
    print(counter2())  # 101
    """
    # TODO: Implement this function using closures
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Scope and Variables ===\n")
    
    # Test increment_counter
    print("Test 1: Increment Counter")
    print(f"  Initial counter: {counter}")
    # print(f"  After increment: {increment_counter()}")
    # print(f"  After increment: {increment_counter()}")
    # print(f"  Global counter: {counter}")
    
    # Test demonstrate_scope
    print("\nTest 2: Local vs Global Scope")
    # result = demonstrate_scope()
    # print(f"  Result: {result}")
    
    # Test update_setting
    print("\nTest 3: Modify Settings")
    print(f"  Initial settings: {settings}")
    # update_setting("theme", "light")
    # update_setting("font_size", 14)
    # print(f"  Updated settings: {settings}")
    
    # Test outer_function
    print("\nTest 4: Nested Function Scope")
    # print(f"  outer_function(5) = {outer_function(5)}")
    # print(f"  outer_function(20) = {outer_function(20)}")
    
    # Test create_counter
    print("\nTest 5: Counter Generator (Closures)")
    # counter1 = create_counter(0)
    # counter2 = create_counter(100)
    # print(f"  counter1(): {counter1()}")
    # print(f"  counter1(): {counter1()}")
    # print(f"  counter2(): {counter2()}")
    # print(f"  counter1(): {counter1()}")
