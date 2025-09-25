"""
Assignment 3 - Example 1: Basic FOR Loops
========================================

This program introduces the fundamental concept of FOR LOOPS.
A for loop allows you to repeat code a specific number of times
or iterate over a sequence of items.

Key Concepts Demonstrated:
- Basic for loop syntax with range()
- Loop variables and how they change
- Different ways to use range()
- Counting patterns and sequences
- Accumulator patterns (building up totals)
"""

print("=== UNDERSTANDING FOR LOOPS ===")
print()

# WHAT IS A FOR LOOP?
# A for loop repeats a block of code for each item in a sequence.
# The most common sequence is range(), which generates numbers.

print("For loops let you repeat code efficiently!")
print("Instead of writing the same code multiple times,")
print("you write it once and let the loop repeat it.")
print()

# BASIC FOR LOOP SYNTAX
print("=== BASIC FOR LOOP EXAMPLES ===")
print()

# Example 1: Simple counting loop
print("Example 1: Count from 0 to 4")
for i in range(5):              # range(5) creates [0, 1, 2, 3, 4]
    print(f"Count: {i}")

print()

# Example 2: Understanding the loop variable
print("Example 2: Understanding the loop variable 'i'")
print("The variable 'i' automatically takes each value in the sequence:")

for number in range(3):         # You can use any name, not just 'i'
    print(f"The loop variable 'number' is now: {number}")
    print(f"  This is iteration #{number + 1}")
    print(f"  We are inside the loop!")
    print()  # Empty line for readability

print("Loop is finished - we're outside the loop now")
print()

# DIFFERENT WAYS TO USE RANGE()
print("=== DIFFERENT WAYS TO USE RANGE() ===")
print()

# range(stop) - starts at 0, goes up to (but not including) stop
print("range(5) produces:")
for i in range(5):
    print(i, end=" ")  # end=" " puts a space instead of newline
print()  # New line after the loop
print()

# range(start, stop) - starts at start, goes up to (but not including) stop
print("range(2, 6) produces:")
for i in range(2, 6):
    print(i, end=" ")
print()
print()

# range(start, stop, step) - starts at start, increases by step each time
print("range(1, 10, 2) produces:")
for i in range(1, 10, 2):      # Odd numbers from 1 to 9
    print(i, end=" ")
print()
print()

# Counting backwards
print("range(10, 0, -1) produces:")
for i in range(10, 0, -1):     # Count backwards from 10 to 1
    print(i, end=" ")
print()
print()

# PRACTICAL COUNTING EXAMPLES
print("=== PRACTICAL COUNTING EXAMPLES ===")
print()

# Example 1: Times table
print("Example 1: Generate 5 times table")
number = int(input("Enter a number for times table: "))

print(f"\nTimes table for {number}:")
for i in range(1, 11):          # 1 to 10 inclusive
    result = number * i
    print(f"{number} × {i} = {result}")

print()

# Example 2: Countdown
print("Example 2: Rocket launch countdown")
print("Countdown starting...")

for count in range(10, 0, -1):  # 10 down to 1
    print(f"{count}...")
    
print("🚀 BLAST OFF!")
print()

# Example 3: Student roll call
print("Example 3: Student roll call")
num_students = int(input("How many students are in class? "))

print(f"\nTaking attendance for {num_students} students:")
for student_number in range(1, num_students + 1):  # 1 to num_students inclusive
    print(f"Student #{student_number}: Present")

print("Attendance complete!")
print()

# ACCUMULATOR PATTERNS - Building up totals
print("=== ACCUMULATOR PATTERNS ===")
print()

# Example 1: Sum of numbers
print("Example 1: Calculate sum of numbers 1 to 10")

total = 0                       # Initialize accumulator
print(f"Starting total: {total}")

for number in range(1, 11):     # 1 to 10 inclusive
    total = total + number      # Add current number to total
    print(f"Adding {number}: total is now {total}")

print(f"Final total: {total}")
print()

# Example 2: Build a string
print("Example 2: Build a string with loop")

message = ""                    # Initialize empty string
for i in range(5):
    message = message + f"Step {i+1} "
    print(f"Building message: '{message}'")

print(f"Final message: '{message}'")
print()

# Example 3: Count even numbers
print("Example 3: Count even numbers from 1 to 20")

even_count = 0                  # Initialize counter
print("Checking numbers from 1 to 20:")

for number in range(1, 21):     # 1 to 20 inclusive
    if number % 2 == 0:         # If number is even
        even_count = even_count + 1
        print(f"{number} is even (count: {even_count})")
    else:
        print(f"{number} is odd")

print(f"Total even numbers found: {even_count}")
print()

# INTERACTIVE EXAMPLE
print("=== INTERACTIVE EXAMPLE: GRADE CALCULATOR ===")
print()

print("Grade Calculator - Calculate average of multiple test scores")
num_tests = int(input("How many test scores do you want to enter? "))

total_score = 0                 # Accumulator for sum
print(f"\nPlease enter {num_tests} test scores:")

for test_number in range(1, num_tests + 1):
    score = float(input(f"Enter score for test #{test_number}: "))
    total_score = total_score + score
    print(f"  Running total: {total_score}")

# Calculate average
average_score = total_score / num_tests

print(f"\n=== GRADE SUMMARY ===")
print(f"Number of tests: {num_tests}")
print(f"Total points: {total_score}")
print(f"Average score: {average_score:.2f}")

# Determine letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B" 
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Letter grade: {letter_grade}")
print()

# MATHEMATICAL PATTERNS WITH LOOPS
print("=== MATHEMATICAL PATTERNS ===")
print()

# Example 1: Powers of 2
print("Example 1: Powers of 2")
print("Power | Result")
print("------|-------")

for power in range(8):          # 0 to 7
    result = 2 ** power
    print(f"  2^{power}  |  {result}")

print()

# Example 2: Fibonacci sequence (first 10 numbers)
print("Example 2: Fibonacci sequence")
print("The Fibonacci sequence: each number is the sum of the two before it")

# Initialize first two numbers
a, b = 0, 1
print(f"1: {a}")
print(f"2: {b}")

# Generate next 8 numbers
for i in range(3, 11):          # Numbers 3 through 10
    next_num = a + b            # Next Fibonacci number
    print(f"{i}: {next_num}")
    a, b = b, next_num          # Update for next iteration

print()

# Example 3: Factorial calculation
print("Example 3: Calculate factorial")
number = int(input("Enter a number to calculate its factorial: "))

factorial = 1                   # Initialize factorial
calculation_steps = f"{number}! = "

for i in range(1, number + 1):  # 1 to number inclusive
    factorial = factorial * i
    if i == 1:
        calculation_steps += str(i)
    else:
        calculation_steps += f" × {i}"

calculation_steps += f" = {factorial}"

print(f"\nFactorial calculation:")
print(calculation_steps)
print(f"Result: {number}! = {factorial}")
print()

# PATTERN PRINTING
print("=== PATTERN PRINTING ===")
print()

# Example 1: Number triangle
print("Example 1: Number triangle")
for row in range(1, 6):         # Rows 1 to 5
    for number in range(1, row + 1):  # Numbers 1 to row
        print(number, end=" ")
    print()                     # New line after each row

print()

# Example 2: Star pyramid
print("Example 2: Star pyramid")
for row in range(1, 6):         # 5 rows
    spaces = " " * (5 - row)    # Decreasing spaces
    stars = "*" * row           # Increasing stars
    print(spaces + stars)

print()

print("=== LOOP EFFICIENCY DEMONSTRATION ===")
print()

# Show how loops save code
print("Without loops, to print numbers 1-5, you'd need:")
print('print("1")')
print('print("2")')
print('print("3")')
print('print("4")')
print('print("5")')
print()

print("With a loop, you just need:")
print('for i in range(1, 6):')
print('    print(i)')
print()

print("The loop version:")
for i in range(1, 6):
    print(i)

print()

print("=== SUMMARY ===")
print()
print("Key Points about FOR loops:")
print("1. Use 'for variable in sequence:' syntax")
print("2. range() is the most common sequence")
print("3. range(n) goes from 0 to n-1")
print("4. range(start, stop) goes from start to stop-1") 
print("5. range(start, stop, step) allows custom increments")
print("6. Loop variables automatically take each value in sequence")
print("7. Use accumulators to build up totals or counts")
print("8. Indentation defines what's inside the loop")

"""
KEY TAKEAWAYS:
==============
1. for loops repeat code for each item in a sequence
2. range() generates sequences of numbers for counting
3. Loop variables automatically take each value in the sequence
4. Accumulator pattern: initialize, then update in loop
5. range(start, stop, step) gives flexible counting options
6. Proper indentation is crucial for loop structure

COMMON MISTAKES:
================
- Confusing range() behavior (range(5) is 0-4, not 1-5)
- Forgetting that range() excludes the stop value
- Not understanding that loop variables change automatically
- Modifying the loop variable inside the loop (usually wrong)
- Incorrect indentation causing code to be outside the loop

NEXT STEP:
Go to 02-for-loops-with-sequences.py to learn about iterating over lists and strings!
"""