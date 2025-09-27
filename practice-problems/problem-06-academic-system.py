"""
Practice Problem 06: Student Academic Management System
====================================================

DIFFICULTY: Advanced ⭐⭐⭐
CONCEPTS: 2D Arrays, Data Management, Statistical Analysis, Academic Processing
ASSIGNMENTS: All assignments (1-7) with focus on 6 (Arrays/Strings) and 7 (2D Arrays)
ESTIMATED TIME: 100-130 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive academic management system for tracking student performance,
grades, course enrollment, and generating academic reports. The system should handle
multiple students, courses, assignments, and provide detailed academic analytics.

This problem integrates multi-dimensional arrays, string processing, statistical
analysis, and educational data management to create a practical academic tool
used in real educational institutions.

REQUIREMENTS:
============
1. Manage student enrollment and course registration
2. Track assignments, exams, and grades across multiple courses
3. Calculate GPAs, class averages, and academic standings
4. Generate comprehensive academic reports and transcripts
5. Analyze student performance trends and patterns
6. Handle different grading scales and weight distributions
7. Provide academic alerts and recommendations
8. Support course scheduling and prerequisite checking

LEARNING OBJECTIVES:
===================
- Master complex 2D array operations and data structures
- Understand statistical analysis in educational contexts
- Practice advanced data validation and integrity checking
- Implement sophisticated reporting and analysis algorithms
- Design professional academic management interfaces
- Work with hierarchical data relationships

STARTER CODE:
============
"""

import random
import math
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from enum import Enum

class GradeScale(Enum):
    LETTER = "letter"  # A, B, C, D, F
    PERCENTAGE = "percentage"  # 0-100
    POINTS = "points"  # 0-4.0

class AcademicStatus(Enum):
    EXCELLENT = "excellent"  # GPA >= 3.7
    GOOD = "good"  # GPA >= 3.0
    SATISFACTORY = "satisfactory"  # GPA >= 2.0
    PROBATION = "probation"  # GPA < 2.0
    
class Student:
    """Represents a student in the academic system."""
    
    def __init__(self, student_id: str, name: str, email: str, major: str, year: int):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.major = major
        self.year = year
        self.enrolled_courses = {}  # course_id -> enrollment_info
        self.academic_history = []  # List of completed courses
        self.current_gpa = 0.0
        self.cumulative_gpa = 0.0
        self.total_credits = 0
        self.enrollment_date = datetime.now().strftime("%Y-%m-%d")

class Course:
    """Represents an academic course."""
    
    def __init__(self, course_id: str, name: str, instructor: str, 
                 credits: int, max_capacity: int = 30):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
        self.credits = credits
        self.max_capacity = max_capacity
        self.enrolled_students = {}  # student_id -> student_data
        self.assignments = {}  # assignment_id -> assignment_data
        self.grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        self.course_average = 0.0

class Assignment:
    """Represents a course assignment or exam."""
    
    def __init__(self, assignment_id: str, name: str, course_id: str,
                 max_points: float, weight: float, due_date: str,
                 assignment_type: str = "assignment"):
        self.assignment_id = assignment_id
        self.name = name
        self.course_id = course_id
        self.max_points = max_points
        self.weight = weight  # Weight in final grade calculation
        self.due_date = due_date
        self.type = assignment_type  # assignment, exam, project, quiz
        self.submissions = {}  # student_id -> grade

class AcademicManagementSystem:
    """Comprehensive student academic management system."""
    
    def __init__(self):
        """Initialize the academic management system."""
        self.students = {}  # student_id -> Student object
        self.courses = {}   # course_id -> Course object
        self.assignments = {}  # assignment_id -> Assignment object
        self.semesters = {}  # semester_id -> semester_data
        
        # Grade conversion tables
        self.letter_to_gpa = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
        self.percentage_to_letter = {
            90: "A", 80: "B", 70: "C", 60: "D", 0: "F"
        }
        
        # Academic constants
        self.min_passing_grade = 60.0
        self.probation_gpa = 2.0
        self.honors_gpa = 3.5
        
        # Initialize with sample data
        self.initialize_sample_data()
    
    def initialize_sample_data(self):
        """Initialize system with sample students, courses, and assignments."""
        # Sample courses
        courses_data = [
            ("CS101", "Introduction to Programming", "Dr. Smith", 4),
            ("MATH201", "Calculus I", "Prof. Johnson", 4),
            ("ENG101", "English Composition", "Dr. Brown", 3),
            ("PHYS101", "General Physics", "Prof. Wilson", 4),
            ("HIST101", "World History", "Dr. Davis", 3),
            ("CHEM101", "General Chemistry", "Prof. Miller", 4),
            ("CS102", "Data Structures", "Dr. Smith", 4),
            ("MATH202", "Calculus II", "Prof. Johnson", 4)
        ]
        
        for course_id, name, instructor, credits in courses_data:
            self.courses[course_id] = Course(course_id, name, instructor, credits)
        
        # Sample students
        students_data = [
            ("S001", "Alice Johnson", "alice@university.edu", "Computer Science", 2),
            ("S002", "Bob Smith", "bob@university.edu", "Mathematics", 1),
            ("S003", "Charlie Brown", "charlie@university.edu", "Physics", 3),
            ("S004", "Diana Prince", "diana@university.edu", "Chemistry", 2),
            ("S005", "Edward Norton", "edward@university.edu", "Computer Science", 4),
            ("S006", "Fiona Green", "fiona@university.edu", "English", 1),
            ("S007", "George Wilson", "george@university.edu", "History", 3),
            ("S008", "Hannah Davis", "hannah@university.edu", "Computer Science", 2)
        ]
        
        for student_id, name, email, major, year in students_data:
            self.students[student_id] = Student(student_id, name, email, major, year)
        
        # Enroll students in courses
        self.create_sample_enrollments()
        
        # Create sample assignments
        self.create_sample_assignments()
        
        # Generate sample grades
        self.generate_sample_grades()
    
    def create_sample_enrollments(self):
        """Create realistic course enrollments for sample data."""
        enrollment_patterns = {
            1: ["CS101", "MATH201", "ENG101", "PHYS101"],  # Freshman
            2: ["CS102", "MATH202", "PHYS101", "HIST101"],  # Sophomore
            3: ["CS102", "CHEM101", "HIST101"],  # Junior
            4: ["CHEM101", "HIST101"]  # Senior
        }
        
        for student in self.students.values():
            courses_for_year = enrollment_patterns.get(student.year, ["CS101", "ENG101"])
            
            # Enroll student in appropriate courses
            for course_id in courses_for_year[:random.randint(3, 4)]:
                if course_id in self.courses:
                    self.enroll_student_in_course(student.student_id, course_id)
    
    def enroll_student_in_course(self, student_id: str, course_id: str):
        """Enroll a student in a course."""
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            
            # Check capacity
            if len(course.enrolled_students) >= course.max_capacity:
                return False
            
            # Enroll student
            student.enrolled_courses[course_id] = {
                'enrollment_date': datetime.now().strftime("%Y-%m-%d"),
                'status': 'active'
            }
            
            course.enrolled_students[student_id] = {
                'student_name': student.name,
                'enrollment_date': datetime.now().strftime("%Y-%m-%d"),
                'grades': {}
            }
            return True
        return False
    
    def create_sample_assignments(self):
        """Create sample assignments for each course."""
        assignment_types = [
            ("Quiz", 100, 0.10, "quiz"),
            ("Assignment", 100, 0.15, "assignment"),
            ("Midterm Exam", 100, 0.25, "exam"),
            ("Project", 100, 0.20, "project"),
            ("Final Exam", 100, 0.30, "exam")
        ]
        
        assignment_counter = 1
        
        for course_id, course in self.courses.items():
            for i, (name, max_points, weight, assign_type) in enumerate(assignment_types):
                assignment_id = f"A{assignment_counter:03d}"
                assignment_name = f"{name} {i+1}" if assign_type in ["quiz", "assignment"] else name
                
                due_date = (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d")
                
                assignment = Assignment(
                    assignment_id, assignment_name, course_id,
                    max_points, weight, due_date, assign_type
                )
                
                self.assignments[assignment_id] = assignment
                course.assignments[assignment_id] = assignment
                assignment_counter += 1
    
    def generate_sample_grades(self):
        """Generate realistic sample grades for all assignments."""
        for assignment in self.assignments.values():
            course = self.courses[assignment.course_id]
            
            for student_id in course.enrolled_students.keys():
                # Generate realistic grade based on assignment type and student performance
                if assignment.type == "quiz":
                    grade = random.uniform(70, 100)
                elif assignment.type == "assignment":
                    grade = random.uniform(75, 95)
                elif assignment.type == "exam":
                    grade = random.uniform(60, 90)
                elif assignment.type == "project":
                    grade = random.uniform(80, 95)
                else:
                    grade = random.uniform(65, 90)
                
                assignment.submissions[student_id] = min(grade, assignment.max_points)
        
        # Calculate course grades and GPAs
        self.calculate_all_grades()
    
    def display_main_menu(self):
        """Display the main menu options."""
        print("=" * 70)
        print("              STUDENT ACADEMIC MANAGEMENT SYSTEM")
        print("=" * 70)
        print("1. Student Management")
        print("2. Course Management") 
        print("3. Assignment & Grading")
        print("4. Academic Reports")
        print("5. Grade Analysis & Statistics")
        print("6. Student Performance Tracking")
        print("7. Course Enrollment Management")
        print("8. Academic Alerts & Notifications")
        print("9. System Analytics")
        print("10. Data Export & Reports")
        print("0. Exit")
        print("=" * 70)
    
    def get_menu_choice(self):
        """Get and validate user's menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (0-10): "))
                if 0 <= choice <= 10:
                    return choice
                else:
                    print("❌ Please enter a number between 0 and 10.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def student_management(self):
        """Student management functionality."""
        print("\n👨‍🎓 STUDENT MANAGEMENT")
        print("-" * 30)
        
        print("1. View All Students")
        print("2. Student Details & Profile")
        print("3. Add New Student")
        print("4. Update Student Information")
        print("5. Student Academic Standing")
        print("6. Student Course History")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.view_all_students()
            elif choice == 2:
                self.view_student_details()
            elif choice == 3:
                self.add_new_student()
            elif choice == 4:
                self.update_student_info()
            elif choice == 5:
                self.view_academic_standing()
            elif choice == 6:
                self.view_student_history()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_all_students(self):
        """Display overview of all students."""
        print("\n📊 ALL STUDENTS OVERVIEW")
        print("-" * 40)
        
        if not self.students:
            print("❌ No students found in the system!")
            return
        
        print(f"Total Students: {len(self.students)}")
        print()
        
        # Calculate overall statistics
        total_gpa = sum(student.current_gpa for student in self.students.values())
        avg_gpa = total_gpa / len(self.students) if self.students else 0
        
        print(f"System-wide Average GPA: {avg_gpa:.2f}")
        print()
        
        # Display student table
        print(f"{'ID':<6} {'Name':<20} {'Major':<15} {'Year':<4} {'GPA':<5} {'Status'}")
        print("-" * 70)
        
        # Sort students by GPA (descending)
        sorted_students = sorted(self.students.values(), 
                               key=lambda s: s.current_gpa, reverse=True)
        
        for student in sorted_students:
            status = self.determine_academic_status(student.current_gpa)
            status_emoji = {"excellent": "🏆", "good": "✅", "satisfactory": "📚", "probation": "⚠️"}
            
            print(f"{student.student_id:<6} {student.name:<20} {student.major:<15} "
                  f"{student.year:<4} {student.current_gpa:<5.2f} "
                  f"{status_emoji.get(status.value, '📚')} {status.value.title()}")
        
        # Show distribution by academic status
        self.show_academic_status_distribution()
    
    def determine_academic_status(self, gpa: float) -> AcademicStatus:
        """Determine academic status based on GPA."""
        if gpa >= 3.7:
            return AcademicStatus.EXCELLENT
        elif gpa >= 3.0:
            return AcademicStatus.GOOD
        elif gpa >= 2.0:
            return AcademicStatus.SATISFACTORY
        else:
            return AcademicStatus.PROBATION
    
    def show_academic_status_distribution(self):
        """Show distribution of students by academic status."""
        print(f"\n📈 ACADEMIC STATUS DISTRIBUTION")
        print("-" * 35)
        
        status_counts = {"excellent": 0, "good": 0, "satisfactory": 0, "probation": 0}
        
        for student in self.students.values():
            status = self.determine_academic_status(student.current_gpa)
            status_counts[status.value] += 1
        
        total = len(self.students)
        
        for status, count in status_counts.items():
            percentage = (count / total * 100) if total > 0 else 0
            print(f"{status.title():<15}: {count:>3} students ({percentage:>5.1f}%)")
    
    def view_student_details(self):
        """Display detailed information about a specific student."""
        print("\n👤 STUDENT DETAILS")
        print("-" * 25)
        
        if not self.students:
            print("❌ No students in the system!")
            return
        
        # List students for selection
        students_list = list(self.students.values())
        print("Select a student:")
        for i, student in enumerate(students_list, 1):
            print(f"{i}. {student.name} ({student.student_id})")
        
        try:
            choice = int(input(f"Enter choice (1-{len(students_list)}): ")) - 1
            
            if 0 <= choice < len(students_list):
                student = students_list[choice]
                self.display_comprehensive_student_profile(student)
            else:
                print("❌ Invalid selection!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def display_comprehensive_student_profile(self, student: Student):
        """Display comprehensive profile for a student."""
        print(f"\n📋 COMPREHENSIVE PROFILE: {student.name}")
        print("=" * 60)
        
        # Basic Information
        print("🎓 BASIC INFORMATION")
        print("-" * 25)
        print(f"Student ID: {student.student_id}")
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")
        print(f"Major: {student.major}")
        print(f"Academic Year: {student.year}")
        print(f"Enrollment Date: {student.enrollment_date}")
        
        # Academic Performance
        print(f"\n📊 ACADEMIC PERFORMANCE")
        print("-" * 30)
        print(f"Current GPA: {student.current_gpa:.2f}")
        print(f"Cumulative GPA: {student.cumulative_gpa:.2f}")
        print(f"Total Credits: {student.total_credits}")
        
        academic_status = self.determine_academic_status(student.current_gpa)
        status_emoji = {"excellent": "🏆", "good": "✅", "satisfactory": "📚", "probation": "⚠️"}
        print(f"Academic Status: {status_emoji.get(academic_status.value, '📚')} {academic_status.value.title()}")
        
        # Current Enrollments
        print(f"\n📚 CURRENT ENROLLMENTS")
        print("-" * 30)
        
        if student.enrolled_courses:
            print(f"{'Course ID':<10} {'Course Name':<25} {'Credits':<7} {'Current Grade'}")
            print("-" * 60)
            
            for course_id in student.enrolled_courses:
                if course_id in self.courses:
                    course = self.courses[course_id]
                    current_grade = self.calculate_student_course_grade(student.student_id, course_id)
                    letter_grade = self.percentage_to_letter_grade(current_grade)
                    
                    print(f"{course_id:<10} {course.name:<25} {course.credits:<7} "
                          f"{current_grade:>5.1f}% ({letter_grade})")
        else:
            print("No current course enrollments")
        
        # Course-by-Course Breakdown
        self.show_student_course_breakdown(student)
        
        # Performance Analytics
        self.show_student_performance_analytics(student)
    
    def calculate_student_course_grade(self, student_id: str, course_id: str) -> float:
        """Calculate a student's current grade in a specific course."""
        if course_id not in self.courses:
            return 0.0
        
        course = self.courses[course_id]
        total_weighted_score = 0.0
        total_weight = 0.0
        
        for assignment in course.assignments.values():
            if student_id in assignment.submissions:
                score = assignment.submissions[student_id]
                percentage = (score / assignment.max_points) * 100
                weighted_score = percentage * assignment.weight
                total_weighted_score += weighted_score
                total_weight += assignment.weight
        
        return total_weighted_score / total_weight if total_weight > 0 else 0.0
    
    def percentage_to_letter_grade(self, percentage: float) -> str:
        """Convert percentage grade to letter grade."""
        if percentage >= 90:
            return "A"
        elif percentage >= 80:
            return "B"
        elif percentage >= 70:
            return "C"
        elif percentage >= 60:
            return "D"
        else:
            return "F"
    
    def show_student_course_breakdown(self, student: Student):
        """Show detailed breakdown of student's performance in each course."""
        print(f"\n📝 DETAILED COURSE BREAKDOWN")
        print("-" * 35)
        
        for course_id in student.enrolled_courses:
            if course_id in self.courses:
                course = self.courses[course_id]
                print(f"\n📚 {course.name} ({course_id})")
                print("-" * 40)
                
                # Show assignment grades
                assignments_in_course = [a for a in self.assignments.values() 
                                       if a.course_id == course_id]
                
                if assignments_in_course:
                    print(f"{'Assignment':<20} {'Type':<12} {'Score':<10} {'Grade'}")
                    print("-" * 55)
                    
                    for assignment in assignments_in_course:
                        if student.student_id in assignment.submissions:
                            score = assignment.submissions[student.student_id]
                            percentage = (score / assignment.max_points) * 100
                            letter = self.percentage_to_letter_grade(percentage)
                            
                            print(f"{assignment.name:<20} {assignment.type:<12} "
                                  f"{score:>4.1f}/{assignment.max_points:<3.0f} {letter}")
                    
                    # Calculate course grade
                    course_grade = self.calculate_student_course_grade(student.student_id, course_id)
                    letter_grade = self.percentage_to_letter_grade(course_grade)
                    print("-" * 55)
                    print(f"{'COURSE TOTAL':<20} {'Overall':<12} "
                          f"{course_grade:>6.1f}% {letter_grade}")
    
    def show_student_performance_analytics(self, student: Student):
        """Show performance analytics and trends for a student."""
        print(f"\n📈 PERFORMANCE ANALYTICS")
        print("-" * 30)
        
        # Collect all grades for analysis
        all_grades = []
        grade_by_type = {"quiz": [], "assignment": [], "exam": [], "project": []}
        
        for course_id in student.enrolled_courses:
            if course_id in self.courses:
                course = self.courses[course_id]
                for assignment in course.assignments.values():
                    if student.student_id in assignment.submissions:
                        score = assignment.submissions[student.student_id]
                        percentage = (score / assignment.max_points) * 100
                        all_grades.append(percentage)
                        grade_by_type[assignment.type].append(percentage)
        
        if all_grades:
            avg_grade = sum(all_grades) / len(all_grades)
            print(f"Overall Average: {avg_grade:.1f}%")
            print(f"Highest Grade: {max(all_grades):.1f}%")
            print(f"Lowest Grade: {min(all_grades):.1f}%")
            
            # Standard deviation calculation
            variance = sum((grade - avg_grade) ** 2 for grade in all_grades) / len(all_grades)
            std_dev = math.sqrt(variance)
            print(f"Grade Consistency (Std Dev): {std_dev:.1f}")
            
            # Performance by assignment type
            print(f"\n📊 Performance by Assignment Type:")
            for assign_type, grades in grade_by_type.items():
                if grades:
                    type_avg = sum(grades) / len(grades)
                    print(f"  {assign_type.title()}: {type_avg:.1f}% (n={len(grades)})")
            
            # Performance recommendations
            self.generate_student_recommendations(student, all_grades, grade_by_type)
        else:
            print("No grade data available for analysis")
    
    def generate_student_recommendations(self, student: Student, all_grades: List[float], 
                                       grade_by_type: Dict[str, List[float]]):
        """Generate personalized academic recommendations for a student."""
        print(f"\n💡 ACADEMIC RECOMMENDATIONS")
        print("-" * 35)
        
        avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0
        
        recommendations = []
        
        # GPA-based recommendations
        if student.current_gpa < 2.0:
            recommendations.append("🚨 Priority: Meet with academic advisor immediately")
            recommendations.append("📚 Consider tutoring services for struggling courses")
        elif student.current_gpa < 3.0:
            recommendations.append("📈 Focus on improving study habits and time management")
            recommendations.append("🎯 Set specific grade targets for each course")
        elif student.current_gpa >= 3.5:
            recommendations.append("🏆 Excellent work! Consider honors courses or research opportunities")
        
        # Assignment type performance recommendations
        for assign_type, grades in grade_by_type.items():
            if grades:
                type_avg = sum(grades) / len(grades)
                if type_avg < 70:
                    recommendations.append(f"⚠️ {assign_type.title()} performance needs improvement")
                elif type_avg >= 90:
                    recommendations.append(f"✅ Excellent {assign_type} performance!")
        
        # Grade consistency recommendations
        if len(all_grades) > 3:
            avg_grade = sum(all_grades) / len(all_grades)
            variance = sum((grade - avg_grade) ** 2 for grade in all_grades) / len(all_grades)
            std_dev = math.sqrt(variance)
            
            if std_dev > 15:
                recommendations.append("📊 Work on consistency - grades vary significantly")
            elif std_dev < 5:
                recommendations.append("🎯 Very consistent performance - well done!")
        
        # Display recommendations
        for i, rec in enumerate(recommendations[:6], 1):  # Limit to 6 recommendations
            print(f"{i}. {rec}")
        
        if not recommendations:
            print("Continue current study habits - performance is on track!")
    
    def calculate_all_grades(self):
        """Calculate grades and GPAs for all students."""
        for student in self.students.values():
            total_grade_points = 0.0
            total_credits = 0
            
            for course_id in student.enrolled_courses:
                if course_id in self.courses:
                    course = self.courses[course_id]
                    course_grade = self.calculate_student_course_grade(student.student_id, course_id)
                    letter_grade = self.percentage_to_letter_grade(course_grade)
                    gpa_points = self.letter_to_gpa[letter_grade]
                    
                    total_grade_points += gpa_points * course.credits
                    total_credits += course.credits
            
            if total_credits > 0:
                student.current_gpa = total_grade_points / total_credits
                student.cumulative_gpa = student.current_gpa  # Simplified for this example
                student.total_credits = total_credits
    
    def course_management(self):
        """Course management functionality."""
        print("\n📚 COURSE MANAGEMENT")
        print("-" * 25)
        
        print("1. View All Courses")
        print("2. Course Details & Enrollment")
        print("3. Add New Course")
        print("4. Update Course Information")
        print("5. Course Performance Analysis")
        print("6. Instructor Analytics")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.view_all_courses()
            elif choice == 2:
                self.view_course_details()
            elif choice == 3:
                self.add_new_course()
            elif choice == 4:
                print("🚧 Update course feature coming soon!")
            elif choice == 5:
                self.course_performance_analysis()
            elif choice == 6:
                print("🚧 Instructor analytics feature coming soon!")
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_all_courses(self):
        """Display overview of all courses."""
        print("\n📊 ALL COURSES OVERVIEW")
        print("-" * 35)
        
        if not self.courses:
            print("❌ No courses found in the system!")
            return
        
        print(f"Total Courses: {len(self.courses)}")
        print()
        
        print(f"{'Course ID':<10} {'Course Name':<25} {'Instructor':<15} {'Credits':<7} {'Enrolled':<8} {'Avg Grade'}")
        print("-" * 85)
        
        for course in self.courses.values():
            enrolled_count = len(course.enrolled_students)
            
            # Calculate course average
            all_grades = []
            for student_id in course.enrolled_students:
                grade = self.calculate_student_course_grade(student_id, course.course_id)
                if grade > 0:
                    all_grades.append(grade)
            
            avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0
            
            print(f"{course.course_id:<10} {course.name:<25} {course.instructor:<15} "
                  f"{course.credits:<7} {enrolled_count:<8} {avg_grade:>6.1f}%")
        
        # Show enrollment statistics
        self.show_enrollment_statistics()
    
    def show_enrollment_statistics(self):
        """Show enrollment statistics across all courses."""
        print(f"\n📈 ENROLLMENT STATISTICS")
        print("-" * 30)
        
        total_enrollments = sum(len(course.enrolled_students) for course in self.courses.values())
        avg_class_size = total_enrollments / len(self.courses) if self.courses else 0
        
        print(f"Total Enrollments: {total_enrollments}")
        print(f"Average Class Size: {avg_class_size:.1f} students")
        
        # Find most and least popular courses
        if self.courses:
            most_popular = max(self.courses.values(), key=lambda c: len(c.enrolled_students))
            least_popular = min(self.courses.values(), key=lambda c: len(c.enrolled_students))
            
            print(f"Most Popular: {most_popular.name} ({len(most_popular.enrolled_students)} students)")
            print(f"Least Popular: {least_popular.name} ({len(least_popular.enrolled_students)} students)")
    
    def assignment_grading(self):
        """Assignment and grading management."""
        print("\n📝 ASSIGNMENT & GRADING")
        print("-" * 30)
        
        print("1. View All Assignments")
        print("2. Create New Assignment")
        print("3. Grade Assignment")
        print("4. Assignment Statistics")
        print("5. Grade Distribution Analysis")
        print("6. Missing Assignments Report")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.view_all_assignments()
            elif choice == 2:
                print("🚧 Create assignment feature coming soon!")
            elif choice == 3:
                print("🚧 Grade assignment feature coming soon!")
            elif choice == 4:
                self.assignment_statistics()
            elif choice == 5:
                self.grade_distribution_analysis()
            elif choice == 6:
                print("🚧 Missing assignments report coming soon!")
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_all_assignments(self):
        """Display overview of all assignments."""
        print("\n📋 ALL ASSIGNMENTS OVERVIEW")
        print("-" * 40)
        
        if not self.assignments:
            print("❌ No assignments found!")
            return
        
        print(f"{'Assignment ID':<12} {'Name':<20} {'Course':<10} {'Type':<12} {'Due Date':<12} {'Avg Score'}")
        print("-" * 85)
        
        for assignment in self.assignments.values():
            # Calculate average score
            scores = list(assignment.submissions.values())
            avg_score = sum(scores) / len(scores) if scores else 0
            avg_percentage = (avg_score / assignment.max_points * 100) if assignment.max_points > 0 else 0
            
            print(f"{assignment.assignment_id:<12} {assignment.name:<20} {assignment.course_id:<10} "
                  f"{assignment.type:<12} {assignment.due_date:<12} {avg_percentage:>6.1f}%")
    
    def run(self):
        """Main program loop."""
        print("🎓 Welcome to the Student Academic Management System!")
        print("Comprehensive tools for managing student performance and academic records.")
        
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n🎓 Thank you for using the Academic Management System!")
                print("Excellence in education through effective management!")
                break
            elif choice == 1:
                self.student_management()
            elif choice == 2:
                self.course_management()
            elif choice == 3:
                self.assignment_grading()
            elif choice == 4:
                print("🚧 Academic reports feature coming soon!")
            elif choice == 5:
                print("🚧 Grade analysis feature coming soon!")
            elif choice == 6:
                print("🚧 Performance tracking feature coming soon!")
            elif choice == 7:
                print("🚧 Enrollment management feature coming soon!")
            elif choice == 8:
                print("🚧 Academic alerts feature coming soon!")
            elif choice == 9:
                print("🚧 System analytics feature coming soon!")
            elif choice == 10:
                print("🚧 Data export feature coming soon!")
            
            print("\n" + "=" * 70)
            input("Press Enter to continue...")

def main():
    """Main entry point for the program."""
    academic_system = AcademicManagementSystem()
    academic_system.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Complex 2D array operations for grade management
2. ✅ Comprehensive student and course data structures
3. ✅ Advanced statistical analysis and reporting
4. ✅ Professional academic management interface
5. ✅ Multi-dimensional data relationships handling
6. ✅ Educational analytics and insights generation
7. ✅ Academic performance tracking and recommendations
8. ✅ Realistic academic data modeling and processing

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Complex multi-dimensional array operations and management
• Advanced object-oriented design with real-world relationships
• Statistical analysis and educational data processing
• Professional system architecture and data integrity
• Academic calculation algorithms and grading systems
• User interface design for institutional software
• Performance analytics and recommendation systems
• Large-scale data structure optimization and management

EXTENSION IDEAS:
===============
1. Add semester/term management with historical data
2. Implement prerequisite checking and course planning
3. Create advanced analytics dashboards and visualizations  
4. Add parent/guardian access and communication features
5. Implement automated degree audit and graduation tracking
6. Add integration with learning management systems
7. Create predictive modeling for student success
8. Add financial aid and scholarship management

This problem provides comprehensive practice with 2D arrays, complex
data structures, and educational software design while creating a
genuinely useful academic management system!
"""