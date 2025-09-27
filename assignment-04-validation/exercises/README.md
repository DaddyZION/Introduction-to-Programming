"""
Assignment 4 - Validation and Input Handling Exercises
=======================================================

This file contains practice exercises to reinforce validation concepts.
Complete each exercise by implementing the required validation functions.
Test your solutions with the provided test cases.

Learning Objectives:
- Apply basic validation techniques
- Implement type and format validation
- Handle edge cases and error conditions
- Create user-friendly error messages
- Build comprehensive validation systems
"""

print("=== VALIDATION EXERCISES ===")
print("Complete the following exercises to practice validation techniques.")
print()

# EXERCISE 1: BASIC STUDENT GRADE VALIDATION
print("EXERCISE 1: Student Grade Validation")
print("=====================================")

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
    # Hint: Check type, then check range
    pass

# Test Exercise 1
print("Testing Exercise 1:")
test_grades = [85, -5, 105, "abc", 0, 100, 75.5, None]

for grade in test_grades:
    try:
        is_valid, message = validate_student_grade(grade)
        status = "✅" if is_valid else "❌"
        print(f"  Grade {grade}: {status} {message}")
    except Exception as e:
        print(f"  Grade {grade}: ❌ Error: {e}")

print()

# EXERCISE 2: USERNAME VALIDATION
print("EXERCISE 2: Username Validation")
print("===============================")

def validate_username(username):
    """
    Validate a username for account creation.
    
    Requirements:
    - Must be a string
    - Length between 3 and 20 characters
    - Can contain letters, numbers, and underscores only
    - Cannot start with a number
    - Cannot be in list of reserved names: ['admin', 'root', 'user', 'test']
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_username("john_doe") → (True, "Username is valid")
    - validate_username("ab") → (False, "Username too short (minimum 3 characters)")
    - validate_username("admin") → (False, "Username is reserved")
    - validate_username("2fast") → (False, "Username cannot start with number")
    """
    # TODO: Implement this function
    # Hints: 
    # - Check type and length first
    # - Use string methods like isalnum(), startswith()
    # - Check against reserved list
    pass

# Test Exercise 2
print("Testing Exercise 2:")
test_usernames = ["john_doe", "ab", "admin", "2fast", "valid_user123", "user-name", ""]

for username in test_usernames:
    try:
        is_valid, message = validate_username(username)
        status = "✅" if is_valid else "❌"
        print(f"  '{username}': {status} {message}")
    except Exception as e:
        print(f"  '{username}': ❌ Error: {e}")

print()

# EXERCISE 3: EMAIL VALIDATION
print("EXERCISE 3: Email Address Validation")
print("====================================")

def validate_email_address(email):
    """
    Validate an email address.
    
    Requirements:
    - Must be a string
    - Must contain exactly one @ symbol
    - Must have at least one character before @
    - Must have at least one character after @
    - Domain part must contain at least one dot
    - No spaces allowed anywhere
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_email_address("user@example.com") → (True, "Email is valid")
    - validate_email_address("invalid.email") → (False, "Email must contain @ symbol")
    - validate_email_address("user @domain.com") → (False, "Email cannot contain spaces")
    - validate_email_address("user@domain") → (False, "Domain must contain a dot")
    """
    # TODO: Implement this function
    # Hints:
    # - Use string methods like count(), split()
    # - Check for spaces with ' ' in email
    # - Split on @ to check parts separately
    pass

# Test Exercise 3
print("Testing Exercise 3:")
test_emails = [
    "user@example.com",
    "invalid.email", 
    "user @domain.com",
    "user@domain",
    "@domain.com",
    "user@",
    "user@domain.co.uk"
]

for email in test_emails:
    try:
        is_valid, message = validate_email_address(email)
        status = "✅" if is_valid else "❌"
        print(f"  '{email}': {status} {message}")
    except Exception as e:
        print(f"  '{email}': ❌ Error: {e}")

print()

# EXERCISE 4: PRODUCT PRICE VALIDATION
print("EXERCISE 4: Product Price Validation")
print("====================================")

def validate_product_price(price, category="general"):
    """
    Validate product pricing based on category.
    
    Requirements:
    - Price must be a number (int or float)
    - Price must be positive (> 0)
    - Category-specific rules:
      - "electronics": minimum $10, maximum $10000
      - "books": minimum $5, maximum $500
      - "clothing": minimum $15, maximum $1000
      - "general": minimum $1, maximum $5000
    - Round price to 2 decimal places
    - Return (is_valid, formatted_price, message) tuple
    
    Test Cases:
    - validate_product_price(25.99, "books") → (True, 25.99, "Valid book price")
    - validate_product_price(3, "books") → (False, 3.00, "Book price too low (minimum $5)")
    - validate_product_price("invalid", "general") → (False, None, "Price must be a number")
    """
    # TODO: Implement this function
    # Hints:
    # - Check type and convert to float
    # - Use round(price, 2) for formatting
    # - Use if/elif for category-specific validation
    pass

# Test Exercise 4
print("Testing Exercise 4:")
test_prices = [
    (25.99, "books"),
    (3, "books"),
    ("invalid", "general"),
    (150, "electronics"),
    (5, "electronics"),
    (50.555, "clothing")
]

for price, category in test_prices:
    try:
        is_valid, formatted_price, message = validate_product_price(price, category)
        status = "✅" if is_valid else "❌"
        print(f"  ${price} ({category}): {status} Price: ${formatted_price}, {message}")
    except Exception as e:
        print(f"  ${price} ({category}): ❌ Error: {e}")

print()

# EXERCISE 5: DATE VALIDATION
print("EXERCISE 5: Date Range Validation")
print("=================================")

def validate_event_date(event_date):
    """
    Validate an event date string.
    
    Requirements:
    - Date must be in format "YYYY-MM-DD"
    - Date must be a valid calendar date
    - Date must be in the future (after today)
    - Date must be within next 2 years
    - Return (is_valid, days_from_now, message) tuple
    
    Test Cases:
    - validate_event_date("2024-12-25") → (True, X, "Valid future date")
    - validate_event_date("2020-01-01") → (False, X, "Date must be in the future")
    - validate_event_date("2024-13-01") → (False, None, "Invalid date format")
    
    Note: You'll need to import datetime module
    """
    # TODO: Implement this function
    # Hints:
    # - import datetime at the top of the function
    # - Use datetime.strptime() to parse date
    # - Calculate days difference with .days attribute
    # - Handle ValueError for invalid dates
    pass

# Test Exercise 5
print("Testing Exercise 5:")
test_dates = [
    "2024-12-25",
    "2020-01-01", 
    "2024-13-01",
    "invalid-date",
    "2024-02-29",  # Valid leap year date
    "2023-02-29"   # Invalid leap year date
]

for date_str in test_dates:
    try:
        is_valid, days_from_now, message = validate_event_date(date_str)
        status = "✅" if is_valid else "❌"
        print(f"  '{date_str}': {status} Days from now: {days_from_now}, {message}")
    except Exception as e:
        print(f"  '{date_str}': ❌ Error: {e}")

print()

# EXERCISE 6: COMPREHENSIVE FORM VALIDATION
print("EXERCISE 6: Registration Form Validation")
print("=======================================")

def validate_registration_form(form_data):
    """
    Validate a complete registration form.
    
    Requirements:
    - form_data is a dictionary with keys: name, email, password, age, terms
    - Use your previous validation functions where applicable
    - Additional requirements:
      - name: 2-50 characters, letters and spaces only
      - password: minimum 8 characters, must contain letter and number
      - age: integer between 13 and 120
      - terms: must be True (accepted terms and conditions)
    - Return (is_valid, errors_list) tuple where errors_list contains all validation errors
    
    Test Case:
    valid_form = {
        "name": "John Doe",
        "email": "john@example.com", 
        "password": "password123",
        "age": 25,
        "terms": True
    }
    validate_registration_form(valid_form) → (True, [])
    """
    # TODO: Implement this function
    # Hints:
    # - Check if form_data is a dictionary
    # - Validate each field and collect errors
    # - Use your previous validation functions
    # - Return overall validity and list of specific errors
    pass

# Test Exercise 6
print("Testing Exercise 6:")

test_forms = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123", 
        "age": 25,
        "terms": True
    },
    {
        "name": "J",  # Too short
        "email": "invalid-email",  # Invalid format
        "password": "123",  # Too short, no letters
        "age": 12,  # Too young
        "terms": False  # Not accepted
    },
    {
        "name": "Valid User",
        "email": "user@domain.com"
        # Missing password, age, terms
    }
]

for i, form in enumerate(test_forms, 1):
    print(f"\n--- Test Form {i} ---")
    try:
        is_valid, errors = validate_registration_form(form)
        status = "✅ VALID" if is_valid else "❌ INVALID"
        print(f"Result: {status}")
        
        if errors:
            print("Errors found:")
            for error in errors:
                print(f"  • {error}")
        else:
            print("No validation errors!")
            
    except Exception as e:
        print(f"❌ Error: {e}")

print()

print("=== EXERCISE SOLUTIONS ===")
print()
print("Complete the functions above and test your solutions.")
print("Here are some hints for implementation:")
print()
print("💡 GENERAL TIPS:")
print("• Always check data types before processing")
print("• Handle None and empty values appropriately") 
print("• Provide clear, helpful error messages")
print("• Use try/except blocks for error-prone operations")
print("• Test edge cases and boundary conditions")
print()
print("💡 VALIDATION PATTERNS:")
print("• Type checking: isinstance(value, expected_type)")
print("• Range checking: min_value <= value <= max_value")
print("• Format checking: use string methods and regular expressions")
print("• Required fields: check for None, empty strings, etc.")
print("• Cross-validation: check relationships between fields")
print()
print("💡 RETURN FORMATS:")
print("• Consistent return types (tuples with specific elements)")
print("• Boolean validity status as first element")
print("• Descriptive messages for user feedback")
print("• Additional data when useful (formatted values, etc.)")

"""
EXERCISE COMPLETION CHECKLIST:
==============================

□ Exercise 1: validate_student_grade()
  - Check if grade is a number
  - Validate range 0-100
  - Return appropriate messages

□ Exercise 2: validate_username() 
  - Check string type and length 3-20
  - Allow only letters, numbers, underscores
  - Prevent starting with number
  - Block reserved names

□ Exercise 3: validate_email_address()
  - Require exactly one @ symbol
  - Validate parts before/after @
  - Require dot in domain
  - Prohibit spaces

□ Exercise 4: validate_product_price()
  - Convert to number and validate positive
  - Apply category-specific price ranges
  - Format to 2 decimal places
  - Return formatted price

□ Exercise 5: validate_event_date()
  - Parse YYYY-MM-DD format
  - Check valid calendar date
  - Ensure future date within 2 years
  - Calculate days from now

□ Exercise 6: validate_registration_form()
  - Validate dictionary structure
  - Apply all field-specific validations
  - Collect and return all errors
  - Use previous validation functions

ADVANCED CHALLENGES:
===================
Once you complete the basic exercises, try these enhancements:

1. Add more sophisticated email validation using regex
2. Implement password strength checking with multiple criteria
3. Add international phone number validation
4. Create a validation decorator for functions
5. Build a validation rule engine with configurable rules
6. Add data sanitization to prevent security issues
7. Implement bulk validation for lists of data
8. Create custom exception classes for different validation errors

Remember: Good validation is about user experience as much as data integrity!
"""