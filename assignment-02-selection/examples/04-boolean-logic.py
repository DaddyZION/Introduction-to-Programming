"""
Assignment 2 - Example 4: Boolean Logic and Logical Operators
============================================================

This program demonstrates how to combine multiple conditions using logical
operators. Boolean logic is essential for making complex decisions where
multiple factors need to be considered simultaneously.

Key Concepts Demonstrated:
- Logical operators (and, or, not)
- Complex boolean expressions
- Truth tables and logical evaluation
- Combining multiple conditions
- Short-circuit evaluation
- Practical decision-making scenarios
"""

print("=== BOOLEAN LOGIC AND LOGICAL OPERATORS ===")
print()

print("Boolean logic allows us to combine multiple conditions")
print("to make more sophisticated decisions in our programs.")
print()

# LOGICAL OPERATORS OVERVIEW
print("=== THE THREE LOGICAL OPERATORS ===")
print()

print("Python has three main logical operators:")
print("• AND - Both conditions must be True")
print("• OR  - At least one condition must be True") 
print("• NOT - Flips True to False, False to True")
print()

# THE AND OPERATOR
print("=== THE 'AND' OPERATOR ===")
print()

print("The 'and' operator requires BOTH conditions to be True")
print("If either condition is False, the entire expression is False")
print()

# Example 1: Weather conditions
print("Example 1: Perfect picnic weather")
temperature = 75
weather = "sunny"

print(f"Current conditions: {temperature}°F, {weather}")
print()

# Individual condition checks
temp_good = temperature >= 70 and temperature <= 85
weather_good = weather == "sunny"

print(f"Temperature good (70-85°F): {temperature} -> {temp_good}")
print(f"Weather good (sunny): '{weather}' -> {weather_good}")

# Combined condition
perfect_weather = temp_good and weather_good
print(f"Perfect picnic weather: {temp_good} AND {weather_good} = {perfect_weather}")

if perfect_weather:
    print("✅ Great day for a picnic!")
else:
    print("❌ Maybe stay inside today")

print()

# Example 2: Login validation
print("Example 2: User login validation")

username = "alice123"
password = "secure_password"
account_active = True

correct_username = username == "alice123"
correct_password = password == "secure_password"

print(f"Username correct: '{username}' -> {correct_username}")
print(f"Password correct: '[hidden]' -> {correct_password}")  
print(f"Account active: {account_active}")

# All conditions must be true for login
login_success = correct_username and correct_password and account_active

print(f"Login successful: {correct_username} AND {correct_password} AND {account_active} = {login_success}")

if login_success:
    print("✅ Welcome! Login successful")
else:
    print("❌ Login failed - check credentials")

print()

# THE OR OPERATOR
print("=== THE 'OR' OPERATOR ===")
print()

print("The 'or' operator requires AT LEAST ONE condition to be True")
print("Only when ALL conditions are False is the expression False")
print()

# Example 1: Weekend detection
print("Example 1: Is it the weekend?")

day = "Saturday"

is_saturday = day == "Saturday"
is_sunday = day == "Sunday"

print(f"Is Saturday: '{day}' -> {is_saturday}")
print(f"Is Sunday: '{day}' -> {is_sunday}")

is_weekend = is_saturday or is_sunday
print(f"Is weekend: {is_saturday} OR {is_sunday} = {is_weekend}")

if is_weekend:
    print("🎉 It's the weekend! Time to relax")
else:
    print("📚 It's a weekday - time for work/school")

print()

# Example 2: Payment method acceptance
print("Example 2: Payment method validation")

payment_method = "credit_card"

accepts_cash = payment_method == "cash"
accepts_credit = payment_method == "credit_card"
accepts_debit = payment_method == "debit_card"

print(f"Payment method: '{payment_method}'")
print(f"Cash: {accepts_cash}")
print(f"Credit card: {accepts_credit}")  
print(f"Debit card: {accepts_debit}")

payment_accepted = accepts_cash or accepts_credit or accepts_debit
print(f"Payment accepted: {accepts_cash} OR {accepts_credit} OR {accepts_debit} = {payment_accepted}")

if payment_accepted:
    print("✅ Payment method accepted")
else:
    print("❌ Payment method not supported")

print()

# THE NOT OPERATOR
print("=== THE 'NOT' OPERATOR ===")
print()

print("The 'not' operator flips the boolean value")
print("not True becomes False, not False becomes True")
print()

# Example 1: Access control
print("Example 1: Access control system")

is_banned = False
is_minor = False

print(f"User is banned: {is_banned}")
print(f"User is minor: {is_minor}")

# Use NOT to check if user is NOT banned and NOT a minor
can_access = not is_banned and not is_minor

print(f"Can access: NOT {is_banned} AND NOT {is_minor} = {can_access}")

if can_access:
    print("✅ Access granted")
else:
    print("❌ Access denied")

print()

# Example 2: Inventory check
print("Example 2: Inventory availability")

out_of_stock = False
discontinued = True

print(f"Out of stock: {out_of_stock}")
print(f"Discontinued: {discontinued}")

# Item is available if it's NOT out of stock AND NOT discontinued
item_available = not out_of_stock and not discontinued

print(f"Item available: NOT {out_of_stock} AND NOT {discontinued} = {item_available}")

if item_available:
    print("✅ Item is available for purchase")
else:
    print("❌ Item is not available")

print()

# COMBINING ALL LOGICAL OPERATORS
print("=== COMBINING LOGICAL OPERATORS ===")
print()

print("Real-world decisions often require combining AND, OR, and NOT")
print()

# Example: College admission system
print("Example: College admission criteria")

gpa = 3.7
sat_score = 1250
has_extracurriculars = True
has_recommendation = True
is_legacy = False

print(f"Student profile:")
print(f"  GPA: {gpa}")
print(f"  SAT Score: {sat_score}")
print(f"  Has extracurriculars: {has_extracurriculars}")
print(f"  Has recommendation: {has_recommendation}")
print(f"  Is legacy student: {is_legacy}")
print()

# Define admission criteria
print("Admission criteria analysis:")

# Academic requirements
meets_gpa = gpa >= 3.5
meets_sat = sat_score >= 1200
academic_qualified = meets_gpa and meets_sat

print(f"Meets GPA requirement (≥3.5): {gpa} -> {meets_gpa}")
print(f"Meets SAT requirement (≥1200): {sat_score} -> {meets_sat}")
print(f"Academically qualified: {meets_gpa} AND {meets_sat} = {academic_qualified}")

# Additional factors
has_strong_extras = has_extracurriculars and has_recommendation
legacy_boost = is_legacy

print(f"Strong extracurriculars: {has_extracurriculars} AND {has_recommendation} = {has_strong_extras}")
print(f"Legacy student boost: {legacy_boost}")

# Final admission decision
# Must be academically qualified AND (have strong extras OR be legacy)
admitted = academic_qualified and (has_strong_extras or legacy_boost)

print(f"\nAdmission decision:")
print(f"Academic qualified: {academic_qualified}")
print(f"Strong extras OR legacy: {has_strong_extras} OR {legacy_boost} = {has_strong_extras or legacy_boost}")
print(f"FINAL DECISION: {academic_qualified} AND ({has_strong_extras} OR {legacy_boost}) = {admitted}")

if admitted:
    print("🎓 CONGRATULATIONS! You've been admitted!")
else:
    print("📝 Unfortunately, you don't meet our admission criteria")

print()

# TRUTH TABLES
print("=== UNDERSTANDING TRUTH TABLES ===")
print()

print("Truth tables show all possible combinations of boolean values:")
print()

print("AND Truth Table:")
print("A     B     A and B")
print("True  True  True")
print("True  False False")
print("False True  False") 
print("False False False")
print()

print("OR Truth Table:")
print("A     B     A or B")
print("True  True  True")
print("True  False True")
print("False True  True")
print("False False False")
print()

print("NOT Truth Table:")
print("A     not A")
print("True  False")
print("False True")
print()

# SHORT-CIRCUIT EVALUATION
print("=== SHORT-CIRCUIT EVALUATION ===")
print()

print("Python uses 'short-circuit evaluation' for efficiency:")
print("• With AND: if first condition is False, don't check the second")
print("• With OR: if first condition is True, don't check the second")
print()

# Example of short-circuit with AND
print("Example: Safe division with AND")

number = 10
divisor = 0

print(f"Number: {number}")
print(f"Divisor: {divisor}")

# This is safe because if divisor == 0, the division never happens
if divisor != 0 and number / divisor > 5:
    print("Result is greater than 5")
else:
    print("Either divisor is zero or result is not greater than 5")

print("Note: Division by zero was safely avoided!")
print()

# Example of short-circuit with OR
print("Example: Default value with OR")

user_name = ""  # Empty string
default_name = "Guest"

print(f"User name: '{user_name}'")
print(f"Default name: '{default_name}'")

# If user_name is empty (falsy), use default_name
display_name = user_name or default_name
print(f"Display name: '{display_name}'")

print()

# PRACTICAL DECISION MAKING
print("=== PRACTICAL DECISION MAKING SCENARIOS ===")
print()

# Scenario 1: Shopping discount eligibility
print("Scenario 1: Shopping discount eligibility")

purchase_amount = 150
is_member = True
has_coupon = False
is_sale_day = True

print(f"Purchase amount: ${purchase_amount}")
print(f"Is member: {is_member}")
print(f"Has coupon: {has_coupon}")
print(f"Is sale day: {is_sale_day}")
print()

# Complex discount logic
print("Discount eligibility:")

# Regular discount: member AND (purchase over $100 OR has coupon)
regular_discount = is_member and (purchase_amount > 100 or has_coupon)

# Sale day bonus: sale day AND purchase over $50
sale_bonus = is_sale_day and purchase_amount > 50

# Gets discount if either condition is met
gets_discount = regular_discount or sale_bonus

print(f"Regular discount qualified: {is_member} AND ({purchase_amount > 100} OR {has_coupon}) = {regular_discount}")
print(f"Sale day bonus qualified: {is_sale_day} AND {purchase_amount > 50} = {sale_bonus}")
print(f"Gets discount: {regular_discount} OR {sale_bonus} = {gets_discount}")

if gets_discount:
    print("🎉 You qualify for a discount!")
else:
    print("💰 No discount available")

print()

# Scenario 2: Event attendance validation
print("Scenario 2: Event attendance validation")

age = 25
has_ticket = True
is_vip = False
event_full = False

print(f"Age: {age}")
print(f"Has ticket: {has_ticket}")
print(f"Is VIP: {is_vip}")
print(f"Event full: {event_full}")
print()

# Attendance logic
print("Attendance validation:")

# Must be adult (18+) AND have ticket
basic_requirements = age >= 18 and has_ticket

# Can attend if: (basic requirements AND event not full) OR is VIP
can_attend = (basic_requirements and not event_full) or is_vip

print(f"Basic requirements: {age >= 18} AND {has_ticket} = {basic_requirements}")
print(f"Event not full: NOT {event_full} = {not event_full}")
print(f"Can attend: ({basic_requirements} AND {not event_full}) OR {is_vip} = {can_attend}")

if can_attend:
    print("🎫 Welcome to the event!")
    if is_vip:
        print("👑 VIP access granted!")
else:
    print("🚫 Cannot attend event")

print()

# COMPLEX NESTED CONDITIONS
print("=== COMPLEX NESTED CONDITIONS ===")
print()

print("Sometimes we need multiple levels of decision making:")

# Example: Job application screening
print("Example: Automated job application screening")

years_experience = 3
has_degree = True
degree_relevant = True
salary_expectation = 75000
max_budget = 80000
has_references = True

print(f"Candidate profile:")
print(f"  Years experience: {years_experience}")
print(f"  Has degree: {has_degree}")
print(f"  Degree relevant: {degree_relevant}")
print(f"  Salary expectation: ${salary_expectation:,}")
print(f"  Company budget: ${max_budget:,}")
print(f"  Has references: {has_references}")
print()

# Multi-level screening
print("Screening process:")

# Education check
education_ok = has_degree and degree_relevant
print(f"Education requirement: {has_degree} AND {degree_relevant} = {education_ok}")

# Experience check  
experience_ok = years_experience >= 2
print(f"Experience requirement: {years_experience} ≥ 2 = {experience_ok}")

# Salary feasibility
salary_feasible = salary_expectation <= max_budget
print(f"Salary feasible: ${salary_expectation:,} ≤ ${max_budget:,} = {salary_feasible}")

# Overall qualification
# Must have (education OR experience) AND salary feasible AND references
qualified = (education_ok or experience_ok) and salary_feasible and has_references

print(f"\nFinal assessment:")
print(f"Education OR Experience: {education_ok} OR {experience_ok} = {education_ok or experience_ok}")
print(f"Qualified: ({education_ok or experience_ok}) AND {salary_feasible} AND {has_references} = {qualified}")

if qualified:
    print("✅ CANDIDATE APPROVED - Schedule interview!")
else:
    print("❌ Candidate does not meet requirements")

print()

print("=== SUMMARY ===")
print()
print("Boolean Logic Key Points:")
print("1. AND requires ALL conditions to be True")
print("2. OR requires AT LEAST ONE condition to be True")
print("3. NOT flips the boolean value")
print("4. Use parentheses to control evaluation order")
print("5. Short-circuit evaluation can prevent errors")
print("6. Complex decisions often combine multiple operators")
print("7. Truth tables help understand logical operations")

"""
KEY TAKEAWAYS:
==============
1. Logical operators combine simple conditions into complex decisions
2. AND: All conditions must be true
3. OR: At least one condition must be true  
4. NOT: Flips true/false values
5. Use parentheses to control order of operations
6. Short-circuit evaluation provides safety and efficiency
7. Real-world logic often requires combining multiple operators

COMMON PATTERNS:
================
• Validation: condition1 AND condition2 AND condition3
• Options: option1 OR option2 OR option3
• Exclusion: condition AND NOT excluded_condition
• Safety: safe_condition AND risky_operation
• Default: user_value OR default_value

BEST PRACTICES:
===============
• Use parentheses to make complex expressions clear
• Put safety checks first in AND expressions
• Consider short-circuit evaluation in your logic
• Break complex conditions into smaller, named variables
• Test edge cases where conditions might be unexpected

NEXT STEP:
Go to 05-nested-conditions.py to learn about conditions inside conditions!
"""