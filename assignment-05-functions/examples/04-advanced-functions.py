"""
Assignment 5 - Example 4: Advanced Function Concepts
====================================================

This program explores advanced function concepts including nested functions,
lambda functions, higher-order functions, and basic recursion. These concepts
enable powerful programming patterns and functional programming techniques.

Key Concepts Demonstrated:
- Nested functions and closures
- Lambda functions (anonymous functions)
- Higher-order functions (functions that take/return functions)
- Function decorators (basic introduction)
- Recursion fundamentals
- Functional programming patterns
"""

print("=== ADVANCED FUNCTION CONCEPTS ===")
print()

print("Advanced function concepts enable sophisticated programming patterns:")
print("• Nested Functions: Functions defined inside other functions")
print("• Closures: Inner functions that remember outer function variables")
print("• Lambda Functions: Anonymous functions for simple operations")
print("• Higher-Order Functions: Functions that work with other functions")
print("• Recursion: Functions that call themselves")
print()

# NESTED FUNCTIONS AND CLOSURES
print("=== NESTED FUNCTIONS AND CLOSURES ===")
print()

def create_multiplier(factor):
    """
    Factory function that creates customized multiplier functions.
    Demonstrates closures - inner function remembers outer function's variables.
    
    Args:
        factor (float): The multiplication factor
    
    Returns:
        function: A function that multiplies by the given factor
    """
    def multiplier(number):
        return number * factor
    
    return multiplier

def create_formatter(prefix, suffix):
    """
    Create a custom text formatter function.
    
    Args:
        prefix (str): Text to add before the content
        suffix (str): Text to add after the content
    
    Returns:
        function: A function that formats text with prefix and suffix
    """
    def format_text(content):
        return f"{prefix}{content}{suffix}"
    
    return format_text

def create_validator(min_value, max_value):
    """
    Create a validator function for a specific range.
    
    Args:
        min_value (float): Minimum valid value
        max_value (float): Maximum valid value
    
    Returns:
        function: A function that validates if a number is in range
    """
    def validate(number):
        if min_value <= number <= max_value:
            return True, f"{number} is valid (range: {min_value}-{max_value})"
        else:
            return False, f"{number} is outside valid range ({min_value}-{max_value})"
    
    return validate

print("Nested functions and closures create specialized functions:")

# Create specialized multiplier functions
double = create_multiplier(2)
triple = create_multiplier(3)
half = create_multiplier(0.5)

print(f"Double 15: {double(15)}")
print(f"Triple 8: {triple(8)}")
print(f"Half of 20: {half(20)}")
print()

# Create specialized formatters
html_bold = create_formatter("<b>", "</b>")
parentheses = create_formatter("(", ")")
quotes = create_formatter('"', '"')

print(f"HTML bold: {html_bold('Important Text')}")
print(f"Parentheses: {parentheses('optional info')}")
print(f"Quotes: {quotes('Hello World')}")
print()

# Create specialized validators
age_validator = create_validator(0, 120)
percentage_validator = create_validator(0, 100)
temperature_validator = create_validator(-50, 50)

test_values = [25, 150, -10, 75]
print("Age validation:")
for value in test_values:
    is_valid, message = age_validator(value)
    status = "✅" if is_valid else "❌"
    print(f"  {status} {message}")
print()

# LAMBDA FUNCTIONS
print("=== LAMBDA FUNCTIONS ===")
print()

# Lambda functions are anonymous functions for simple operations
print("Lambda functions provide concise syntax for simple functions:")

# Basic lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda n: n % 2 == 0
full_name = lambda first, last: f"{first} {last}"

print(f"Square of 7: {square(7)}")
print(f"Add 15 and 25: {add(15, 25)}")
print(f"Is 8 even? {is_even(8)}")
print(f"Is 9 even? {is_even(9)}")
print(f"Full name: {full_name('Alice', 'Johnson')}")
print()

# Lambda functions with conditional expressions
absolute_value = lambda x: x if x >= 0 else -x
max_of_two = lambda a, b: a if a > b else b
grade_status = lambda grade: "Pass" if grade >= 60 else "Fail"
price_with_tax = lambda price, tax_rate=0.08: price * (1 + tax_rate)

print("Lambda functions with conditional expressions:")
print(f"Absolute value of -15: {absolute_value(-15)}")
print(f"Max of 23 and 19: {max_of_two(23, 19)}")
print(f"Grade 75 status: {grade_status(75)}")
print(f"Grade 45 status: {grade_status(45)}")
print(f"$100 with 8% tax: ${price_with_tax(100):.2f}")
print(f"$50 with 10% tax: ${price_with_tax(50, 0.10):.2f}")
print()

# HIGHER-ORDER FUNCTIONS
print("=== HIGHER-ORDER FUNCTIONS ===")
print()

def apply_operation(numbers, operation):
    """
    Apply an operation to each number in a list.
    
    Args:
        numbers (list): List of numbers
        operation (function): Function to apply to each number
    
    Returns:
        list: Results of applying operation to each number
    """
    results = []
    for number in numbers:
        results.append(operation(number))
    return results

def filter_numbers(numbers, condition):
    """
    Filter numbers based on a condition function.
    
    Args:
        numbers (list): List of numbers to filter
        condition (function): Function that returns True/False
    
    Returns:
        list: Numbers that satisfy the condition
    """
    filtered = []
    for number in numbers:
        if condition(number):
            filtered.append(number)
    return filtered

def create_operation_chain(*operations):
    """
    Create a function that applies multiple operations in sequence.
    
    Args:
        *operations: Variable number of operation functions
    
    Returns:
        function: Function that applies all operations in order
    """
    def chained_operation(value):
        result = value
        for operation in operations:
            result = operation(result)
        return result
    
    return chained_operation

print("Higher-order functions work with other functions as data:")

test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using functions as arguments
squared_numbers = apply_operation(test_numbers, square)
doubled_numbers = apply_operation(test_numbers, lambda x: x * 2)
cubed_numbers = apply_operation(test_numbers, lambda x: x ** 3)

print(f"Original: {test_numbers}")
print(f"Squared: {squared_numbers}")
print(f"Doubled: {doubled_numbers}")
print(f"Cubed: {cubed_numbers[:5]}...")  # Show first 5 to save space
print()

# Filtering with function conditions
even_numbers = filter_numbers(test_numbers, is_even)
large_numbers = filter_numbers(test_numbers, lambda x: x > 5)
perfect_squares = filter_numbers(test_numbers, lambda x: int(x**0.5)**2 == x)

print("Filtering with conditions:")
print(f"Even numbers: {even_numbers}")
print(f"Numbers > 5: {large_numbers}")
print(f"Perfect squares: {perfect_squares}")
print()

# Function composition
add_ten = lambda x: x + 10
multiply_by_three = lambda x: x * 3
square_it = lambda x: x ** 2

# Create composed operation: ((x + 10) * 3) ** 2
complex_operation = create_operation_chain(add_ten, multiply_by_three, square_it)

print("Function composition:")
for i in range(1, 4):
    result = complex_operation(i)
    print(f"Complex operation on {i}: (({i} + 10) * 3)² = {result}")
print()

# BUILT-IN HIGHER-ORDER FUNCTIONS
print("=== BUILT-IN HIGHER-ORDER FUNCTIONS ===")
print()

# Python's built-in higher-order functions
sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
words = ["apple", "banana", "cherry", "date", "elderberry"]
prices = [19.99, 29.95, 12.50, 45.00, 8.75]

print("Python's built-in higher-order functions:")

# map() - applies function to each element
squared_map = list(map(lambda x: x**2, sample_data))
uppercase_words = list(map(str.upper, words))
formatted_prices = list(map(lambda p: f"${p:.2f}", prices))

print(f"map() examples:")
print(f"  Squared: {squared_map}")
print(f"  Uppercase: {uppercase_words}")
print(f"  Formatted prices: {formatted_prices}")
print()

# filter() - filters elements based on condition
even_filtered = list(filter(is_even, sample_data))
long_words = list(filter(lambda w: len(w) > 5, words))
expensive_items = list(filter(lambda p: p > 20, prices))

print(f"filter() examples:")
print(f"  Even numbers: {even_filtered}")
print(f"  Long words: {long_words}")
print(f"  Expensive items: ${expensive_items}")
print()

# sorted() with custom key functions
sorted_by_length = sorted(words, key=len)
sorted_by_last_char = sorted(words, key=lambda w: w[-1])
sorted_prices_desc = sorted(prices, reverse=True)

print(f"sorted() with custom keys:")
print(f"  By length: {sorted_by_length}")
print(f"  By last character: {sorted_by_last_char}")
print(f"  Prices descending: {sorted_prices_desc}")
print()

# BASIC FUNCTION DECORATORS
print("=== BASIC FUNCTION DECORATORS ===")
print()

def timing_decorator(func):
    """
    A simple decorator that prints when a function is called.
    This is a basic introduction to decorators.
    
    Args:
        func (function): Function to decorate
    
    Returns:
        function: Wrapped function with timing behavior
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    
    return wrapper

def validation_decorator(validator_func):
    """
    Decorator factory that creates validators for function arguments.
    
    Args:
        validator_func (function): Function that validates arguments
    
    Returns:
        function: Decorator function
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not validator_func(*args, **kwargs):
                raise ValueError(f"Validation failed for {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Using decorators
@timing_decorator
def calculate_factorial(n):
    """Calculate factorial with timing decorator."""
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@validation_decorator(lambda x: x >= 0)
def calculate_square_root(number):
    """Calculate square root with validation decorator."""
    return number ** 0.5

print("Function decorators add behavior to existing functions:")

# Decorated function calls
factorial_5 = calculate_factorial(5)
print(f"Factorial of 5: {factorial_5}")
print()

try:
    sqrt_16 = calculate_square_root(16)
    print(f"Square root of 16: {sqrt_16}")
    
    sqrt_negative = calculate_square_root(-4)  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")
print()

# RECURSION FUNDAMENTALS
print("=== RECURSION FUNDAMENTALS ===")
print()

def recursive_factorial(n):
    """
    Calculate factorial using recursion.
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return n * recursive_factorial(n - 1)

def recursive_fibonacci(n):
    """
    Calculate nth Fibonacci number using recursion.
    
    Args:
        n (int): Position in Fibonacci sequence
    
    Returns:
        int: nth Fibonacci number
    """
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive case: F(n) = F(n-1) + F(n-2)
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def recursive_power(base, exponent):
    """
    Calculate power using recursion.
    
    Args:
        base (float): Base number
        exponent (int): Non-negative exponent
    
    Returns:
        float: base raised to the power of exponent
    """
    # Base case
    if exponent == 0:
        return 1
    
    # Recursive case
    return base * recursive_power(base, exponent - 1)

def count_down(n):
    """
    Count down from n to 1 using recursion.
    Demonstrates recursive procedure (no return value).
    
    Args:
        n (int): Starting number
    """
    if n > 0:
        print(f"Counting: {n}")
        count_down(n - 1)  # Recursive call
    else:
        print("Blast off! 🚀")

print("Recursion: functions that call themselves")

# Recursive factorial
print("Recursive factorial calculations:")
for i in range(6):
    fact = recursive_factorial(i)
    print(f"  {i}! = {fact}")
print()

# Recursive Fibonacci (note: inefficient for large numbers)
print("Recursive Fibonacci sequence:")
for i in range(8):
    fib = recursive_fibonacci(i)
    print(f"  F({i}) = {fib}")
print()

# Recursive power
print("Recursive power calculations:")
print(f"  2^5 = {recursive_power(2, 5)}")
print(f"  3^4 = {recursive_power(3, 4)}")
print(f"  5^0 = {recursive_power(5, 0)}")
print()

# Recursive countdown
print("Recursive countdown:")
count_down(5)
print()

# PRACTICAL EXAMPLE: FUNCTIONAL PROGRAMMING STYLE
print("=== FUNCTIONAL PROGRAMMING EXAMPLE ===")
print()

def create_data_processor():
    """
    Create a data processing pipeline using functional programming concepts.
    Demonstrates combining multiple advanced function concepts.
    """
    
    # Data transformation functions
    clean_data = lambda items: [item.strip().lower() for item in items if item and item.strip()]
    remove_duplicates = lambda items: list(set(items))
    sort_data = lambda items: sorted(items)
    
    # Statistics functions
    calculate_stats = lambda items: {
        'count': len(items),
        'unique_count': len(set(items)),
        'average_length': sum(len(item) for item in items) / len(items) if items else 0
    }
    
    # Main processor function
    def process(raw_data, *transformations):
        """
        Process data through a series of transformations.
        
        Args:
            raw_data (list): Raw input data
            *transformations: Functions to apply in sequence
        
        Returns:
            dict: Processed data and statistics
        """
        result = raw_data
        
        # Apply each transformation
        for transform in transformations:
            result = transform(result)
        
        # Calculate statistics
        stats = calculate_stats(result)
        
        return {
            'original_count': len(raw_data),
            'processed_data': result,
            'statistics': stats
        }
    
    return process

# Demonstrate functional data processing
print("Functional data processing pipeline:")

processor = create_data_processor()

# Sample data with various issues
sample_data = [
    "  Apple  ", "banana", "CHERRY", "", "apple", 
    "Date", "elderberry", "  ", "BANANA", "cherry"
]

# Create processing pipeline
clean_func = lambda items: [item.strip().lower() for item in items if item and item.strip()]
unique_func = lambda items: list(set(items))
sort_func = lambda items: sorted(items)

# Process the data
result = processor(sample_data, clean_func, unique_func, sort_func)

print(f"Original data: {sample_data}")
print(f"Original count: {result['original_count']}")
print(f"Processed data: {result['processed_data']}")
print(f"Final count: {result['statistics']['count']}")
print(f"Unique items: {result['statistics']['unique_count']}")
print(f"Average length: {result['statistics']['average_length']:.1f}")
print()

print("=== SUMMARY ===")
print()
print("Advanced Function Concepts Summary:")
print("1. Nested functions enable closures and specialized function creation")
print("2. Lambda functions provide concise syntax for simple operations")
print("3. Higher-order functions work with functions as data")
print("4. Function decorators add behavior to existing functions")
print("5. Recursion solves problems by breaking them into smaller subproblems")
print("6. Functional programming patterns create clean, reusable code")

"""
KEY TAKEAWAYS:
==============
1. Nested functions and closures create specialized, stateful functions
2. Lambda functions are perfect for simple, one-line operations
3. Higher-order functions enable powerful abstraction patterns
4. Recursion is elegant for problems with recursive structure
5. Function decorators add cross-cutting concerns cleanly
6. Combining these concepts enables sophisticated programming patterns

ADVANCED FUNCTION PATTERNS:
===========================
• Factory Functions: Return specialized functions (closures)
• Function Composition: Chain functions together
• Currying: Transform multi-argument functions into single-argument functions
• Decorators: Add behavior without modifying original function
• Recursive Patterns: Base case + recursive case

WHEN TO USE EACH:
=================
• Nested Functions: When you need specialized versions of similar functionality
• Lambda: For simple transformations in map(), filter(), sorted()
• Higher-Order Functions: When building flexible, reusable processing pipelines
• Recursion: For naturally recursive problems (trees, mathematical sequences)
• Decorators: For cross-cutting concerns (logging, validation, caching)

RECURSION GUIDELINES:
====================
• Always define a base case (stopping condition)
• Ensure recursive calls work toward the base case
• Be aware of performance implications for deep recursion
• Consider iterative alternatives for simple cases
• Use recursion for problems with recursive structure

NEXT STEP:
Go to 05-modular-programming.py to learn about code organization and modules!
"""