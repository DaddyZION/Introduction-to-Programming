"""
Assignment 4 - Example 4: Format Validation and Pattern Matching
================================================================

This program demonstrates how to validate that data follows specific formats
and patterns. Format validation ensures data structure correctness using
techniques like regular expressions, string analysis, and pattern matching.

Key Concepts Demonstrated:
- Email address format validation
- Phone number format validation
- Credit card number validation (Luhn algorithm)
- Password strength validation
- URL and web address validation
- Regular expressions for pattern matching
- Custom format validation functions
- International format considerations
"""

import re
import string

print("=== FORMAT VALIDATION AND PATTERN MATCHING ===")
print()

print("Format validation ensures data follows expected patterns:")
print("• Email: user@domain.com (specific structure)")
print("• Phone: (555) 123-4567 (standardized format)")
print("• Credit Card: 4532-1234-5678-9012 (checksum validation)")
print("• Password: Complex rules for security")
print()

# EMAIL VALIDATION
print("=== EMAIL ADDRESS VALIDATION ===")
print()

def validate_email_basic(email):
    """
    Basic email validation using string analysis.
    This is a simplified version - real email validation is very complex!
    """
    if not email:
        return False, "Email cannot be empty"
    
    email = email.strip().lower()
    
    # Basic structure checks
    if email.count('@') != 1:
        return False, "Email must contain exactly one @ symbol"
    
    if email.startswith('@') or email.endswith('@'):
        return False, "Email cannot start or end with @ symbol"
    
    # Split into local and domain parts
    local, domain = email.split('@')
    
    # Local part validation (before @)
    if len(local) == 0:
        return False, "Email local part (before @) cannot be empty"
    
    if len(local) > 64:
        return False, "Email local part cannot exceed 64 characters"
    
    # Check for valid local part characters
    valid_local_chars = string.ascii_letters + string.digits + ".-_+"
    for char in local:
        if char not in valid_local_chars:
            return False, f"Email local part contains invalid character: '{char}'"
    
    # Domain part validation (after @)
    if len(domain) == 0:
        return False, "Email domain part (after @) cannot be empty"
    
    if domain.count('.') == 0:
        return False, "Email domain must contain at least one dot"
    
    if domain.startswith('.') or domain.endswith('.'):
        return False, "Email domain cannot start or end with a dot"
    
    if '..' in domain:
        return False, "Email domain cannot contain consecutive dots"
    
    # Domain parts validation
    domain_parts = domain.split('.')
    for part in domain_parts:
        if len(part) == 0:
            return False, "Email domain parts cannot be empty"
        
        if not part.replace('-', '').isalnum():
            return False, f"Email domain part '{part}' contains invalid characters"
    
    # Top-level domain check
    tld = domain_parts[-1]
    if len(tld) < 2:
        return False, "Top-level domain must be at least 2 characters"
    
    return True, f"Valid email: {email}"

def validate_email_regex(email):
    """
    Email validation using regular expressions (more robust).
    """
    if not email:
        return False, "Email cannot be empty"
    
    # Regular expression pattern for email validation
    # This is a simplified pattern - full RFC compliance is extremely complex
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, email.strip()):
        return True, f"Valid email: {email.strip().lower()}"
    else:
        return False, "Email format is invalid"

print("Testing email validation (basic method):")

test_emails = [
    "user@example.com",
    "test.email+tag@domain.co.uk", 
    "invalid-email",
    "user@",
    "@domain.com",
    "user..double@example.com",
    "user@domain",
    "valid@sub.domain.com",
    "",
    "user@domain..com"
]

for email in test_emails:
    is_valid, message = validate_email_basic(email)
    status = "✅" if is_valid else "❌"
    print(f"  '{email}': {status} {message}")

print("\nTesting email validation (regex method):")

for email in test_emails:
    is_valid, message = validate_email_regex(email)
    status = "✅" if is_valid else "❌"
    print(f"  '{email}': {status} {message}")

print()

# PHONE NUMBER VALIDATION
print("=== PHONE NUMBER VALIDATION ===")
print()

def validate_phone_us(phone):
    """
    Validate US phone number in various formats.
    Accepts: (555) 123-4567, 555-123-4567, 5551234567, +1-555-123-4567
    """
    if not phone:
        return False, "", "Phone number cannot be empty"
    
    # Remove common formatting characters
    cleaned = re.sub(r'[^\d]', '', phone)
    
    # Handle country code
    if cleaned.startswith('1') and len(cleaned) == 11:
        cleaned = cleaned[1:]  # Remove country code
    
    # Check length
    if len(cleaned) != 10:
        return False, cleaned, f"US phone number must have 10 digits, found {len(cleaned)}"
    
    # Extract parts
    area_code = cleaned[:3]
    exchange = cleaned[3:6]
    number = cleaned[6:]
    
    # Validate area code (first digit cannot be 0 or 1)
    if area_code[0] in ['0', '1']:
        return False, cleaned, "Area code cannot start with 0 or 1"
    
    # Validate exchange (first digit cannot be 0 or 1)
    if exchange[0] in ['0', '1']:
        return False, cleaned, "Exchange code cannot start with 0 or 1"
    
    # Format as standard US phone number
    formatted = f"({area_code}) {exchange}-{number}"
    
    return True, formatted, f"Valid US phone: {formatted}"

def validate_phone_international(phone):
    """
    Basic international phone number validation.
    """
    if not phone:
        return False, "", "Phone number cannot be empty"
    
    # Remove formatting, keep only digits and +
    cleaned = re.sub(r'[^\d+]', '', phone)
    
    # Must start with + for international
    if not cleaned.startswith('+'):
        return False, cleaned, "International phone must start with +"
    
    # Remove + and check digits
    digits = cleaned[1:]
    
    if not digits.isdigit():
        return False, cleaned, "Phone number must contain only digits after +"
    
    if len(digits) < 7 or len(digits) > 15:
        return False, cleaned, "International phone must have 7-15 digits"
    
    return True, cleaned, f"Valid international phone: {cleaned}"

print("Testing US phone number validation:")

test_phones_us = [
    "(555) 123-4567",
    "555-123-4567", 
    "5551234567",
    "+1-555-123-4567",
    "1-555-123-4567",
    "(155) 123-4567",  # Invalid area code
    "(555) 023-4567",  # Invalid exchange
    "555-123-456",     # Too short
    "555-123-45678",   # Too long
    ""
]

for phone in test_phones_us:
    is_valid, formatted, message = validate_phone_us(phone)
    status = "✅" if is_valid else "❌"
    print(f"  '{phone}': {status} {message}")

print("\nTesting international phone number validation:")

test_phones_intl = [
    "+1-555-123-4567",   # US
    "+44-20-7946-0958",  # UK
    "+33-1-42-68-53-00", # France
    "+81-3-1234-5678",   # Japan
    "555-123-4567",      # Missing +
    "+1234567890123456", # Too long
    "+123456",           # Too short
    ""
]

for phone in test_phones_intl:
    is_valid, formatted, message = validate_phone_international(phone)
    status = "✅" if is_valid else "❌"
    print(f"  '{phone}': {status} {message}")

print()

# CREDIT CARD VALIDATION
print("=== CREDIT CARD VALIDATION ===")
print()

def luhn_checksum(card_number):
    """
    Calculate Luhn checksum for credit card validation.
    """
    def luhn_checksum_digits(digits):
        return sum(digits[::2]) + sum(sum(divmod(2 * d, 10)) for d in digits[1::2])
    
    digits = [int(d) for d in str(card_number)]
    return luhn_checksum_digits(digits) % 10 == 0

def identify_card_type(card_number):
    """
    Identify credit card type based on number pattern.
    """
    card_str = str(card_number)
    
    # Visa: starts with 4, 13-19 digits
    if card_str.startswith('4') and len(card_str) in [13, 16, 19]:
        return "Visa"
    
    # Mastercard: starts with 5, 16 digits
    elif card_str.startswith('5') and len(card_str) == 16:
        return "Mastercard"
    
    # American Express: starts with 34 or 37, 15 digits
    elif (card_str.startswith('34') or card_str.startswith('37')) and len(card_str) == 15:
        return "American Express"
    
    # Discover: starts with 6, 16 digits
    elif card_str.startswith('6') and len(card_str) == 16:
        return "Discover"
    
    else:
        return "Unknown"

def validate_credit_card(card_input):
    """
    Comprehensive credit card validation.
    """
    if not card_input:
        return False, "", "", "Credit card number cannot be empty"
    
    # Remove formatting (spaces, hyphens)
    cleaned = re.sub(r'[^\d]', '', card_input)
    
    if not cleaned:
        return False, "", "", "Credit card number must contain digits"
    
    # Check length
    if len(cleaned) < 13 or len(cleaned) > 19:
        return False, cleaned, "", f"Credit card number must be 13-19 digits, found {len(cleaned)}"
    
    # Identify card type
    card_type = identify_card_type(cleaned)
    
    # Validate using Luhn algorithm
    if not luhn_checksum(cleaned):
        return False, cleaned, card_type, "Credit card number failed Luhn checksum validation"
    
    # Format for display (mask middle digits)
    if len(cleaned) == 16:
        formatted = f"{cleaned[:4]}-{cleaned[4:8]}-{cleaned[8:12]}-{cleaned[12:]}"
        masked = f"{cleaned[:4]}-****-****-{cleaned[12:]}"
    elif len(cleaned) == 15:
        formatted = f"{cleaned[:4]}-{cleaned[4:10]}-{cleaned[10:]}"
        masked = f"{cleaned[:4]}-******-{cleaned[10:]}"
    else:
        formatted = cleaned
        masked = cleaned[:4] + '*' * (len(cleaned) - 8) + cleaned[-4:]
    
    return True, formatted, card_type, f"Valid {card_type} card: {masked}"

print("Testing credit card validation:")

test_cards = [
    "4532-1234-5678-9012",  # Valid Visa (example)
    "5555-5555-5555-4444",  # Valid Mastercard (test number)
    "3782-822463-10005",    # Valid AmEx (test number)
    "6011-1111-1111-1117",  # Valid Discover (test number)
    "4532-1234-5678-9013",  # Invalid Luhn
    "1234-5678-9012-3456",  # Invalid format
    "4532-1234-5678",       # Too short
    "4532-1234-5678-9012-3456", # Too long
    ""
]

for card in test_cards:
    is_valid, formatted, card_type, message = validate_credit_card(card)
    status = "✅" if is_valid else "❌"
    print(f"  '{card}': {status} {message}")

print()

# PASSWORD STRENGTH VALIDATION
print("=== PASSWORD STRENGTH VALIDATION ===")
print()

def validate_password_strength(password):
    """
    Comprehensive password strength validation.
    """
    if not password:
        return False, 0, [], "Password cannot be empty"
    
    issues = []
    score = 0
    
    # Length check
    if len(password) < 8:
        issues.append("Must be at least 8 characters long")
    elif len(password) >= 12:
        score += 2  # Bonus for longer passwords
    else:
        score += 1
    
    # Character type checks
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if not has_lower:
        issues.append("Must contain lowercase letters")
    else:
        score += 1
    
    if not has_upper:
        issues.append("Must contain uppercase letters")
    else:
        score += 1
    
    if not has_digit:
        issues.append("Must contain digits")
    else:
        score += 1
    
    if not has_special:
        issues.append("Must contain special characters (!@#$%^&* etc.)")
    else:
        score += 2  # Special characters are worth more
    
    # Common patterns to avoid
    common_patterns = [
        "password", "123456", "qwerty", "admin", "login",
        "welcome", "monkey", "dragon", "master", "hello"
    ]
    
    password_lower = password.lower()
    for pattern in common_patterns:
        if pattern in password_lower:
            issues.append(f"Cannot contain common pattern: '{pattern}'")
            score = max(0, score - 2)
    
    # Consecutive character check
    consecutive_count = 0
    for i in range(len(password) - 1):
        if ord(password[i+1]) == ord(password[i]) + 1:
            consecutive_count += 1
        else:
            consecutive_count = 0
        
        if consecutive_count >= 2:
            issues.append("Cannot contain 3+ consecutive characters (abc, 123, etc.)")
            score = max(0, score - 1)
            break
    
    # Repeated character check
    for char in set(password):
        if password.count(char) > 2:
            issues.append(f"Cannot repeat character '{char}' more than 2 times")
            score = max(0, score - 1)
            break
    
    # Determine strength level
    if len(issues) == 0:
        if score >= 7:
            strength = "Very Strong"
        elif score >= 5:
            strength = "Strong"
        else:
            strength = "Moderate"
        return True, score, [], f"Password strength: {strength} (Score: {score}/8)"
    else:
        strength = "Weak"
        return False, score, issues, f"Password strength: {strength} (Score: {score}/8)"

print("Testing password strength validation:")

test_passwords = [
    "MySecurePass123!",     # Strong password
    "password123",          # Common pattern
    "Pass123!",            # Good but short
    "ALLUPPERCASE123!",    # Missing lowercase
    "alllowercase123!",    # Missing uppercase
    "MyPassword!",         # Missing digits
    "MyPassword123",       # Missing special chars
    "MyPass111!",         # Repeated characters
    "MyPassABC!",         # Consecutive characters
    ""                    # Empty
]

for password in test_passwords:
    is_valid, score, issues, message = validate_password_strength(password)
    status = "✅" if is_valid else "❌"
    
    print(f"  Password: {status} {message}")
    
    if issues:
        for issue in issues:
            print(f"    • {issue}")
    print()

# URL VALIDATION
print("=== URL VALIDATION ===")
print()

def validate_url(url):
    """
    Basic URL validation using regex.
    """
    if not url:
        return False, "URL cannot be empty"
    
    url = url.strip()
    
    # URL regex pattern (simplified)
    url_pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    
    if re.match(url_pattern, url):
        # Additional checks
        if len(url) > 2000:
            return False, "URL is too long (maximum 2000 characters)"
        
        # Check for suspicious patterns
        suspicious_patterns = ['javascript:', 'data:', 'file:', 'ftp:']
        url_lower = url.lower()
        
        for pattern in suspicious_patterns:
            if pattern in url_lower and not url_lower.startswith('http'):
                return False, f"URL contains suspicious pattern: {pattern}"
        
        return True, f"Valid URL: {url}"
    else:
        return False, "URL format is invalid"

print("Testing URL validation:")

test_urls = [
    "https://www.example.com",
    "http://subdomain.example.com/path",
    "https://example.com/path/to/page?param=value",
    "ftp://example.com",           # Invalid protocol
    "https://",                    # Missing domain
    "example.com",                 # Missing protocol
    "https://example",             # Invalid domain
    "javascript:alert('xss')",     # Suspicious content
    ""
]

for url in test_urls:
    is_valid, message = validate_url(url)
    status = "✅" if is_valid else "❌"
    print(f"  '{url}': {status} {message}")

print()

# CUSTOM FORMAT VALIDATOR CLASS
print("=== CUSTOM FORMAT VALIDATOR CLASS ===")
print()

class FormatValidator:
    """
    A flexible class for creating custom format validators.
    """
    
    def __init__(self, pattern, pattern_name, format_func=None, additional_checks=None):
        self.pattern = re.compile(pattern)
        self.pattern_name = pattern_name
        self.format_func = format_func
        self.additional_checks = additional_checks or []
    
    def validate(self, value):
        """
        Validate value against the pattern and additional checks.
        """
        if not value:
            return False, f"{self.pattern_name} cannot be empty"
        
        value = str(value).strip()
        
        # Check regex pattern
        if not self.pattern.match(value):
            return False, f"Invalid {self.pattern_name} format"
        
        # Run additional checks
        for check_func in self.additional_checks:
            is_valid, message = check_func(value)
            if not is_valid:
                return False, message
        
        # Apply formatting if provided
        formatted_value = self.format_func(value) if self.format_func else value
        
        return True, f"Valid {self.pattern_name}: {formatted_value}"

# Create specialized format validators
print("Creating custom format validators:")

# Social Security Number validator
def format_ssn(ssn):
    digits = re.sub(r'\D', '', ssn)
    return f"{digits[:3]}-{digits[3:5]}-{digits[5:]}"

def check_ssn_not_all_same(ssn):
    digits = re.sub(r'\D', '', ssn)
    if len(set(digits)) == 1:
        return False, "SSN cannot have all identical digits"
    return True, "SSN digits are varied"

ssn_validator = FormatValidator(
    r'^\d{3}-?\d{2}-?\d{4}$',
    "Social Security Number",
    format_ssn,
    [check_ssn_not_all_same]
)

# ZIP code validator
def format_zip(zip_code):
    if len(zip_code) == 5:
        return zip_code
    elif len(zip_code) == 9:
        return f"{zip_code[:5]}-{zip_code[5:]}"
    else:
        return zip_code

zip_validator = FormatValidator(
    r'^\d{5}(-?\d{4})?$',
    "ZIP Code",
    format_zip
)

# Test custom validators
validators_to_test = [
    (ssn_validator, ["123-45-6789", "123456789", "111-11-1111", "12345678", ""]),
    (zip_validator, ["12345", "12345-6789", "123456789", "1234", "abcde"])
]

for validator, test_values in validators_to_test:
    print(f"\nTesting {validator.pattern_name}:")
    for test_val in test_values:
        is_valid, message = validator.validate(test_val)
        status = "✅" if is_valid else "❌"
        print(f"  '{test_val}': {status} {message}")

print()

# COMPREHENSIVE FORMAT VALIDATION EXAMPLE
print("=== COMPREHENSIVE FORM VALIDATION EXAMPLE ===")
print()

def validate_user_registration(user_data):
    """
    Comprehensive validation of user registration form.
    """
    results = {}
    all_valid = True
    
    # Validate each field
    fields_to_validate = [
        ('email', validate_email_regex),
        ('phone', validate_phone_us),
        ('password', validate_password_strength),
    ]
    
    for field_name, validator_func in fields_to_validate:
        if field_name in user_data:
            value = user_data[field_name]
            
            if field_name == 'password':
                is_valid, score, issues, message = validator_func(value)
                results[field_name] = {
                    'valid': is_valid,
                    'message': message,
                    'issues': issues
                }
            elif field_name == 'phone':
                is_valid, formatted, message = validator_func(value)
                results[field_name] = {
                    'valid': is_valid,
                    'formatted': formatted if is_valid else value,
                    'message': message
                }
            else:
                is_valid, message = validator_func(value)
                results[field_name] = {
                    'valid': is_valid,
                    'message': message
                }
            
            if not is_valid:
                all_valid = False
        else:
            results[field_name] = {
                'valid': False,
                'message': f"{field_name} is required"
            }
            all_valid = False
    
    return all_valid, results

# Test comprehensive validation
print("Testing comprehensive user registration validation:")

test_registrations = [
    {
        'email': 'john.doe@example.com',
        'phone': '(555) 123-4567', 
        'password': 'MySecure123!'
    },
    {
        'email': 'invalid-email',
        'phone': '555-123-456',
        'password': 'weak'
    },
    {
        'email': 'jane@company.com',
        'phone': '5551234567',
        'password': 'StrongPassword123!'
    }
]

for i, user_data in enumerate(test_registrations, 1):
    print(f"\n--- Registration Attempt {i} ---")
    print(f"Data: {user_data}")
    
    all_valid, results = validate_user_registration(user_data)
    
    print(f"Overall Result: {'✅ VALID' if all_valid else '❌ INVALID'}")
    
    for field, result in results.items():
        status = "✅" if result['valid'] else "❌"
        print(f"  {field}: {status} {result['message']}")
        
        if 'issues' in result and result['issues']:
            for issue in result['issues']:
                print(f"    • {issue}")

print()

print("=== SUMMARY ===")
print()
print("Format Validation Best Practices:")
print("1. Use regular expressions for complex pattern matching")
print("2. Implement multiple layers of validation (pattern + logic)")
print("3. Provide specific error messages for different failure types")
print("4. Consider international formats and variations")
print("5. Validate business logic beyond just format (e.g., Luhn checksum)")
print("6. Sanitize and format data consistently")
print("7. Create reusable validators for common formats")
print("8. Test with edge cases and malicious input")

"""
KEY TAKEAWAYS:
==============
1. Format validation ensures data follows expected patterns and structures
2. Regular expressions are powerful tools for pattern matching
3. Combine pattern matching with business logic validation (e.g., checksums)
4. Different validation approaches suit different complexity levels
5. Consider international variations and edge cases
6. Provide clear, specific error messages for each validation failure
7. Create reusable validation components for consistency

COMMON FORMAT VALIDATION PATTERNS:
===================================
• Email: Complex regex patterns with multiple validation layers
• Phone: Handle multiple formats, country codes, and standardize output  
• Credit Cards: Pattern matching + Luhn algorithm + type identification
• Passwords: Multiple criteria scoring with detailed feedback
• URLs: Protocol, domain, and security pattern validation
• Dates: Format validation + logical date checking
• Postal Codes: Country-specific patterns and formats

IMPLEMENTATION STRATEGIES:
==========================
• Start with basic string analysis, move to regex for complex patterns
• Layer pattern validation with business logic validation
• Create validator classes for reusability and consistency
• Test with both valid and invalid inputs extensively
• Consider user experience - format data for display
• Handle international variations appropriately

SECURITY CONSIDERATIONS:
========================
• Validate input length to prevent buffer overflows
• Check for injection patterns in URLs and text fields
• Use whitelist approaches when possible (valid chars vs invalid chars)
• Sanitize data after validation but before storage/processing

NEXT STEP:
Go to 05-advanced-validation.py to learn complex validation scenarios and security!
"""