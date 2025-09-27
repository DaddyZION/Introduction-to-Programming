"""
Assignment 5 - Example 5: Modular Programming
==============================================

This program demonstrates modular programming concepts including code organization,
function libraries, import mechanisms, and best practices for creating maintainable,
reusable code. Modular programming is essential for building large applications.

Key Concepts Demonstrated:
- Code organization principles
- Creating function libraries
- Module import mechanisms
- Namespace management
- Package structure concepts
- Documentation and testing integration
- Best practices for modular design
"""

print("=== MODULAR PROGRAMMING ===")
print()

print("Modular programming organizes code into logical, reusable units:")
print("• Modules: Files containing related functions and classes")
print("• Packages: Directories containing multiple related modules")
print("• Libraries: Collections of modules for specific purposes")
print("• Namespaces: Organize names to avoid conflicts")
print("• Separation of Concerns: Each module has a specific responsibility")
print()

# ORGANIZING FUNCTIONS BY PURPOSE
print("=== ORGANIZING FUNCTIONS BY PURPOSE ===")
print()

# MATHEMATICAL UTILITIES MODULE
print("# Mathematical Utilities Module (math_utils.py concept)")

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract second number from first."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide first number by second."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def factorial(n):
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    """Calculate Greatest Common Divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return abs(a)

# Demonstrate mathematical utilities
print("Mathematical utilities demonstration:")
print(f"  25 + 17 = {add(25, 17)}")
print(f"  100 - 37 = {subtract(100, 37)}")
print(f"  12 * 8 = {multiply(12, 8)}")
print(f"  144 / 12 = {divide(144, 12)}")
print(f"  2^10 = {power(2, 10)}")
print(f"  6! = {factorial(6)}")
print(f"  Is 17 prime? {is_prime(17)}")
print(f"  GCD(48, 18) = {gcd(48, 18)}")
print()

# STRING UTILITIES MODULE
print("# String Utilities Module (string_utils.py concept)")

def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Return the reverse of a string."""
    return text[::-1]

def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def remove_punctuation(text):
    """Remove common punctuation from text."""
    punctuation = '.,!?;:()[]{}"\'-'
    for char in punctuation:
        text = text.replace(char, '')
    return text

def word_frequency(text):
    """Count frequency of each word in text."""
    words = text.lower().split()
    frequency = {}
    for word in words:
        clean_word = remove_punctuation(word)
        if clean_word:
            frequency[clean_word] = frequency.get(clean_word, 0) + 1
    return frequency

def format_phone_number(digits):
    """Format a 10-digit number as a phone number."""
    if len(digits) == 10 and digits.isdigit():
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    else:
        raise ValueError("Phone number must be exactly 10 digits")

def slugify(text):
    """Convert text to URL-friendly slug."""
    slug = text.lower()
    slug = remove_punctuation(slug)
    slug = slug.replace(' ', '-')
    return slug

# Demonstrate string utilities
print("String utilities demonstration:")
sample_text = "Hello, world! This is a test."
print(f"  Original: '{sample_text}'")
print(f"  Capitalized: '{capitalize_words(sample_text)}'")
print(f"  Reversed: '{reverse_string(sample_text)}'")
print(f"  Vowel count: {count_vowels(sample_text)}")
print(f"  Without punctuation: '{remove_punctuation(sample_text)}'")
print(f"  Word frequency: {word_frequency(sample_text)}")
print(f"  Phone format: {format_phone_number('5551234567')}")
print(f"  Slugified: '{slugify('My Blog Post Title!')}'")
print()

# DATA VALIDATION MODULE
print("# Data Validation Module (validation.py concept)")

def validate_email(email):
    """Validate email address format."""
    if not email or '@' not in email:
        return False, "Email must contain @ symbol"
    
    parts = email.split('@')
    if len(parts) != 2:
        return False, "Email must contain exactly one @ symbol"
    
    local, domain = parts
    if not local or not domain:
        return False, "Email must have content before and after @"
    
    if '.' not in domain:
        return False, "Domain must contain at least one dot"
    
    return True, "Email format is valid"

def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not (has_upper and has_lower and has_digit):
        return False, "Password must contain uppercase, lowercase, and digit"
    
    return True, "Password meets requirements"

def validate_age(age):
    """Validate age value."""
    try:
        age_int = int(age)
        if age_int < 0:
            return False, "Age cannot be negative"
        if age_int > 150:
            return False, "Age seems unrealistic"
        return True, f"Age {age_int} is valid"
    except ValueError:
        return False, "Age must be a number"

def validate_credit_card(card_number):
    """Basic credit card number validation (Luhn algorithm)."""
    # Remove spaces and hyphens
    digits = ''.join(c for c in card_number if c.isdigit())
    
    if len(digits) < 13 or len(digits) > 19:
        return False, "Credit card must be 13-19 digits"
    
    # Luhn algorithm
    total = 0
    reverse_digits = digits[::-1]
    
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:  # Every second digit from the right
            n *= 2
            if n > 9:
                n -= 9
        total += n
    
    is_valid = total % 10 == 0
    return is_valid, "Credit card number is valid" if is_valid else "Invalid credit card number"

# Demonstrate validation utilities
print("Data validation utilities demonstration:")
test_data = [
    ("email", "user@example.com"),
    ("email", "invalid.email"),
    ("password", "StrongPass123"),
    ("password", "weak"),
    ("age", "25"),
    ("age", "-5"),
    ("credit_card", "4532015112830366"),  # Valid test number
    ("credit_card", "1234567890123456")   # Invalid number
]

for data_type, value in test_data:
    if data_type == "email":
        is_valid, message = validate_email(value)
    elif data_type == "password":
        is_valid, message = validate_password(value)
    elif data_type == "age":
        is_valid, message = validate_age(value)
    elif data_type == "credit_card":
        is_valid, message = validate_credit_card(value)
    
    status = "✅" if is_valid else "❌"
    print(f"  {status} {data_type.title()} '{value}': {message}")
print()

# FILE OPERATIONS MODULE
print("# File Operations Module (file_utils.py concept)")

def read_lines_from_string(text):
    """Simulate reading lines from a file (using string instead)."""
    return text.strip().split('\n')

def count_lines(lines):
    """Count number of lines."""
    return len(lines)

def count_words(lines):
    """Count total words across all lines."""
    total_words = 0
    for line in lines:
        words = line.split()
        total_words += len(words)
    return total_words

def count_characters(lines):
    """Count total characters across all lines."""
    return sum(len(line) for line in lines)

def find_longest_line(lines):
    """Find the longest line."""
    if not lines:
        return ""
    return max(lines, key=len)

def filter_empty_lines(lines):
    """Remove empty lines."""
    return [line for line in lines if line.strip()]

def add_line_numbers(lines):
    """Add line numbers to each line."""
    return [f"{i+1:3}: {line}" for i, line in enumerate(lines)]

# Demonstrate file operations
print("File operations utilities demonstration:")
sample_file_content = """This is line 1
This is a longer line with more content
Short line

Another line after empty line
Final line"""

lines = read_lines_from_string(sample_file_content)
print(f"  Total lines: {count_lines(lines)}")
print(f"  Total words: {count_words(lines)}")
print(f"  Total characters: {count_characters(lines)}")
print(f"  Longest line: '{find_longest_line(lines)}'")

filtered_lines = filter_empty_lines(lines)
print(f"  Lines after removing empty: {len(filtered_lines)}")

numbered_lines = add_line_numbers(filtered_lines)
print("  With line numbers:")
for line in numbered_lines:
    print(f"    {line}")
print()

# CREATING A SIMPLE LIBRARY INTERFACE
print("=== CREATING A LIBRARY INTERFACE ===")
print()

class MathLibrary:
    """
    A library class that organizes mathematical functions.
    Demonstrates how to create a cohesive library interface.
    """
    
    @staticmethod
    def basic_operations():
        """Get basic mathematical operations."""
        return {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide
        }
    
    @staticmethod
    def advanced_operations():
        """Get advanced mathematical operations."""
        return {
            'power': power,
            'factorial': factorial,
            'gcd': gcd,
            'is_prime': is_prime
        }
    
    @staticmethod
    def calculate_statistics(numbers):
        """Calculate basic statistics for a list of numbers."""
        if not numbers:
            return {}
        
        total = sum(numbers)
        count = len(numbers)
        mean = total / count
        
        sorted_numbers = sorted(numbers)
        if count % 2 == 0:
            median = (sorted_numbers[count//2 - 1] + sorted_numbers[count//2]) / 2
        else:
            median = sorted_numbers[count//2]
        
        return {
            'count': count,
            'sum': total,
            'mean': mean,
            'median': median,
            'min': min(numbers),
            'max': max(numbers),
            'range': max(numbers) - min(numbers)
        }

class StringLibrary:
    """
    A library class for string operations.
    """
    
    @staticmethod
    def formatting():
        """Get string formatting functions."""
        return {
            'capitalize_words': capitalize_words,
            'reverse_string': reverse_string,
            'slugify': slugify,
            'format_phone': format_phone_number
        }
    
    @staticmethod
    def analysis():
        """Get string analysis functions."""
        return {
            'count_vowels': count_vowels,
            'word_frequency': word_frequency,
            'remove_punctuation': remove_punctuation
        }

class ValidationLibrary:
    """
    A library class for data validation.
    """
    
    @staticmethod
    def validators():
        """Get all validation functions."""
        return {
            'email': validate_email,
            'password': validate_password,
            'age': validate_age,
            'credit_card': validate_credit_card
        }
    
    @staticmethod
    def validate_user_data(user_data):
        """Validate complete user data dictionary."""
        results = {}
        validators = ValidationLibrary.validators()
        
        for field, value in user_data.items():
            if field in validators:
                is_valid, message = validators[field](value)
                results[field] = {'valid': is_valid, 'message': message}
            else:
                results[field] = {'valid': True, 'message': 'No validation rule'}
        
        return results

# Demonstrate library interfaces
print("Library interface demonstration:")

# Math library usage
math_lib = MathLibrary()
sample_numbers = [5, 2, 8, 1, 9, 3, 7, 6, 4]

basic_ops = math_lib.basic_operations()
print(f"Using math library - Add: {basic_ops['add'](15, 25)}")

stats = math_lib.calculate_statistics(sample_numbers)
print(f"Statistics for {sample_numbers}:")
for key, value in stats.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")
print()

# String library usage
string_lib = StringLibrary()
formatting_funcs = string_lib.formatting()
analysis_funcs = string_lib.analysis()

test_string = "Hello World! How are you today?"
print(f"String library example with '{test_string}':")
print(f"  Capitalized: {formatting_funcs['capitalize_words'](test_string)}")
print(f"  Vowel count: {analysis_funcs['count_vowels'](test_string)}")
print()

# Validation library usage
validation_lib = ValidationLibrary()
test_user = {
    'email': 'user@example.com',
    'password': 'SecurePass123',
    'age': '25',
    'credit_card': '4532015112830366'
}

validation_results = validation_lib.validate_user_data(test_user)
print("User data validation results:")
for field, result in validation_results.items():
    status = "✅" if result['valid'] else "❌"
    print(f"  {status} {field}: {result['message']}")
print()

# NAMESPACE MANAGEMENT
print("=== NAMESPACE MANAGEMENT ===")
print()

def demonstrate_namespaces():
    """
    Demonstrate how namespaces help organize and avoid conflicts.
    """
    
    # Simulate different modules with same function names
    class DatabaseModule:
        @staticmethod
        def connect():
            return "Connected to database"
        
        @staticmethod
        def query(sql):
            return f"Executing database query: {sql}"
    
    class NetworkModule:
        @staticmethod
        def connect():
            return "Connected to network"
        
        @staticmethod
        def request(url):
            return f"Making network request to: {url}"
    
    class FileModule:
        @staticmethod
        def open(filename):
            return f"Opening file: {filename}"
        
        @staticmethod
        def read(filename):
            return f"Reading from file: {filename}"
    
    # Using namespaces to avoid conflicts
    db = DatabaseModule()
    net = NetworkModule()
    file_ops = FileModule()
    
    print("Namespace management prevents function name conflicts:")
    print(f"  Database connect: {db.connect()}")
    print(f"  Network connect: {net.connect()}")
    print(f"  Database query: {db.query('SELECT * FROM users')}")
    print(f"  Network request: {net.request('https://api.example.com')}")
    print(f"  File operations: {file_ops.open('data.txt')}")

demonstrate_namespaces()
print()

# MODULAR DESIGN PRINCIPLES
print("=== MODULAR DESIGN PRINCIPLES ===")
print()

def demonstrate_design_principles():
    """
    Demonstrate key principles of modular design.
    """
    
    print("Key Modular Design Principles:")
    print()
    
    print("1. SINGLE RESPONSIBILITY PRINCIPLE")
    print("   Each module should have one reason to change")
    
    # Good: Focused module
    class UserAuthenticationModule:
        @staticmethod
        def login(username, password):
            return f"Authenticating {username}..."
        
        @staticmethod
        def logout(session_id):
            return f"Logging out session {session_id}"
        
        @staticmethod
        def validate_session(session_id):
            return f"Validating session {session_id}"
    
    print("   ✅ UserAuthenticationModule focuses only on authentication")
    print()
    
    print("2. LOOSE COUPLING")
    print("   Modules should depend on abstractions, not concrete implementations")
    
    class EmailService:
        def send_email(self, to, subject, body):
            return f"Sending email to {to}: {subject}"
    
    class NotificationModule:
        def __init__(self, email_service):
            self.email_service = email_service  # Depends on abstraction
        
        def notify_user(self, user_email, message):
            return self.email_service.send_email(user_email, "Notification", message)
    
    email = EmailService()
    notifications = NotificationModule(email)
    print(f"   ✅ {notifications.notify_user('user@example.com', 'Hello!')}")
    print()
    
    print("3. HIGH COHESION")
    print("   Related functionality should be grouped together")
    
    class OrderProcessingModule:
        @staticmethod
        def calculate_total(items):
            return sum(item['price'] for item in items)
        
        @staticmethod
        def apply_discount(total, discount_percent):
            return total * (1 - discount_percent / 100)
        
        @staticmethod
        def calculate_tax(total, tax_rate):
            return total * tax_rate
        
        @staticmethod
        def process_order(items, discount=0, tax_rate=0.08):
            subtotal = OrderProcessingModule.calculate_total(items)
            discounted = OrderProcessingModule.apply_discount(subtotal, discount)
            tax = OrderProcessingModule.calculate_tax(discounted, tax_rate)
            return discounted + tax
    
    sample_items = [{'name': 'Widget', 'price': 19.99}, {'name': 'Gadget', 'price': 29.99}]
    total = OrderProcessingModule.process_order(sample_items, discount=10)
    print(f"   ✅ Order total: ${total:.2f}")
    print()
    
    print("4. INTERFACE SEGREGATION")
    print("   Provide specific interfaces for different use cases")
    
    class DataStore:
        def read_user_data(self, user_id):
            return f"User data for {user_id}"
        
        def write_user_data(self, user_id, data):
            return f"Saved data for {user_id}"
        
        def read_product_data(self, product_id):
            return f"Product data for {product_id}"
        
        def write_product_data(self, product_id, data):
            return f"Saved product data for {product_id}"
    
    # Specific interfaces for different concerns
    class UserDataInterface:
        def __init__(self, data_store):
            self._store = data_store
        
        def get_user(self, user_id):
            return self._store.read_user_data(user_id)
        
        def save_user(self, user_id, data):
            return self._store.write_user_data(user_id, data)
    
    class ProductDataInterface:
        def __init__(self, data_store):
            self._store = data_store
        
        def get_product(self, product_id):
            return self._store.read_product_data(product_id)
        
        def save_product(self, product_id, data):
            return self._store.write_product_data(product_id, data)
    
    store = DataStore()
    user_interface = UserDataInterface(store)
    product_interface = ProductDataInterface(store)
    
    print(f"   ✅ {user_interface.get_user('12345')}")
    print(f"   ✅ {product_interface.get_product('ABC123')}")

demonstrate_design_principles()
print()

print("=== SUMMARY ===")
print()
print("Modular Programming Summary:")
print("1. Organize related functions into logical modules")
print("2. Create library interfaces for cohesive functionality")
print("3. Use namespaces to prevent naming conflicts")
print("4. Follow design principles: SRP, loose coupling, high cohesion")
print("5. Provide clear, documented interfaces")
print("6. Design for reusability and maintainability")
print("7. Test modules independently")

"""
KEY TAKEAWAYS:
==============
1. Modular programming organizes code into logical, reusable units
2. Each module should have a clear, single responsibility
3. Library interfaces provide clean access to functionality
4. Namespaces prevent naming conflicts and organize code
5. Good modular design follows established principles
6. Documentation and testing are integral to modular code

MODULAR DESIGN BENEFITS:
========================
• Code Reusability: Write once, use many times
• Maintainability: Changes isolated to specific modules
• Testing: Test modules independently
• Collaboration: Teams can work on different modules
• Organization: Logical structure makes code easier to navigate
• Scalability: Add new modules without changing existing code

ORGANIZATION STRATEGIES:
========================
• By Function: math_utils, string_utils, file_utils
• By Domain: user_management, order_processing, inventory
• By Layer: database, business_logic, presentation
• By Feature: authentication, reporting, notifications

IMPORT PATTERNS:
================
• import module_name
• from module_name import function_name
• from module_name import *  (use sparingly)
• import module_name as alias

BEST PRACTICES:
===============
• Keep modules focused on single responsibility
• Use clear, descriptive module and function names
• Provide comprehensive documentation
• Include error handling in module functions
• Design for both current and future needs
• Test modules thoroughly with unit tests
• Version modules for backward compatibility

NEXT STEP:
Go to 06-complete-program.py to see all function concepts in a comprehensive application!
"""