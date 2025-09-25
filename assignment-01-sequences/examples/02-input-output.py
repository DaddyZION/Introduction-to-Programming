"""
Assignment 1 - Example 2: Input and Output Operations  
====================================================

This program demonstrates how to GET information FROM users (input)
and how to DISPLAY information TO users (output).

Key Concepts Demonstrated:
- Using input() to get user data
- Using print() to display information  
- Converting string input to numbers
- Formatting output nicely
- Sequential execution of input/output operations
"""

print("=== INPUT AND OUTPUT BASICS ===")
print()

# OUTPUT - Displaying information to the user
# The print() function displays text on the screen
print("Welcome to the Student Information Program!")
print("This program will collect and display your information.")
print()  # Empty print() creates a blank line for spacing


# BASIC INPUT - Getting text from the user
# The input() function pauses the program and waits for user to type something
print("Let's start by getting your basic information...")
print()

# input() always returns a STRING (text), even if user types numbers
student_name = input("Please enter your full name: ")
print("Hello", student_name + "!")  # Using + to join strings together
print()

# GETTING NUMERIC INPUT
# Since input() returns strings, we need to convert to numbers for math
print("Now let's get some numeric information...")

# Getting an integer (whole number)
age_as_string = input("Enter your age: ")          # This is a string like "20"
age = int(age_as_string)                           # Convert string to integer
print("You entered:", age_as_string, "(as text)")
print("Converted to number:", age)
print()

# Shorter way - convert directly in one line
current_year = int(input("What year is it? "))     # Convert immediately
birth_year = current_year - age                    # Now we can do math!
print("You were born in:", birth_year)
print()

# Getting a float (decimal number) 
height = float(input("Enter your height in meters (e.g., 1.75): "))
print("Your height is:", height, "meters")
print()

# FORMATTED OUTPUT - Making output look nice
print("=== FORMATTED OUTPUT ===")
print()

# Method 1: Using commas in print (adds spaces automatically)
print("Name:", student_name)
print("Age:", age, "years old")
print("Height:", height, "meters")
print()

# Method 2: Using + to join strings (no automatic spaces)
print("Hello " + student_name + ", you are " + str(age) + " years old.")
print()  # Note: str(age) converts number back to string for joining

# Method 3: Using f-strings (modern Python - very readable!)
print(f"Student Profile:")
print(f"Name: {student_name}")
print(f"Age: {age} years") 
print(f"Height: {height} meters")
print(f"Born in: {birth_year}")
print()

# SEQUENTIAL EXECUTION EXAMPLE
print("=== SEQUENTIAL EXECUTION DEMO ===")
print()
print("Programs execute line by line, from top to bottom.")
print("Watch the order of these statements:")
print()

print("Statement 1: This prints first")
user_input = input("Statement 2: Enter anything and press Enter: ")
print("Statement 3: You entered:", user_input)
print("Statement 4: This prints last")
print()

# PRACTICAL EXAMPLE - A simple calculator
print("=== PRACTICAL EXAMPLE: SIMPLE CALCULATOR ===")
print()

print("Let's create a simple calculator!")
print("Enter two numbers and I'll add them together.")
print()

# Get first number
first_number = float(input("Enter the first number: "))

# Get second number  
second_number = float(input("Enter the second number: "))

# Calculate the sum
total = first_number + second_number

# Display the result
print()
print("CALCULATION RESULT:")
print(f"{first_number} + {second_number} = {total}")
print()

# MULTIPLE INPUTS AND OUTPUTS
print("=== COLLECTING MULTIPLE PIECES OF INFORMATION ===")
print()

# Collecting course information
print("Let's record information about a course:")
course_name = input("Course name: ")
course_code = input("Course code: ")  
credits = int(input("Number of credits: "))
instructor = input("Instructor name: ")

print()
print("COURSE SUMMARY:")
print("-" * 40)  # Print a line of dashes
print(f"Course: {course_name} ({course_code})")
print(f"Credits: {credits}")
print(f"Instructor: {instructor}")
print("-" * 40)
print()

# DEMONSTRATING DATA TYPE CONVERSION
print("=== DATA TYPE CONVERSIONS ===")
print()

print("Remember: input() ALWAYS returns a string!")
user_input = input("Enter a number: ")
print(f"What you entered: '{user_input}' (type: {type(user_input)})")

# Convert to different types
as_integer = int(user_input)
as_float = float(user_input)
print(f"As integer: {as_integer} (type: {type(as_integer)})")
print(f"As float: {as_float} (type: {type(as_float)})")
print()

print("=== SUMMARY ===")
print()
print("Key points about Input/Output:")
print("1. input() gets text from the user (always returns a string)")
print("2. print() displays information to the user")
print("3. Convert strings to numbers using int() or float()")
print("4. Use f-strings for neat, readable output formatting")
print("5. Programs execute statements in sequential order")
print()
print("Great job! You now understand the basics of input and output.")

"""
KEY TAKEAWAYS:
==============
1. input() - gets data FROM the user (always returns string)
2. print() - shows data TO the user
3. Convert input strings to numbers: int() for whole numbers, float() for decimals
4. Use f-strings for clean output formatting: f"Hello {name}"
5. Statements execute in order from top to bottom

COMMON MISTAKES:
================
- Forgetting to convert input() to numbers before doing math
- Not using descriptive variable names
- Forgetting that input() pauses the program until user responds

NEXT STEP:
Go to 03-arithmetic-operations.py to learn about mathematical calculations!
"""