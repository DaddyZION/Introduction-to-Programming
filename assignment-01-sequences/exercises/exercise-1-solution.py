"""
Assignment 1 - Exercise Solutions: Personal Information Calculator
================================================================

This file provides detailed solutions for Exercise 1: Personal Information Calculator
Study the code and comments to understand different approaches and techniques.

PROBLEM:
Create a program that:
1. Asks the user for their name, age, and birth year
2. Calculates and displays their age next year
3. Calculates how many years until they turn 65
4. Displays a nicely formatted summary
"""

print("=== PERSONAL INFORMATION CALCULATOR ===")
print()

# SOLUTION 1: Basic Version
print("Solution 1: Basic Implementation")
print("-" * 35)

# Get user information
name = input("Enter your name: ").strip().title()  # Clean and format input
age = int(input("Enter your age: "))               # Convert to integer
birth_year = int(input("Enter your birth year: "))  # Convert to integer

# Perform calculations
age_next_year = age + 1                           # Simple addition
years_to_retirement = 65 - age                    # Subtraction

# Display results
print()
print("=== PERSONAL INFORMATION SUMMARY ===")
print(f"Name: {name}")
print(f"Current Age: {age}")
print(f"Birth Year: {birth_year}")
print(f"Age Next Year: {age_next_year}")
print(f"Years Until Retirement (65): {years_to_retirement}")
print()

# SOLUTION 2: Enhanced Version with Validation and Additional Features
print("Solution 2: Enhanced Implementation with Extra Features")
print("-" * 55)

# Get user information with better prompts
full_name = input("Please enter your full name: ").strip().title()
current_age = int(input("What is your current age? "))
year_born = int(input("What year were you born? "))

# Additional calculations
age_in_10_years = current_age + 10
age_in_25_years = current_age + 25
years_lived = current_age
years_since_2000 = 2025 - 2000  # Assuming current year is 2025

# Create a comprehensive report
print()
print("=" * 50)
print("COMPREHENSIVE PERSONAL INFORMATION REPORT".center(50))
print("=" * 50)

print(f"\nBASIC INFORMATION:")
print(f"Full Name: {full_name}")
print(f"Current Age: {current_age} years old")
print(f"Birth Year: {year_born}")

print(f"\nFUTURE AGE PREDICTIONS:")
print(f"Age next year (2026): {current_age + 1}")
print(f"Age in 10 years: {age_in_10_years}")
print(f"Age in 25 years: {age_in_25_years}")

print(f"\nRETIREMENT PLANNING:")
retirement_age = 65
years_to_retire = retirement_age - current_age
retirement_year = 2025 + years_to_retire  # Assuming current year is 2025

if years_to_retire > 0:
    print(f"Years until retirement (age 65): {years_to_retire}")
    print(f"Expected retirement year: {retirement_year}")
else:
    print("You have already reached retirement age!")

print(f"\nLIFE STATISTICS:")
print(f"Years lived so far: {current_age}")
print(f"Approximate days lived: {current_age * 365:,}")  # Comma separator for large numbers
print(f"You were born {2025 - year_born} years ago")

print("=" * 50)
print("Report generated successfully!")
print()

# SOLUTION 3: Advanced Version with Error Handling and Formatting
print("Solution 3: Production-Ready Version")
print("-" * 35)

print("Advanced Personal Information System")
print("Please provide accurate information for best results.")
print()

# Get information with more user-friendly prompts
person_name = input("Your name: ").strip()
if person_name:
    person_name = person_name.title()  # Proper case formatting
else:
    person_name = "Anonymous User"     # Default if no name provided

person_age = int(input("Your current age: "))
birth_year_input = int(input("Year you were born: "))

# Validation and cross-checking
current_year = 2025  # You could use datetime.datetime.now().year for actual current year
calculated_age = current_year - birth_year_input

print(f"\nValidation Check:")
print(f"You said you are {person_age} years old")
print(f"Based on birth year {birth_year_input}, you should be {calculated_age}")

if abs(person_age - calculated_age) <= 1:  # Allow for birthday timing
    print("✅ Information appears consistent")
    working_age = person_age
else:
    print("⚠️ There might be a discrepancy in the information")
    working_age = calculated_age
    print(f"Using calculated age of {calculated_age} for calculations")

# Enhanced calculations
next_year_age = working_age + 1
retirement_years_left = max(0, 65 - working_age)  # Don't show negative years

# Milestone calculations
milestone_30 = max(0, 30 - working_age)
milestone_40 = max(0, 40 - working_age)
milestone_50 = max(0, 50 - working_age)

# Generate professional report
print()
print("┌" + "─" * 48 + "┐")
print("│" + " PERSONAL INFORMATION REPORT ".center(48) + "│")
print("├" + "─" * 48 + "┤")
print(f"│ Name: {person_name:<39} │")
print(f"│ Current Age: {working_age:<32} │")
print(f"│ Birth Year: {birth_year_input:<33} │")
print("├" + "─" * 48 + "┤")
print(f"│ Age Next Year: {next_year_age:<31} │")
print(f"│ Years to Retirement: {retirement_years_left:<24} │")
print("├" + "─" * 48 + "┤")

# Milestone reporting
print("│ UPCOMING MILESTONES:                         │")
if milestone_30 > 0:
    print(f"│ • Age 30 in {milestone_30} year(s)                       │")
if milestone_40 > 0:
    print(f"│ • Age 40 in {milestone_40} year(s)                       │")
if milestone_50 > 0:
    print(f"│ • Age 50 in {milestone_50} year(s)                       │")

print("└" + "─" * 48 + "┘")

print()
print("Thank you for using the Personal Information Calculator!")

"""
LEARNING POINTS FROM THESE SOLUTIONS:
=====================================

1. BASIC SOLUTION:
   - Demonstrates core concepts: input, calculation, output
   - Shows proper variable naming conventions
   - Uses f-string formatting for clean output

2. ENHANCED SOLUTION:
   - Adds more calculations and features
   - Shows how to build comprehensive reports
   - Demonstrates professional output formatting
   - Uses mathematical operations creatively

3. ADVANCED SOLUTION:
   - Includes input validation and error checking
   - Shows how to handle edge cases
   - Demonstrates professional report formatting
   - Uses conditional logic for better user experience

KEY TECHNIQUES DEMONSTRATED:
============================
• Input validation and cleaning (.strip(), .title())
• Type conversion (int(), float())
• Mathematical calculations and expressions
• String formatting and alignment
• Professional report generation
• Error handling basics
• User-friendly prompts and feedback

COMMON MISTAKES TO AVOID:
=========================
• Forgetting to convert input() to numbers
• Not handling empty input gracefully
• Poor variable naming (using x, y, z instead of descriptive names)
• Not formatting output for readability
• Not validating user input for reasonableness

PRACTICE SUGGESTIONS:
=====================
1. Modify the program to include more personal information
2. Add calculations for different retirement ages
3. Create a version that works with dates instead of just ages
4. Add input validation to ensure ages are reasonable (0-150)
5. Format the output in different styles (tables, bullet points, etc.)
"""
