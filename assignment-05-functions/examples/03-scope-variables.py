"""
Assignment 5 - Example 3: Scope and Variables
==============================================

This program explores variable scope, lifetime, and the rules that govern
where variables can be accessed in Python programs. Understanding scope
is essential for writing functions that work correctly and predictably.

Key Concepts Demonstrated:
- Local scope vs global scope
- Variable lifetime and creation/destruction
- Global keyword for modifying global variables
- Nonlocal keyword for nested functions
- Scope resolution order (LEGB rule)
- Best practices for variable scope management
"""

print("=== SCOPE AND VARIABLES ===")
print()

print("Variable scope determines where variables can be accessed:")
print("• Local Scope: Inside functions")
print("• Global Scope: At module level")
print("• Enclosing Scope: In nested functions")
print("• Built-in Scope: Python built-in names")
print()

# GLOBAL SCOPE
print("=== GLOBAL SCOPE ===")
print()

# Global variables - accessible throughout the module
global_counter = 0
company_name = "TechCorp Solutions"
max_users = 1000

def display_globals():
    """
    Function that reads global variables.
    Functions can read global variables without special syntax.
    """
    print(f"Company: {company_name}")
    print(f"Max users: {max_users}")
    print(f"Current counter: {global_counter}")

def increment_and_display():
    """
    This function tries to increment global_counter.
    Without 'global' keyword, this creates a local variable.
    """
    global_counter = global_counter + 1  # This will cause an error!
    print(f"Counter incremented to: {global_counter}")

print("Global variables can be read from anywhere:")
print(f"Global counter value: {global_counter}")
display_globals()
print()

print("Attempting to modify global variable without 'global' keyword:")
try:
    increment_and_display()
except UnboundLocalError as e:
    print(f"Error: {e}")
    print("This happens because Python sees assignment and creates local variable")
print()

# LOCAL SCOPE
print("=== LOCAL SCOPE ===")
print()

def calculate_area():
    """
    Function demonstrating local variables.
    Variables created inside functions are local to that function.
    """
    # These are local variables
    length = 10
    width = 5
    area = length * width
    
    print(f"Inside function - Length: {length}, Width: {width}")
    print(f"Inside function - Area: {area}")
    
    return area

def process_user_data():
    """
    Another function with local variables.
    Local variables in different functions don't conflict.
    """
    # Different local variables with same names as above function
    length = 20  # Different from calculate_area's length
    user_name = "Alice"
    user_id = 12345
    
    print(f"Processing user: {user_name} (ID: {user_id})")
    print(f"Data length: {length} characters")
    
    return user_name

print("Local variables exist only within their function:")
area_result = calculate_area()
user_result = process_user_data()

print(f"Area result returned: {area_result}")
print(f"User result returned: {user_result}")

# Trying to access local variables outside their function causes errors
try:
    print(f"Accessing length outside function: {length}")
except NameError as e:
    print(f"Error: {e}")
    print("Local variables are not accessible outside their function")
print()

# GLOBAL KEYWORD
print("=== GLOBAL KEYWORD ===")
print()

# Global variables for demonstration
total_sales = 0
current_user = "guest"
system_status = "offline"

def update_sales(amount):
    """
    Function that modifies a global variable using 'global' keyword.
    """
    global total_sales
    total_sales += amount
    print(f"Added ${amount} to sales. Total now: ${total_sales}")

def change_user(new_user):
    """
    Function that changes the current user.
    """
    global current_user
    old_user = current_user
    current_user = new_user
    print(f"User changed from '{old_user}' to '{current_user}'")

def toggle_system():
    """
    Function that toggles system status.
    """
    global system_status
    if system_status == "online":
        system_status = "offline"
    else:
        system_status = "online"
    print(f"System status changed to: {system_status}")

def display_system_info():
    """
    Function that reads multiple global variables.
    """
    print(f"Current User: {current_user}")
    print(f"Total Sales: ${total_sales}")
    print(f"System Status: {system_status}")

print("Using 'global' keyword to modify global variables:")
print("Initial state:")
display_system_info()
print()

# Modify global variables from functions
update_sales(150.00)
update_sales(75.50)
change_user("admin")
toggle_system()

print("\nFinal state:")
display_system_info()
print()

# NESTED FUNCTIONS AND ENCLOSING SCOPE
print("=== NESTED FUNCTIONS AND ENCLOSING SCOPE ===")
print()

def outer_function(multiplier):
    """
    Outer function that contains a nested function.
    Variables in outer function are in 'enclosing' scope for inner function.
    """
    # This variable is in the enclosing scope
    base_value = 10
    
    print(f"Outer function called with multiplier: {multiplier}")
    
    def inner_function(number):
        """
        Inner function that can access enclosing scope variables.
        """
        # Can access variables from enclosing (outer) function
        result = number * multiplier * base_value
        print(f"Inner function: {number} * {multiplier} * {base_value} = {result}")
        return result
    
    # Call the inner function
    inner_result = inner_function(5)
    return inner_result

def create_counter():
    """
    Function that returns a nested function (closure).
    The inner function remembers the enclosing scope even after outer function returns.
    """
    count = 0
    
    def increment():
        # This would cause an error without 'nonlocal'
        nonlocal count
        count += 1
        return count
    
    return increment

print("Nested functions can access enclosing scope:")
result = outer_function(3)
print(f"Result returned: {result}")
print()

print("Closures remember enclosing scope:")
counter1 = create_counter()
counter2 = create_counter()

print(f"Counter1: {counter1()}")  # 1
print(f"Counter1: {counter1()}")  # 2
print(f"Counter2: {counter2()}")  # 1 (independent counter)
print(f"Counter1: {counter1()}")  # 3
print(f"Counter2: {counter2()}")  # 2
print()

# NONLOCAL KEYWORD
print("=== NONLOCAL KEYWORD ===")
print()

def create_bank_account(initial_balance):
    """
    Create a simple bank account using closures.
    Demonstrates nonlocal keyword usage.
    """
    balance = initial_balance
    
    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            return f"Deposited ${amount}. New balance: ${balance}"
        else:
            return "Deposit amount must be positive"
    
    def withdraw(amount):
        nonlocal balance
        if amount > 0 and amount <= balance:
            balance -= amount
            return f"Withdrew ${amount}. New balance: ${balance}"
        elif amount > balance:
            return f"Insufficient funds. Balance: ${balance}"
        else:
            return "Withdrawal amount must be positive"
    
    def get_balance():
        return f"Current balance: ${balance}"
    
    # Return dictionary of functions that have access to balance
    return {
        'deposit': deposit,
        'withdraw': withdraw,
        'balance': get_balance
    }

def create_settings_manager():
    """
    Create a settings manager that can store and modify configuration.
    """
    settings = {
        'theme': 'light',
        'notifications': True,
        'auto_save': True
    }
    
    def get_setting(key):
        return settings.get(key, "Setting not found")
    
    def set_setting(key, value):
        nonlocal settings
        old_value = settings.get(key, "Not set")
        settings[key] = value
        return f"Changed '{key}' from '{old_value}' to '{value}'"
    
    def get_all_settings():
        return dict(settings)  # Return a copy
    
    def reset_settings():
        nonlocal settings
        settings = {
            'theme': 'light',
            'notifications': True,
            'auto_save': True
        }
        return "Settings reset to defaults"
    
    return {
        'get': get_setting,
        'set': set_setting,
        'all': get_all_settings,
        'reset': reset_settings
    }

print("Using nonlocal to modify enclosing scope variables:")

# Bank account example
account = create_bank_account(100)
print(account['balance']())
print(account['deposit'](50))
print(account['withdraw'](25))
print(account['withdraw'](200))  # Insufficient funds
print()

# Settings manager example
settings = create_settings_manager()
print("Initial settings:", settings['all']())
print(settings['set']('theme', 'dark'))
print(settings['set']('notifications', False))
print("Updated settings:", settings['all']())
print(settings['reset']())
print("After reset:", settings['all']())
print()

# SCOPE RESOLUTION ORDER (LEGB RULE)
print("=== SCOPE RESOLUTION ORDER (LEGB RULE) ===")
print()

# Built-in scope: Python's built-in functions and constants
# Global scope: Module-level variables
name = "Global Name"
value = "Global Value"

def demonstrate_legb():
    """
    Demonstrate Local, Enclosing, Global, Built-in (LEGB) scope resolution.
    """
    # Enclosing scope variable
    name = "Enclosing Name"
    
    def inner_demo():
        # Local scope variable
        name = "Local Name" 
        
        print("=== LEGB Scope Resolution Demo ===")
        print(f"Local variable 'name': {name}")
        print(f"Global variable 'value': {value}")  # Accessed from global scope
        print(f"Built-in function 'len': {len}")     # Accessed from built-in scope
        
        # Demonstrating scope lookup
        def show_scope_lookup():
            # No local 'name', so looks in enclosing scope
            print(f"From inner function, 'name' resolves to: {name}")  # Local 'name'
        
        show_scope_lookup()
    
    # Call inner function
    inner_demo()
    
    # At this level, 'name' is the enclosing scope variable
    print(f"In enclosing scope, 'name' is: {name}")

print("LEGB Rule: Local → Enclosing → Global → Built-in")
demonstrate_legb()
print(f"At global level, 'name' is: {name}")
print()

# VARIABLE LIFETIME DEMONSTRATION
print("=== VARIABLE LIFETIME ===")
print()

def demonstrate_lifetime():
    """
    Demonstrate how variables are created and destroyed.
    """
    print("Function started - local variables created")
    local_var = "I exist only during function execution"
    temporary_list = [1, 2, 3, 4, 5]
    
    print(f"Local variable: {local_var}")
    print(f"Temporary list: {temporary_list}")
    
    def inner_lifetime():
        inner_var = "I exist only during inner function execution"
        print(f"Inner variable: {inner_var}")
        return "Inner function completed"
    
    result = inner_lifetime()
    print(f"Inner function result: {result}")
    # inner_var is destroyed when inner_lifetime() finishes
    
    print("Function ending - local variables will be destroyed")
    return "Function completed"

print("Demonstrating variable lifetime:")
final_result = demonstrate_lifetime()
print(f"Final result: {final_result}")
# All local variables from demonstrate_lifetime() are now destroyed
print()

# BEST PRACTICES FOR SCOPE MANAGEMENT
print("=== BEST PRACTICES FOR SCOPE MANAGEMENT ===")
print()

def well_designed_function(input_data):
    """
    Example of well-designed function with clear scope management.
    
    Best Practices Demonstrated:
    1. Clear parameter names
    2. Local variables for calculations
    3. Minimal global variable access
    4. Return values instead of modifying globals
    5. Clear variable naming
    """
    # Use descriptive local variable names
    processed_data = []
    error_count = 0
    
    for item in input_data:
        try:
            # Process each item locally
            cleaned_item = str(item).strip().upper()
            if cleaned_item:
                processed_data.append(cleaned_item)
            else:
                error_count += 1
        except Exception:
            error_count += 1
    
    # Return results instead of modifying global state
    return {
        'processed': processed_data,
        'errors': error_count,
        'success_rate': (len(processed_data) / len(input_data)) * 100 if input_data else 0
    }

def configuration_manager():
    """
    Example of managing state through closures instead of global variables.
    """
    config = {
        'debug_mode': False,
        'max_retries': 3,
        'timeout': 30
    }
    
    def get_config():
        return config.copy()  # Return copy to prevent external modification
    
    def update_config(**updates):
        nonlocal config
        for key, value in updates.items():
            if key in config:
                config[key] = value
        return get_config()
    
    return get_config, update_config

# Avoid this - poor scope management
poorly_managed_global = []

def bad_function(item):
    """
    Example of poor scope management - modifies global state directly.
    """
    global poorly_managed_global
    poorly_managed_global.append(item)  # Bad: modifies global state

# Prefer this - good scope management
def good_function(current_list, new_item):
    """
    Example of good scope management - returns new state.
    """
    updated_list = current_list.copy()
    updated_list.append(new_item)
    return updated_list

print("Demonstrating best practices:")

# Good scope management
test_data = ["  apple  ", "BANANA", "", "cherry", None, 123]
result = well_designed_function(test_data)
print(f"Processed {len(result['processed'])} items with {result['errors']} errors")
print(f"Success rate: {result['success_rate']:.1f}%")
print(f"Results: {result['processed']}")
print()

# Configuration management with closures
get_config, update_config = configuration_manager()
print("Initial config:", get_config())
print("Updated config:", update_config(debug_mode=True, timeout=60))
print()

# Comparison of good vs bad practices
my_list = [1, 2, 3]

# Bad approach - modifies global
bad_function(4)
print(f"After bad_function: {poorly_managed_global}")

# Good approach - returns new state
my_list = good_function(my_list, 4)
print(f"After good_function: {my_list}")
print()

print("=== SUMMARY ===")
print()
print("Scope and Variable Management Summary:")
print("1. Local scope: Variables inside functions")
print("2. Global scope: Variables at module level")
print("3. Use 'global' keyword to modify global variables")
print("4. Use 'nonlocal' keyword to modify enclosing scope variables")
print("5. LEGB rule: Local → Enclosing → Global → Built-in")
print("6. Variables have limited lifetime based on their scope")
print("7. Prefer local variables and return values over global state")
print("8. Use closures for maintaining state without global variables")

"""
KEY TAKEAWAYS:
==============
1. Scope determines where variables can be accessed
2. Local variables are created when functions are called
3. Global variables persist for the program's lifetime
4. Use 'global' keyword to modify global variables in functions
5. Use 'nonlocal' keyword to modify enclosing scope variables
6. LEGB rule governs scope resolution order
7. Good scope management improves code maintainability

SCOPE TYPES:
============
• Local: Inside current function
• Enclosing: In outer function (for nested functions)
• Global: At module level
• Built-in: Python's built-in namespace

BEST PRACTICES:
===============
• Minimize global variable usage
• Use function parameters and return values
• Keep variables in smallest appropriate scope
• Use descriptive variable names
• Prefer closures over global state for stateful functions
• Return new values instead of modifying global state
• Use constants for global configuration values

COMMON PITFALLS:
================
• Forgetting 'global' keyword when modifying global variables
• Name conflicts between local and global variables
• Unintended variable shadowing in nested functions
• Modifying mutable global objects without 'global' keyword
• Creating accidental global variables through typos

NEXT STEP:
Go to 04-advanced-functions.py to explore nested functions, lambda, and recursion!
"""