"""
Assignment 4 - Exercise 2: String Format Validation
Difficulty: 🟡 Intermediate

TODO: Implement validation functions for string formats.

This exercise practices validating formatted strings like usernames, emails, etc.
"""

# ==================== FUNCTION 1: Username Validation ====================
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
    pass


# ==================== FUNCTION 2: Email Validation ====================
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
    pass


# ==================== FUNCTION 3: Password Strength Validation ====================
def validate_password_strength(password):
    """
    Validate password strength.
    
    Requirements:
    - Must be at least 8 characters long
    - Must contain at least one uppercase letter
    - Must contain at least one lowercase letter
    - Must contain at least one digit
    - Must contain at least one special character (!@#$%^&*)
    - Return (is_valid, strength_score, message) tuple
    - Strength score: 0-5 (one point for each requirement met)
    
    Test Cases:
    - validate_password_strength("Pass123!") → (True, 5, "Strong password")
    - validate_password_strength("password") → (False, 1, "Weak: Missing uppercase, digits, special chars")
    - validate_password_strength("Pass123") → (False, 4, "Missing special character")
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Date Format Validation ====================
def validate_date_format(date_string):
    """
    Validate date string format (MM/DD/YYYY).
    
    Requirements:
    - Must be a string
    - Must match MM/DD/YYYY format
    - Month must be 01-12
    - Day must be 01-31 (simplified - don't check month-specific days)
    - Year must be 1900-2100
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_date_format("12/25/2024") → (True, "Valid date format")
    - validate_date_format("13/01/2024") → (False, "Invalid month (must be 01-12)")
    - validate_date_format("12-25-2024") → (False, "Use MM/DD/YYYY format with slashes")
    - validate_date_format("1/5/2024") → (False, "Month and day must be 2 digits")
    """
    # TODO: Implement this function
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing String Format Validation ===\n")
    
    # Test username validation
    print("Test 1: Username Validation")
    test_usernames = ["john_doe", "ab", "admin", "2fast", "valid_user123", "user-name"]
    for username in test_usernames:
        result = validate_username(username)
        print(f"  '{username}': {result}")
    
    # Test email validation
    print("\nTest 2: Email Validation")
    test_emails = ["user@example.com", "invalid.email", "user @domain.com", 
                   "user@domain", "@domain.com", "user@domain.co.uk"]
    for email in test_emails:
        result = validate_email_address(email)
        print(f"  '{email}': {result}")
    
    # Test password validation
    print("\nTest 3: Password Strength")
    test_passwords = ["Pass123!", "password", "Pass123", "PASSWORD123!", "Aa1!"]
    for pwd in test_passwords:
        result = validate_password_strength(pwd)
        print(f"  '{pwd}': {result}")
    
    # Test date validation
    print("\nTest 4: Date Format Validation")
    test_dates = ["12/25/2024", "13/01/2024", "12-25-2024", "1/5/2024", "06/15/2025"]
    for date in test_dates:
        result = validate_date_format(date)
        print(f"  '{date}': {result}")
