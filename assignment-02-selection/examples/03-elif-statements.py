"""
Assignment 2 - Example 3: ELIF Statements
========================================

This program demonstrates ELIF (else if) statements, which allow you to test
multiple conditions in sequence. This is essential when you have more than
two possible outcomes to consider.

Key Concepts Demonstrated:
- elif statement syntax and logic
- Multiple condition testing
- Sequential condition evaluation
- Grade classification systems
- Menu-driven programs
- Complex decision trees
"""

print("=== UNDERSTANDING ELIF STATEMENTS ===")
print()

# WHAT IS ELIF?
# elif stands for "else if" and allows testing multiple conditions in sequence.
# Python tests conditions from top to bottom and executes the FIRST True condition it finds.
# If no conditions are True, the final else block executes (if present).

print("ELIF allows testing multiple conditions in order!")
print("Perfect for when you have more than 2 possible outcomes.")
print()

# BASIC ELIF SYNTAX DEMONSTRATION
print("=== BASIC ELIF EXAMPLES ===")
print()

# Example 1: Grade classification system
score = int(input("Enter your exam score (0-100): "))

print(f"Your score: {score}")
print("Determining your grade...")

if score >= 90:
    print("🏆 Grade: A+ (Outstanding!)")
    print("   Exceptional performance")
elif score >= 80:
    print("⭐ Grade: A (Excellent!)")
    print("   Very strong performance")  
elif score >= 70:
    print("👍 Grade: B (Good!)")
    print("   Solid understanding demonstrated")
elif score >= 60:
    print("✅ Grade: C (Satisfactory)")
    print("   Meets minimum requirements")
elif score >= 50:
    print("⚠️ Grade: D (Below expectations)")
    print("   Additional study recommended")
else:
    print("❌ Grade: F (Fail)")
    print("   Course retake required")

print("Grade classification complete.")
print()

# Example 2: Weather recommendations
print("=== WEATHER-BASED RECOMMENDATIONS ===")
print()

temperature = int(input("Enter current temperature (°C): "))

print(f"Temperature: {temperature}°C")
print("Weather analysis and recommendations:")

if temperature >= 35:
    print("🔥 EXTREME HEAT WARNING")
    print("   Stay indoors with air conditioning")
    print("   Drink lots of water")
    print("   Avoid outdoor activities")
elif temperature >= 25:
    print("☀️ Hot and sunny")
    print("   Great beach weather!")
    print("   Wear sunscreen and light clothing")
    print("   Stay hydrated")
elif temperature >= 15:
    print("🌤️ Pleasant and mild")
    print("   Perfect for outdoor activities")
    print("   Light jacket recommended for evening")
elif temperature >= 5:
    print("🧥 Cool weather")
    print("   Wear a warm jacket")
    print("   Good for brisk walks")
elif temperature >= -5:
    print("🥶 Cold weather")
    print("   Bundle up in warm clothes")
    print("   Hot drinks recommended")
else:
    print("🧊 EXTREME COLD WARNING")
    print("   Dangerous conditions - stay indoors")
    print("   Risk of frostbite")
    print("   Ensure heating is working")

print()

# Example 3: Age-based categories
print("=== AGE CATEGORY CLASSIFICATION ===")
print()

age = int(input("Enter your age: "))

print(f"Age: {age}")
print("Age category analysis:")

if age < 0:
    print("❌ Invalid age entered")
elif age < 2:
    print("👶 Infant")
    print("   Requires constant supervision")
    print("   Focus on basic needs and development")
elif age < 13:
    print("🧒 Child") 
    print("   Elementary school age")
    print("   Learning fundamental skills")
elif age < 20:
    print("👦 Teenager")
    print("   High school / early college age")
    print("   Developing independence")
elif age < 65:
    print("👨 Adult")
    print("   Working age")
    print("   Full legal responsibilities")
elif age < 100:
    print("👴 Senior")
    print("   Retirement age")
    print("   Eligible for senior discounts")
else:
    print("🎂 Centenarian!")
    print("   Congratulations on reaching 100+!")
    print("   That's an incredible achievement!")

print()

# COMPLEX ELIF EXAMPLE: STUDENT CLASSIFICATION
print("=== COMPREHENSIVE STUDENT CLASSIFICATION ===")
print()

print("Student Performance Analysis System")
print("Enter your course information:")

attendance = int(input("Attendance percentage (0-100): "))
assignment_avg = float(input("Assignment average (0-100): "))
exam_score = int(input("Final exam score (0-100): "))

# Calculate overall performance
overall = (attendance * 0.2) + (assignment_avg * 0.4) + (exam_score * 0.4)

print(f"\nPerformance Summary:")
print(f"Attendance: {attendance}%")
print(f"Assignment Average: {assignment_avg}%") 
print(f"Exam Score: {exam_score}%")
print(f"Overall Score: {overall:.1f}%")
print()

print("Classification and Recommendations:")

if overall >= 85 and attendance >= 90:
    print("🏆 EXCEPTIONAL STUDENT")
    print("   Outstanding performance in all areas")
    print("   Recommended for advanced programs")
    print("   Consider peer tutoring opportunities")
elif overall >= 75 and attendance >= 80:
    print("⭐ EXCELLENT STUDENT")
    print("   Strong performance across the board")
    print("   Continue current study habits")
    print("   Eligible for honors programs")
elif overall >= 65 and attendance >= 70:
    print("👍 GOOD STUDENT")
    print("   Solid performance with room for improvement")
    print("   Focus on weaker areas")
    print("   Consider study groups")
elif overall >= 50 and attendance >= 60:
    print("⚠️ SATISFACTORY STUDENT")
    print("   Meeting minimum requirements")
    print("   Significant improvement needed")
    print("   Attend all classes and seek help")
elif overall >= 40:
    print("🚨 AT-RISK STUDENT")
    print("   Immediate intervention required")
    print("   Meet with academic advisor")
    print("   Consider reducing course load")
else:
    print("❌ FAILING STUDENT")
    print("   Critical situation - immediate action needed")
    print("   Meet with counselor immediately")
    print("   Consider course withdrawal and retake")

print()

# ELIF WITH STRING CONDITIONS
print("=== MENU SELECTION SYSTEM ===")
print()

print("University Information System")
print("Select an option:")
print("A - View Academic Records")
print("B - Register for Courses") 
print("C - Check Financial Aid")
print("D - Campus Services")
print("E - Exit System")

choice = input("Enter your choice (A-E): ").strip().upper()

print(f"You selected: {choice}")
print()

if choice == "A":
    print("📚 ACADEMIC RECORDS")
    print("   Loading your transcript...")
    print("   GPA: 3.75")
    print("   Credits completed: 45")
    print("   Expected graduation: Spring 2026")
elif choice == "B":
    print("📝 COURSE REGISTRATION")
    print("   Available courses for next semester:")
    print("   COMP102 - Data Structures")
    print("   MATH201 - Calculus II")
    print("   ENGL150 - Technical Writing")
elif choice == "C":
    print("💰 FINANCIAL AID")
    print("   Current aid package:")
    print("   Pell Grant: $3,500")
    print("   Work Study: $2,000")
    print("   Outstanding balance: $1,250")
elif choice == "D":
    print("🏢 CAMPUS SERVICES")
    print("   Available services:")
    print("   Library hours: 8 AM - 10 PM")
    print("   Dining hall: Open until 9 PM")
    print("   Gym: 24/7 access with student ID")
elif choice == "E":
    print("👋 GOODBYE")
    print("   Thank you for using the system")
    print("   Have a great day!")
else:
    print("❌ INVALID CHOICE")
    print("   Please enter A, B, C, D, or E")
    print("   Try again with a valid option")

print()

# DEMONSTRATING CONDITION ORDER IMPORTANCE
print("=== IMPORTANCE OF CONDITION ORDER ===")
print()

number = int(input("Enter a number: "))

print(f"Testing number: {number}")
print()

print("Correct order (specific to general):")
if number == 0:
    print("The number is exactly zero")
elif number > 0:
    print("The number is positive")
else:
    print("The number is negative")

print()

print("What if we used the wrong order?")
print("(This is just for demonstration - we're not actually running it)")
print()
print("if number > -1000:")
print("    print('Number is greater than -1000')")
print("elif number > 0:")
print("    print('Number is positive')  # This would never execute!")
print("elif number == 0:")
print("    print('Number is zero')       # This would never execute!")
print()
print("The first condition would always be True for most numbers,")
print("so the more specific conditions would never be tested!")

print()

# PRACTICAL EXAMPLE: SHIPPING CALCULATOR
print("=== PRACTICAL EXAMPLE: SHIPPING COST CALCULATOR ===")
print()

weight = float(input("Enter package weight (kg): "))
distance = int(input("Enter shipping distance (km): "))

print(f"Package weight: {weight} kg")
print(f"Shipping distance: {distance} km")
print()

print("Calculating shipping cost...")

# Base cost calculation
if weight <= 1:
    base_cost = 5.00
elif weight <= 5:
    base_cost = 10.00
elif weight <= 10:
    base_cost = 20.00
elif weight <= 25:
    base_cost = 35.00
else:
    base_cost = 50.00

# Distance multiplier
if distance <= 50:
    multiplier = 1.0
    zone = "Local"
elif distance <= 200:
    multiplier = 1.5
    zone = "Regional"
elif distance <= 500:
    multiplier = 2.0
    zone = "National"
else:
    multiplier = 3.0
    zone = "International"

total_cost = base_cost * multiplier

print("SHIPPING COST BREAKDOWN:")
print(f"Weight category base cost: £{base_cost:.2f}")
print(f"Distance zone: {zone} (×{multiplier})")
print(f"TOTAL SHIPPING COST: £{total_cost:.2f}")

print()

print("=== SUMMARY ===")
print()
print("ELIF Statement Key Points:")
print("1. Use elif to test multiple conditions in sequence")
print("2. Python tests conditions from top to bottom")
print("3. First True condition executes - others are skipped")
print("4. Always put most specific conditions first")
print("5. Use final else to handle 'everything else' cases")
print("6. Perfect for classification systems and menus")
print("7. More efficient than multiple independent if statements")

"""
KEY TAKEAWAYS:
==============
1. elif allows testing multiple mutually exclusive conditions
2. Conditions are tested in order from top to bottom
3. Only the FIRST True condition executes
4. Order matters - put specific conditions before general ones
5. Use final else to catch all remaining cases
6. Perfect for classification, grading, menus, and categories

WHEN TO USE ELIF:
=================
- Grade classification systems
- Age/category groupings  
- Menu selection systems
- Multi-tier pricing
- Weather condition responses
- Any time you have 3+ mutually exclusive outcomes

COMMON MISTAKES:
================
- Wrong order of conditions (general before specific)
- Using multiple if statements instead of elif chain
- Forgetting the final else case
- Overlapping conditions that could cause confusion

NEXT STEP:
Go to 04-boolean-logic.py to learn about combining conditions!
"""