"""
Assignment 2 - Example 6: Complete Selection Program
===================================================

This is a comprehensive program that demonstrates all the selection concepts
from Assignment 2. It implements a complete student management system that
uses every type of conditional statement and decision-making pattern we've learned.

PROGRAM PURPOSE:
This program manages a student database with complex decision-making for:
- Student registration and validation
- Grade calculation with multiple criteria
- Scholarship eligibility determination
- Academic standing evaluation
- Interactive menu system with validation

CONCEPTS DEMONSTRATED:
✓ Basic if statements
✓ if-else statements  
✓ elif chains for multiple conditions
✓ Boolean logic (and, or, not)
✓ Nested conditional statements
✓ Complex decision trees
✓ Input validation
✓ Menu-driven programming
✓ Real-world business logic
"""

print("=" * 60)
print("     COMPREHENSIVE STUDENT MANAGEMENT SYSTEM")
print("=" * 60)
print()

print("Welcome to the Student Management System!")
print("This program demonstrates all selection concepts through")
print("a complete student registration and evaluation system.")
print()

# SECTION 1: STUDENT DATA STRUCTURE
print("=== SECTION 1: SYSTEM INITIALIZATION ===")
print()

# Initialize student database
students = []

# System configuration
PASSING_GRADE = 60
HONORS_THRESHOLD = 85
DEAN_LIST_THRESHOLD = 90
MAX_ABSENCES = 5
SCHOLARSHIP_GPA_REQUIREMENT = 3.5

print("📊 System Configuration:")
print(f"   Passing Grade: {PASSING_GRADE}")
print(f"   Honors Threshold: {HONORS_THRESHOLD}")
print(f"   Dean's List Threshold: {DEAN_LIST_THRESHOLD}")
print(f"   Maximum Absences: {MAX_ABSENCES}")
print(f"   Scholarship GPA Requirement: {SCHOLARSHIP_GPA_REQUIREMENT}")
print()

# SECTION 2: STUDENT REGISTRATION WITH COMPREHENSIVE VALIDATION
print("=== SECTION 2: STUDENT REGISTRATION SYSTEM ===")
print()

def validate_student_data(name, age, email, gpa, major):
    """
    Comprehensive validation using nested conditions and boolean logic.
    Returns tuple: (is_valid, error_message)
    """
    
    print(f"🔍 Validating student data for: {name}")
    
    # Name validation using basic if statements
    if not name:
        return False, "Name cannot be empty"
    
    if len(name.strip()) < 2:
        return False, "Name must be at least 2 characters long"
    
    # Check for valid characters in name
    if not name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
        return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
    
    print("   ✅ Name validation passed")
    
    # Age validation with nested conditions
    if age is not None:
        if age < 16:
            return False, "Student must be at least 16 years old"
        elif age > 100:
            return False, "Age seems unrealistic (over 100)"
        else:
            print("   ✅ Age validation passed")
    else:
        return False, "Age is required"
    
    # Email validation using boolean logic
    if email:
        # Basic email validation using logical operators
        has_at = "@" in email
        has_dot = "." in email
        not_too_short = len(email) >= 5
        no_spaces = " " not in email
        
        # All conditions must be true using AND
        if has_at and has_dot and not_too_short and no_spaces:
            # Additional checks with nested conditions
            at_position = email.find("@")
            if at_position > 0 and at_position < len(email) - 1:
                domain_part = email[at_position + 1:]
                if "." in domain_part and len(domain_part) >= 3:
                    print("   ✅ Email validation passed")
                else:
                    return False, "Email domain format is invalid"
            else:
                return False, "Email format is invalid (@ position)"
        else:
            return False, "Email format is invalid"
    else:
        return False, "Email is required"
    
    # GPA validation with nested conditions
    if gpa is not None:
        if gpa < 0.0:
            return False, "GPA cannot be negative"
        elif gpa > 4.0:
            return False, "GPA cannot exceed 4.0"
        else:
            print("   ✅ GPA validation passed")
    else:
        return False, "GPA is required"
    
    # Major validation
    valid_majors = [
        "Computer Science", "Mathematics", "Physics", "Chemistry", "Biology",
        "Engineering", "Business", "Economics", "Psychology", "History",
        "English", "Art", "Music", "Philosophy", "Political Science"
    ]
    
    if major:
        if major in valid_majors:
            print("   ✅ Major validation passed")
        else:
            return False, f"Major must be one of: {', '.join(valid_majors)}"
    else:
        return False, "Major is required"
    
    # All validations passed
    print("   🎉 All validations passed!")
    return True, "Valid student data"

# Sample student registration attempts
print("🎓 Processing student registration attempts:")

registration_attempts = [
    {
        "name": "Alice Johnson",
        "age": 20,
        "email": "alice.johnson@university.edu",
        "gpa": 3.7,
        "major": "Computer Science"
    },
    {
        "name": "Bob Smith",
        "age": 19,
        "email": "invalid-email",  # Invalid email
        "gpa": 2.8,
        "major": "Mathematics"
    },
    {
        "name": "Charlie Brown",
        "age": 22,
        "email": "charlie@school.edu",
        "gpa": 3.9,
        "major": "Physics"
    },
    {
        "name": "",  # Invalid name
        "age": 21,
        "email": "empty@name.edu",
        "gpa": 3.2,
        "major": "Chemistry"
    }
]

for i, attempt in enumerate(registration_attempts, 1):
    print(f"\n--- Registration Attempt {i} ---")
    
    is_valid, message = validate_student_data(
        attempt["name"],
        attempt["age"], 
        attempt["email"],
        attempt["gpa"],
        attempt["major"]
    )
    
    if is_valid:
        students.append(attempt)
        print(f"✅ {attempt['name']} registered successfully!")
    else:
        print(f"❌ Registration failed: {message}")

print(f"\n📈 Registration Summary:")
print(f"   Total attempts: {len(registration_attempts)}")
print(f"   Successful registrations: {len(students)}")
print(f"   Failed registrations: {len(registration_attempts) - len(students)}")

print()

# SECTION 3: GRADE CALCULATION WITH COMPLEX BUSINESS LOGIC
print("=== SECTION 3: GRADE CALCULATION SYSTEM ===")
print()

def calculate_final_grade(exam_scores, homework_scores, attendance_rate, participation):
    """
    Calculate final grade using complex nested conditions and business logic.
    """
    
    print(f"📊 Calculating final grade...")
    print(f"   Exam scores: {exam_scores}")
    print(f"   Homework scores: {homework_scores}")
    print(f"   Attendance rate: {attendance_rate * 100:.1f}%")
    print(f"   Participation: {participation}")
    
    # Basic grade calculation
    if exam_scores and homework_scores:
        exam_average = sum(exam_scores) / len(exam_scores)
        homework_average = sum(homework_scores) / len(homework_scores)
        base_grade = (exam_average * 0.7) + (homework_average * 0.3)  # 70% exams, 30% homework
        
        print(f"   Exam average: {exam_average:.1f}")
        print(f"   Homework average: {homework_average:.1f}")
        print(f"   Base grade: {base_grade:.1f}")
    else:
        return 0, "F", "Incomplete data"
    
    # Attendance adjustments using nested conditions
    final_grade = base_grade
    attendance_adjustment = 0
    
    if attendance_rate >= 0.95:  # 95% or better
        print("   🏆 Excellent attendance (≥95%)")
        attendance_adjustment = 5
    elif attendance_rate >= 0.90:  # 90-94%
        print("   ✅ Good attendance (90-94%)")
        attendance_adjustment = 2
    elif attendance_rate >= 0.80:  # 80-89%
        print("   ⚠️ Fair attendance (80-89%)")
        attendance_adjustment = 0
    elif attendance_rate >= 0.70:  # 70-79%
        print("   ⚠️ Poor attendance (70-79%)")
        attendance_adjustment = -5
    else:  # Below 70%
        print("   🚨 Very poor attendance (<70%)")
        attendance_adjustment = -10
    
    # Participation bonus using boolean logic
    participation_bonus = 0
    if participation == "Excellent":
        participation_bonus = 5
        print("   🌟 Excellent participation: +5 points")
    elif participation == "Good":
        participation_bonus = 3
        print("   ✅ Good participation: +3 points")
    elif participation == "Fair":
        participation_bonus = 1
        print("   📝 Fair participation: +1 point")
    elif participation == "Poor":
        participation_bonus = -2
        print("   ❌ Poor participation: -2 points")
    else:
        participation_bonus = 0
        print("   • No participation data")
    
    # Apply adjustments
    final_grade += attendance_adjustment + participation_bonus
    
    # Ensure grade is within valid range
    final_grade = max(0, min(100, final_grade))
    
    print(f"   Attendance adjustment: {attendance_adjustment:+d}")
    print(f"   Participation bonus: {participation_bonus:+d}")
    print(f"   Final grade: {final_grade:.1f}")
    
    # Letter grade assignment using elif chain
    if final_grade >= 97:
        letter_grade = "A+"
        performance = "Outstanding"
    elif final_grade >= 93:
        letter_grade = "A"
        performance = "Excellent"
    elif final_grade >= 90:
        letter_grade = "A-"
        performance = "Very Good"
    elif final_grade >= 87:
        letter_grade = "B+"
        performance = "Good"
    elif final_grade >= 83:
        letter_grade = "B"
        performance = "Above Average"
    elif final_grade >= 80:
        letter_grade = "B-"
        performance = "Average"
    elif final_grade >= 77:
        letter_grade = "C+"
        performance = "Below Average"
    elif final_grade >= 73:
        letter_grade = "C"
        performance = "Poor"
    elif final_grade >= 70:
        letter_grade = "C-"
        performance = "Very Poor"
    elif final_grade >= 65:
        letter_grade = "D+"
        performance = "Failing"
    elif final_grade >= 60:
        letter_grade = "D"
        performance = "Failing"
    else:
        letter_grade = "F"
        performance = "Failing"
    
    return final_grade, letter_grade, performance

# Calculate grades for registered students
print("🎯 Calculating final grades for registered students:")

# Sample grade data
grade_data = [
    {
        "exam_scores": [88, 92, 85, 90],
        "homework_scores": [95, 88, 92, 87, 94],
        "attendance_rate": 0.96,
        "participation": "Excellent"
    },
    {
        "exam_scores": [75, 82, 78],
        "homework_scores": [80, 85, 75, 88],
        "attendance_rate": 0.85,
        "participation": "Good"
    },
    {
        "exam_scores": [92, 95, 89, 94],
        "homework_scores": [98, 95, 92, 96, 89],
        "attendance_rate": 0.98,
        "participation": "Excellent"
    }
]

for i, student in enumerate(students):
    if i < len(grade_data):  # Only process if we have grade data
        print(f"\n--- Grade Calculation for {student['name']} ---")
        
        data = grade_data[i]
        final_grade, letter_grade, performance = calculate_final_grade(
            data["exam_scores"],
            data["homework_scores"],
            data["attendance_rate"],
            data["participation"]
        )
        
        # Store calculated grades
        student["final_grade"] = final_grade
        student["letter_grade"] = letter_grade
        student["performance"] = performance
        
        print(f"   📊 Final Grade: {final_grade:.1f} ({letter_grade})")
        print(f"   📈 Performance Level: {performance}")

print()

# SECTION 4: SCHOLARSHIP ELIGIBILITY WITH COMPLEX CRITERIA
print("=== SECTION 4: SCHOLARSHIP ELIGIBILITY SYSTEM ===")
print()

def determine_scholarship_eligibility(student):
    """
    Complex scholarship determination using nested conditions and multiple criteria.
    """
    
    name = student["name"]
    gpa = student["gpa"]
    final_grade = student.get("final_grade", 0)
    major = student["major"]
    age = student["age"]
    
    print(f"🎓 Evaluating scholarship eligibility for {name}:")
    print(f"   GPA: {gpa}")
    print(f"   Final Grade: {final_grade:.1f}")
    print(f"   Major: {major}")
    print(f"   Age: {age}")
    
    scholarships = []
    
    # Academic Excellence Scholarship
    if gpa >= 3.8:
        print("   ✅ Meets Academic Excellence GPA requirement")
        
        if final_grade >= 90:
            print("   ✅ Meets Academic Excellence grade requirement")
            scholarships.append(("Academic Excellence", 5000, "Outstanding academic performance"))
        else:
            print("   ❌ Does not meet Academic Excellence grade requirement (need ≥90)")
    else:
        print("   ❌ Does not meet Academic Excellence GPA requirement (need ≥3.8)")
    
    # Merit Scholarship (less restrictive)
    if gpa >= 3.5:
        print("   ✅ Meets Merit Scholarship GPA requirement")
        
        if final_grade >= 85:
            print("   ✅ Meets Merit Scholarship grade requirement")
            
            # Additional criteria based on major
            stem_majors = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "Engineering"]
            if major in stem_majors:
                print("   ✅ STEM major - enhanced merit scholarship")
                scholarships.append(("STEM Merit", 3500, "Excellence in STEM field"))
            else:
                scholarships.append(("General Merit", 2500, "Academic merit"))
        else:
            print("   ❌ Does not meet Merit Scholarship grade requirement (need ≥85)")
    else:
        print("   ❌ Does not meet Merit Scholarship GPA requirement (need ≥3.5)")
    
    # Need-based considerations (simplified)
    # In real system, this would check financial data
    if age >= 21:  # Assume older students may have more financial need
        print("   ✅ Eligible for need-based considerations")
        
        if gpa >= 3.0 and final_grade >= 75:
            scholarships.append(("Need-Based", 2000, "Financial need with academic merit"))
    
    # Leadership scholarship based on participation
    # This would typically check extracurricular data
    if gpa >= 3.2 and final_grade >= 80:
        # Simulate leadership evaluation
        import random
        has_leadership = random.choice([True, False])  # Simulate leadership activities
        
        if has_leadership:
            print("   ✅ Demonstrates leadership qualities")
            scholarships.append(("Leadership", 1500, "Leadership potential"))
    
    return scholarships

# Evaluate scholarships for all students
print("💰 Evaluating scholarship eligibility:")

total_scholarship_value = 0

for student in students:
    if "final_grade" in student:  # Only evaluate if grades calculated
        print(f"\n--- Scholarship Evaluation for {student['name']} ---")
        
        scholarships = determine_scholarship_eligibility(student)
        student["scholarships"] = scholarships
        
        if scholarships:
            print(f"   🎉 {student['name']} is eligible for {len(scholarships)} scholarship(s):")
            student_total = 0
            for name, amount, reason in scholarships:
                print(f"     • {name}: ${amount:,} - {reason}")
                student_total += amount
            
            print(f"   💰 Total scholarship value: ${student_total:,}")
            total_scholarship_value += student_total
        else:
            print(f"   ❌ {student['name']} is not eligible for any scholarships")

print(f"\n📊 Scholarship Summary:")
print(f"   Total scholarship funds awarded: ${total_scholarship_value:,}")

print()

# SECTION 5: ACADEMIC STANDING EVALUATION
print("=== SECTION 5: ACADEMIC STANDING EVALUATION ===")
print()

def evaluate_academic_standing(student):
    """
    Comprehensive academic standing evaluation using complex nested conditions.
    """
    
    name = student["name"]
    gpa = student["gpa"]
    final_grade = student.get("final_grade", 0)
    letter_grade = student.get("letter_grade", "N/A")
    
    print(f"📚 Evaluating academic standing for {name}:")
    
    # Primary standing determination
    if final_grade >= DEAN_LIST_THRESHOLD:
        if gpa >= 3.7:
            standing = "Dean's List"
            status_color = "🏆"
            actions = ["Congratulations letter", "Priority course registration", "Academic recognition ceremony"]
        else:
            standing = "High Achievement"
            status_color = "🌟"
            actions = ["Recognition letter", "Merit certificate"]
    
    elif final_grade >= HONORS_THRESHOLD:
        if gpa >= 3.5:
            standing = "Honors"
            status_color = "✨"
            actions = ["Honor roll recognition", "Academic achievement certificate"]
        else:
            standing = "Good Standing"
            status_color = "✅"
            actions = ["Continue current performance"]
    
    elif final_grade >= PASSING_GRADE:
        if gpa >= 3.0:
            standing = "Good Standing"
            status_color = "✅"
            actions = ["Continue current performance"]
        elif gpa >= 2.5:
            standing = "Academic Watch"
            status_color = "⚠️"
            actions = ["Academic advisor meeting", "Study skills workshop"]
        else:
            standing = "Academic Warning"
            status_color = "🔸"
            actions = ["Mandatory academic counseling", "Study plan development"]
    
    else:  # Below passing grade
        if gpa >= 2.0:
            standing = "Academic Probation"
            status_color = "⚠️"
            actions = ["Academic probation contract", "Weekly advisor meetings", "Tutoring requirements"]
        else:
            standing = "Academic Suspension Risk"
            status_color = "🚨"
            actions = ["Emergency academic intervention", "Dean meeting required", "Possible course withdrawal"]
    
    # Additional considerations
    additional_notes = []
    
    # Check for improvement potential
    grade_vs_gpa_diff = final_grade / 25 - gpa  # Convert grade to 4.0 scale for comparison
    if grade_vs_gpa_diff > 0.3:
        additional_notes.append("Showing academic improvement this semester")
    elif grade_vs_gpa_diff < -0.3:
        additional_notes.append("Performance decline - needs attention")
    
    # Check for consistency
    if abs(grade_vs_gpa_diff) <= 0.2:
        additional_notes.append("Consistent academic performance")
    
    return standing, status_color, actions, additional_notes

# Evaluate academic standing for all students
print("📊 Academic Standing Evaluation:")

standing_summary = {
    "Dean's List": 0,
    "High Achievement": 0,
    "Honors": 0,
    "Good Standing": 0,
    "Academic Watch": 0,
    "Academic Warning": 0,
    "Academic Probation": 0,
    "Academic Suspension Risk": 0
}

for student in students:
    if "final_grade" in student:
        print(f"\n--- Academic Standing for {student['name']} ---")
        
        standing, status_color, actions, notes = evaluate_academic_standing(student)
        student["academic_standing"] = standing
        
        standing_summary[standing] += 1
        
        print(f"   {status_color} Academic Standing: {standing}")
        print(f"   📋 Required Actions:")
        for action in actions:
            print(f"     • {action}")
        
        if notes:
            print(f"   📝 Additional Notes:")
            for note in notes:
                print(f"     • {note}")

print(f"\n📈 Academic Standing Distribution:")
for standing, count in standing_summary.items():
    if count > 0:
        print(f"   {standing}: {count} student{'s' if count != 1 else ''}")

print()

# SECTION 6: INTERACTIVE REPORTING SYSTEM
print("=== SECTION 6: INTERACTIVE REPORTING SYSTEM ===")
print()

def display_student_report(student):
    """Display comprehensive student report."""
    
    print(f"\n{'='*50}")
    print(f"         STUDENT REPORT: {student['name'].upper()}")
    print(f"{'='*50}")
    
    print(f"📋 Basic Information:")
    print(f"   Name: {student['name']}")
    print(f"   Age: {student['age']}")
    print(f"   Email: {student['email']}")
    print(f"   Major: {student['major']}")
    print(f"   Cumulative GPA: {student['gpa']}")
    
    if "final_grade" in student:
        print(f"\n📊 Academic Performance:")
        print(f"   Final Grade: {student['final_grade']:.1f}")
        print(f"   Letter Grade: {student['letter_grade']}")
        print(f"   Performance Level: {student['performance']}")
        print(f"   Academic Standing: {student['academic_standing']}")
    
    if "scholarships" in student and student["scholarships"]:
        print(f"\n💰 Scholarships:")
        total_value = 0
        for name, amount, reason in student["scholarships"]:
            print(f"   • {name}: ${amount:,}")
            print(f"     Reason: {reason}")
            total_value += amount
        print(f"   Total Value: ${total_value:,}")
    else:
        print(f"\n💰 Scholarships: None awarded")

# Interactive menu system using complex selection structures
print("🖥️ Interactive Student Management System")

while True:
    print(f"\n{'='*40}")
    print("   STUDENT MANAGEMENT MENU")
    print(f"{'='*40}")
    print("1. Display all students summary")
    print("2. View detailed student report")
    print("3. Search by academic standing")
    print("4. Scholarship recipients report")
    print("5. System statistics")
    print("6. Exit system")
    
    # Input validation with nested conditions
    while True:
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice in ['1', '2', '3', '4', '5', '6']:
                choice = int(choice)
                break
            else:
                print("❌ Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    # Process menu choice using elif chain
    if choice == 1:
        print(f"\n📋 ALL STUDENTS SUMMARY")
        print(f"{'='*60}")
        
        if students:
            for i, student in enumerate(students, 1):
                print(f"\n{i}. {student['name']}")
                print(f"   Major: {student['major']} | GPA: {student['gpa']}")
                
                if "final_grade" in student:
                    print(f"   Grade: {student['final_grade']:.1f} ({student['letter_grade']}) | Standing: {student['academic_standing']}")
                    
                    scholarship_count = len(student.get("scholarships", []))
                    if scholarship_count > 0:
                        total_value = sum(amount for _, amount, _ in student["scholarships"])
                        print(f"   Scholarships: {scholarship_count} (${total_value:,})")
        else:
            print("No students registered.")
    
    elif choice == 2:
        print(f"\n👤 DETAILED STUDENT REPORT")
        
        if students:
            print("\nAvailable students:")
            for i, student in enumerate(students, 1):
                print(f"   {i}. {student['name']}")
            
            while True:
                try:
                    student_choice = int(input(f"\nEnter student number (1-{len(students)}): "))
                    if 1 <= student_choice <= len(students):
                        display_student_report(students[student_choice - 1])
                        break
                    else:
                        print(f"❌ Please enter a number between 1 and {len(students)}")
                except ValueError:
                    print("❌ Please enter a valid number.")
        else:
            print("No students registered.")
    
    elif choice == 3:
        print(f"\n🎯 SEARCH BY ACADEMIC STANDING")
        
        print("\nAvailable academic standings:")
        available_standings = set()
        for student in students:
            if "academic_standing" in student:
                available_standings.add(student["academic_standing"])
        
        if available_standings:
            for standing in sorted(available_standings):
                print(f"   • {standing}")
            
            search_standing = input("\nEnter academic standing to search: ").strip()
            
            matching_students = [s for s in students 
                               if s.get("academic_standing") == search_standing]
            
            if matching_students:
                print(f"\n📚 Students with '{search_standing}' standing:")
                for student in matching_students:
                    print(f"   • {student['name']} - {student['final_grade']:.1f} ({student['letter_grade']})")
            else:
                print(f"❌ No students found with '{search_standing}' standing.")
        else:
            print("No academic standings available.")
    
    elif choice == 4:
        print(f"\n💰 SCHOLARSHIP RECIPIENTS REPORT")
        
        scholarship_recipients = [s for s in students if s.get("scholarships")]
        
        if scholarship_recipients:
            total_awarded = 0
            print(f"\n🏆 Scholarship Recipients ({len(scholarship_recipients)} students):")
            
            for student in scholarship_recipients:
                student_total = sum(amount for _, amount, _ in student["scholarships"])
                total_awarded += student_total
                
                print(f"\n   {student['name']}:")
                for name, amount, reason in student["scholarships"]:
                    print(f"     • {name}: ${amount:,}")
                print(f"     Total: ${student_total:,}")
            
            print(f"\n💰 Total Scholarship Funds Awarded: ${total_awarded:,}")
            print(f"📊 Average Award per Recipient: ${total_awarded // len(scholarship_recipients):,}")
        else:
            print("❌ No scholarship recipients found.")
    
    elif choice == 5:
        print(f"\n📊 SYSTEM STATISTICS")
        print(f"{'='*40}")
        
        print(f"📈 Registration Statistics:")
        print(f"   Total Students: {len(students)}")
        
        if students:
            # GPA statistics
            gpas = [s["gpa"] for s in students]
            avg_gpa = sum(gpas) / len(gpas)
            highest_gpa = max(gpas)
            lowest_gpa = min(gpas)
            
            print(f"   Average GPA: {avg_gpa:.2f}")
            print(f"   Highest GPA: {highest_gpa}")
            print(f"   Lowest GPA: {lowest_gpa}")
            
            # Major distribution
            major_counts = {}
            for student in students:
                major = student["major"]
                major_counts[major] = major_counts.get(major, 0) + 1
            
            print(f"\n🎓 Major Distribution:")
            for major, count in sorted(major_counts.items()):
                percentage = (count / len(students)) * 100
                print(f"   {major}: {count} ({percentage:.1f}%)")
            
            # Academic standing distribution
            if any("academic_standing" in s for s in students):
                print(f"\n📚 Academic Standing Distribution:")
                for standing, count in standing_summary.items():
                    if count > 0:
                        percentage = (count / len(students)) * 100
                        print(f"   {standing}: {count} ({percentage:.1f}%)")
            
            # Scholarship statistics
            scholarship_recipients = [s for s in students if s.get("scholarships")]
            if scholarship_recipients:
                total_awarded = sum(sum(amount for _, amount, _ in s["scholarships"]) 
                                  for s in scholarship_recipients)
                print(f"\n💰 Scholarship Statistics:")
                print(f"   Recipients: {len(scholarship_recipients)} ({(len(scholarship_recipients)/len(students))*100:.1f}%)")
                print(f"   Total Awarded: ${total_awarded:,}")
    
    elif choice == 6:
        print(f"\n👋 Exiting Student Management System")
        print(f"Thank you for using the system!")
        break
    
    # Ask if user wants to continue (except for exit)
    if choice != 6:
        while True:
            continue_choice = input("\nPress Enter to return to main menu, or 'q' to quit: ").lower().strip()
            if continue_choice in ['', 'q']:
                if continue_choice == 'q':
                    print(f"\n👋 Goodbye!")
                    exit()
                break

print()

# PROGRAM CONCLUSION
print("=" * 60)
print("           PROGRAM ANALYSIS COMPLETE")
print("=" * 60)
print()

print("🎓 SELECTION CONCEPTS DEMONSTRATED IN THIS PROGRAM:")
print()
print("✅ BASIC IF STATEMENTS:")
print("   • Simple condition checking")
print("   • Data validation")
print("   • Status determination")
print()
print("✅ IF-ELSE STATEMENTS:")
print("   • Binary decision making")
print("   • Alternative actions")
print("   • Default behaviors")
print()
print("✅ ELIF CHAINS:")
print("   • Multiple condition testing")
print("   • Grade assignment")
print("   • Category determination")
print("   • Menu systems")
print()
print("✅ BOOLEAN LOGIC:")
print("   • AND operators for multiple requirements")
print("   • OR operators for alternative conditions")
print("   • NOT operators for negation")
print("   • Complex condition combinations")
print()
print("✅ NESTED CONDITIONS:")
print("   • Multi-level validation")
print("   • Step-by-step decision trees")
print("   • Hierarchical business logic")
print("   • Complex eligibility determination")
print()
print("🚀 REAL-WORLD APPLICATIONS:")
print("   • Student information systems")
print("   • Financial aid processing")
print("   • Academic evaluation")
print("   • Menu-driven interfaces")
print("   • Data validation and processing")
print()
print("💡 KEY LEARNING OUTCOMES:")
print("1. Selection constructs enable intelligent program behavior")
print("2. Different selection types serve different purposes")
print("3. Complex decisions require combining multiple techniques")
print("4. Proper validation prevents errors and improves UX")
print("5. Real-world systems need sophisticated decision logic")
print("6. Code organization and readability are crucial")
print()
print("🎯 YOU'VE MASTERED SELECTION CONSTRUCTS!")
print("   Ready for Assignment 3: Iteration and Loops")

"""
PROGRAM SUMMARY:
================
This comprehensive program demonstrates ALL selection concepts:

1. BASIC IF STATEMENTS: Used for simple validation and checks
2. IF-ELSE STATEMENTS: Used for binary decisions and alternatives
3. ELIF CHAINS: Used for multiple categories and menu systems
4. BOOLEAN LOGIC: Used for complex condition combinations
5. NESTED CONDITIONS: Used for multi-level validation and business logic

PRACTICAL APPLICATIONS:
=======================
• Student registration with comprehensive validation
• Academic performance evaluation with complex criteria
• Scholarship eligibility with multiple requirements
• Academic standing determination with hierarchical rules
• Interactive menu system with input validation
• Comprehensive reporting with conditional formatting

ADVANCED CONCEPTS:
==================
• Input validation patterns
• Complex business logic implementation
• Error handling and user feedback
• Data processing with conditional logic
• Interactive system design
• Comprehensive reporting systems

NEXT STEPS:
===========
You've now mastered selection constructs - the foundation of program logic!
Next you'll learn:
• Assignment 3: Iteration and Loops
• Assignment 4: Data Validation and Input Handling
• Assignment 5: Functions and Modular Programming

CONGRATULATIONS! 🎉
You can now create sophisticated decision-making programs!
"""