"""
Assignment 5 - Example 2: Parameters and Arguments
===================================================

This program explores the different types of function parameters and
argument passing mechanisms in Python. Understanding parameters is crucial
for creating flexible, reusable functions that can handle various inputs.

Key Concepts Demonstrated:
- Required positional parameters
- Default parameter values
- Keyword arguments
- Variable-length arguments (*args)
- Keyword variable-length arguments (**kwargs)
- Parameter order rules
- Argument unpacking
"""

print("=== PARAMETERS AND ARGUMENTS ===")
print()

print("Parameters vs Arguments:")
print("• Parameters: Variables in function definition")
print("• Arguments: Actual values passed when calling function")
print("• Python offers flexible parameter mechanisms for different needs")
print()

# REQUIRED POSITIONAL PARAMETERS
print("=== REQUIRED POSITIONAL PARAMETERS ===")
print()

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index from weight and height.
    Both parameters are required and positional.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        float: BMI value rounded to 2 decimal places
    """
    bmi = weight / (height * height)
    return round(bmi, 2)

def format_name(first, middle, last):
    """
    Format a full name from three required parts.
    
    Args:
        first (str): First name
        middle (str): Middle name or initial
        last (str): Last name
    
    Returns:
        str: Formatted full name
    """
    return f"{first} {middle} {last}"

print("Required positional parameters must be provided in order:")
print()

# All required parameters must be provided
bmi = calculate_bmi(70, 1.75)  # weight=70kg, height=1.75m
print(f"BMI for 70kg, 1.75m person: {bmi}")

name = format_name("John", "Michael", "Smith")
print(f"Formatted name: {name}")
print()

# This would cause an error - missing required parameters:
# bmi = calculate_bmi(70)  # Missing height parameter
# name = format_name("John")  # Missing middle and last name

# DEFAULT PARAMETERS
print("=== DEFAULT PARAMETER VALUES ===")
print()

def greet_user(name, greeting="Hello", punctuation="!"):
    """
    Greet a user with customizable greeting and punctuation.
    
    Args:
        name (str): User's name (required)
        greeting (str, optional): Greeting word. Defaults to "Hello".
        punctuation (str, optional): End punctuation. Defaults to "!".
    
    Returns:
        str: Complete greeting message
    """
    return f"{greeting}, {name}{punctuation}"

def calculate_discount(price, discount_percent=10, tax_rate=8.5):
    """
    Calculate final price after discount and tax.
    
    Args:
        price (float): Original price (required)
        discount_percent (float, optional): Discount percentage. Defaults to 10.
        tax_rate (float, optional): Tax rate percentage. Defaults to 8.5.
    
    Returns:
        float: Final price after discount and tax
    """
    discounted_price = price * (1 - discount_percent / 100)
    final_price = discounted_price * (1 + tax_rate / 100)
    return round(final_price, 2)

def create_user_profile(username, email, role="user", active=True):
    """
    Create a user profile with default values.
    
    Args:
        username (str): Username (required)
        email (str): Email address (required)
        role (str, optional): User role. Defaults to "user".
        active (bool, optional): Account status. Defaults to True.
    
    Returns:
        dict: User profile dictionary
    """
    return {
        'username': username,
        'email': email,
        'role': role,
        'active': active,
        'created_at': '2024-01-15'  # Would be current timestamp in real app
    }

print("Default parameters provide flexibility in function calls:")
print()

# Using default parameters
print(greet_user("Alice"))                        # Uses default greeting and punctuation
print(greet_user("Bob", "Hi"))                    # Custom greeting, default punctuation
print(greet_user("Charlie", "Hey", "."))          # Custom greeting and punctuation
print()

# Price calculation with different parameter combinations
print("Price calculations with defaults:")
print(f"$100 with defaults: ${calculate_discount(100)}")
print(f"$100 with 20% discount: ${calculate_discount(100, 20)}")
print(f"$100 with 15% discount, 5% tax: ${calculate_discount(100, 15, 5)}")
print()

# User profile creation
user1 = create_user_profile("john_doe", "john@example.com")
user2 = create_user_profile("admin_user", "admin@company.com", "admin")
user3 = create_user_profile("temp_user", "temp@test.com", "guest", False)

print("User profiles:")
for user in [user1, user2, user3]:
    print(f"  {user['username']}: {user['role']}, active: {user['active']}")
print()

# KEYWORD ARGUMENTS
print("=== KEYWORD ARGUMENTS ===")
print()

def book_flight(passenger, departure, destination, date, seat_class="economy", meal="standard"):
    """
    Book a flight with various options.
    
    Args:
        passenger (str): Passenger name
        departure (str): Departure city
        destination (str): Destination city
        date (str): Flight date
        seat_class (str, optional): Seat class. Defaults to "economy".
        meal (str, optional): Meal preference. Defaults to "standard".
    
    Returns:
        dict: Flight booking details
    """
    return {
        'passenger': passenger,
        'route': f"{departure} -> {destination}",
        'date': date,
        'class': seat_class,
        'meal': meal,
        'booking_id': f"FL{hash(passenger + date) % 10000:04d}"
    }

def configure_server(hostname, port, ssl_enabled=False, backup_enabled=True, 
                    max_connections=100, timeout=30):
    """
    Configure server settings with many optional parameters.
    
    Args:
        hostname (str): Server hostname
        port (int): Server port
        ssl_enabled (bool, optional): Enable SSL. Defaults to False.
        backup_enabled (bool, optional): Enable backups. Defaults to True.
        max_connections (int, optional): Max connections. Defaults to 100.
        timeout (int, optional): Connection timeout. Defaults to 30.
    
    Returns:
        dict: Server configuration
    """
    return {
        'hostname': hostname,
        'port': port,
        'ssl_enabled': ssl_enabled,
        'backup_enabled': backup_enabled,
        'max_connections': max_connections,
        'timeout': timeout
    }

print("Keyword arguments allow calling parameters by name:")
print()

# Using keyword arguments for clarity
flight1 = book_flight(
    passenger="Alice Johnson",
    departure="New York",
    destination="London",
    date="2024-06-15",
    seat_class="business",
    meal="vegetarian"
)

# Mix of positional and keyword arguments
flight2 = book_flight("Bob Smith", "Chicago", "Tokyo", "2024-07-20", meal="kosher")

# Keywords can be in any order
flight3 = book_flight(
    meal="halal",
    passenger="Carol Davis",
    seat_class="first",
    date="2024-08-10",
    destination="Dubai", 
    departure="Los Angeles"
)

print("Flight bookings:")
for flight in [flight1, flight2, flight3]:
    print(f"  {flight['passenger']}: {flight['route']} on {flight['date']}")
    print(f"    Class: {flight['class']}, Meal: {flight['meal']}, ID: {flight['booking_id']}")
print()

# Server configuration with selective keyword arguments
server1 = configure_server("web01.company.com", 8080)
server2 = configure_server("api.service.com", 443, ssl_enabled=True, max_connections=500)
server3 = configure_server(hostname="db.internal.com", port=5432, backup_enabled=False)

print("Server configurations:")
for i, config in enumerate([server1, server2, server3], 1):
    print(f"  Server {i}: {config['hostname']}:{config['port']}")
    print(f"    SSL: {config['ssl_enabled']}, Max conn: {config['max_connections']}")
print()

# VARIABLE-LENGTH ARGUMENTS (*args)
print("=== VARIABLE-LENGTH ARGUMENTS (*args) ===")
print()

def calculate_sum(*numbers):
    """
    Calculate the sum of any number of arguments.
    
    Args:
        *numbers: Variable number of numeric arguments
    
    Returns:
        float: Sum of all provided numbers
    """
    total = 0
    for number in numbers:
        total += number
    return total

def find_maximum(*values):
    """
    Find the maximum value from any number of arguments.
    
    Args:
        *values: Variable number of comparable values
    
    Returns:
        The maximum value, or None if no values provided
    """
    if not values:
        return None
    
    max_value = values[0]
    for value in values[1:]:
        if value > max_value:
            max_value = value
    return max_value

def create_report(title, *content_sections):
    """
    Create a report with a title and variable content sections.
    
    Args:
        title (str): Report title
        *content_sections: Variable number of content sections
    
    Returns:
        str: Formatted report
    """
    report = f"=== {title.upper()} ===\n\n"
    
    for i, section in enumerate(content_sections, 1):
        report += f"Section {i}: {section}\n"
    
    return report

print("*args allows functions to accept any number of arguments:")
print()

# Functions with variable arguments
print(f"Sum of 1, 2, 3: {calculate_sum(1, 2, 3)}")
print(f"Sum of 1, 2, 3, 4, 5: {calculate_sum(1, 2, 3, 4, 5)}")
print(f"Sum of single number: {calculate_sum(42)}")
print(f"Sum of no numbers: {calculate_sum()}")
print()

print(f"Maximum of 5, 2, 8, 1: {find_maximum(5, 2, 8, 1)}")
print(f"Maximum of strings: {find_maximum('apple', 'banana', 'cherry')}")
print(f"Maximum of no values: {find_maximum()}")
print()

# Report generation with variable content
report = create_report(
    "Monthly Sales Report",
    "Total revenue increased by 15%",
    "New customers: 1,247",
    "Top selling product: Premium Widget",
    "Regional performance varies significantly"
)
print(report)

# KEYWORD VARIABLE-LENGTH ARGUMENTS (**kwargs)
print("=== KEYWORD VARIABLE-LENGTH ARGUMENTS (**kwargs) ===")
print()

def create_database_connection(host, port, **config):
    """
    Create database connection with flexible configuration.
    
    Args:
        host (str): Database host
        port (int): Database port
        **config: Additional configuration parameters
    
    Returns:
        dict: Database connection configuration
    """
    connection_config = {
        'host': host,
        'port': port,
        'connected': True
    }
    
    # Add all additional keyword arguments
    for key, value in config.items():
        connection_config[key] = value
    
    return connection_config

def log_event(level, message, **metadata):
    """
    Log an event with optional metadata.
    
    Args:
        level (str): Log level (INFO, WARNING, ERROR)
        message (str): Log message
        **metadata: Additional metadata fields
    
    Returns:
        str: Formatted log entry
    """
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"[{timestamp}] {level}: {message}"
    
    if metadata:
        meta_str = ", ".join(f"{k}={v}" for k, v in metadata.items())
        log_entry += f" ({meta_str})"
    
    return log_entry

def build_api_url(base_url, endpoint, **params):
    """
    Build API URL with query parameters.
    
    Args:
        base_url (str): Base API URL
        endpoint (str): API endpoint
        **params: Query parameters
    
    Returns:
        str: Complete API URL with parameters
    """
    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
    
    if params:
        param_pairs = []
        for key, value in params.items():
            param_pairs.append(f"{key}={value}")
        url += "?" + "&".join(param_pairs)
    
    return url

print("**kwargs allows functions to accept any number of keyword arguments:")
print()

# Database connections with flexible config
db1 = create_database_connection("localhost", 5432, database="users", username="admin")
db2 = create_database_connection(
    "prod.db.com", 3306, 
    database="inventory", 
    username="app_user", 
    password="secret123",
    ssl_mode="required",
    timeout=30
)

print("Database connections:")
for i, db in enumerate([db1, db2], 1):
    print(f"  DB{i}: {db['host']}:{db['port']}")
    other_config = {k: v for k, v in db.items() if k not in ['host', 'port', 'connected']}
    if other_config:
        config_str = ", ".join(f"{k}={v}" for k, v in other_config.items())
        print(f"       Config: {config_str}")
print()

# Logging with metadata
log1 = log_event("INFO", "User logged in", user_id=12345, ip_address="192.168.1.1")
log2 = log_event("ERROR", "Database connection failed", error_code=500, retry_count=3)
log3 = log_event("WARNING", "High memory usage detected")

print("Log entries:")
for log in [log1, log2, log3]:
    print(f"  {log}")
print()

# API URL building
api1 = build_api_url("https://api.example.com", "/users")
api2 = build_api_url("https://api.service.com/v1", "products", category="electronics", limit=50)
api3 = build_api_url("https://search.api.com", "/query", q="python", sort="date", page=1)

print("API URLs:")
for url in [api1, api2, api3]:
    print(f"  {url}")
print()

# COMBINING DIFFERENT PARAMETER TYPES
print("=== COMBINING PARAMETER TYPES ===")
print()

def advanced_function(required_param, default_param="default", *args, **kwargs):
    """
    Function demonstrating all parameter types together.
    Parameter order must be: required, default, *args, **kwargs
    
    Args:
        required_param: Required parameter
        default_param: Parameter with default value
        *args: Variable positional arguments
        **kwargs: Variable keyword arguments
    
    Returns:
        dict: Summary of all received parameters
    """
    return {
        'required': required_param,
        'default': default_param,
        'args': args,
        'kwargs': kwargs,
        'total_args': len(args),
        'total_kwargs': len(kwargs)
    }

def process_order(customer_id, *items, priority="normal", **shipping_info):
    """
    Process an order with flexible item list and shipping options.
    
    Args:
        customer_id (str): Customer ID (required)
        *items: Variable number of items to order
        priority (str): Order priority
        **shipping_info: Shipping address and preferences
    
    Returns:
        dict: Order processing result
    """
    order = {
        'customer_id': customer_id,
        'items': list(items),
        'item_count': len(items),
        'priority': priority,
        'shipping': shipping_info,
        'order_total': len(items) * 19.99  # Simplified pricing
    }
    return order

print("Functions can combine all parameter types (in specific order):")
print()

# Testing advanced function with various argument combinations
result1 = advanced_function("test")
result2 = advanced_function("test", "custom", 1, 2, 3)
result3 = advanced_function("test", extra1="value1", extra2="value2")
result4 = advanced_function("test", "custom", 1, 2, 3, extra1="value1", extra2="value2")

print("Advanced function results:")
for i, result in enumerate([result1, result2, result3, result4], 1):
    print(f"  Call {i}: required='{result['required']}', default='{result['default']}'")
    print(f"         args={result['args']}, kwargs={result['kwargs']}")
print()

# Order processing examples
order1 = process_order("CUST001", "Widget", "Gadget")
order2 = process_order(
    "CUST002", 
    "Premium Widget", "Deluxe Gadget", "Super Tool",
    priority="urgent",
    address="123 Main St",
    city="New York",
    express_delivery=True
)

print("Order processing:")
for i, order in enumerate([order1, order2], 1):
    print(f"  Order {i}: Customer {order['customer_id']}")
    print(f"           {order['item_count']} items, priority: {order['priority']}")
    print(f"           Total: ${order['order_total']}")
    if order['shipping']:
        shipping = ", ".join(f"{k}={v}" for k, v in order['shipping'].items())
        print(f"           Shipping: {shipping}")
print()

# ARGUMENT UNPACKING
print("=== ARGUMENT UNPACKING ===")
print()

def calculate_rectangle_properties(length, width, height=1):
    """
    Calculate rectangle properties from dimensions.
    
    Args:
        length (float): Rectangle length
        width (float): Rectangle width  
        height (float, optional): Rectangle height. Defaults to 1.
    
    Returns:
        dict: Rectangle properties (area, perimeter, volume)
    """
    area = length * width
    perimeter = 2 * (length + width)
    volume = length * width * height
    
    return {
        'area': area,
        'perimeter': perimeter,
        'volume': volume
    }

print("Argument unpacking allows passing collections as arguments:")
print()

# Unpacking lists and tuples with *
dimensions_2d = [5, 3]  # length, width
dimensions_3d = (4, 6, 2)  # length, width, height

print("Using * to unpack sequences:")
rect1 = calculate_rectangle_properties(*dimensions_2d)
rect2 = calculate_rectangle_properties(*dimensions_3d)

print(f"2D rectangle {dimensions_2d}: area={rect1['area']}, perimeter={rect1['perimeter']}")
print(f"3D rectangle {dimensions_3d}: area={rect2['area']}, volume={rect2['volume']}")
print()

# Unpacking dictionaries with **
config_params = {
    'host': 'api.example.com',
    'port': 443,
    'ssl_enabled': True,
    'timeout': 60,
    'retries': 3
}

print("Using ** to unpack dictionaries:")
server_config = configure_server(**config_params)
print(f"Server configured: {server_config['hostname']}:{server_config['port']}")
print(f"SSL: {server_config['ssl_enabled']}, Timeout: {server_config['timeout']}")
print()

print("=== SUMMARY ===")
print()
print("Parameter and Argument Types Summary:")
print("1. Required positional parameters - must be provided in order")
print("2. Default parameters - optional with fallback values")
print("3. Keyword arguments - can be called by name for clarity")
print("4. *args - accepts variable number of positional arguments")
print("5. **kwargs - accepts variable number of keyword arguments")
print("6. Parameter order: required, defaults, *args, **kwargs")
print("7. Unpacking: * for sequences, ** for dictionaries")

"""
KEY TAKEAWAYS:
==============
1. Different parameter types provide flexibility in function design
2. Required parameters ensure essential data is provided
3. Default parameters make functions easier to use
4. Keyword arguments improve code readability
5. *args and **kwargs enable highly flexible functions
6. Parameter order matters: required, defaults, *args, **kwargs
7. Argument unpacking helps work with existing data structures

PARAMETER ORDER RULES:
=====================
1. Required positional parameters
2. Default parameters
3. *args (variable positional)
4. **kwargs (variable keyword)

Example:
def func(required, default="value", *args, **kwargs):
    pass

COMMON PATTERNS:
================
• API functions: use **kwargs for flexible options
• Mathematical functions: use *args for variable inputs
• Configuration functions: mix required, defaults, and **kwargs
• Wrapper functions: use *args and **kwargs to pass through arguments

NEXT STEP:
Go to 03-scope-variables.py to learn about variable scope and lifetime!
"""