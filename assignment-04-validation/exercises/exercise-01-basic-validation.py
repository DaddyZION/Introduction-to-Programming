"""
Assignment 4 - Exercise 1: Basic Validation Functions
Difficulty: 🟢 Beginner

TODO: Implement basic validation functions for common data types.

This exercise contains 4 validation functions to practice basic validation logic.
"""

# ==================== FUNCTION 1: Student Grade Validation ====================
def validate_student_grade(grade):
    """
    Validate a student grade entry.
    
    Requirements:
    - Grade must be a number (int or float)
    - Grade must be between 0 and 100 (inclusive)
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_student_grade(85) → (True, "Valid grade: 85")
    - validate_student_grade(-5) → (False, "Grade cannot be negative")
    - validate_student_grade(105) → (False, "Grade cannot exceed 100")
    - validate_student_grade("abc") → (False, "Grade must be a number")
    """
    # TODO: Implement this function
    # Hint: Check type first using isinstance(), then check range
    pass


# ==================== FUNCTION 2: Age Validation ====================
def validate_age(age):
    """
    Validate an age input.
    
    Requirements:
    - Age must be an integer
    - Age must be between 0 and 150
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_age(25) → (True, "Valid age")
    - validate_age(-5) → (False, "Age cannot be negative")
    - validate_age(200) → (False, "Age must be realistic (0-150)")
    - validate_age(25.5) → (False, "Age must be a whole number")
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Phone Number Validation ====================
def validate_phone_number(phone):
    """
    Validate a phone number (basic format).
    
    Requirements:
    - Must be a string
    - Must be exactly 10 digits after removing dashes and spaces
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_phone_number("123-456-7890") → (True, "Valid phone number")
    - validate_phone_number("1234567890") → (True, "Valid phone number")
    - validate_phone_number("123-456") → (False, "Phone must be 10 digits")
    - validate_phone_number("abc-def-ghij") → (False, "Phone must contain only digits")
    """
    # TODO: Implement this function
    # Hint: Remove dashes and spaces, then check if remaining string is digits
    pass


# ==================== FUNCTION 4: Positive Number Validation ====================
def validate_positive_number(number):
    """
    Validate that a number is positive.
    
    Requirements:
    - Must be a number (int or float)
    - Must be greater than 0
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_positive_number(5) → (True, "Valid positive number")
    - validate_positive_number(-3) → (False, "Number must be positive")
    - validate_positive_number(0) → (False, "Number must be greater than zero")
    """
    # TODO: Implement this function
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Basic Validation Functions ===\n")
    
    # Test validate_student_grade
    print("Test 1: Student Grade Validation")
    test_grades = [85, -5, 105, "abc", 0, 100, 75.5]
    for grade in test_grades:
        result = validate_student_grade(grade)
        print(f"  Grade {grade}: {result}")
    
    print("\nTest 2: Age Validation")
    test_ages = [25, -5, 200, 25.5, 0, 150]
    for age in test_ages:
        result = validate_age(age)
        print(f"  Age {age}: {result}")
    
    print("\nTest 3: Phone Number Validation")
    test_phones = ["123-456-7890", "1234567890", "123-456", "abc-def-ghij"]
    for phone in test_phones:
        result = validate_phone_number(phone)
        print(f"  Phone '{phone}': {result}")
    
    print("\nTest 4: Positive Number Validation")
    test_numbers = [5, -3, 0, 100.5, "text"]
    for num in test_numbers:
        result = validate_positive_number(num)
        print(f"  Number {num}: {result}")
