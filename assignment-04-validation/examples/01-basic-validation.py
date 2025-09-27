"""
Assignment 4 - Example 1: Basic Input Validation
===============================================

This program introduces the fundamental concepts of input validation.
Validation ensures that data meets specific criteria before your program
processes it. This prevents crashes, security issues, and incorrect results.

Key Concepts Demonstrated:
- Why validation is essential
- Basic validation patterns
- Validation vs verification
- User feedback and error messages
- Simple validation functions
- Validation workflow design
"""

print("=== INTRODUCTION TO INPUT VALIDATION ===")
print()

print("Input validation is like having a bouncer at a club:")
print("• Check ID (is it the right format?)")
print("• Verify age (meets requirements?)")
print("• Ensure dress code (follows rules?)")
print("• Only let valid people enter!")
print()

# WHY VALIDATION MATTERS
print("=== WHY VALIDATION IS CRITICAL ===")
print()

print("Without validation, programs are fragile and dangerous:")
print()

# Example of what happens WITHOUT validation
print("❌ DANGEROUS: No validation")
print("Code: age = int(input('Enter age: '))")
print("What happens if user enters:")
print("  • 'twenty' -> ValueError: invalid literal for int()")
print("  • '-50' -> Logic errors (negative age?)")
print("  • '999' -> Unrealistic data")
print("  • '' (empty) -> ValueError")
print("  • 'DROP TABLE users' -> Potential security issue")
print()

print("🛡️ SAFE: With validation")
print("We check BEFORE processing:")
print("  • Is it a number? ✓")
print("  • Is it in valid range? ✓") 
print("  • Does it make sense? ✓")
print("  • Is it safe to use? ✓")
print()

# BASIC VALIDATION CONCEPTS
print("=== BASIC VALIDATION CONCEPTS ===")
print()

print("There are different types of validation:")
print()

print("1. TYPE VALIDATION")
print("   • Is it a number when we need a number?")
print("   • Is it text when we need text?")
print()

print("2. RANGE VALIDATION") 
print("   • Is the age between 0 and 150?")
print("   • Is the grade between 0 and 100?")
print()

print("3. FORMAT VALIDATION")
print("   • Does the email contain @ and a domain?")
print("   • Is the phone number the right length?")
print()

print("4. BUSINESS RULE VALIDATION")
print("   • Can someone under 18 apply for a credit card?")
print("   • Is this username already taken?")
print()

# SIMPLE VALIDATION EXAMPLES
print("=== SIMPLE VALIDATION EXAMPLES ===")
print()

# Example 1: Age validation
print("Example 1: Age Validation")
print()

def validate_age(age_input):
    """
    Simple age validation function.
    Returns tuple: (is_valid, cleaned_value, error_message)
    """
    
    # Check if empty
    if not age_input.strip():
        return False, None, "Age cannot be empty"
    
    # Check if it's a valid number
    try:
        age = int(age_input.strip())
    except ValueError:
        return False, None, "Age must be a whole number"
    
    # Check range
    if age < 0:
        return False, None, "Age cannot be negative"
    elif age > 150:
        return False, None, "Age seems unrealistic (over 150)"
    
    # All checks passed
    return True, age, "Valid age"

# Test the validation function
print("Testing age validation:")

test_ages = ["25", "  30  ", "-5", "abc", "200", "", "0", "150"]

for test_age in test_ages:
    is_valid, clean_value, message = validate_age(test_age)
    status = "✅ VALID" if is_valid else "❌ INVALID"
    
    print(f"Input: '{test_age}'")
    print(f"  Result: {status}")
    print(f"  Value: {clean_value}")
    print(f"  Message: {message}")
    print()

# Example 2: Email validation (basic)
print("Example 2: Basic Email Validation")
print()

def validate_email(email_input):
    """
    Basic email validation.
    Real email validation is much more complex!
    """
    
    # Remove whitespace
    email = email_input.strip().lower()
    
    # Check if empty
    if not email:
        return False, None, "Email cannot be empty"
    
    # Basic format checks
    if " " in email:
        return False, None, "Email cannot contain spaces"
    
    if "@" not in email:
        return False, None, "Email must contain @ symbol"
    
    if email.count("@") != 1:
        return False, None, "Email must contain exactly one @ symbol"
    
    # Split into local and domain parts
    local_part, domain_part = email.split("@")
    
    # Check local part (before @)
    if len(local_part) == 0:
        return False, None, "Email must have text before @"
    
    if len(local_part) > 64:
        return False, None, "Email local part too long (max 64 characters)"
    
    # Check domain part (after @)
    if len(domain_part) == 0:
        return False, None, "Email must have domain after @"
    
    if "." not in domain_part:
        return False, None, "Domain must contain a dot (.)"
    
    # Check domain has valid structure
    domain_parts = domain_part.split(".")
    if len(domain_parts) < 2:
        return False, None, "Domain needs at least one dot"
    
    # Check each domain part
    for part in domain_parts:
        if len(part) == 0:
            return False, None, "Domain parts cannot be empty"
    
    # Basic length check
    if len(email) > 254:
        return False, None, "Email too long (max 254 characters)"
    
    return True, email, "Valid email format"

# Test email validation
print("Testing email validation:")

test_emails = [
    "user@example.com",
    "  USER@EXAMPLE.COM  ",  # Should be cleaned
    "invalid.email",         # No @
    "@example.com",          # No local part
    "user@",                 # No domain
    "user@domain",           # No dot in domain
    "user name@example.com", # Space
    "user@@example.com",     # Double @
    ""                       # Empty
]

for test_email in test_emails:
    is_valid, clean_value, message = validate_email(test_email)
    status = "✅ VALID" if is_valid else "❌ INVALID"
    
    print(f"Input: '{test_email}'")
    print(f"  Result: {status}")
    print(f"  Cleaned: '{clean_value}'")
    print(f"  Message: {message}")
    print()

# VALIDATION WORKFLOW
print("=== VALIDATION WORKFLOW DEMONSTRATION ===")
print()

print("Real programs use a validation workflow:")
print("1. Get user input")
print("2. Validate input") 
print("3. If valid: process and continue")
print("4. If invalid: show error and ask again")
print()

def get_valid_age():
    """
    Demonstrates the validation loop pattern.
    Keeps asking until valid input is provided.
    """
    
    print("📝 Age Collection with Validation")
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts}/{max_attempts}")
        
        age_input = input("Please enter your age: ")
        
        # Validate the input
        is_valid, age, message = validate_age(age_input)
        
        if is_valid:
            print(f"✅ {message}")
            return age
        else:
            print(f"❌ {message}")
            if attempts < max_attempts:
                print("Please try again.")
            else:
                print("Too many invalid attempts.")
    
    return None

# Demonstrate the validation workflow
print("Demonstrating validation workflow:")
print("(For demo, we'll simulate user input)")

# Simulate different user inputs
simulated_inputs = ["abc", "-10", "25"]
input_index = 0

def mock_input(prompt):
    """Mock input function for demonstration"""
    global input_index
    if input_index < len(simulated_inputs):
        value = simulated_inputs[input_index]
        input_index += 1
        print(f"{prompt}{value}")  # Show what was "entered"
        return value
    return "25"  # Default valid input

# Replace input function temporarily for demo
original_input = input
input = mock_input

result_age = get_valid_age()
if result_age:
    print(f"\n🎉 Successfully collected age: {result_age}")
else:
    print(f"\n❌ Failed to collect valid age")

# Restore original input function
input = original_input

print()

# VALIDATION BEST PRACTICES
print("=== VALIDATION BEST PRACTICES ===")
print()

print("✅ DO:")
print("1. Validate ALL user input")
print("2. Provide clear, helpful error messages")
print("3. Clean/normalize data (trim whitespace, etc.)")
print("4. Validate early - before processing")
print("5. Use consistent validation patterns")
print("6. Test edge cases (empty, extreme values)")
print("7. Limit validation attempts to prevent abuse")
print()

print("❌ DON'T:")
print("1. Trust any input without validation")
print("2. Give vague error messages ('Invalid input')")
print("3. Crash the program on bad input")
print("4. Validate the same data multiple times")
print("5. Allow unlimited validation attempts")
print("6. Forget to handle empty input")
print("7. Mix validation with business logic")
print()

# DIFFERENT VALIDATION APPROACHES
print("=== DIFFERENT VALIDATION APPROACHES ===")
print()

print("Approach 1: Immediate Validation")
print("Validate each piece of data as it's entered")

def immediate_validation_demo():
    print("\n--- Immediate Validation Example ---")
    
    # Name validation
    while True:
        name = input("Enter your name: ").strip()
        if name and len(name) >= 2:
            print(f"✅ Name '{name}' is valid")
            break
        print("❌ Name must be at least 2 characters")
    
    # Age validation  
    while True:
        age_input = input("Enter your age: ")
        is_valid, age, message = validate_age(age_input)
        if is_valid:
            print(f"✅ Age {age} is valid")
            break
        print(f"❌ {message}")
    
    return {"name": name, "age": age}

print("This approach gives immediate feedback but can be repetitive")
print()

print("Approach 2: Batch Validation")
print("Collect all data first, then validate everything together")

def batch_validation_demo():
    print("\n--- Batch Validation Example ---")
    
    # Collect all data
    data = {}
    data["name"] = input("Enter your name: ").strip()
    data["age_input"] = input("Enter your age: ")
    data["email_input"] = input("Enter your email: ")
    
    # Validate all data
    errors = []
    
    # Validate name
    if not data["name"] or len(data["name"]) < 2:
        errors.append("Name must be at least 2 characters")
    
    # Validate age
    is_valid, age, message = validate_age(data["age_input"])
    if not is_valid:
        errors.append(f"Age: {message}")
    else:
        data["age"] = age
    
    # Validate email
    is_valid, email, message = validate_email(data["email_input"])
    if not is_valid:
        errors.append(f"Email: {message}")
    else:
        data["email"] = email
    
    # Report results
    if errors:
        print("❌ Validation failed:")
        for error in errors:
            print(f"  • {error}")
        return None
    else:
        print("✅ All validation passed!")
        return {
            "name": data["name"],
            "age": data["age"], 
            "email": data["email"]
        }

print("This approach is more efficient but less interactive")
print()

# VALIDATION FUNCTION PATTERNS
print("=== VALIDATION FUNCTION PATTERNS ===")
print()

print("Pattern 1: Boolean Return")
def is_valid_name(name):
    """Returns True if valid, False if not"""
    return name and len(name.strip()) >= 2

print("Pattern 2: Exception on Error")
def validate_name_strict(name):
    """Raises exception if invalid"""
    if not name or len(name.strip()) < 2:
        raise ValueError("Name must be at least 2 characters")
    return name.strip()

print("Pattern 3: Tuple Return (recommended)")
def validate_name_complete(name):
    """Returns (is_valid, cleaned_value, message)"""
    if not name:
        return False, None, "Name is required"
    
    cleaned = name.strip()
    if len(cleaned) < 2:
        return False, None, "Name must be at least 2 characters"
    
    return True, cleaned, "Valid name"

# Test the patterns
print("\nTesting validation patterns:")

test_name = "  Alice  "

# Pattern 1
if is_valid_name(test_name):
    print(f"Pattern 1: '{test_name}' is valid")

# Pattern 2
try:
    clean_name = validate_name_strict(test_name)
    print(f"Pattern 2: Cleaned name is '{clean_name}'")
except ValueError as e:
    print(f"Pattern 2: Error - {e}")

# Pattern 3  
is_valid, clean_name, message = validate_name_complete(test_name)
print(f"Pattern 3: Valid={is_valid}, Name='{clean_name}', Message='{message}'")

print()

# REAL-WORLD VALIDATION EXAMPLE
print("=== REAL-WORLD EXAMPLE: USER REGISTRATION ===")
print()

def validate_user_registration(username, password, email, age):
    """
    Comprehensive user registration validation.
    Returns dict with validation results.
    """
    
    results = {
        "valid": True,
        "errors": [],
        "data": {}
    }
    
    # Username validation
    if not username or len(username.strip()) < 3:
        results["errors"].append("Username must be at least 3 characters")
        results["valid"] = False
    elif len(username.strip()) > 20:
        results["errors"].append("Username cannot exceed 20 characters")
        results["valid"] = False
    elif not username.strip().replace("_", "").replace("-", "").isalnum():
        results["errors"].append("Username can only contain letters, numbers, hyphens, and underscores")
        results["valid"] = False
    else:
        results["data"]["username"] = username.strip()
    
    # Password validation
    if not password or len(password) < 8:
        results["errors"].append("Password must be at least 8 characters")
        results["valid"] = False
    else:
        # Check password strength
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        if not (has_upper and has_lower and has_digit):
            results["errors"].append("Password must contain uppercase, lowercase, and numbers")
            results["valid"] = False
        else:
            results["data"]["password"] = password  # In real app, would hash this!
    
    # Email validation
    is_valid, clean_email, message = validate_email(email)
    if not is_valid:
        results["errors"].append(f"Email: {message}")
        results["valid"] = False
    else:
        results["data"]["email"] = clean_email
    
    # Age validation
    is_valid, clean_age, message = validate_age(str(age))
    if not is_valid:
        results["errors"].append(f"Age: {message}")
        results["valid"] = False
    elif clean_age < 13:
        results["errors"].append("Must be at least 13 years old to register")
        results["valid"] = False
    else:
        results["data"]["age"] = clean_age
    
    return results

# Test user registration validation
print("Testing user registration validation:")

test_registrations = [
    {
        "username": "alice_123",
        "password": "SecurePass123",
        "email": "alice@example.com",
        "age": "25"
    },
    {
        "username": "ab",  # Too short
        "password": "weak", # Too weak
        "email": "invalid", # Bad email
        "age": "10" # Too young
    }
]

for i, reg_data in enumerate(test_registrations, 1):
    print(f"\n--- Registration Test {i} ---")
    print(f"Data: {reg_data}")
    
    results = validate_user_registration(
        reg_data["username"],
        reg_data["password"], 
        reg_data["email"],
        reg_data["age"]
    )
    
    if results["valid"]:
        print("✅ Registration data is valid!")
        print(f"Cleaned data: {results['data']}")
    else:
        print("❌ Registration failed:")
        for error in results["errors"]:
            print(f"  • {error}")

print()

print("=== SUMMARY ===")
print()
print("Input Validation Key Points:")
print("1. Never trust user input - validate everything")
print("2. Provide clear, helpful error messages")
print("3. Use consistent validation patterns")
print("4. Clean and normalize data during validation") 
print("5. Handle edge cases (empty, extreme values)")
print("6. Validate early to catch problems quickly")
print("7. Use validation loops for interactive input")
print("8. Separate validation logic from business logic")

"""
KEY TAKEAWAYS:
==============
1. Input validation prevents crashes and security issues
2. Always validate type, range, format, and business rules
3. Provide helpful error messages to guide users
4. Use validation loops to handle invalid input gracefully
5. Clean and normalize data during validation
6. Test edge cases thoroughly
7. Create reusable validation functions

VALIDATION PATTERNS:
===================
• Type checking: Can this be converted to the expected type?
• Range validation: Is the value within acceptable bounds?
• Format validation: Does the data match expected patterns?
• Business rules: Does this data make sense in our domain?
• Error handling: How do we respond to invalid data?

BEST PRACTICES:
===============
• Validate early and often
• Be specific with error messages
• Sanitize data (trim whitespace, normalize case)
• Use whitelisting (allow known good patterns)
• Limit validation attempts
• Test with malicious/edge case inputs
• Keep validation logic separate from business logic

NEXT STEP:
Go to 02-type-validation.py to learn about type checking and conversion!
"""