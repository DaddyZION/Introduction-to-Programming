"""
Assignment 5 - Exercise 2: Parameters and Arguments
Difficulty: 🟡 Intermediate

TODO: Practice different parameter types and argument passing.

This exercise covers default parameters, keyword arguments, and flexible parameters.
"""

# ==================== FUNCTION 1: Greet Person ====================
def greet_person(name, greeting="Hello", punctuation="!"):
    """
    Create a personalized greeting with customizable elements.
    
    Requirements:
    - name: required parameter
    - greeting: optional, defaults to "Hello"
    - punctuation: optional, defaults to "!"
    - Return formatted greeting string
    
    Test Cases:
    - greet_person("Alice") → "Hello, Alice!"
    - greet_person("Bob", "Hi") → "Hi, Bob!"
    - greet_person("Carol", "Hey", ".") → "Hey, Carol."
    - greet_person("David", punctuation="?") → "Hello, David?"
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Calculate Total Cost ====================
def calculate_total_cost(*prices, tax_rate=0.08, discount=0.0):
    """
    Calculate total cost with tax and discount from variable number of prices.
    
    Requirements:
    - Accept variable number of price arguments (*prices)
    - tax_rate: optional, defaults to 0.08 (8%)
    - discount: optional, defaults to 0.0 (no discount)
    - Apply discount first, then tax
    - Return final total rounded to 2 decimal places
    
    Test Cases:
    - calculate_total_cost(10.00, 20.00, 15.00) → 48.60 (with 8% tax)
    - calculate_total_cost(100.00, tax_rate=0.10) → 110.00
    - calculate_total_cost(50.00, discount=0.20) → 43.20 (20% off, then tax)
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Create User Profile ====================
def create_user_profile(username, email, **additional_info):
    """
    Create a user profile dictionary with flexible additional information.
    
    Requirements:
    - username and email are required
    - Accept any additional keyword arguments
    - Return dictionary with all provided information
    - Add a 'created_date' field with value '2024-10-02'
    
    Test Cases:
    - create_user_profile("john", "john@email.com") 
      → {'username': 'john', 'email': 'john@email.com', 'created_date': '2024-10-02'}
    - create_user_profile("jane", "jane@email.com", age=25, city="NYC")
      → includes age and city fields
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Format Name ====================
def format_name(first, last, middle="", title=""):
    """
    Format a person's name in various styles.
    
    Requirements:
    - first and last are required
    - middle and title are optional
    - Return formatted name string
    - If middle provided: "First Middle Last"
    - If title provided: "Title First Last"
    - If both: "Title First Middle Last"
    
    Test Cases:
    - format_name("John", "Doe") → "John Doe"
    - format_name("John", "Doe", middle="Smith") → "John Smith Doe"
    - format_name("John", "Doe", title="Dr.") → "Dr. John Doe"
    - format_name("John", "Doe", "Smith", "Dr.") → "Dr. John Smith Doe"
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Build URL ====================
def build_url(base_url, path="", **params):
    """
    Build a URL with optional path and query parameters.
    
    Requirements:
    - base_url is required
    - path is optional
    - Accept any number of query parameters as keyword arguments
    - Return formatted URL string
    
    Format: "base_url/path?param1=value1&param2=value2"
    
    Test Cases:
    - build_url("https://api.example.com") → "https://api.example.com"
    - build_url("https://api.example.com", "users") → "https://api.example.com/users"
    - build_url("https://api.example.com", "search", q="python", page=1) 
      → "https://api.example.com/search?q=python&page=1"
    """
    # TODO: Implement this function
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Parameters and Arguments ===\n")
    
    # Test greet_person
    print("Test 1: Greet Person")
    print(f"  greet_person('Alice') = {greet_person('Alice')}")
    print(f"  greet_person('Bob', 'Hi') = {greet_person('Bob', 'Hi')}")
    print(f"  greet_person('Carol', 'Hey', '.') = {greet_person('Carol', 'Hey', '.')}")
    
    # Test calculate_total_cost
    print("\nTest 2: Calculate Total Cost")
    print(f"  calculate_total_cost(10, 20, 15) = {calculate_total_cost(10, 20, 15)}")
    print(f"  calculate_total_cost(100, tax_rate=0.10) = {calculate_total_cost(100, tax_rate=0.10)}")
    
    # Test create_user_profile
    print("\nTest 3: Create User Profile")
    print(f"  create_user_profile('john', 'john@email.com') = {create_user_profile('john', 'john@email.com')}")
    print(f"  create_user_profile('jane', 'jane@email.com', age=25) = {create_user_profile('jane', 'jane@email.com', age=25)}")
    
    # Test format_name
    print("\nTest 4: Format Name")
    print(f"  format_name('John', 'Doe') = {format_name('John', 'Doe')}")
    print(f"  format_name('John', 'Doe', middle='Smith') = {format_name('John', 'Doe', middle='Smith')}")
    
    # Test build_url
    print("\nTest 5: Build URL")
    print(f"  build_url('https://api.example.com') = {build_url('https://api.example.com')}")
    print(f"  build_url('https://api.example.com', 'users') = {build_url('https://api.example.com', 'users')}")
