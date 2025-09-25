"""
Assignment 3 - Example 3: WHILE Loops
====================================

This program demonstrates WHILE loops, which repeat code as long as
a condition remains True. Unlike for loops that iterate over sequences,
while loops are condition-based and continue until something changes.

Key Concepts Demonstrated:
- Basic while loop syntax and logic
- Loop conditions and how they change
- Avoiding infinite loops
- User input validation with while loops
- Sentinel-controlled loops
- Counter-controlled loops with while
"""
# %% 
print("=== UNDERSTANDING WHILE LOOPS ===")
print()
# %% 

# WHAT IS A WHILE LOOP?
# A while loop repeats code as long as a condition is True.
# It checks the condition before each iteration.
# If the condition is False initially, the loop never executes.

print("While loops repeat code based on conditions!")
print("They keep going as long as the condition is True.")
print("You must change something inside the loop to make it stop.")
print()

# BASIC WHILE LOOP SYNTAX
print("=== BASIC WHILE LOOP EXAMPLES ===")
print()

# Example 1: Simple counting with while
print("Example 1: Count from 1 to 5 using while loop")

count = 1                       # Initialize the counter
print(f"Starting count: {count}")

while count <= 5:               # Condition: continue while count is 5 or less
    print(f"Count is: {count}")
    count = count + 1           # INCREMENT - very important!
    print(f"  Incremented to: {count}")

print(f"Loop finished. Final count: {count}")
print("Notice: The loop stopped when count became 6 (condition became False)")
print()

# Example 2: Countdown
print("Example 2: Countdown using while loop")

countdown = 10
print(f"Starting countdown from {countdown}")

while countdown > 0:            # Continue while countdown is greater than 0
    print(f"Countdown: {countdown}")
    countdown = countdown - 1   # DECREMENT each time

print("🚀 Blast off!")
print(f"Final countdown value: {countdown}")
print()

# COMPARISON: WHILE vs FOR LOOP
print("=== WHILE vs FOR LOOP COMPARISON ===")
print()

# Same task done both ways
print("Task: Print numbers 1 to 3")

print("\nUsing FOR loop:")
for i in range(1, 4):
    print(f"FOR: {i}")

print("\nUsing WHILE loop:")
i = 1                           # Initialize counter
while i < 4:                    # Continue condition
    print(f"WHILE: {i}")
    i = i + 1                   # Increment counter

print("\nBoth produce the same result!")
print("FOR loops are better when you know how many times to repeat")
print("WHILE loops are better when you repeat based on a condition")
print()

# USER INPUT VALIDATION WITH WHILE LOOPS
print("=== USER INPUT VALIDATION ===")
print()

# Example 1: Keep asking until valid input
print("Example 1: Get a number between 1 and 10")

number = 0                      # Initialize with invalid value
while number < 1 or number > 10:
    number = int(input("Enter a number between 1 and 10: "))
    
    if number < 1 or number > 10:
        print("❌ Invalid! Please try again.")
    else:
        print("✅ Valid number entered!")

print(f"Thank you! You entered: {number}")
print()

# Example 2: Password validation
print("Example 2: Password validation")

correct_password = "python123"
attempts = 0
max_attempts = 3

print("Please enter the password (hint: python123)")

while attempts < max_attempts:
    password = input("Password: ")
    attempts = attempts + 1
    
    if password == correct_password:
        print("✅ Access granted!")
        break                   # Exit the loop immediately
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Incorrect password. {remaining} attempts remaining.")
        else:
            print("❌ Access denied. Too many failed attempts.")

print(f"Total attempts used: {attempts}")
print()

# SENTINEL-CONTROLLED LOOPS
print("=== SENTINEL-CONTROLLED LOOPS ===")
print()

# A sentinel is a special value that signals the end of input
print("Example: Calculate average of numbers (enter -1 to stop)")

total = 0
count = 0
number = 0                      # Initialize

print("Enter numbers to average (enter -1 to finish):")

while number != -1:             # Continue until sentinel value (-1) is entered
    number = float(input("Enter number: "))
    
    if number != -1:            # Don't include the sentinel in calculations
        total = total + number
        count = count + 1
        print(f"  Added {number}. Running total: {total}, Count: {count}")

if count > 0:                   # Avoid division by zero
    average = total / count
    print(f"\n=== RESULTS ===")
    print(f"Numbers entered: {count}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
else:
    print("No valid numbers were entered.")

print()

# GUESSING GAME EXAMPLE
print("=== PRACTICAL EXAMPLE: NUMBER GUESSING GAME ===")
print()

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)
guess = 0
attempts = 0
max_attempts = 7

print("🎯 Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.")
print()

while guess != secret_number and attempts < max_attempts:
    attempts = attempts + 1
    remaining = max_attempts - attempts + 1
    
    print(f"Attempt {attempts}/{max_attempts}")
    guess = int(input("Enter your guess: "))
    
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
    elif guess < secret_number:
        print(f"📈 Too low! You have {remaining} attempts left.")
    else:
        print(f"📉 Too high! You have {remaining} attempts left.")
    
    print()

if guess != secret_number:
    print(f"😞 Game over! The number was {secret_number}")

print()

# ACCUMULATOR PATTERNS WITH WHILE LOOPS
print("=== ACCUMULATOR PATTERNS WITH WHILE ===")
print()

# Example: Build a factorial
print("Factorial calculation using while loop")
number = int(input("Enter a number to calculate its factorial: "))

original_number = number
factorial = 1
calculation = f"{original_number}! = "

# Build the calculation string and compute factorial
if number == 0:
    factorial = 1
    calculation = "0! = 1 (by definition)"
else:
    first = True
    while number > 0:
        if not first:
            calculation += " × "
        calculation += str(number)
        
        factorial = factorial * number
        number = number - 1
        first = False

calculation += f" = {factorial}"

print(calculation)
print(f"Result: {original_number}! = {factorial}")
print()

# NESTED CONDITIONS IN WHILE LOOPS
print("=== MENU-DRIVEN PROGRAM WITH WHILE ===")
print()

print("📊 Simple Calculator")
choice = ""

while choice != "quit":
    print("\n=== CALCULATOR MENU ===")
    print("1. Add two numbers")
    print("2. Multiply two numbers")
    print("3. Calculate square")
    print("Type 'quit' to exit")
    
    choice = input("\nEnter your choice: ").lower().strip()
    
    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
        
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"Result: {num1} × {num2} = {result}")
        
    elif choice == "3":
        num = float(input("Enter number to square: "))
        result = num ** 2
        print(f"Result: {num}² = {result}")
        
    elif choice == "quit":
        print("👋 Thank you for using the calculator!")
        
    else:
        print("❌ Invalid choice. Please try again.")

print()

# WARNING: INFINITE LOOPS
print("=== AVOIDING INFINITE LOOPS ===")
print()

print("⚠️ IMPORTANT: Avoiding Infinite Loops")
print()
print("An infinite loop happens when the condition never becomes False.")
print("Here are examples of what NOT to do:")
print()

print("❌ WRONG - This would run forever:")
print("count = 1")
print("while count <= 5:")
print("    print(count)")
print("    # Missing: count = count + 1")
print()

print("❌ WRONG - Condition never changes:")
print("x = 10")
print("while x > 5:")
print("    print('This runs forever')")
print("    # Missing: something to change x")
print()

print("✅ CORRECT - Always update the condition variable:")
print("count = 1")
print("while count <= 5:")
print("    print(count)")
print("    count = count + 1  # This makes the loop eventually stop")
print()

# WHEN TO USE WHILE vs FOR
print("=== WHEN TO USE WHILE vs FOR ===")
print()

print("Use WHILE loops when:")
print("• You don't know how many iterations you need")
print("• You're waiting for user input or a condition to change")
print("• You're validating input")
print("• You have a condition-based stopping point")
print()

print("Use FOR loops when:")
print("• You know exactly how many times to repeat")
print("• You're iterating over a sequence (list, string, etc.)")
print("• You're counting in a specific range")
print("• You're processing each item in a collection")
print()

# INTERACTIVE EXAMPLE: BANK ACCOUNT
print("=== FINAL EXAMPLE: SIMPLE BANK ACCOUNT ===")
print()

balance = 100.00
transaction_count = 0

print(f"💰 Welcome to Simple Bank!")
print(f"Your starting balance: £{balance:.2f}")

while True:                     # Infinite loop - we'll break out of it
    print(f"\nCurrent balance: £{balance:.2f}")
    print("Options: deposit, withdraw, balance, exit")
    
    action = input("What would you like to do? ").lower().strip()
    transaction_count += 1
    
    if action == "deposit":
        amount = float(input("Enter deposit amount: £"))
        if amount > 0:
            balance += amount
            print(f"✅ Deposited £{amount:.2f}")
        else:
            print("❌ Invalid amount")
            
    elif action == "withdraw":
        amount = float(input("Enter withdrawal amount: £"))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"✅ Withdrew £{amount:.2f}")
        elif amount > balance:
            print("❌ Insufficient funds")
        else:
            print("❌ Invalid amount")
            
    elif action == "balance":
        print(f"💰 Your balance is £{balance:.2f}")
        
    elif action == "exit":
        print(f"👋 Thank you for banking with us!")
        print(f"Final balance: £{balance:.2f}")
        print(f"Total transactions: {transaction_count}")
        break                   # Exit the infinite loop
        
    else:
        print("❌ Invalid option. Please try again.")

print()

print("=== SUMMARY ===")
print()
print("Key Points about WHILE loops:")
print("1. Use 'while condition:' syntax")
print("2. Loop continues as long as condition is True")
print("3. Always update the condition variable inside the loop")
print("4. Perfect for input validation and condition-based repetition")
print("5. Can create infinite loops if condition never becomes False")
print("6. Use break to exit a loop early")
print("7. Great for menu-driven programs and games")

"""
KEY TAKEAWAYS:
==============
1. while loops repeat based on conditions, not fixed counts
2. Always modify the condition variable inside the loop
3. Perfect for input validation and unknown iteration counts
4. Can create infinite loops if not careful with conditions
5. Use break to exit early when needed
6. Great for menu systems, games, and user interaction

WHEN TO USE WHILE:
==================
- Input validation (keep asking until valid)
- Menu-driven programs
- Games with unknown duration
- Processing until a sentinel value
- Waiting for external conditions to change

COMMON MISTAKES:
================
- Forgetting to update the condition variable (infinite loop)
- Wrong condition logic (loop never starts or never stops)
- Not handling edge cases (like division by zero)
- Using while when for would be simpler

NEXT STEP:
Go to 04-loop-control.py to learn about break, continue, and loop management!
"""