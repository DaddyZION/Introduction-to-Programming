"""
Assignment 2 - Example 1: Basic IF Statements
============================================

This program introduces the fundamental concept of CONDITIONAL EXECUTION.
An if statement allows your program to execute certain code ONLY when
a specific condition is true.

Key Concepts Demonstrated:
- Basic if statement syntax
- Condition evaluation (True/False)
- Comparison operators (==, !=, <, >, <=, >=)
- Code blocks and indentation
- Boolean expressions
"""

print("=== UNDERSTANDING IF STATEMENTS ===")
print()

# WHAT IS AN IF STATEMENT?
# An if statement tests a condition and executes code only if that condition is True.
# Think of it like asking a yes/no question:
# "IF the answer is yes, then do something"

print("If statements let programs make decisions!")
print("Let's see how they work...")
print()

# BASIC IF STATEMENT SYNTAX
print("=== BASIC IF STATEMENT EXAMPLES ===")
print()

# Example 1: Simple number comparison
age = 18
print(f"Your age is: {age}")

if age >= 18:
    print("✅ You are an adult!")
    print("   You can vote and drive.")

print("This line always executes (not inside the if block)")
print()

# Example 2: String comparison
student_status = "enrolled"
print(f"Student status: {student_status}")

if student_status == "enrolled":
    print("✅ Welcome to class!")
    print("   You can access course materials.")

print()

# Example 3: Boolean variable
has_passed = True
print(f"Has passed the course: {has_passed}")

if has_passed:  # Same as: if has_passed == True:
    print("🎉 Congratulations on passing!")
    print("   You can register for the next level.")

print()

# COMPARISON OPERATORS - The foundation of conditions
print("=== COMPARISON OPERATORS ===")
print()

score = 85
passing_grade = 60

print(f"Your score: {score}")
print(f"Passing grade: {passing_grade}")
print()

# Equal to (==)
if score == 100:
    print("Perfect score!")

# Not equal to (!=)  
if score != 0:
    print("You attempted the exam")

# Greater than (>)
if score > passing_grade:
    print("✅ You passed the exam!")

# Greater than or equal to (>=)
if score >= 80:
    print("🌟 Excellent work! You got a distinction.")

# Less than (<)
if score < 100:
    print("There's room for improvement")

# Less than or equal to (<=)
if score <= 90:
    print("Good effort!")

print()

# INTERACTIVE EXAMPLE
print("=== INTERACTIVE EXAMPLE ===")
print()

print("Let's check your exam performance!")
user_score = int(input("Enter your exam score (0-100): "))

print(f"\nAnalyzing your score of {user_score}...")

if user_score >= 90:
    print("🏆 Outstanding! You achieved excellence.")

if user_score >= 80:
    print("⭐ Great job! You earned a distinction.")

if user_score >= 70:
    print("👍 Well done! You performed well.")

if user_score >= 60:
    print("✅ Good! You passed the exam.")

if user_score < 60:
    print("❌ Unfortunately, you didn't pass this time.")

if user_score == 100:
    print("🎯 Perfect score! Amazing achievement!")

print()

# MULTIPLE CONDITIONS BEING TESTED
print("=== TESTING MULTIPLE CONDITIONS ===")
print()

temperature = 25
humidity = 80

print(f"Current conditions:")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print()

print("Weather analysis:")

if temperature > 30:
    print("🌡️ It's hot outside!")

if temperature < 0:
    print("🧊 It's freezing!")

if humidity > 70:
    print("💧 It's quite humid today")

if temperature >= 20:
    print("🌤️ Pleasant temperature for outdoor activities")

if temperature == 25:
    print("🎯 Perfect room temperature!")

print()

# WORKING WITH STRING CONDITIONS
print("=== STRING CONDITION EXAMPLES ===")
print()

username = input("Enter your username: ").strip().lower()

print(f"Checking username: '{username}'")

if username == "admin":
    print("🔑 Administrator access granted")
    print("   You have full system privileges")

if username == "guest":
    print("👤 Guest access granted")
    print("   You have limited access")

if len(username) < 3:
    print("⚠️ Username is too short")

if len(username) > 20:
    print("⚠️ Username is too long")

if username == "":
    print("❌ Username cannot be empty")

print()

# BOOLEAN VARIABLES IN CONDITIONS
print("=== BOOLEAN VARIABLES IN CONDITIONS ===")
print()

is_student = True
is_enrolled = True
has_paid_fees = False

print("Account status:")
print(f"Is student: {is_student}")
print(f"Is enrolled: {is_enrolled}")  
print(f"Has paid fees: {has_paid_fees}")
print()

print("Access checks:")

if is_student:
    print("✅ Student status confirmed")

if is_enrolled:
    print("✅ Enrollment is active")

if has_paid_fees:
    print("✅ Fees are up to date")

if not has_paid_fees:  # 'not' reverses the boolean value
    print("⚠️ Outstanding fees need payment")

print()

# PRACTICAL EXAMPLE: GRADE CALCULATOR
print("=== PRACTICAL EXAMPLE: GRADE CLASSIFIER ===")
print()

print("Grade Classification System:")
print("90-100: A+ (Exceptional)")
print("80-89:  A  (Excellent)")  
print("70-79:  B  (Good)")
print("60-69:  C  (Satisfactory)")
print("Below 60: F (Fail)")
print()

grade = int(input("Enter your grade (0-100): "))

print(f"\nGrade analysis for {grade}%:")

if grade >= 90:
    print("🏆 Grade: A+ (Exceptional performance)")

if grade >= 80 and grade < 90:  # We'll learn about 'and' in detail later
    print("⭐ Grade: A (Excellent work)")

if grade >= 70 and grade < 80:
    print("👍 Grade: B (Good effort)")

if grade >= 60 and grade < 70:
    print("✅ Grade: C (Satisfactory)")

if grade < 60:
    print("❌ Grade: F (Needs improvement)")

# Additional feedback
if grade > 100:
    print("⚠️ Grade cannot be over 100%")

if grade < 0:
    print("⚠️ Grade cannot be negative")

if grade == 100:
    print("🎯 Perfect score achieved!")

print()

# UNDERSTANDING INDENTATION
print("=== UNDERSTANDING CODE BLOCKS AND INDENTATION ===")
print()

print("Python uses indentation to group code together.")
print("All lines at the same indentation level belong to the same block.")
print()

condition = True

if condition:
    print("This line is INSIDE the if block (indented)")
    print("This line is also INSIDE the if block (same indentation)")
    print("All these lines execute only if condition is True")

print("This line is OUTSIDE the if block (not indented)")
print("This line always executes regardless of the condition")
print()

# SHOWING THE IMPORTANCE OF CONDITIONS
print("=== WHY CONDITIONS MATTER ===")
print()

balance = 250.50
withdrawal_amount = float(input("Enter withdrawal amount: £"))

print(f"Account balance: £{balance:.2f}")
print(f"Withdrawal request: £{withdrawal_amount:.2f}")
print()

if withdrawal_amount <= balance:
    print("✅ Transaction approved!")
    print(f"   Dispensing £{withdrawal_amount:.2f}")
    remaining_balance = balance - withdrawal_amount
    print(f"   Remaining balance: £{remaining_balance:.2f}")

if withdrawal_amount > balance:
    print("❌ Insufficient funds!")
    print("   Transaction declined")
    print(f"   Available balance: £{balance:.2f}")

print("Thank you for using our ATM service")
print()

print("=== SUMMARY ===")
print()
print("Key Points about IF statements:")
print("1. Use 'if' followed by a condition and a colon (:)")
print("2. Code inside the if block must be indented")
print("3. The condition must evaluate to True or False")
print("4. Comparison operators: ==, !=, <, >, <=, >=")
print("5. If condition is False, the code block is skipped")
print("6. Multiple if statements can be used independently")

"""
KEY TAKEAWAYS:
==============
1. if statements allow conditional execution of code
2. Conditions must evaluate to True or False (boolean values)
3. Use comparison operators to create conditions
4. Indentation is crucial - it defines which code belongs to the if block
5. Multiple if statements can test different conditions independently
6. Conditions can test numbers, strings, or boolean variables

COMMON MISTAKES:
================
- Forgetting the colon (:) after the if condition
- Incorrect indentation of code blocks
- Using assignment (=) instead of comparison (==)
- Not understanding that multiple if statements are independent

NEXT STEP:
Go to 02-if-else-statements.py to learn about two-way decisions!
"""