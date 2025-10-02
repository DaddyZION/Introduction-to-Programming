"""
Assignment 6 - Exercise 5: Grade Book Analyzer
Difficulty: 🟡 Intermediate

TODO: Create a grade book system that manages students and their test scores.

Requirements:
1. Store student names and their test scores
2. Calculate average score for each student
3. Find the class average
4. Identify top and bottom performers
5. Generate a simple report
"""

# Data structure: Dictionary where keys are student names, values are lists of scores
# Example: {'Alice': [85, 90, 88], 'Bob': [78, 82, 85]}


# ==================== FUNCTION 1: Add Student ====================
def add_student(gradebook, name, scores=None):
    """
    Add a new student to the gradebook.
    
    Requirements:
    - Add student with empty score list if scores not provided
    - If student already exists, return False
    - Otherwise add and return True
    
    Parameters:
    - gradebook: dictionary
    - name: string
    - scores: list of numbers (optional)
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Add Score ====================
def add_score(gradebook, name, score):
    """
    Add a score for an existing student.
    
    Requirements:
    - Validate score is between 0-100
    - Add score to student's list
    - Return True if successful, False if student not found or invalid score
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Calculate Student Average ====================
def calculate_student_average(scores):
    """
    Calculate average of scores list.
    
    Returns: float (0.0 if no scores)
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Get All Averages ====================
def get_all_averages(gradebook):
    """
    Calculate average for each student.
    
    Returns: dictionary mapping names to averages
    Example: {'Alice': 87.67, 'Bob': 81.67}
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Calculate Class Average ====================
def calculate_class_average(gradebook):
    """
    Calculate the overall class average.
    
    Returns: float
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Find Top Performer ====================
def find_top_performer(gradebook):
    """
    Find student with highest average.
    
    Returns: (name, average) tuple
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 7: Find Bottom Performer ====================
def find_bottom_performer(gradebook):
    """
    Find student with lowest average.
    
    Returns: (name, average) tuple
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 8: Get Grade Distribution ====================
def get_grade_distribution(gradebook):
    """
    Count how many students in each grade range.
    
    Ranges:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
    
    Returns: dictionary with counts
    Example: {'A': 2, 'B': 3, 'C': 1, 'D': 0, 'F': 0}
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 9: Generate Report ====================
def generate_report(gradebook):
    """
    Generate a formatted grade report.
    
    Format:
    === GRADE BOOK REPORT ===
    
    Student Averages:
    1. Alice: 87.67 (B)
    2. Bob: 81.67 (B)
    3. Carol: 92.33 (A)
    
    Class Statistics:
    Class Average: 87.22
    Top Performer: Carol (92.33)
    Bottom Performer: Bob (81.67)
    
    Grade Distribution:
    A: 1 student(s)
    B: 2 student(s)
    C: 0 student(s)
    D: 0 student(s)
    F: 0 student(s)
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 10: Import Grades from String ====================
def import_grades_from_csv(csv_string):
    """
    Import grades from a CSV-formatted string.
    
    Format: "Name,Score1,Score2,Score3"
    Example: "Alice,85,90,88\nBob,78,82,85"
    
    Returns: gradebook dictionary
    """
    # TODO: Implement this function
    pass


# ==================== MAIN PROGRAM ====================
def main():
    """
    Interactive gradebook manager.
    
    Menu:
    1. Add student
    2. Add score for student
    3. View all students
    4. View student details
    5. Generate report
    6. Exit
    """
    gradebook = {}
    
    print("=== Grade Book Manager ===\n")
    
    # TODO: Implement menu loop
    
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    # Test with sample data
    test_gradebook = {
        'Alice': [85, 90, 88, 92],
        'Bob': [78, 82, 85, 80],
        'Carol': [92, 95, 90, 93],
        'David': [88, 85, 87, 90]
    }
    
    print("Testing Grade Book Analyzer:\n")
    
    print("Test 1: Calculate averages")
    # averages = get_all_averages(test_gradebook)
    # print(f"  Student averages: {averages}")
    
    print("\nTest 2: Class average")
    # class_avg = calculate_class_average(test_gradebook)
    # print(f"  Class average: {class_avg:.2f}")
    
    print("\nTest 3: Top/Bottom performers")
    # top = find_top_performer(test_gradebook)
    # bottom = find_bottom_performer(test_gradebook)
    # print(f"  Top: {top[0]} ({top[1]:.2f})")
    # print(f"  Bottom: {bottom[0]} ({bottom[1]:.2f})")
    
    print("\nTest 4: Grade distribution")
    # distribution = get_grade_distribution(test_gradebook)
    # print(f"  Distribution: {distribution}")
    
    print("\nTest 5: Generate report")
    # generate_report(test_gradebook)
    
    print("\nTo run interactive program:")
    print("  Uncomment: main()")
    # main()
