"""
Assignment 1 - Example 3: Arithmetic Operations
=============================================

This program demonstrates mathematical operations and calculations.
In programming, we can perform various mathematical operations just like
using a calculator, but with much more power and flexibility.

Key Concepts Demonstrated:
- Basic arithmetic operators (+, -, *, /, //, %, **)
- Order of operations (PEMDAS/BODMAS)
- Working with different number types
- Mathematical functions
- Practical calculation examples
"""

print("=== BASIC ARITHMETIC OPERATORS ===")
print()

# Let's start with some basic numbers for our examples
a = 10
b = 3
print(f"We'll use a = {a} and b = {b} for our examples")
print()

# ADDITION (+)
# Adds two numbers together
addition_result = a + b
print(f"Addition: {a} + {b} = {addition_result}")

# SUBTRACTION (-)
# Subtracts the second number from the first
subtraction_result = a - b  
print(f"Subtraction: {a} - {b} = {subtraction_result}")

# MULTIPLICATION (*)
# Multiplies two numbers
multiplication_result = a * b
print(f"Multiplication: {a} * {b} = {multiplication_result}")

# DIVISION (/)
# Divides first number by second - ALWAYS gives a decimal result
division_result = a / b
print(f"Division: {a} / {b} = {division_result}")

# FLOOR DIVISION (//)
# Divides and rounds DOWN to the nearest whole number
floor_division_result = a // b
print(f"Floor Division: {a} // {b} = {floor_division_result}")

# MODULUS (%)
# Gives the REMAINDER after division (very useful!)
modulus_result = a % b
print(f"Modulus (remainder): {a} % {b} = {modulus_result}")

# EXPONENTIATION (**)
# Raises first number to the power of the second number
power_result = a ** b
print(f"Exponentiation: {a} ** {b} = {power_result}")
print()

# UNDERSTANDING MODULUS (%) - Very Important!
print("=== UNDERSTANDING MODULUS (REMAINDER) ===")
print()
print("Modulus (%) gives you the remainder after division:")

examples = [(10, 3), (15, 4), (20, 5), (17, 6)]
for x, y in examples:
    remainder = x % y
    quotient = x // y
    print(f"{x} ÷ {y} = {quotient} remainder {remainder}")
    print(f"  So {x} % {y} = {remainder}")
    print(f"  Check: {quotient} × {y} + {remainder} = {quotient * y + remainder}")
    print()

# ORDER OF OPERATIONS (PEMDAS/BODMAS)
print("=== ORDER OF OPERATIONS ===")
print()
print("Just like in math, programming follows order of operations:")
print("1. Parentheses/Brackets")
print("2. Exponents/Orders")  
print("3. Multiplication and Division (left to right)")
print("4. Addition and Subtraction (left to right)")
print()

# Examples showing order of operations
expression1 = 2 + 3 * 4
expression2 = (2 + 3) * 4
expression3 = 2 ** 3 * 4
expression4 = 2 * 3 ** 4

print("Expression examples:")
print(f"2 + 3 * 4 = {expression1} (multiply first, then add)")
print(f"(2 + 3) * 4 = {expression2} (parentheses first)")
print(f"2 ** 3 * 4 = {expression3} (exponent first: 8 * 4)")
print(f"2 * 3 ** 4 = {expression4} (exponent first: 2 * 81)")
print()

# WORKING WITH DIFFERENT NUMBER TYPES
print("=== WORKING WITH INTEGERS AND FLOATS ===")
print()

# Integers (whole numbers)
int1 = 10
int2 = 3

# Floats (decimal numbers)
float1 = 10.5
float2 = 2.5

print("Integer operations:")
print(f"{int1} + {int2} = {int1 + int2} (result type: {type(int1 + int2)})")
print(f"{int1} / {int2} = {int1 / int2} (result type: {type(int1 / int2)})")
print()

print("Float operations:")
print(f"{float1} + {float2} = {float1 + float2} (result type: {type(float1 + float2)})")
print(f"{float1} * {int2} = {float1 * int2} (result type: {type(float1 * int2)})")
print()

# ROUNDING AND FORMATTING NUMBERS
print("=== ROUNDING AND FORMATTING NUMBERS ===")
print()

result = 22 / 7  # Approximation of pi
print(f"22 / 7 = {result}")
print(f"Rounded to 2 decimal places: {round(result, 2)}")
print(f"Rounded to nearest integer: {round(result)}")
print(f"Formatted with f-string: {result:.3f}")  # 3 decimal places
print()

# PRACTICAL EXAMPLE 1: CALCULATING AREA AND PERIMETER
print("=== PRACTICAL EXAMPLE 1: RECTANGLE CALCULATIONS ===")
print()

# Get dimensions from user
print("Let's calculate the area and perimeter of a rectangle!")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display results
print(f"\nRectangle with length {length} and width {width}:")
print(f"Area = length × width = {length} × {width} = {area}")
print(f"Perimeter = 2 × (length + width) = 2 × ({length} + {width}) = {perimeter}")
print()

# PRACTICAL EXAMPLE 2: TEMPERATURE CONVERSION
print("=== PRACTICAL EXAMPLE 2: TEMPERATURE CONVERSION ===")
print()

print("Converting Celsius to Fahrenheit")
celsius = float(input("Enter temperature in Celsius: "))

# Formula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")
print(f"Formula used: F = (C × 9/5) + 32")
print(f"Calculation: F = ({celsius} × 9/5) + 32 = {fahrenheit}")
print()

# PRACTICAL EXAMPLE 3: FINANCIAL CALCULATIONS
print("=== PRACTICAL EXAMPLE 3: SHOPPING BILL CALCULATOR ===")
print()

print("Calculate total bill with tax")
item_price = float(input("Enter item price: £"))
quantity = int(input("Enter quantity: "))
tax_rate = float(input("Enter tax rate (as decimal, e.g., 0.20 for 20%): "))

# Calculate subtotal, tax amount, and total
subtotal = item_price * quantity
tax_amount = subtotal * tax_rate  
total = subtotal + tax_amount

print(f"\nBILL BREAKDOWN:")
print(f"Item price: £{item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: £{item_price:.2f} × {quantity} = £{subtotal:.2f}")
print(f"Tax ({tax_rate*100:.0f}%): £{subtotal:.2f} × {tax_rate} = £{tax_amount:.2f}")
print(f"TOTAL: £{subtotal:.2f} + £{tax_amount:.2f} = £{total:.2f}")
print()

# ADVANCED OPERATIONS WITH MULTIPLE STEPS
print("=== ADVANCED: COMPOUND CALCULATIONS ===")
print()

print("Calculate compound interest")
principal = float(input("Enter initial amount (£): "))
rate = float(input("Enter annual interest rate (as decimal): "))
time = int(input("Enter number of years: "))

# Compound interest formula: A = P(1 + r)^t
amount = principal * ((1 + rate) ** time)
interest_earned = amount - principal

print(f"\nCOMPOUND INTEREST CALCULATION:")
print(f"Principal: £{principal:.2f}")
print(f"Rate: {rate*100:.1f}% per year")
print(f"Time: {time} years")
print(f"Formula: A = P(1 + r)^t")
print(f"Amount = £{principal:.2f} × (1 + {rate})^{time}")
print(f"Amount = £{principal:.2f} × {(1 + rate):.3f}^{time}")
print(f"Amount = £{principal:.2f} × {(1 + rate)**time:.3f}")
print(f"Final Amount: £{amount:.2f}")
print(f"Interest Earned: £{interest_earned:.2f}")
print()

print("=== SUMMARY ===")
print()
print("Arithmetic Operators:")
print("+ (addition), - (subtraction), * (multiplication)")
print("/ (division), // (floor division), % (modulus), ** (exponentiation)")
print()
print("Key Points:")
print("1. Follow order of operations (PEMDAS)")
print("2. Use parentheses to control order")
print("3. Division (/) always gives float result")
print("4. Modulus (%) gives remainder - very useful!")
print("5. Mix integers and floats carefully")
print("6. Use round() or f-strings for neat number display")

"""
KEY TAKEAWAYS:
==============
1. Basic operators: + - * / // % **
2. Order of operations matters (PEMDAS/BODMAS)
3. Division (/) always returns a float
4. Floor division (//) returns integer part
5. Modulus (%) returns remainder - very useful for many problems!
6. Use parentheses to control calculation order
7. round() function helps format decimal results

COMMON MISTAKES:
================
- Forgetting order of operations
- Confusing / and // operators
- Not understanding what modulus (%) does
- Integer division giving unexpected results in older Python versions

NEXT STEP:
Go to 04-string-operations.py to learn about working with text!
"""