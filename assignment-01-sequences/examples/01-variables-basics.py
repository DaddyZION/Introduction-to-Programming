"""
Assignment 1 - Example 1: Variables Basics
==========================================

This program introduces the fundamental concept of VARIABLES.
Variables are like labeled containers that store different types of data.

Key Concepts Demonstrated:
- Variable declaration and assignment
- Different data types (int, float, string, boolean)
- Variable naming conventions
- Memory concepts
"""

# WHAT IS A VARIABLE?
# A variable is a named storage location in computer memory.
# Think of it like a labeled box where you can put different things.



print("=== UNDERSTANDING VARIABLES ===")
print()

# INTEGER VARIABLES
# Integers are whole numbers (positive, negative, or zero)
student_age = 20              # This creates a variable called 'student_age' and stores 20 in it
course_credits = 3            # Another integer variable
year_of_study = 1             # Variables should have meaningful names

print("Integer Variables:")
print("Student age:", student_age)
print("Course credits:", course_credits) 
print("Year of study:", year_of_study)
print()

# FLOAT VARIABLES  
# Floats are decimal numbers (numbers with fractional parts)
student_gpa = 3.75            # Grade Point Average as a decimal
height_in_meters = 1.75       # Height with decimal precision
temperature = 23.5            # Temperature can be fractional

print("Float Variables:")
print("Student GPA:", student_gpa)
print("Height in meters:", height_in_meters)
print("Temperature:", temperature)
print()

# STRING VARIABLES
# Strings are text data - sequences of characters enclosed in quotes
student_name = "Alice Johnson"     # Double quotes work
course_code = 'COMP101'           # Single quotes also work
university = "Tech University"     # Use consistent style

print("String Variables:")
print("Student name:", student_name)
print("Course code:", course_code)
print("University:", university)
print()

# BOOLEAN VARIABLES
# Booleans store True or False values (yes/no, on/off type data)
is_enrolled = True            # Student is enrolled (True/False)
has_passed = False           # Has the student passed? (not yet)
is_full_time = True          # Is this a full-time student?

print("Boolean Variables:")
print("Is enrolled:", is_enrolled)
print("Has passed:", has_passed) 
print("Is full-time:", is_full_time)
print()

# VARIABLE NAMING RULES AND CONVENTIONS
print("=== VARIABLE NAMING ===")
print()

# GOOD variable names (descriptive and clear):
first_name = "John"           # Uses underscore for multiple words
lastName = "Smith"            # Camel case is also acceptable  
age_in_years = 25            # Very descriptive
total_score = 95             # Clear what this represents

# AVOID these variable names:
# x = "John"                 # Too short, not descriptive
# n = "Smith"               # What does 'n' mean?
# a = 25                    # Could be anything
# ts = 95                   # Abbreviation is unclear

print("Good variable names help make code readable!")
print("first_name:", first_name)
print("lastName:", lastName) 
print("age_in_years:", age_in_years)
print("total_score:", total_score)
print()

# VARIABLES CAN BE REASSIGNED
print("=== VARIABLE REASSIGNMENT ===")
print()

# Variables can change their values during program execution
current_score = 0            # Start with 0 points
print("Initial score:", current_score)

current_score = 25           # Player earns 25 points
print("After earning points:", current_score)

current_score = current_score + 10    # Add 10 more points
print("After bonus points:", current_score)
print()

# MULTIPLE ASSIGNMENT
print("=== MULTIPLE ASSIGNMENT ===")
print()

# You can assign the same value to multiple variables
x = y = z = 0               # All three variables get the value 0
print("x =", x, "y =", y, "z =", z)

# Or assign multiple values at once
name, age, grade = "Bob", 22, "A"    # Assigns three values to three variables
print("Name:", name, "Age:", age, "Grade:", grade)
print()

print("=== MEMORY CONCEPT ===")
print()
print("When you create a variable, the computer:")
print("1. Reserves a space in memory")
print("2. Labels that space with your variable name")  
print("3. Stores your data in that space")
print("4. Lets you access the data using the variable name")
print()
print("This is the foundation of all programming!")

"""
KEY TAKEAWAYS:
==============
1. Variables are named containers for storing data
2. Python has different data types: int, float, str, bool
3. Variable names should be descriptive and meaningful
4. Variables can be reassigned new values
5. Understanding variables is crucial for all programming

NEXT STEP:
Go to 02-input-output.py to learn about getting data from users!
"""