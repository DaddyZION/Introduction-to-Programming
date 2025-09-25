"""
Assignment 1 - Example 5: Complete Program
=========================================

This program brings together ALL the concepts from Assignment 1:
- Variables and data types
- Input and output operations  
- Arithmetic operations
- String operations
- Sequential execution

This is a comprehensive Student Grade Calculator that demonstrates
real-world application of sequence constructs.

Key Concepts Demonstrated:
- Combining all previous concepts in one program
- Sequential program flow
- Data collection and processing
- Calculations and formatting
- User-friendly output
- Real-world problem solving
"""

print("="*60)
print("STUDENT GRADE CALCULATOR".center(60))
print("Assignment 1 - Complete Sequence Constructs Example".center(60))
print("="*60)
print()

# PROGRAM INTRODUCTION
print("Welcome to the Student Grade Calculator!")
print("This program will:")
print("• Collect your student information")
print("• Record your assignment grades")
print("• Calculate your overall course grade")
print("• Generate a comprehensive grade report")
print()

# SECTION 1: STUDENT INFORMATION COLLECTION
print("-" * 40)
print("SECTION 1: STUDENT INFORMATION")
print("-" * 40)

# Collect basic student information using input validation
student_name = input("Enter your full name: ").strip().title()
student_id = input("Enter your student ID: ").strip().upper()
course_code = input("Enter course code (e.g., COMP101): ").strip().upper()
course_name = input("Enter course name: ").strip().title()

# Get current academic year
current_year = int(input("Enter current academic year (e.g., 2025): "))
print()

# SECTION 2: GRADE COLLECTION
print("-" * 40)
print("SECTION 2: ASSIGNMENT GRADES")
print("-" * 40)

print("Enter your grades for each assignment (out of 100):")
print("If you haven't completed an assignment yet, enter 0")
print()

# Collect grades for all 7 assignments (as per COMP101 structure)
assignment1 = float(input("Assignment 1 - Sequence Constructs (12%): "))
assignment2 = float(input("Assignment 2 - Selection Constructs (12%): "))
assignment3 = float(input("Assignment 3 - Iteration Constructs (13%): "))
assignment4 = float(input("Assignment 4 - Validation Control (13%): "))
assignment5 = float(input("Assignment 5 - Functions (16%): "))
assignment6 = float(input("Assignment 6 - 1D Arrays & Strings (16%): "))
assignment7 = float(input("Assignment 7 - 2D Arrays & Numerics (18%): "))
print()

# SECTION 3: CALCULATIONS
print("-" * 40)
print("SECTION 3: GRADE CALCULATIONS")
print("-" * 40)

# Define the weightings for each assignment (as per course specification)
weight1 = 0.12  # 12%
weight2 = 0.12  # 12% 
weight3 = 0.13  # 13%
weight4 = 0.13  # 13%
weight5 = 0.16  # 16%
weight6 = 0.16  # 16%
weight7 = 0.18  # 18%

# Calculate weighted scores for each assignment
weighted1 = assignment1 * weight1
weighted2 = assignment2 * weight2
weighted3 = assignment3 * weight3
weighted4 = assignment4 * weight4
weighted5 = assignment5 * weight5
weighted6 = assignment6 * weight6
weighted7 = assignment7 * weight7

# Calculate overall grade
overall_grade = weighted1 + weighted2 + weighted3 + weighted4 + weighted5 + weighted6 + weighted7

# Calculate additional statistics
completed_assignments = 0
total_raw_points = 0

# Count completed assignments and sum raw scores
assignments = [assignment1, assignment2, assignment3, assignment4, assignment5, assignment6, assignment7]
for grade in assignments:
    if grade > 0:
        completed_assignments += 1
        total_raw_points += grade

# Calculate average of completed assignments
if completed_assignments > 0:
    average_grade = total_raw_points / completed_assignments
else:
    average_grade = 0

# Determine letter grade
if overall_grade >= 90:
    letter_grade = "A+"
elif overall_grade >= 85:
    letter_grade = "A"
elif overall_grade >= 80:
    letter_grade = "A-"
elif overall_grade >= 75:
    letter_grade = "B+"
elif overall_grade >= 70:
    letter_grade = "B"
elif overall_grade >= 65:
    letter_grade = "B-"
elif overall_grade >= 60:
    letter_grade = "C+"
elif overall_grade >= 55:
    letter_grade = "C"
elif overall_grade >= 50:
    letter_grade = "C-"
elif overall_grade >= 40:
    letter_grade = "D"
else:
    letter_grade = "F"

# Determine pass/fail status
pass_status = "PASS" if overall_grade >= 40 else "FAIL"

print("Calculations completed successfully!")
print(f"Processed {completed_assignments} out of 7 assignments")
print()

# SECTION 4: DETAILED GRADE REPORT
print("="*60)
print("COMPREHENSIVE GRADE REPORT".center(60))
print("="*60)

# Student Information Section
print("\nSTUDENT INFORMATION:")
print("-" * 20)
print(f"Name: {student_name}")
print(f"Student ID: {student_id}")
print(f"Course: {course_code} - {course_name}")
print(f"Academic Year: {current_year}")

# Individual Assignment Breakdown
print("\nASSIGNMENT BREAKDOWN:")
print("-" * 20)
print(f"Assignment 1 (Sequences):     {assignment1:6.1f}/100 × 12% = {weighted1:5.2f} points")
print(f"Assignment 2 (Selection):     {assignment2:6.1f}/100 × 12% = {weighted2:5.2f} points")
print(f"Assignment 3 (Iteration):     {assignment3:6.1f}/100 × 13% = {weighted3:5.2f} points")
print(f"Assignment 4 (Validation):    {assignment4:6.1f}/100 × 13% = {weighted4:5.2f} points")
print(f"Assignment 5 (Functions):     {assignment5:6.1f}/100 × 16% = {weighted5:5.2f} points")
print(f"Assignment 6 (Arrays/Strings):{assignment6:6.1f}/100 × 16% = {weighted6:5.2f} points")
print(f"Assignment 7 (2D Arrays):     {assignment7:6.1f}/100 × 18% = {weighted7:5.2f} points")
print("-" * 50)
print(f"TOTAL WEIGHTED SCORE:                           {overall_grade:5.2f}/100")

# Overall Performance Summary
print("\nOVERALL PERFORMANCE:")
print("-" * 20)
print(f"Final Grade: {overall_grade:.2f}%")
print(f"Letter Grade: {letter_grade}")
print(f"Status: {pass_status}")
print(f"Assignments Completed: {completed_assignments}/7")

if completed_assignments > 0:
    print(f"Average of Completed Assignments: {average_grade:.2f}%")

# Progress and Recommendations
print("\nPROGRESS ANALYSIS:")
print("-" * 20)

if completed_assignments == 7:
    print("✅ All assignments completed!")
    if overall_grade >= 70:
        print("🎉 Excellent work! You're performing very well in this course.")
    elif overall_grade >= 50:
        print("👍 Good progress! You're on track to pass the course.")
    else:
        print("📚 Keep working hard! Consider reviewing fundamental concepts.")
else:
    remaining = 7 - completed_assignments
    print(f"📝 {remaining} assignment(s) remaining")
    
    # Calculate potential final grade if remaining assignments score 100%
    max_possible_points = overall_grade
    remaining_weights = [weight1, weight2, weight3, weight4, weight5, weight6, weight7]
    
    for i, grade in enumerate(assignments):
        if grade == 0:  # Not completed yet
            max_possible_points += 100 * remaining_weights[i]
    
    print(f"💡 If you score 100% on remaining assignments: {max_possible_points:.1f}%")

# Study Recommendations
print("\nRECOMMendations:")
print("-" * 16)
if overall_grade < 40:
    print("🚨 Priority: Focus on fundamental concepts")
    print("   - Review all course materials")
    print("   - Seek help from instructor or tutors")
    print("   - Practice basic programming concepts daily")
elif overall_grade < 60:
    print("📖 Suggested: Strengthen understanding")
    print("   - Review challenging topics")
    print("   - Complete practice exercises")
    print("   - Form study groups with classmates")
elif overall_grade < 80:
    print("⭐ Goal: Aim for distinction")
    print("   - Focus on advanced topics")
    print("   - Help other students (teaching reinforces learning)")
    print("   - Attempt bonus challenges")
else:
    print("🏆 Excellent! Maintain this performance")
    print("   - Continue consistent study habits")
    print("   - Explore advanced programming concepts")
    print("   - Consider mentoring other students")

# SECTION 5: PROGRAM SUMMARY
print("\n" + "="*60)
print("PROGRAM EXECUTION SUMMARY".center(60))
print("="*60)

print("\nThis program demonstrated sequence constructs by:")
print("1. 📝 Collecting student information (INPUT)")
print("2. 🔢 Processing numerical data (ARITHMETIC)")
print("3. 📊 Performing complex calculations (EXPRESSIONS)")
print("4. 💬 Formatting and displaying results (STRING OPERATIONS)")
print("5. 🔄 Executing all steps in sequential order (SEQUENCE)")

print(f"\nTotal lines of output generated: Approximately 50+ lines")
print(f"Variables used: {len(['student_name', 'student_id', 'course_code', 'course_name', 'current_year', 'assignment1', 'assignment2', 'assignment3', 'assignment4', 'assignment5', 'assignment6', 'assignment7', 'overall_grade', 'letter_grade'])}+ variables")
print(f"Calculations performed: 15+ mathematical operations")
print(f"String operations: 10+ formatting and manipulation operations")

print("\n🎓 Congratulations! You've successfully completed a comprehensive")
print("   program using sequence constructs!")

print("\n" + "="*60)
print("END OF PROGRAM".center(60))
print("="*60)

"""
WHAT THIS PROGRAM DEMONSTRATES:
===============================

1. VARIABLES & DATA TYPES:
   - String variables for names, IDs, courses
   - Integer variables for years, counts
   - Float variables for grades and calculations
   - Boolean logic for pass/fail determination

2. INPUT OPERATIONS:
   - Multiple input() calls for data collection
   - String processing with .strip() and .title()
   - Type conversion with int() and float()
   - User-friendly prompts and instructions

3. OUTPUT OPERATIONS:
   - Formatted output with f-strings
   - Table-like formatting with alignment
   - Multi-line output for reports
   - User-friendly presentation

4. ARITHMETIC OPERATIONS:
   - Multiplication for weighted scores
   - Addition for totals
   - Division for averages
   - Comparison operations for grading

5. STRING OPERATIONS:
   - String formatting and alignment
   - Case conversion (.upper(), .title())
   - String concatenation and f-strings
   - Multi-line string formatting

6. SEQUENTIAL EXECUTION:
   - Logical flow from data collection to results
   - Step-by-step processing
   - Building up complex results from simple operations
   - Clear program structure and organization

REAL-WORLD APPLICATIONS:
========================
This type of program structure is used in:
- Student information systems
- Grade calculation software
- Business reporting systems
- Data collection and analysis tools
- Financial calculators
- Survey processing systems

KEY LEARNING OUTCOMES:
======================
After studying this program, you should be able to:
✅ Create variables of different data types
✅ Collect user input and validate it
✅ Perform mathematical calculations
✅ Format and display results professionally
✅ Write programs that execute in logical sequence
✅ Combine multiple concepts in a single program
✅ Create user-friendly interfaces
✅ Handle real-world programming problems

This completes Assignment 1: Sequence Constructs!
Next: Assignment 2 will cover Selection Constructs (if/else statements)
"""