"""
Assignment 2 - Example 2: IF-ELSE Statements
==========================================

This program demonstrates IF-ELSE statements, which provide two-way decision making.
While a simple IF statement either executes code or skips it, IF-ELSE ensures
that one of two code blocks will always execute.

Key Concepts Demonstrated:
- if-else statement syntax
- Two-way decision making
- Mutually exclusive code paths
- When to use if-else vs multiple if statements
- Practical decision-making scenarios
"""

print("=== UNDERSTANDING IF-ELSE STATEMENTS ===")
print()

# WHAT IS AN IF-ELSE STATEMENT?
# An if-else statement creates two possible paths:
# - IF the condition is True, execute the first block
# - ELSE (if condition is False), execute the second block
# 
# Exactly ONE of the two blocks will always execute - never both, never neither.

print("If-else statements create two-way decisions!")
print("One path for True, one path for False.")
print()

# BASIC IF-ELSE SYNTAX
print("=== BASIC IF-ELSE EXAMPLES ===")
print()

# Example 1: Age verification
age = int(input("Enter your age: "))

print(f"Your age: {age}")

if age >= 18:
    print("✅ You are an adult")
    print("   You can vote, drive, and make legal decisions")
else:
    print("👶 You are a minor")
    print("   You have certain legal protections and restrictions")

print("Age verification complete.")
print()

# Example 2: Pass/Fail determination
print("=== PASS/FAIL EXAMPLE ===")
print()

exam_score = int(input("Enter your exam score (0-100): "))

print(f"Your score: {exam_score}")

if exam_score >= 60:
    print("🎉 CONGRATULATIONS! You PASSED!")
    print("   Well done on your achievement.")
    print("   You can proceed to the next level.")
else:
    print("❌ Unfortunately, you did not pass this time.")
    print("   Don't give up! You can retake the exam.")
    print("   Consider additional study and practice.")

print("Grade processing complete.")
print()

# Example 3: Even or Odd number
print("=== EVEN OR ODD NUMBER CHECKER ===")
print()

number = int(input("Enter any integer: "))

print(f"Analyzing number: {number}")

# The modulus operator (%) gives the remainder after division
# If a number divided by 2 has remainder 0, it's even
if number % 2 == 0:
    print(f"✅ {number} is an EVEN number")
    print("   Even numbers are divisible by 2")
else:
    print(f"✅ {number} is an ODD number") 
    print("   Odd numbers have remainder 1 when divided by 2")

print(f"Proof: {number} ÷ 2 = {number // 2} remainder {number % 2}")
print()

# COMPARISON: IF-ELSE vs MULTIPLE IF STATEMENTS
print("=== IF-ELSE vs MULTIPLE IF STATEMENTS ===")
print()

temperature = int(input("Enter temperature in Celsius: "))

print(f"Temperature: {temperature}°C")
print()

# Using IF-ELSE (exactly one message will be printed)
print("Using IF-ELSE approach:")
if temperature >= 25:
    print("🌡️ It's warm today!")
else:
    print("🧊 It's cool today!")

print()

# Using multiple IF statements (both might print, or neither)
print("Using multiple IF statements:")
if temperature >= 25:
    print("🌡️ It's warm today!")

if temperature < 25:
    print("🧊 It's cool today!")

print("Notice: Both approaches give the same result here,")
print("but IF-ELSE guarantees exactly one path executes.")
print()

# STRING COMPARISON EXAMPLE
print("=== STRING COMPARISON WITH IF-ELSE ===")
print()

user_input = input("Enter 'yes' or 'no': ").strip().lower()

print(f"You entered: '{user_input}'")

if user_input == "yes":
    print("✅ You confirmed YES")
    print("   Proceeding with the action...")
    print("   Action completed successfully!")
else:
    print("❌ You did not confirm (or entered something other than 'yes')")
    print("   Action cancelled for safety.")
    print("   No changes were made.")

print()

# BOOLEAN VARIABLE EXAMPLE
print("=== BOOLEAN VARIABLE WITH IF-ELSE ===")
print()

is_raining = input("Is it raining? (yes/no): ").strip().lower() == "yes"

print(f"Raining status: {is_raining}")

if is_raining:
    print("☔ It's raining!")
    print("   Take an umbrella")
    print("   Wear waterproof clothing")
    print("   Drive carefully")
else:
    print("☀️ It's not raining!")
    print("   No umbrella needed")
    print("   Perfect weather for outdoor activities")
    print("   Enjoy the sunshine!")

print()

# PRACTICAL EXAMPLE: LOGIN SYSTEM
print("=== PRACTICAL EXAMPLE: SIMPLE LOGIN SYSTEM ===")
print()

# Simulate a simple login system
correct_password = "python123"
entered_password = input("Enter password: ")

print("Verifying credentials...")

if entered_password == correct_password:
    print("🔓 ACCESS GRANTED")
    print("   Welcome to the system!")
    print("   Loading user dashboard...")
    print("   You have 3 new messages")
    print("   System status: All systems operational")
else:
    print("🔒 ACCESS DENIED")
    print("   Incorrect password")
    print("   Please check your credentials")
    print("   Contact administrator if you forgot your password")
    print("   Security log: Failed login attempt recorded")

print("Login attempt processed.")
print()

# FINANCIAL DECISION EXAMPLE
print("=== FINANCIAL DECISION EXAMPLE ===")
print()

account_balance = 500.00
purchase_amount = float(input("Enter purchase amount: £"))

print(f"Account balance: £{account_balance:.2f}")
print(f"Purchase amount: £{purchase_amount:.2f}")
print()

print("Processing transaction...")

if purchase_amount <= account_balance:
    print("✅ TRANSACTION APPROVED")
    new_balance = account_balance - purchase_amount
    print(f"   Purchase amount: £{purchase_amount:.2f}")
    print(f"   Remaining balance: £{new_balance:.2f}")
    print("   Thank you for your purchase!")
    print("   Receipt sent to your email.")
else:
    print("❌ TRANSACTION DECLINED")
    insufficient_amount = purchase_amount - account_balance
    print(f"   Insufficient funds")
    print(f"   You need £{insufficient_amount:.2f} more")
    print("   Consider adding funds to your account")
    print("   Or choose a smaller purchase amount")

print("Transaction processing complete.")
print()

# GRADE CLASSIFICATION WITH DETAILED FEEDBACK
print("=== ADVANCED EXAMPLE: DETAILED GRADE FEEDBACK ===")
print()

final_grade = int(input("Enter your final course grade (0-100): "))

print(f"Final Grade: {final_grade}%")
print()

print("Generating detailed feedback report...")
print("-" * 40)

if final_grade >= 60:
    print("🎉 COURSE STATUS: PASSED")
    print()
    print("✅ Congratulations on completing the course!")
    print("✅ You have met the minimum requirements")
    print("✅ Certificate will be issued")
    print("✅ You can enroll in advanced courses")
    print()
    
    # Additional feedback for passing students
    if final_grade >= 90:
        print("🏆 ACHIEVEMENT LEVEL: DISTINCTION")
        print("   Outstanding performance!")
        print("   You're in the top 10% of students")
    else:
        print("👍 ACHIEVEMENT LEVEL: STANDARD PASS")
        print("   Solid performance!")
        print("   Continue building on this foundation")
        
else:
    print("❌ COURSE STATUS: NOT PASSED")
    print()
    print("📚 Don't be discouraged - learning is a journey!")
    print("📚 You can retake the course next semester")
    print("📚 Consider these improvement strategies:")
    print("   • Attend all lectures and tutorials")
    print("   • Form study groups with classmates") 
    print("   • Use office hours to ask questions")
    print("   • Practice more coding exercises")
    print()
    
    # Specific feedback based on how close they were
    points_needed = 60 - final_grade
    print(f"💡 You needed {points_needed} more points to pass")
    
    if points_needed <= 10:
        print("   You were very close! A little more effort will get you there.")
    else:
        print("   Focus on understanding fundamental concepts first.")

print("-" * 40)
print("End of feedback report")
print()

# DEMONSTRATING THE POWER OF IF-ELSE
print("=== WHY IF-ELSE IS POWERFUL ===")
print()

print("Key advantages of if-else statements:")
print("1. 🎯 Guarantees exactly one path executes")
print("2. 🔄 Handles all possible cases (True and False)")
print("3. 🧹 Makes code cleaner and more efficient")
print("4. 🛡️ Provides safety through complete coverage")
print("5. 💭 Matches how humans make binary decisions")
print()

# Final interactive example
user_choice = input("Do you understand if-else statements? (yes/no): ").strip().lower()

if user_choice == "yes":
    print("🎉 Excellent! You're ready for the next topic.")
    print("   Next, you'll learn about elif statements")
    print("   for handling multiple conditions.")
else:
    print("📖 That's okay! Learning takes time.")
    print("   Review the examples above")
    print("   Try running the code and changing values")
    print("   Practice makes perfect!")

print()
print("=== SUMMARY ===")
print()
print("IF-ELSE Statement Key Points:")
print("1. Provides exactly two possible execution paths")
print("2. One block executes if condition is True")
print("3. Other block executes if condition is False")
print("4. Guarantees one path will always execute")
print("5. Use when you need to handle both True and False cases")
print("6. More efficient than multiple independent if statements")
print("7. Makes program logic clearer and more predictable")

"""
KEY TAKEAWAYS:
==============
1. if-else provides two-way decision making
2. Exactly one of the two code blocks will always execute
3. if block executes when condition is True
4. else block executes when condition is False
5. More predictable than multiple independent if statements
6. Perfect for binary decisions (yes/no, pass/fail, etc.)

WHEN TO USE IF-ELSE:
====================
- Binary decisions (two possible outcomes)
- When you need to handle both True and False cases
- When you want to guarantee one path executes
- Validating user input (valid/invalid)
- Authentication (success/failure)

COMMON MISTAKES:
================
- Using multiple if statements when if-else would be better
- Forgetting that exactly one path will execute
- Not handling the 'else' case properly
- Complex conditions that should use elif instead

NEXT STEP:
Go to 03-elif-statements.py to learn about multiple conditions!
"""