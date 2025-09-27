"""
Assignment 5 - Functions and Modular Programming Exercises
==========================================================

This file contains practice exercises to reinforce function concepts.
Complete each exercise by implementing the required functions.
Test your solutions with the provided test cases.

Learning Objectives:
- Apply function definition and calling patterns
- Use parameters and return values effectively
- Understand variable scope and lifetime
- Implement modular programming concepts
- Practice real-world function design patterns
"""

print("=== FUNCTION EXERCISES ===")
print("Complete the following exercises to master function programming.")
print()

# EXERCISE 1: BASIC FUNCTION OPERATIONS
print("EXERCISE 1: Calculator Functions")
print("=================================")

def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Requirements:
    - Accept two numeric parameters
    - Return their sum
    - Handle both integers and floats
    
    Test Cases:
    - add_numbers(5, 3) → 8
    - add_numbers(2.5, 1.5) → 4.0
    - add_numbers(-10, 15) → 5
    """
    # TODO: Implement this function
    pass

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Requirements:
    - Accept a list of numbers
    - Return the average as a float
    - Return 0 if the list is empty
    - Handle edge cases gracefully
    
    Test Cases:
    - calculate_average([1, 2, 3, 4, 5]) → 3.0
    - calculate_average([10, 20, 30]) → 20.0
    - calculate_average([]) → 0.0
    - calculate_average([5]) → 5.0
    """
    # TODO: Implement this function
    # Hints:
    # - Check if the list is empty first
    # - Use sum() and len() functions
    # - Convert result to float
    pass

def find_maximum(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Requirements:
    - Accept a list of numbers
    - Return the maximum value
    - Return None if the list is empty
    - Don't use the built-in max() function
    
    Test Cases:
    - find_maximum([1, 5, 3, 9, 2]) → 9
    - find_maximum([-1, -5, -3]) → -1
    - find_maximum([]) → None
    - find_maximum([42]) → 42
    """
    # TODO: Implement this function
    # Hints:
    # - Check for empty list first
    # - Start with first element as max
    # - Compare with each subsequent element
    pass

# Test Exercise 1
print("Testing Exercise 1:")

# Test add_numbers
test_add_cases = [(5, 3), (2.5, 1.5), (-10, 15), (0, 0)]
for a, b in test_add_cases:
    try:
        result = add_numbers(a, b)
        print(f"  add_numbers({a}, {b}) = {result}")
    except Exception as e:
        print(f"  add_numbers({a}, {b}) - Error: {e}")

# Test calculate_average
test_avg_cases = [
    [1, 2, 3, 4, 5],
    [10, 20, 30],
    [],
    [5],
    [-2, -4, -6]
]
for numbers in test_avg_cases:
    try:
        result = calculate_average(numbers)
        print(f"  calculate_average({numbers}) = {result}")
    except Exception as e:
        print(f"  calculate_average({numbers}) - Error: {e}")

# Test find_maximum
test_max_cases = [
    [1, 5, 3, 9, 2],
    [-1, -5, -3],
    [],
    [42],
    [1.5, 2.7, 1.2]
]
for numbers in test_max_cases:
    try:
        result = find_maximum(numbers)
        print(f"  find_maximum({numbers}) = {result}")
    except Exception as e:
        print(f"  find_maximum({numbers}) - Error: {e}")

print()

# EXERCISE 2: PARAMETER VARIATIONS
print("EXERCISE 2: Flexible Parameter Functions")
print("========================================")

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
    # Hints:
    # - Sum all prices
    # - Apply discount: subtotal * (1 - discount)
    # - Apply tax: discounted_total * (1 + tax_rate)
    # - Use round(result, 2)
    pass

def create_user_profile(username, email, **additional_info):
    """
    Create a user profile dictionary with flexible additional information.
    
    Requirements:
    - username and email are required
    - Accept any additional keyword arguments
    - Return dictionary with all provided information
    - Add a 'created_date' field with value '2024-09-26'
    
    Test Cases:
    - create_user_profile("john", "john@email.com") 
      → {'username': 'john', 'email': 'john@email.com', 'created_date': '2024-09-26'}
    - create_user_profile("jane", "jane@email.com", age=25, city="NYC")
      → includes age and city fields
    """
    # TODO: Implement this function
    # Hints:
    # - Start with base dictionary
    # - Add additional_info items using update() or loop
    # - Don't forget created_date
    pass

# Test Exercise 2
print("Testing Exercise 2:")

# Test greet_person
greet_test_cases = [
    ("Alice",),
    ("Bob", "Hi"),
    ("Carol", "Hey", "."),
    # Test keyword arguments
    ("David",), # Will test with punctuation="?" separately
]

for args in greet_test_cases:
    try:
        result = greet_person(*args)
        print(f"  greet_person{args} = '{result}'")
    except Exception as e:
        print(f"  greet_person{args} - Error: {e}")

# Test with keyword argument
try:
    result = greet_person("David", punctuation="?")
    print(f"  greet_person('David', punctuation='?') = '{result}'")
except Exception as e:
    print(f"  greet_person keyword test - Error: {e}")

# Test calculate_total_cost
cost_test_cases = [
    (10.00, 20.00, 15.00),
    (100.00,),  # Will add tax_rate=0.10 separately
    (50.00,),   # Will add discount=0.20 separately
]

for prices in cost_test_cases:
    try:
        result = calculate_total_cost(*prices)
        print(f"  calculate_total_cost{prices} = {result}")
    except Exception as e:
        print(f"  calculate_total_cost{prices} - Error: {e}")

# Test with different parameters
try:
    result = calculate_total_cost(100.00, tax_rate=0.10)
    print(f"  calculate_total_cost(100.00, tax_rate=0.10) = {result}")
except Exception as e:
    print(f"  Tax rate test - Error: {e}")

try:
    result = calculate_total_cost(50.00, discount=0.20)
    print(f"  calculate_total_cost(50.00, discount=0.20) = {result}")
except Exception as e:
    print(f"  Discount test - Error: {e}")

# Test create_user_profile
profile_test_cases = [
    ("john", "john@email.com", {}),
    ("jane", "jane@email.com", {"age": 25, "city": "NYC"}),
]

for username, email, extra in profile_test_cases:
    try:
        result = create_user_profile(username, email, **extra)
        print(f"  create_user_profile('{username}', '{email}', {extra}) = {result}")
    except Exception as e:
        print(f"  Profile test - Error: {e}")

print()

# EXERCISE 3: SCOPE AND VALIDATION
print("EXERCISE 3: Scope and Data Validation")
print("=====================================")

# Global variable for this exercise
total_processed_items = 0

def validate_and_process_data(data, min_length=1, max_length=100):
    """
    Validate and process a data item, updating global counter.
    
    Requirements:
    - Check if data is a string
    - Check length is between min_length and max_length
    - If valid, increment global total_processed_items counter
    - Return (is_valid, processed_data, message) tuple
    - processed_data should be cleaned (stripped and title-cased)
    
    Test Cases:
    - validate_and_process_data("  hello world  ") → (True, "Hello World", "Data processed successfully")
    - validate_and_process_data("") → (False, None, "Data too short")
    - validate_and_process_data(123) → (False, None, "Data must be a string")
    """
    # TODO: Implement this function
    # Hints:
    # - Use global keyword to modify total_processed_items
    # - Use isinstance(data, str) to check if data is string
    # - Use len() to check length
    # - Use strip() and title() for cleaning
    pass

def get_processing_statistics():
    """
    Return the current value of total_processed_items.
    
    Requirements:
    - Access global total_processed_items variable
    - Return the current count
    
    Test Case:
    - After processing some items, should return correct count
    """
    # TODO: Implement this function
    pass

def reset_processing_counter():
    """
    Reset the global counter to zero.
    
    Requirements:
    - Use global keyword to modify total_processed_items
    - Set it to 0
    - Return confirmation message
    """
    # TODO: Implement this function
    pass

# Test Exercise 3
print("Testing Exercise 3:")

# Reset counter first
try:
    reset_msg = reset_processing_counter()
    print(f"  {reset_msg}")
except Exception as e:
    print(f"  Reset counter - Error: {e}")

# Test validation
validation_test_cases = [
    "  hello world  ",
    "",
    123,
    "Valid Data",
    "x" * 150,  # Too long
]

for data in validation_test_cases:
    try:
        is_valid, processed, message = validate_and_process_data(data)
        status = "✅" if is_valid else "❌"
        print(f"  {status} validate_and_process_data({repr(data)[:20]}...): {message}")
        if processed:
            print(f"      Processed: '{processed}'")
    except Exception as e:
        print(f"  validate_and_process_data({repr(data)[:20]}...) - Error: {e}")

# Check counter
try:
    count = get_processing_statistics()
    print(f"  Total processed items: {count}")
except Exception as e:
    print(f"  Get statistics - Error: {e}")

print()

# EXERCISE 4: HIGHER-ORDER FUNCTIONS
print("EXERCISE 4: Higher-Order Functions")
print("=================================")

def apply_operation_to_list(numbers, operation):
    """
    Apply an operation function to each number in a list.
    
    Requirements:
    - Accept a list of numbers and an operation function
    - Apply the operation to each number
    - Return list of results
    - Handle empty lists
    
    Test Cases:
    - apply_operation_to_list([1, 2, 3], lambda x: x * 2) → [2, 4, 6]
    - apply_operation_to_list([1, 2, 3], lambda x: x ** 2) → [1, 4, 9]
    - apply_operation_to_list([], lambda x: x * 2) → []
    """
    # TODO: Implement this function
    pass

def filter_by_condition(items, condition):
    """
    Filter items based on a condition function.
    
    Requirements:
    - Accept a list of items and a condition function
    - Return list of items where condition returns True
    - Handle empty lists
    - Don't use built-in filter() function
    
    Test Cases:
    - filter_by_condition([1, 2, 3, 4, 5], lambda x: x > 3) → [4, 5]
    - filter_by_condition(['apple', 'banana', 'cherry'], lambda x: len(x) > 5) → ['banana', 'cherry']
    - filter_by_condition([], lambda x: True) → []
    """
    # TODO: Implement this function
    pass

def create_multiplier_function(factor):
    """
    Create and return a function that multiplies by the given factor.
    
    Requirements:
    - Return a function that takes one parameter
    - The returned function should multiply its input by factor
    - Use closure concept
    
    Test Cases:
    - double = create_multiplier_function(2)
    - double(5) → 10
    - triple = create_multiplier_function(3)  
    - triple(4) → 12
    """
    # TODO: Implement this function
    # Hints:
    # - Define an inner function that uses the factor parameter
    # - Return the inner function
    pass

# Test Exercise 4
print("Testing Exercise 4:")

# Test apply_operation_to_list
operation_test_cases = [
    ([1, 2, 3], lambda x: x * 2),
    ([1, 2, 3], lambda x: x ** 2),
    ([], lambda x: x * 2),
    ([5, 10, 15], lambda x: x / 5),
]

for numbers, operation in operation_test_cases:
    try:
        result = apply_operation_to_list(numbers, operation)
        print(f"  apply_operation_to_list({numbers}, operation) = {result}")
    except Exception as e:
        print(f"  apply_operation_to_list test - Error: {e}")

# Test filter_by_condition
filter_test_cases = [
    ([1, 2, 3, 4, 5], lambda x: x > 3),
    (['apple', 'banana', 'cherry'], lambda x: len(x) > 5),
    ([], lambda x: True),
    ([1, 2, 3, 4, 5], lambda x: x % 2 == 0),  # Even numbers
]

for items, condition in filter_test_cases:
    try:
        result = filter_by_condition(items, condition)
        print(f"  filter_by_condition({items}, condition) = {result}")
    except Exception as e:
        print(f"  filter_by_condition test - Error: {e}")

# Test create_multiplier_function
try:
    double = create_multiplier_function(2)
    triple = create_multiplier_function(3)
    
    print(f"  double = create_multiplier_function(2)")
    print(f"  double(5) = {double(5)}")
    print(f"  triple = create_multiplier_function(3)")
    print(f"  triple(4) = {triple(4)}")
except Exception as e:
    print(f"  create_multiplier_function test - Error: {e}")

print()

# EXERCISE 5: MODULAR DESIGN
print("EXERCISE 5: Modular Library Design")
print("==================================")

# Create a simple math library
class MathUtils:
    """
    A utility class containing mathematical functions.
    Implement the missing methods.
    """
    
    @staticmethod
    def factorial(n):
        """
        Calculate factorial of a non-negative integer.
        
        Requirements:
        - Handle n >= 0
        - Return 1 for n = 0 or n = 1
        - Use recursion or iteration
        - Raise ValueError for negative numbers
        
        Test Cases:
        - factorial(0) → 1
        - factorial(1) → 1
        - factorial(5) → 120
        - factorial(-1) → raises ValueError
        """
        # TODO: Implement this method
        pass
    
    @staticmethod
    def is_prime(n):
        """
        Check if a number is prime.
        
        Requirements:
        - Return True if n is prime, False otherwise
        - Handle edge cases (n < 2)
        - Use efficient algorithm
        
        Test Cases:
        - is_prime(2) → True
        - is_prime(17) → True
        - is_prime(4) → False
        - is_prime(1) → False
        """
        # TODO: Implement this method
        pass
    
    @staticmethod
    def gcd(a, b):
        """
        Calculate Greatest Common Divisor using Euclidean algorithm.
        
        Requirements:
        - Handle both positive and negative numbers
        - Return positive result
        - Use iterative approach
        
        Test Cases:
        - gcd(48, 18) → 6
        - gcd(17, 13) → 1
        - gcd(0, 5) → 5
        """
        # TODO: Implement this method
        pass

# Create a string utilities library
class StringUtils:
    """
    A utility class containing string manipulation functions.
    Implement the missing methods.
    """
    
    @staticmethod
    def reverse_words(sentence):
        """
        Reverse the order of words in a sentence.
        
        Requirements:
        - Split sentence into words
        - Reverse the order
        - Join back with spaces
        - Handle edge cases (empty string)
        
        Test Cases:
        - reverse_words("Hello World") → "World Hello"
        - reverse_words("The quick brown fox") → "fox brown quick The"
        - reverse_words("") → ""
        - reverse_words("SingleWord") → "SingleWord"
        """
        # TODO: Implement this method
        pass
    
    @staticmethod
    def count_vowels(text):
        """
        Count the number of vowels in text.
        
        Requirements:
        - Count a, e, i, o, u (case insensitive)
        - Return integer count
        - Handle empty strings
        
        Test Cases:
        - count_vowels("Hello World") → 3
        - count_vowels("Programming") → 3
        - count_vowels("xyz") → 0
        - count_vowels("") → 0
        """
        # TODO: Implement this method
        pass
    
    @staticmethod
    def title_case(text):
        """
        Convert text to title case (first letter of each word capitalized).
        
        Requirements:
        - Capitalize first letter of each word
        - Make other letters lowercase
        - Handle multiple spaces
        - Don't use built-in title() method
        
        Test Cases:
        - title_case("hello world") → "Hello World"
        - title_case("PYTHON programming") → "Python Programming"
        - title_case("") → ""
        """
        # TODO: Implement this method
        pass

# Test Exercise 5
print("Testing Exercise 5:")

print("MathUtils tests:")
# Test factorial
factorial_cases = [0, 1, 5]
for n in factorial_cases:
    try:
        result = MathUtils.factorial(n)
        print(f"  factorial({n}) = {result}")
    except Exception as e:
        print(f"  factorial({n}) - Error: {e}")

# Test negative factorial
try:
    result = MathUtils.factorial(-1)
    print(f"  factorial(-1) = {result} (should raise error)")
except ValueError:
    print(f"  factorial(-1) - ✅ Correctly raised ValueError")
except Exception as e:
    print(f"  factorial(-1) - Error: {e}")

# Test is_prime
prime_cases = [2, 17, 4, 1]
for n in prime_cases:
    try:
        result = MathUtils.is_prime(n)
        print(f"  is_prime({n}) = {result}")
    except Exception as e:
        print(f"  is_prime({n}) - Error: {e}")

# Test gcd
gcd_cases = [(48, 18), (17, 13), (0, 5)]
for a, b in gcd_cases:
    try:
        result = MathUtils.gcd(a, b)
        print(f"  gcd({a}, {b}) = {result}")
    except Exception as e:
        print(f"  gcd({a}, {b}) - Error: {e}")

print("\nStringUtils tests:")
# Test reverse_words
reverse_cases = ["Hello World", "The quick brown fox", "", "SingleWord"]
for text in reverse_cases:
    try:
        result = StringUtils.reverse_words(text)
        print(f"  reverse_words('{text}') = '{result}'")
    except Exception as e:
        print(f"  reverse_words('{text}') - Error: {e}")

# Test count_vowels
vowel_cases = ["Hello World", "Programming", "xyz", ""]
for text in vowel_cases:
    try:
        result = StringUtils.count_vowels(text)
        print(f"  count_vowels('{text}') = {result}")
    except Exception as e:
        print(f"  count_vowels('{text}') - Error: {e}")

# Test title_case
title_cases = ["hello world", "PYTHON programming", ""]
for text in title_cases:
    try:
        result = StringUtils.title_case(text)
        print(f"  title_case('{text}') = '{result}'")
    except Exception as e:
        print(f"  title_case('{text}') - Error: {e}")

print()

print("=== EXERCISE SOLUTIONS GUIDE ===")
print()
print("Complete the functions above and test your solutions.")
print("Here are some implementation hints:")
print()
print("💡 GENERAL TIPS:")
print("• Start with input validation (check types, ranges, empty cases)")
print("• Use descriptive variable names")
print("• Handle edge cases explicitly")
print("• Write clear return statements")
print("• Test with the provided test cases")
print()
print("💡 SPECIFIC HINTS:")
print()
print("EXERCISE 1:")
print("• add_numbers: Simple return a + b")
print("• calculate_average: Check for empty list, then sum(numbers) / len(numbers)")
print("• find_maximum: Loop through list, track maximum value")
print()
print("EXERCISE 2:")
print("• greet_person: Use f-string formatting: f'{greeting}, {name}{punctuation}'")
print("• calculate_total_cost: subtotal = sum(prices), apply discount, then tax")
print("• create_user_profile: Start with base dict, add **additional_info items")
print()
print("EXERCISE 3:")
print("• Use 'global total_processed_items' to modify global variable")
print("• Validate with isinstance(data, str) and len(data)")
print("• Clean data with data.strip().title()")
print()
print("EXERCISE 4:")
print("• apply_operation_to_list: Use list comprehension or loop")
print("• filter_by_condition: Loop and append items where condition(item) is True")
print("• create_multiplier_function: Return lambda x: x * factor")
print()
print("EXERCISE 5:")
print("• factorial: Use loop from 1 to n, multiply results")
print("• is_prime: Check divisibility from 2 to sqrt(n)")
print("• gcd: Use while loop with remainder operations")
print("• reverse_words: text.split() then reverse list")
print("• count_vowels: Loop through text, check if char.lower() in 'aeiou'")
print("• title_case: Split into words, capitalize first letter of each")

"""
EXERCISE COMPLETION CHECKLIST:
==============================

□ Exercise 1: Basic Function Operations
  - add_numbers(): Simple addition with type flexibility
  - calculate_average(): Handle empty list, compute mean
  - find_maximum(): Manual maximum finding without built-in

□ Exercise 2: Flexible Parameters
  - greet_person(): Default parameters for greeting customization
  - calculate_total_cost(): *args for prices, **kwargs for options
  - create_user_profile(): Required + **kwargs pattern

□ Exercise 3: Scope and Validation  
  - validate_and_process_data(): Global variable manipulation
  - get_processing_statistics(): Read global state
  - reset_processing_counter(): Modify global state

□ Exercise 4: Higher-Order Functions
  - apply_operation_to_list(): Function as parameter pattern
  - filter_by_condition(): Custom filtering with function condition
  - create_multiplier_function(): Closure creation and return

□ Exercise 5: Modular Design
  - MathUtils class: factorial, is_prime, gcd methods
  - StringUtils class: reverse_words, count_vowels, title_case methods

ADVANCED CHALLENGES:
===================
Once you complete the basic exercises, try these enhancements:

1. Add error handling to all functions with try/except blocks
2. Implement recursive versions of iterative functions
3. Create a decorator that logs function calls and execution time
4. Build a configuration system using closures
5. Implement a simple cache decorator for expensive functions
6. Create a validator framework using higher-order functions
7. Build a pipeline system that chains multiple operations
8. Implement a simple event system with function callbacks

TESTING YOUR SOLUTIONS:
=======================
• Run each function with the provided test cases
• Try edge cases (empty inputs, extreme values)
• Test error conditions and exception handling
• Verify that global variables work correctly
• Check that higher-order functions accept and use other functions properly
• Ensure modular classes provide clean, consistent interfaces

Remember: Good functions are focused, well-documented, and handle edge cases gracefully!
"""