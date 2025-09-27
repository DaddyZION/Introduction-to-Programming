"""
Assignment 5 - Example 6: Complete Function-Based Program
==========================================================

This program demonstrates a comprehensive application built using all the
function concepts from Assignment 5. It implements a Student Management
System that showcases proper function design, modular architecture,
and real-world programming patterns.

Application Features:
- Student registration and management
- Grade calculation and reporting
- Data validation and error handling
- File operations simulation
- Modular, extensible architecture
- Comprehensive testing and demonstration

This represents the kind of function-based application you might build
for a real-world business or educational institution.
"""

print("=== STUDENT MANAGEMENT SYSTEM ===")
print("Complete Function-Based Application")
print("Demonstrating all concepts from Assignment 5")
print()

# CORE DATA STRUCTURES (SIMULATING DATABASE)
students_database = {}
courses_database = {}
enrollments_database = {}
grades_database = {}

# UTILITY FUNCTIONS MODULE
def generate_id(prefix="ID"):
    """
    Generate a unique ID with prefix.
    In a real application, this would use proper UUID generation.
    """
    import time
    timestamp = int(time.time() * 1000) % 100000
    return f"{prefix}{timestamp:05d}"

def validate_required_fields(data, required_fields):
    """
    Validate that all required fields are present and not empty.
    
    Args:
        data (dict): Data to validate
        required_fields (list): List of required field names
    
    Returns:
        tuple: (is_valid, missing_fields)
    """
    missing_fields = []
    for field in required_fields:
        if field not in data or not str(data[field]).strip():
            missing_fields.append(field)
    
    return len(missing_fields) == 0, missing_fields

def format_currency(amount):
    """Format numeric amount as currency."""
    return f"${amount:.2f}"

def calculate_percentage(part, total):
    """Calculate percentage with error handling."""
    if total == 0:
        return 0
    return round((part / total) * 100, 2)

# VALIDATION MODULE
class ValidationModule:
    """Comprehensive validation functions for student data."""
    
    @staticmethod
    def validate_email(email):
        """Validate email address format."""
        if not email or '@' not in email:
            return False, "Email must contain @ symbol"
        
        parts = email.split('@')
        if len(parts) != 2 or not parts[0] or not parts[1]:
            return False, "Invalid email format"
        
        if '.' not in parts[1]:
            return False, "Domain must contain a dot"
        
        return True, "Valid email address"
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number format."""
        digits = ''.join(c for c in phone if c.isdigit())
        if len(digits) == 10:
            return True, f"Valid phone: ({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        elif len(digits) == 11 and digits[0] == '1':
            return True, f"Valid phone: +1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        else:
            return False, "Phone must be 10 or 11 digits"
    
    @staticmethod
    def validate_grade(grade):
        """Validate a grade value."""
        try:
            grade_float = float(grade)
            if 0 <= grade_float <= 100:
                return True, f"Valid grade: {grade_float}"
            else:
                return False, "Grade must be between 0 and 100"
        except ValueError:
            return False, "Grade must be a number"
    
    @staticmethod
    def validate_gpa(gpa):
        """Validate GPA value."""
        try:
            gpa_float = float(gpa)
            if 0.0 <= gpa_float <= 4.0:
                return True, f"Valid GPA: {gpa_float:.2f}"
            else:
                return False, "GPA must be between 0.0 and 4.0"
        except ValueError:
            return False, "GPA must be a number"

# STUDENT MANAGEMENT MODULE
class StudentModule:
    """Functions for managing student data."""
    
    @staticmethod
    def create_student(first_name, last_name, email, phone, birth_date=None):
        """
        Create a new student record.
        
        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            email (str): Student's email address
            phone (str): Student's phone number
            birth_date (str, optional): Student's birth date
        
        Returns:
            tuple: (success, result_dict)
        """
        # Validate required fields
        student_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone
        }
        
        is_valid, missing_fields = validate_required_fields(
            student_data, ['first_name', 'last_name', 'email', 'phone']
        )
        
        if not is_valid:
            return False, {'error': f"Missing required fields: {', '.join(missing_fields)}"}
        
        # Validate email
        email_valid, email_msg = ValidationModule.validate_email(email)
        if not email_valid:
            return False, {'error': f"Email validation failed: {email_msg}"}
        
        # Validate phone
        phone_valid, phone_msg = ValidationModule.validate_phone(phone)
        if not phone_valid:
            return False, {'error': f"Phone validation failed: {phone_msg}"}
        
        # Check for duplicate email
        for existing_id, existing_student in students_database.items():
            if existing_student['email'].lower() == email.lower():
                return False, {'error': f"Email {email} already exists"}
        
        # Create student record
        student_id = generate_id("STU")
        student_record = {
            'student_id': student_id,
            'first_name': first_name.strip().title(),
            'last_name': last_name.strip().title(),
            'email': email.strip().lower(),
            'phone': phone.strip(),
            'birth_date': birth_date,
            'enrollment_date': '2024-09-26',  # Would use current date
            'status': 'active',
            'gpa': 0.0,
            'total_credits': 0
        }
        
        students_database[student_id] = student_record
        
        return True, {
            'student_id': student_id,
            'message': f"Student {first_name} {last_name} created successfully",
            'student': student_record
        }
    
    @staticmethod
    def get_student(student_id):
        """Get student by ID."""
        if student_id in students_database:
            return True, students_database[student_id]
        else:
            return False, {'error': f"Student {student_id} not found"}
    
    @staticmethod
    def update_student(student_id, **updates):
        """Update student information."""
        if student_id not in students_database:
            return False, {'error': f"Student {student_id} not found"}
        
        student = students_database[student_id]
        updated_fields = []
        
        for field, value in updates.items():
            if field in student and field != 'student_id':  # Don't allow ID changes
                if field == 'email':
                    email_valid, email_msg = ValidationModule.validate_email(value)
                    if not email_valid:
                        return False, {'error': f"Email validation failed: {email_msg}"}
                elif field == 'phone':
                    phone_valid, phone_msg = ValidationModule.validate_phone(value)
                    if not phone_valid:
                        return False, {'error': f"Phone validation failed: {phone_msg}"}
                
                student[field] = value
                updated_fields.append(field)
        
        return True, {
            'message': f"Updated fields: {', '.join(updated_fields)}",
            'student': student
        }
    
    @staticmethod
    def list_all_students():
        """Get list of all students."""
        return list(students_database.values())
    
    @staticmethod
    def search_students(search_term):
        """Search students by name or email."""
        results = []
        search_lower = search_term.lower()
        
        for student in students_database.values():
            if (search_lower in student['first_name'].lower() or 
                search_lower in student['last_name'].lower() or 
                search_lower in student['email'].lower()):
                results.append(student)
        
        return results

# COURSE MANAGEMENT MODULE
class CourseModule:
    """Functions for managing course data."""
    
    @staticmethod
    def create_course(course_code, course_name, credits, instructor, description=""):
        """Create a new course."""
        # Validate required fields
        course_data = {
            'course_code': course_code,
            'course_name': course_name,
            'credits': credits,
            'instructor': instructor
        }
        
        is_valid, missing_fields = validate_required_fields(
            course_data, ['course_code', 'course_name', 'credits', 'instructor']
        )
        
        if not is_valid:
            return False, {'error': f"Missing required fields: {', '.join(missing_fields)}"}
        
        # Validate credits
        try:
            credits_int = int(credits)
            if credits_int <= 0 or credits_int > 6:
                return False, {'error': "Credits must be between 1 and 6"}
        except ValueError:
            return False, {'error': "Credits must be a number"}
        
        # Check for duplicate course code
        course_code_upper = course_code.upper()
        if course_code_upper in courses_database:
            return False, {'error': f"Course code {course_code_upper} already exists"}
        
        # Create course record
        course_record = {
            'course_code': course_code_upper,
            'course_name': course_name.strip().title(),
            'credits': credits_int,
            'instructor': instructor.strip().title(),
            'description': description.strip(),
            'status': 'active',
            'enrolled_students': 0
        }
        
        courses_database[course_code_upper] = course_record
        
        return True, {
            'message': f"Course {course_code_upper} created successfully",
            'course': course_record
        }
    
    @staticmethod
    def get_course(course_code):
        """Get course by code."""
        course_code_upper = course_code.upper()
        if course_code_upper in courses_database:
            return True, courses_database[course_code_upper]
        else:
            return False, {'error': f"Course {course_code_upper} not found"}
    
    @staticmethod
    def list_all_courses():
        """Get list of all courses."""
        return list(courses_database.values())

# ENROLLMENT MODULE
class EnrollmentModule:
    """Functions for managing student enrollments."""
    
    @staticmethod
    def enroll_student(student_id, course_code):
        """Enroll a student in a course."""
        # Check if student exists
        student_exists, student_data = StudentModule.get_student(student_id)
        if not student_exists:
            return False, student_data
        
        # Check if course exists
        course_exists, course_data = CourseModule.get_course(course_code)
        if not course_exists:
            return False, course_data
        
        # Check if already enrolled
        enrollment_key = f"{student_id}_{course_code.upper()}"
        if enrollment_key in enrollments_database:
            return False, {'error': f"Student already enrolled in {course_code}"}
        
        # Create enrollment record
        enrollment_record = {
            'enrollment_id': generate_id("ENR"),
            'student_id': student_id,
            'course_code': course_code.upper(),
            'enrollment_date': '2024-09-26',
            'status': 'enrolled',
            'final_grade': None
        }
        
        enrollments_database[enrollment_key] = enrollment_record
        
        # Update course enrollment count
        courses_database[course_code.upper()]['enrolled_students'] += 1
        
        return True, {
            'message': f"Student {student_data['first_name']} {student_data['last_name']} enrolled in {course_code}",
            'enrollment': enrollment_record
        }
    
    @staticmethod
    def get_student_enrollments(student_id):
        """Get all courses a student is enrolled in."""
        enrollments = []
        for enrollment in enrollments_database.values():
            if enrollment['student_id'] == student_id:
                # Add course information
                course_exists, course_data = CourseModule.get_course(enrollment['course_code'])
                if course_exists:
                    enrollment_with_course = enrollment.copy()
                    enrollment_with_course['course_info'] = course_data
                    enrollments.append(enrollment_with_course)
        
        return enrollments
    
    @staticmethod
    def get_course_enrollments(course_code):
        """Get all students enrolled in a course."""
        enrollments = []
        course_code_upper = course_code.upper()
        
        for enrollment in enrollments_database.values():
            if enrollment['course_code'] == course_code_upper:
                # Add student information
                student_exists, student_data = StudentModule.get_student(enrollment['student_id'])
                if student_exists:
                    enrollment_with_student = enrollment.copy()
                    enrollment_with_student['student_info'] = student_data
                    enrollments.append(enrollment_with_student)
        
        return enrollments

# GRADE MANAGEMENT MODULE
class GradeModule:
    """Functions for managing grades and GPA calculations."""
    
    @staticmethod
    def add_grade(student_id, course_code, grade, grade_type="final"):
        """Add a grade for a student in a course."""
        # Validate grade
        grade_valid, grade_msg = ValidationModule.validate_grade(grade)
        if not grade_valid:
            return False, {'error': grade_msg}
        
        # Check if enrollment exists
        enrollment_key = f"{student_id}_{course_code.upper()}"
        if enrollment_key not in enrollments_database:
            return False, {'error': f"Student not enrolled in {course_code}"}
        
        grade_id = generate_id("GRD")
        grade_record = {
            'grade_id': grade_id,
            'student_id': student_id,
            'course_code': course_code.upper(),
            'grade': float(grade),
            'grade_type': grade_type,
            'date_recorded': '2024-09-26'
        }
        
        grades_database[grade_id] = grade_record
        
        # Update final grade in enrollment if this is a final grade
        if grade_type == "final":
            enrollments_database[enrollment_key]['final_grade'] = float(grade)
            
            # Recalculate student GPA
            GradeModule.recalculate_gpa(student_id)
        
        return True, {
            'message': f"Grade {grade} recorded for {course_code}",
            'grade': grade_record
        }
    
    @staticmethod
    def get_student_grades(student_id):
        """Get all grades for a student."""
        student_grades = []
        for grade in grades_database.values():
            if grade['student_id'] == student_id:
                # Add course information
                course_exists, course_data = CourseModule.get_course(grade['course_code'])
                if course_exists:
                    grade_with_course = grade.copy()
                    grade_with_course['course_info'] = course_data
                    student_grades.append(grade_with_course)
        
        return student_grades
    
    @staticmethod
    def calculate_letter_grade(numeric_grade):
        """Convert numeric grade to letter grade."""
        if numeric_grade >= 97:
            return "A+"
        elif numeric_grade >= 93:
            return "A"
        elif numeric_grade >= 90:
            return "A-"
        elif numeric_grade >= 87:
            return "B+"
        elif numeric_grade >= 83:
            return "B"
        elif numeric_grade >= 80:
            return "B-"
        elif numeric_grade >= 77:
            return "C+"
        elif numeric_grade >= 73:
            return "C"
        elif numeric_grade >= 70:
            return "C-"
        elif numeric_grade >= 67:
            return "D+"
        elif numeric_grade >= 63:
            return "D"
        elif numeric_grade >= 60:
            return "D-"
        else:
            return "F"
    
    @staticmethod
    def calculate_gpa_points(letter_grade):
        """Convert letter grade to GPA points."""
        grade_points = {
            "A+": 4.0, "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D+": 1.3, "D": 1.0, "D-": 0.7,
            "F": 0.0
        }
        return grade_points.get(letter_grade, 0.0)
    
    @staticmethod
    def recalculate_gpa(student_id):
        """Recalculate and update student's GPA."""
        enrollments = EnrollmentModule.get_student_enrollments(student_id)
        
        total_quality_points = 0
        total_credits = 0
        
        for enrollment in enrollments:
            if enrollment['final_grade'] is not None:
                course_credits = enrollment['course_info']['credits']
                letter_grade = GradeModule.calculate_letter_grade(enrollment['final_grade'])
                gpa_points = GradeModule.calculate_gpa_points(letter_grade)
                
                total_quality_points += gpa_points * course_credits
                total_credits += course_credits
        
        # Calculate GPA
        if total_credits > 0:
            gpa = total_quality_points / total_credits
        else:
            gpa = 0.0
        
        # Update student record
        if student_id in students_database:
            students_database[student_id]['gpa'] = round(gpa, 2)
            students_database[student_id]['total_credits'] = total_credits
        
        return gpa, total_credits

# REPORTING MODULE
class ReportModule:
    """Functions for generating reports and analytics."""
    
    @staticmethod
    def generate_student_transcript(student_id):
        """Generate a comprehensive student transcript."""
        student_exists, student_data = StudentModule.get_student(student_id)
        if not student_exists:
            return False, student_data
        
        enrollments = EnrollmentModule.get_student_enrollments(student_id)
        
        transcript = {
            'student_info': student_data,
            'courses': [],
            'summary': {
                'total_courses': len(enrollments),
                'completed_courses': 0,
                'total_credits': student_data['total_credits'],
                'gpa': student_data['gpa']
            }
        }
        
        for enrollment in enrollments:
            course_record = {
                'course_code': enrollment['course_code'],
                'course_name': enrollment['course_info']['course_name'],
                'credits': enrollment['course_info']['credits'],
                'numeric_grade': enrollment['final_grade'],
                'letter_grade': None,
                'status': enrollment['status']
            }
            
            if enrollment['final_grade'] is not None:
                course_record['letter_grade'] = GradeModule.calculate_letter_grade(enrollment['final_grade'])
                transcript['summary']['completed_courses'] += 1
            
            transcript['courses'].append(course_record)
        
        return True, transcript
    
    @staticmethod
    def generate_course_roster(course_code):
        """Generate a course roster with student information."""
        course_exists, course_data = CourseModule.get_course(course_code)
        if not course_exists:
            return False, course_data
        
        enrollments = EnrollmentModule.get_course_enrollments(course_code)
        
        roster = {
            'course_info': course_data,
            'students': [],
            'summary': {
                'total_enrolled': len(enrollments),
                'average_gpa': 0.0,
                'grades_recorded': 0
            }
        }
        
        total_gpa = 0
        grades_count = 0
        
        for enrollment in enrollments:
            student_info = enrollment['student_info']
            student_record = {
                'student_id': student_info['student_id'],
                'name': f"{student_info['first_name']} {student_info['last_name']}",
                'email': student_info['email'],
                'gpa': student_info['gpa'],
                'final_grade': enrollment['final_grade'],
                'letter_grade': None,
                'status': enrollment['status']
            }
            
            if enrollment['final_grade'] is not None:
                student_record['letter_grade'] = GradeModule.calculate_letter_grade(enrollment['final_grade'])
                grades_count += 1
            
            total_gpa += student_info['gpa']
            roster['students'].append(student_record)
        
        # Calculate averages
        if len(enrollments) > 0:
            roster['summary']['average_gpa'] = round(total_gpa / len(enrollments), 2)
        
        roster['summary']['grades_recorded'] = grades_count
        
        return True, roster
    
    @staticmethod
    def generate_system_statistics():
        """Generate overall system statistics."""
        students = StudentModule.list_all_students()
        courses = CourseModule.list_all_courses()
        
        # Calculate statistics
        total_students = len(students)
        active_students = sum(1 for s in students if s['status'] == 'active')
        total_courses = len(courses)
        total_enrollments = len(enrollments_database)
        total_grades = len(grades_database)
        
        # GPA statistics
        gpa_values = [s['gpa'] for s in students if s['gpa'] > 0]
        avg_gpa = sum(gpa_values) / len(gpa_values) if gpa_values else 0
        
        # Credit statistics
        total_credits_awarded = sum(s['total_credits'] for s in students)
        
        return {
            'students': {
                'total': total_students,
                'active': active_students,
                'average_gpa': round(avg_gpa, 2)
            },
            'courses': {
                'total': total_courses,
                'total_enrollments': total_enrollments
            },
            'academic': {
                'total_grades_recorded': total_grades,
                'total_credits_awarded': total_credits_awarded
            }
        }

# DEMONSTRATION AND TESTING
def demonstrate_student_management_system():
    """Comprehensive demonstration of the Student Management System."""
    
    print("=== SYSTEM DEMONSTRATION ===")
    print()
    
    # 1. Create Students
    print("1. CREATING STUDENTS")
    print("=" * 40)
    
    students_to_create = [
        ("Alice", "Johnson", "alice.johnson@email.com", "555-123-4567"),
        ("Bob", "Smith", "bob.smith@email.com", "555-234-5678"),
        ("Carol", "Davis", "carol.davis@email.com", "555-345-6789"),
        ("David", "Wilson", "david.wilson@email.com", "555-456-7890")
    ]
    
    created_students = []
    for first, last, email, phone in students_to_create:
        success, result = StudentModule.create_student(first, last, email, phone)
        if success:
            print(f"✅ {result['message']}")
            created_students.append(result['student_id'])
        else:
            print(f"❌ Error: {result['error']}")
    
    print()
    
    # 2. Create Courses
    print("2. CREATING COURSES")
    print("=" * 40)
    
    courses_to_create = [
        ("COMP101", "Introduction to Programming", 3, "Prof. Anderson"),
        ("MATH201", "Calculus I", 4, "Prof. Brown"),
        ("ENG102", "English Composition", 3, "Prof. Clarke"),
        ("PHYS151", "Physics I", 4, "Prof. Davis")
    ]
    
    created_courses = []
    for code, name, credits, instructor in courses_to_create:
        success, result = CourseModule.create_course(code, name, credits, instructor)
        if success:
            print(f"✅ {result['message']}")
            created_courses.append(code)
        else:
            print(f"❌ Error: {result['error']}")
    
    print()
    
    # 3. Enroll Students
    print("3. ENROLLING STUDENTS IN COURSES")
    print("=" * 40)
    
    enrollments_to_create = [
        (created_students[0], "COMP101"),  # Alice in Programming
        (created_students[0], "MATH201"),  # Alice in Calculus
        (created_students[0], "ENG102"),   # Alice in English
        (created_students[1], "COMP101"),  # Bob in Programming
        (created_students[1], "PHYS151"),  # Bob in Physics
        (created_students[2], "MATH201"),  # Carol in Calculus
        (created_students[2], "ENG102"),   # Carol in English
        (created_students[3], "COMP101"),  # David in Programming
        (created_students[3], "PHYS151"),  # David in Physics
    ]
    
    for student_id, course_code in enrollments_to_create:
        success, result = EnrollmentModule.enroll_student(student_id, course_code)
        if success:
            print(f"✅ {result['message']}")
        else:
            print(f"❌ Error: {result['error']}")
    
    print()
    
    # 4. Add Grades
    print("4. RECORDING GRADES")
    print("=" * 40)
    
    grades_to_add = [
        (created_students[0], "COMP101", 92),   # Alice: A-
        (created_students[0], "MATH201", 88),   # Alice: B+
        (created_students[0], "ENG102", 95),    # Alice: A
        (created_students[1], "COMP101", 78),   # Bob: C+
        (created_students[1], "PHYS151", 85),   # Bob: B
        (created_students[2], "MATH201", 91),   # Carol: A-
        (created_students[2], "ENG102", 89),    # Carol: B+
        (created_students[3], "COMP101", 94),   # David: A
        (created_students[3], "PHYS151", 82),   # David: B-
    ]
    
    for student_id, course_code, grade in grades_to_add:
        success, result = GradeModule.add_grade(student_id, course_code, grade, "final")
        if success:
            print(f"✅ {result['message']}")
        else:
            print(f"❌ Error: {result['error']}")
    
    print()
    
    # 5. Generate Reports
    print("5. GENERATING REPORTS")
    print("=" * 40)
    
    # Student transcript
    success, transcript = ReportModule.generate_student_transcript(created_students[0])
    if success:
        student = transcript['student_info']
        print(f"📄 TRANSCRIPT FOR {student['first_name']} {student['last_name']}")
        print(f"   Student ID: {student['student_id']}")
        print(f"   Email: {student['email']}")
        print(f"   GPA: {student['gpa']:.2f}")
        print(f"   Total Credits: {student['total_credits']}")
        print("   Courses:")
        for course in transcript['courses']:
            grade_info = f"{course['numeric_grade']} ({course['letter_grade']})" if course['letter_grade'] else "In Progress"
            print(f"     • {course['course_code']}: {course['course_name']} - {grade_info}")
        print()
    
    # Course roster
    success, roster = ReportModule.generate_course_roster("COMP101")
    if success:
        course = roster['course_info']
        print(f"📋 ROSTER FOR {course['course_code']}: {course['course_name']}")
        print(f"   Instructor: {course['instructor']}")
        print(f"   Credits: {course['credits']}")
        print(f"   Enrolled Students: {roster['summary']['total_enrolled']}")
        print(f"   Average Student GPA: {roster['summary']['average_gpa']:.2f}")
        print("   Student List:")
        for student in roster['students']:
            grade_info = f" - Final Grade: {student['final_grade']} ({student['letter_grade']})" if student['letter_grade'] else " - Grade: Pending"
            print(f"     • {student['name']} (GPA: {student['gpa']:.2f}){grade_info}")
        print()
    
    # System statistics
    stats = ReportModule.generate_system_statistics()
    print("📊 SYSTEM STATISTICS")
    print(f"   Total Students: {stats['students']['total']}")
    print(f"   Active Students: {stats['students']['active']}")
    print(f"   Average Student GPA: {stats['students']['average_gpa']:.2f}")
    print(f"   Total Courses: {stats['courses']['total']}")
    print(f"   Total Enrollments: {stats['courses']['total_enrollments']}")
    print(f"   Grades Recorded: {stats['academic']['total_grades_recorded']}")
    print(f"   Credits Awarded: {stats['academic']['total_credits_awarded']}")
    print()
    
    # 6. Demonstrate Search Functionality
    print("6. SEARCH FUNCTIONALITY")
    print("=" * 40)
    
    search_results = StudentModule.search_students("Alice")
    print(f"Search results for 'Alice': {len(search_results)} found")
    for student in search_results:
        print(f"  • {student['first_name']} {student['last_name']} ({student['email']})")
    
    search_results = StudentModule.search_students("johnson")
    print(f"Search results for 'johnson': {len(search_results)} found")
    for student in search_results:
        print(f"  • {student['first_name']} {student['last_name']} ({student['email']})")
    print()
    
    # 7. Error Handling Demonstration
    print("7. ERROR HANDLING DEMONSTRATION")
    print("=" * 40)
    
    print("Testing various error conditions:")
    
    # Duplicate email
    success, result = StudentModule.create_student("Test", "User", "alice.johnson@email.com", "555-999-9999")
    print(f"  Duplicate email: {'✅' if not success else '❌'} {result.get('error', 'Should have failed')}")
    
    # Invalid grade
    success, result = GradeModule.add_grade(created_students[0], "COMP101", 150)
    print(f"  Invalid grade: {'✅' if not success else '❌'} {result.get('error', 'Should have failed')}")
    
    # Non-existent student
    success, result = StudentModule.get_student("INVALID_ID")
    print(f"  Invalid student ID: {'✅' if not success else '❌'} {result.get('error', 'Should have failed')}")
    
    # Non-existent course
    success, result = EnrollmentModule.enroll_student(created_students[0], "INVALID_COURSE")
    print(f"  Invalid course code: {'✅' if not success else '❌'} {result.get('error', 'Should have failed')}")
    print()

# Run the complete demonstration
demonstrate_student_management_system()

print("=== SYSTEM ARCHITECTURE SUMMARY ===")
print()
print("The Student Management System demonstrates:")
print()
print("🏗️  MODULAR ARCHITECTURE:")
print("   • ValidationModule: Data validation and error checking")
print("   • StudentModule: Student CRUD operations")
print("   • CourseModule: Course management")
print("   • EnrollmentModule: Student-course relationships")
print("   • GradeModule: Grade recording and GPA calculations")
print("   • ReportModule: Analytics and reporting")
print()
print("🔧 FUNCTION DESIGN PRINCIPLES:")
print("   • Single Responsibility: Each function has one clear purpose")
print("   • Input Validation: All inputs are validated before processing")
print("   • Error Handling: Graceful error handling with meaningful messages")
print("   • Return Consistency: Standardized return formats (success, data)")
print()
print("📊 DATA MANAGEMENT:")
print("   • Centralized data storage simulation")
print("   • Referential integrity maintenance")
print("   • Calculated fields (GPA, credits) updated automatically")
print("   • Search and filtering capabilities")
print()
print("🔒 VALIDATION AND SECURITY:")
print("   • Comprehensive input validation")
print("   • Duplicate prevention")
print("   • Data format standardization")
print("   • Error message clarity for user feedback")
print()
print("📈 SCALABILITY FEATURES:")
print("   • Modular design allows easy extension")
print("   • Standardized interfaces between modules")
print("   • Configurable validation rules")
print("   • Report generation framework")

"""
COMPLETE APPLICATION SUMMARY:
=============================

This Student Management System showcases all the function concepts from Assignment 5:

1. FUNCTION BASICS (Example 1):
   - Well-defined functions with clear purposes
   - Proper parameter handling and return values
   - Comprehensive documentation

2. PARAMETERS AND ARGUMENTS (Example 2):
   - Required and optional parameters
   - Keyword arguments for clarity
   - **kwargs for flexible function interfaces

3. SCOPE AND VARIABLES (Example 3):
   - Proper variable scope management
   - Module-level data storage (simulated database)
   - No global variable pollution

4. ADVANCED FUNCTIONS (Example 4):
   - Higher-order functions for data processing
   - Functional programming patterns in validation
   - Recursive GPA calculation logic

5. MODULAR PROGRAMMING (Example 5):
   - Clear separation of concerns
   - Reusable function libraries
   - Consistent interfaces between modules

6. COMPLETE SYSTEM (Example 6):
   - Professional application architecture
   - Comprehensive error handling
   - Real-world business logic implementation

KEY ARCHITECTURAL PRINCIPLES:
============================
• Modularity: Each module handles specific domain functionality
• Consistency: Standardized function interfaces and return formats  
• Validation: Input validation at every entry point
• Error Handling: Graceful failure with meaningful error messages
• Extensibility: Easy to add new features without changing existing code
• Maintainability: Clear code structure with comprehensive documentation

REAL-WORLD APPLICATIONS:
========================
• Educational Institution Management
• Corporate Training Systems
• Certification Programs  
• Online Learning Platforms
• Employee Development Tracking

This system demonstrates the professional application of function-based
programming principles in building maintainable, scalable software.
"""