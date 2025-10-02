"""
Assignment 5 - Exercise 5: Modular Programming Project
Difficulty: 🔴 Expert

TODO: Create a complete grade management system using modular programming.

This comprehensive exercise requires organizing code into multiple functions
that work together to create a complete application.
"""

# ==================== DATA MANAGEMENT FUNCTIONS ====================

def create_student(name, student_id, grades=None):
    """
    Create a student dictionary.
    
    Requirements:
    - Return dictionary with keys: name, student_id, grades
    - grades should be an empty list if not provided
    
    Returns: {'name': str, 'student_id': str, 'grades': list}
    """
    # TODO: Implement this function
    pass


def add_grade(student, subject, score):
    """
    Add a grade to a student's record.
    
    Requirements:
    - Add a new grade dict to student's grades list
    - Grade format: {'subject': str, 'score': float}
    - Validate score is between 0-100
    - Return True if successful, False otherwise
    """
    # TODO: Implement this function
    pass


def calculate_student_average(student):
    """
    Calculate average of all student's grades.
    
    Requirements:
    - Return average as float
    - Return 0.0 if no grades
    - Round to 2 decimal places
    """
    # TODO: Implement this function
    pass


# ==================== SEARCH AND FILTER FUNCTIONS ====================

def find_student_by_id(students, student_id):
    """
    Find a student by their ID.
    
    Requirements:
    - Search through list of student dictionaries
    - Return student dict if found
    - Return None if not found
    """
    # TODO: Implement this function
    pass


def find_students_by_name(students, name):
    """
    Find all students with matching name (case-insensitive partial match).
    
    Requirements:
    - Return list of matching students
    - Support partial name matching
    - Case-insensitive search
    """
    # TODO: Implement this function
    pass


def get_top_students(students, n=5):
    """
    Get top n students by average grade.
    
    Requirements:
    - Calculate average for each student
    - Sort by average (descending)
    - Return top n students
    - Include average in results
    """
    # TODO: Implement this function
    pass


# ==================== STATISTICS FUNCTIONS ====================

def calculate_class_statistics(students):
    """
    Calculate class-wide statistics.
    
    Requirements:
    - Return dictionary with:
      * total_students: int
      * class_average: float
      * highest_average: float
      * lowest_average: float
      * total_grades: int
    """
    # TODO: Implement this function
    pass


def get_subject_statistics(students, subject):
    """
    Get statistics for a specific subject across all students.
    
    Requirements:
    - Find all grades for the subject
    - Return dictionary with:
      * subject: str
      * count: int (number of students with grade)
      * average: float
      * highest: float
      * lowest: float
    """
    # TODO: Implement this function
    pass


# ==================== DISPLAY FUNCTIONS ====================

def display_student(student):
    """
    Display formatted student information.
    
    Format:
    Student: Name (ID: 12345)
    Grades:
      - Math: 85
      - Science: 92
    Average: 88.50
    """
    # TODO: Implement this function
    pass


def display_class_roster(students):
    """
    Display formatted list of all students.
    
    Format:
    === CLASS ROSTER ===
    1. Alice Johnson (ID: 001) - Avg: 88.5
    2. Bob Smith (ID: 002) - Avg: 92.0
    ...
    Total Students: X
    """
    # TODO: Implement this function
    pass


def generate_report_card(student):
    """
    Generate a formatted report card for a student.
    
    Format:
    ═══════════════════════════════
           REPORT CARD
    ═══════════════════════════════
    Student: Name
    ID: 12345
    
    Subject          Score    Grade
    ─────────────────────────────
    Math             85       B
    Science          92       A
    ─────────────────────────────
    AVERAGE:         88.5     B+
    """
    # TODO: Implement this function
    # Hint: Use grade_letter helper function
    pass


# ==================== HELPER FUNCTIONS ====================

def grade_letter(score):
    """
    Convert numeric score to letter grade.
    
    Scale:
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F
    """
    # TODO: Implement this function
    pass


def validate_student_id(student_id):
    """
    Validate student ID format.
    
    Requirements:
    - Must be 3-6 characters
    - Can contain letters and numbers
    - Return (is_valid, message) tuple
    """
    # TODO: Implement this function
    pass


# ==================== MAIN PROGRAM ====================

def main():
    """
    Main program with interactive menu.
    
    Menu Options:
    1. Add new student
    2. Add grade to student
    3. View student details
    4. View class roster
    5. Generate report card
    6. View class statistics
    7. View subject statistics
    8. View top students
    9. Search students
    10. Exit
    """
    students = []  # Main data storage
    
    print("=== GRADE MANAGEMENT SYSTEM ===\n")
    
    # TODO: Implement menu loop
    # TODO: Handle each menu option
    # TODO: Call appropriate functions
    # TODO: Validate all inputs
    
    pass


# ==================== TEST DATA ====================

# Sample data for testing
SAMPLE_STUDENTS = [
    {
        'name': 'Alice Johnson',
        'student_id': '001',
        'grades': [
            {'subject': 'Math', 'score': 85},
            {'subject': 'Science', 'score': 92},
            {'subject': 'English', 'score': 88}
        ]
    },
    {
        'name': 'Bob Smith',
        'student_id': '002',
        'grades': [
            {'subject': 'Math', 'score': 78},
            {'subject': 'Science', 'score': 85},
            {'subject': 'English', 'score': 92}
        ]
    },
    {
        'name': 'Carol Davis',
        'student_id': '003',
        'grades': [
            {'subject': 'Math', 'score': 95},
            {'subject': 'Science', 'score': 89},
            {'subject': 'English', 'score': 91}
        ]
    }
]


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Grade Management System ===\n")
    
    # Test with sample data
    print("Test 1: Create Student")
    # student = create_student("John Doe", "004")
    # print(f"  Created: {student}")
    
    print("\nTest 2: Add Grade")
    # add_grade(student, "Math", 88)
    # print(f"  After adding grade: {student}")
    
    print("\nTest 3: Calculate Average")
    # avg = calculate_student_average(SAMPLE_STUDENTS[0])
    # print(f"  Alice's average: {avg}")
    
    print("\nTest 4: Class Statistics")
    # stats = calculate_class_statistics(SAMPLE_STUDENTS)
    # print(f"  Class stats: {stats}")
    
    print("\nTest 5: Display Student")
    # display_student(SAMPLE_STUDENTS[0])
    
    print("\nTo run the interactive system:")
    print("  Uncomment: main()")
    # main()
