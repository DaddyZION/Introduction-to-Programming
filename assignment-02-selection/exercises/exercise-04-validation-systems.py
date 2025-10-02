"""
Assignment 2 - Exercise 4: Validation Systems
Difficulty: 🟠 Advanced

TODO: Create robust input validation systems.

This exercise contains 4 mini-programs to practice input validation.
"""

# ==================== PROGRAM 1: User Registration Validator ====================
"""
TODO: Validate user registration information.

Requirements:
- Ask for username, password, and age
- Username must be:
    * At least 5 characters long
    * Cannot contain spaces
- Password must be:
    * At least 8 characters long
    * Contain at least one digit
- Age must be:
    * Between 13 and 120
- Display appropriate error messages or "Registration successful"

Example:
    Enter username: john
    Enter password: pass123
    Enter age: 16
    
    Validation results:
    ❌ Username too short (minimum 5 characters)
    ✓ Password is valid
    ✓ Age is valid
"""

# TODO: Write your code here for Program 1


# ==================== PROGRAM 2: Data Quality Checker ====================
"""
TODO: Validate numerical data entries.

Requirements:
- Ask for 3 test scores (each should be 0-100)
- Check each score:
    * Must be a number
    * Must be between 0 and 100
- Display which scores are valid/invalid
- If all valid, calculate and display average

Example:
    Enter score 1: 85
    Enter score 2: 105
    Enter score 3: 92
    
    Score 1 (85): ✓ Valid
    Score 2 (105): ❌ Invalid (must be 0-100)
    Score 3 (92): ✓ Valid
    
    Cannot calculate average - invalid data present
"""

# TODO: Write your code here for Program 2


# ==================== PROGRAM 3: Date Validator ====================
"""
TODO: Validate a date entry (simplified).

Requirements:
- Ask for day, month, and year
- Validate:
    * Month: 1-12
    * Day: 1-31 (simplified, don't worry about different month lengths)
    * Year: 1900-2100
- Display if date is valid or specific errors

Example:
    Enter day: 15
    Enter month: 13
    Enter year: 2024
    
    Invalid date:
    ❌ Month must be between 1 and 12
"""

# TODO: Write your code here for Program 3


# ==================== PROGRAM 4: Email Format Checker ====================
"""
TODO: Basic email format validation.

Requirements:
- Ask for email address
- Check if it:
    * Contains exactly one '@' symbol
    * Contains at least one '.' after the '@'
    * Is at least 5 characters long
    * Doesn't start or end with '@' or '.'
- Display validation result

Example:
    Enter email: user@example.com
    ✓ Email format is valid
    
    Enter email: invalid.email
    ❌ Email must contain '@' symbol
"""

# TODO: Write your code here for Program 4
