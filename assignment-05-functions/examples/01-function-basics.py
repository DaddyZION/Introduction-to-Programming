"""
Assignment 5 - Example 1: Function Basics
==========================================

This program introduces the fundamental concepts of functions in Python.
Functions are reusable blocks of code that perform specific tasks, making
programs more organized, maintainable, and efficient.

Key Concepts Demonstrated:
- Function definition with def keyword
- Function calls and execution flow
- Return values and the return statement
- Function parameters and arguments
- Function documentation with docstrings
- The None return value
"""

print("=== FUNCTION BASICS ===")
print()

print("Functions are the building blocks of modular programming.")
print("They allow us to:")
print("• Break complex problems into smaller, manageable pieces")
print("• Reuse code without repetition")
print("• Organize code logically")
print("• Make debugging and testing easier")
print("• Enable team collaboration")
print()

# BASIC FUNCTION DEFINITION
print("=== BASIC FUNCTION DEFINITION ===")
print()

def greet():
    """
    A simple function that prints a greeting message.
    This function takes no parameters and returns nothing (None).
    """
    print("Hello! Welcome to function programming!")

print("Function definition syntax:")
print("def function_name():")
print("    '''Optional docstring'''")
print("    # Function body")
print("    # Optional return statement")
print()

print("Calling the greet() function:")
greet()  # Function call
print()

# FUNCTION WITH RETURN VALUE
print("=== FUNCTIONS WITH RETURN VALUES ===")
print()

def get_greeting():
    """
    A function that returns a greeting message instead of printing it.
    Return values allow functions to provide data back to the caller.
    """
    return "Hello from the get_greeting function!"

def add_two_numbers():
    """
    A function that performs a calculation and returns the result.
    """
    number1 = 10
    number2 = 15
    result = number1 + number2
    return result

print("Functions can return values using the 'return' statement:")
print()

# Calling function and using return value
message = get_greeting()
print(f"Returned message: {message}")

# Using return value in calculations
sum_result = add_two_numbers()
print(f"Sum result: {sum_result}")

# Return values can be used directly in expressions
print(f"Double the sum: {add_two_numbers() * 2}")
print()

# FUNCTION WITH PARAMETERS
print("=== FUNCTIONS WITH PARAMETERS ===")
print()

def greet_person(name):
    """
    A function that takes a parameter and uses it in the greeting.
    Parameters allow functions to work with different data.
    
    Args:
        name (str): The name of the person to greet
    
    Returns:
        str: A personalized greeting message
    """
    return f"Hello, {name}! Nice to meet you!"

def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    """
    area = length * width
    return area

def create_full_name(first_name, last_name):
    """
    Combine first and last names into a full name.
    
    Args:
        first_name (str): The person's first name
        last_name (str): The person's last name
    
    Returns:
        str: The formatted full name
    """
    full_name = f"{first_name} {last_name}"
    return full_name

print("Functions can accept parameters to work with different data:")
print()

# Using functions with parameters
print(greet_person("Alice"))
print(greet_person("Bob"))
print()

# Mathematical calculations with parameters
rect_area = calculate_rectangle_area(5, 3)
print(f"Rectangle area (5 x 3): {rect_area}")

rect_area = calculate_rectangle_area(7.5, 4.2)
print(f"Rectangle area (7.5 x 4.2): {rect_area}")
print()

# String manipulation with parameters
name1 = create_full_name("John", "Doe")
name2 = create_full_name("Jane", "Smith")
print(f"Full names: {name1}, {name2}")
print()

# MULTIPLE PARAMETERS AND COMPLEX LOGIC
print("=== FUNCTIONS WITH MULTIPLE PARAMETERS ===")
print()

def calculate_grade(points_earned, total_points):
    """
    Calculate a percentage grade from points earned and total points.
    
    Args:
        points_earned (int): Points the student earned
        total_points (int): Total points possible
    
    Returns:
        float: The percentage grade
    """
    if total_points == 0:
        return 0.0  # Avoid division by zero
    
    percentage = (points_earned / total_points) * 100
    return round(percentage, 2)  # Round to 2 decimal places

def get_letter_grade(percentage):
    """
    Convert a percentage to a letter grade.
    
    Args:
        percentage (float): The percentage grade
    
    Returns:
        str: The corresponding letter grade
    """
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def format_temperature(celsius):
    """
    Convert Celsius to Fahrenheit and return formatted string.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        str: Formatted temperature string with both scales
    """
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C = {fahrenheit:.1f}°F"

print("Testing grade calculation functions:")
percentage = calculate_grade(85, 100)
letter = get_letter_grade(percentage)
print(f"Student scored {percentage}% which is a '{letter}' grade")

percentage = calculate_grade(42, 50)
letter = get_letter_grade(percentage)
print(f"Student scored {percentage}% which is a '{letter}' grade")
print()

print("Testing temperature conversion:")
print(format_temperature(0))      # Freezing point
print(format_temperature(100))    # Boiling point
print(format_temperature(25))     # Room temperature
print(format_temperature(-40))    # Same in both scales!
print()

# FUNCTIONS THAT CALL OTHER FUNCTIONS
print("=== FUNCTIONS CALLING OTHER FUNCTIONS ===")
print()

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
    
    Returns:
        float: The area of the circle
    """
    pi = 3.14159
    area = pi * radius * radius
    return area

def calculate_circle_circumference(radius):
    """
    Calculate the circumference of a circle.
    
    Args:
        radius (float): The radius of the circle
    
    Returns:
        float: The circumference of the circle
    """
    pi = 3.14159
    circumference = 2 * pi * radius
    return circumference

def analyze_circle(radius):
    """
    Perform complete circle analysis by calling other functions.
    This demonstrates how functions can work together.
    
    Args:
        radius (float): The radius of the circle
    
    Returns:
        dict: Dictionary containing all circle measurements
    """
    area = calculate_circle_area(radius)
    circumference = calculate_circle_circumference(radius)
    
    return {
        'radius': radius,
        'area': round(area, 2),
        'circumference': round(circumference, 2),
        'diameter': radius * 2
    }

print("Circle analysis using multiple functions:")
circle_data = analyze_circle(5)
print(f"Circle with radius {circle_data['radius']}:")
print(f"  • Diameter: {circle_data['diameter']}")
print(f"  • Area: {circle_data['area']}")
print(f"  • Circumference: {circle_data['circumference']}")
print()

# THE NONE RETURN VALUE
print("=== THE NONE RETURN VALUE ===")
print()

def print_message(message):
    """
    A function that prints a message but doesn't return anything.
    Functions without explicit return statements return None.
    """
    print(f"Message: {message}")
    # No return statement = returns None

def do_calculation():
    """
    A function that performs calculations but doesn't return the result.
    """
    result = 5 + 3
    print(f"The calculation result is: {result}")
    # No return statement

print("Functions without return statements return None:")
return_value = print_message("Hello World")
print(f"Return value: {return_value}")

return_value = do_calculation()
print(f"Return value: {return_value}")
print()

# EARLY RETURNS AND MULTIPLE RETURN POINTS
print("=== MULTIPLE RETURN POINTS ===")
print()

def check_number_type(number):
    """
    Analyze a number and return a description.
    Demonstrates multiple return points in a function.
    
    Args:
        number (int): The number to analyze
    
    Returns:
        str: Description of the number type
    """
    if number == 0:
        return "The number is zero"
    
    if number > 0:
        if number % 2 == 0:
            return f"{number} is a positive even number"
        else:
            return f"{number} is a positive odd number"
    
    # number < 0
    if number % 2 == 0:
        return f"{number} is a negative even number"
    else:
        return f"{number} is a negative odd number"

def validate_age(age):
    """
    Validate an age value and return appropriate message.
    Uses early returns for error conditions.
    
    Args:
        age: The age value to validate
    
    Returns:
        str: Validation result message
    """
    # Early return for invalid types
    if not isinstance(age, (int, float)):
        return "Error: Age must be a number"
    
    # Early return for negative ages
    if age < 0:
        return "Error: Age cannot be negative"
    
    # Early return for unrealistic ages
    if age > 150:
        return "Error: Age seems unrealistic"
    
    # Normal processing if all validations pass
    if age < 13:
        return f"Age {age}: Child"
    elif age < 20:
        return f"Age {age}: Teenager"
    elif age < 65:
        return f"Age {age}: Adult"
    else:
        return f"Age {age}: Senior"

print("Testing number type analysis:")
test_numbers = [0, 5, -3, 8, -12]
for num in test_numbers:
    print(f"  {check_number_type(num)}")
print()

print("Testing age validation:")
test_ages = [25, -5, "abc", 150, 10, 75]
for age in test_ages:
    print(f"  {validate_age(age)}")
print()

# PRACTICAL EXAMPLE: SIMPLE CALCULATOR
print("=== PRACTICAL EXAMPLE: SIMPLE CALCULATOR ===")
print()

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
    """Divide first number by second, with error handling."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculate(operation, num1, num2):
    """
    Perform calculation based on operation string.
    
    Args:
        operation (str): The operation to perform (+, -, *, /)
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        The result of the calculation or error message
    """
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    else:
        return f"Error: Unknown operation '{operation}'"

print("Simple calculator demonstration:")
calculations = [
    ('+', 10, 5),
    ('-', 10, 5),
    ('*', 10, 5),
    ('/', 10, 5),
    ('/', 10, 0),  # Division by zero
    ('%', 10, 5)   # Unknown operation
]

for op, x, y in calculations:
    result = calculate(op, x, y)
    print(f"  {x} {op} {y} = {result}")

print()

print("=== FUNCTION DOCUMENTATION BEST PRACTICES ===")
print()

def process_student_data(student_name, grades_list, extra_credit=0):
    """
    Process student academic data and calculate final grade.
    
    This function demonstrates comprehensive docstring documentation
    following Python conventions.
    
    Args:
        student_name (str): The name of the student
        grades_list (list): List of numeric grades (0-100)
        extra_credit (int, optional): Extra credit points. Defaults to 0.
    
    Returns:
        dict: A dictionary containing:
            - name (str): Student's name
            - average (float): Average grade
            - letter_grade (str): Letter grade (A-F)
            - total_points (float): Average plus extra credit
    
    Raises:
        ValueError: If grades_list is empty or contains invalid grades
        TypeError: If student_name is not a string
    
    Examples:
        >>> process_student_data("John", [85, 90, 78])
        {'name': 'John', 'average': 84.33, 'letter_grade': 'B', 'total_points': 84.33}
        
        >>> process_student_data("Jane", [95, 98, 92], 5)
        {'name': 'Jane', 'average': 95.0, 'letter_grade': 'A', 'total_points': 100.0}
    """
    # Input validation
    if not isinstance(student_name, str):
        raise TypeError("Student name must be a string")
    
    if not grades_list:
        raise ValueError("Grades list cannot be empty")
    
    # Calculate average
    total = sum(grades_list)
    average = total / len(grades_list)
    
    # Add extra credit
    final_score = min(average + extra_credit, 100)  # Cap at 100
    
    # Determine letter grade
    letter = get_letter_grade(final_score)
    
    return {
        'name': student_name,
        'average': round(average, 2),
        'letter_grade': letter,
        'total_points': round(final_score, 2)
    }

print("Processing student data with comprehensive documentation:")
try:
    student_result = process_student_data("Alice Johnson", [88, 92, 85, 90], 3)
    print(f"Student: {student_result['name']}")
    print(f"Average: {student_result['average']}%")
    print(f"With extra credit: {student_result['total_points']}%")
    print(f"Letter grade: {student_result['letter_grade']}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

print()

print("=== SUMMARY ===")
print()
print("Function Basics Summary:")
print("1. Functions are defined with the 'def' keyword")
print("2. Functions can take parameters to work with different data")
print("3. Functions can return values using the 'return' statement")
print("4. Functions without return statements return None")
print("5. Functions can call other functions to build complex behavior")
print("6. Good documentation makes functions easier to understand and use")
print("7. Functions enable code reuse and better organization")

"""
KEY TAKEAWAYS:
==============
1. Functions are the foundation of modular programming
2. Use descriptive names and clear documentation
3. Keep functions focused on specific tasks
4. Parameters make functions flexible and reusable
5. Return values allow functions to provide results
6. Functions can call other functions for complex operations
7. Proper error handling makes functions robust

FUNCTION DEFINITION SYNTAX:
==========================
def function_name(parameter1, parameter2, ...):
    '''
    Docstring describing what the function does
    '''
    # Function body
    # Process parameters
    return result  # Optional

FUNCTION CALL SYNTAX:
====================
result = function_name(argument1, argument2, ...)

BEST PRACTICES:
===============
• Use descriptive function names (verb_noun format)
• Write clear docstrings explaining purpose, parameters, and return values
• Keep functions short and focused on one task
• Use meaningful parameter names
• Handle edge cases and potential errors
• Return consistent data types
• Follow PEP 8 style guidelines

NEXT STEP:
Go to 02-parameters-arguments.py to learn about different parameter types!
"""