"""
Assignment 6 - Exercise 4: Password Validator
Difficulty: 🟡 Intermediate

TODO: Create a password validation and strength checking system.

Requirements:
1. Check password strength based on multiple criteria
2. Provide specific feedback for each missing requirement
3. Suggest improvements
4. Rate password strength (Weak/Fair/Good/Strong)
"""

# ==================== FUNCTION 1: Check Length ====================
def check_length(password, min_length=8):
    """
    Check if password meets minimum length requirement.
    
    Returns: (is_valid, message) tuple
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Check Character Types ====================
def check_character_types(password):
    """
    Check if password contains required character types.
    
    Requirements:
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)
    
    Returns: dictionary with:
    {
        'has_uppercase': bool,
        'has_lowercase': bool,
        'has_digit': bool,
        'has_special': bool,
        'missing': list of missing types
    }
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Check Common Passwords ====================
def check_common_passwords(password):
    """
    Check if password is in list of common passwords.
    
    Common passwords: 
    ['password', '12345678', 'qwerty', 'abc123', 'password123', 
     'admin', 'letmein', 'welcome', '123456789', 'Password1']
    
    Returns: (is_common, message) tuple
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Check Patterns ====================
def check_patterns(password):
    """
    Check for weak patterns in password.
    
    Patterns to check:
    - Sequential characters (abc, 123, etc.)
    - Repeated characters (aaa, 111, etc.)
    - Keyboard patterns (qwerty, asdf, etc.)
    
    Returns: (has_patterns, patterns_found) tuple
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Calculate Strength Score ====================
def calculate_strength_score(password):
    """
    Calculate password strength score.
    
    Scoring (0-100):
    - Length: 5 points per character up to 20 (max 40 points)
    - Character types: 10 points each (max 40 points)
    - No common passwords: 10 points
    - No weak patterns: 10 points
    
    Returns: integer score 0-100
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Get Strength Rating ====================
def get_strength_rating(score):
    """
    Convert score to rating.
    
    Ratings:
    - 0-30: Very Weak
    - 31-50: Weak
    - 51-70: Fair
    - 71-85: Good
    - 86-100: Strong
    
    Returns: string rating
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 7: Generate Feedback ====================
def generate_feedback(password):
    """
    Generate comprehensive feedback for password.
    
    Returns: dictionary with:
    {
        'is_valid': bool,
        'score': int,
        'rating': str,
        'issues': list of strings,
        'suggestions': list of strings
    }
    """
    # TODO: Implement this function
    # Use all the check functions above
    pass


# ==================== FUNCTION 8: Suggest Strong Password ====================
def suggest_strong_password(length=12):
    """
    Generate a suggested strong password.
    
    Requirements:
    - Specified length
    - Mix of uppercase, lowercase, digits, special chars
    - No obvious patterns
    
    Returns: string password
    """
    # TODO: Implement this function
    # Hint: Use random module
    pass


# ==================== MAIN PROGRAM ====================
def main():
    """
    Interactive password validator.
    
    Features:
    1. Test a password
    2. Generate strong password
    3. Compare passwords
    4. Exit
    """
    print("=== Password Validator ===\n")
    
    # TODO: Implement menu loop
    
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    test_passwords = [
        "password",
        "Pass123",
        "MyP@ssw0rd",
        "Str0ng!P@ssW0rd",
        "abc123",
        "Q!w2E#r4T%y6"
    ]
    
    print("Testing Password Validator:\n")
    
    for pwd in test_passwords:
        print(f"Password: {pwd}")
        # feedback = generate_feedback(pwd)
        # print(f"  Rating: {feedback['rating']} (Score: {feedback['score']})")
        # if feedback['issues']:
        #     print(f"  Issues: {', '.join(feedback['issues'])}")
        # if feedback['suggestions']:
        #     print(f"  Suggestions: {', '.join(feedback['suggestions'])}")
        print()
    
    print("To run interactive program:")
    print("  Uncomment: main()")
    # main()
