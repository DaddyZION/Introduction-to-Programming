"""
Assignment 4 - Example 5: Advanced Validation Techniques
========================================================

This program demonstrates sophisticated validation techniques including
data sanitization, security validation, business rule enforcement, and
comprehensive error handling. These advanced concepts are essential for
building robust, secure, and professional applications.

Key Concepts Demonstrated:
- Data sanitization and cleaning
- Security validation (SQL injection, XSS prevention)
- Business rule validation
- Cross-field validation (interdependent fields)
- Bulk data validation
- Validation pipelines
- Custom validation decorators
- Comprehensive error reporting
"""

import re
import html
import datetime
from typing import List, Dict, Any, Tuple, Optional

print("=== ADVANCED VALIDATION TECHNIQUES ===")
print()

print("Advanced validation goes beyond basic format checking:")
print("• Security: Prevent malicious input and attacks")
print("• Sanitization: Clean and normalize data")
print("• Business Rules: Enforce domain-specific constraints")
print("• Cross-validation: Check relationships between fields")
print("• Data Integrity: Maintain consistency and accuracy")
print()

# DATA SANITIZATION
print("=== DATA SANITIZATION AND CLEANING ===")
print()

def sanitize_text_input(text, max_length=None, allow_html=False):
    """
    Comprehensive text sanitization for user input.
    """
    if not text:
        return "", "Text cannot be empty"
    
    # Convert to string and strip whitespace
    text = str(text).strip()
    
    if not text:
        return "", "Text cannot be only whitespace"
    
    # Length validation
    if max_length and len(text) > max_length:
        return text[:max_length], f"Text truncated to {max_length} characters"
    
    # HTML sanitization
    if not allow_html:
        # Escape HTML characters to prevent XSS
        text = html.escape(text)
        
        # Remove any remaining HTML tags (belt and suspenders approach)
        text = re.sub(r'<[^>]+>', '', text)
    
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove control characters except newlines and tabs
    text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', text)
    
    return text, "Text sanitized successfully"

def sanitize_sql_input(text):
    """
    Basic SQL injection prevention through sanitization.
    Note: In real applications, use parameterized queries instead!
    """
    if not text:
        return "", "Input cannot be empty"
    
    text = str(text).strip()
    
    # Dangerous SQL keywords and characters
    dangerous_patterns = [
        r"'.*'", r'".*"',  # Quoted strings
        r'--.*$',  # SQL comments
        r'/\*.*\*/',  # Block comments
        r';\s*\w+',  # Multiple statements
        r'\b(DROP|DELETE|UPDATE|INSERT|ALTER|CREATE|TRUNCATE)\b',  # DDL/DML
        r'\b(UNION|SELECT|FROM|WHERE|ORDER|GROUP)\b',  # Query keywords
        r'\b(EXEC|EXECUTE|SP_|XP_)\b',  # Stored procedures
        r'[\x00-\x1F]',  # Control characters
    ]
    
    issues = []
    original_text = text
    
    for pattern in dangerous_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            issues.append(f"Potentially dangerous SQL pattern detected: {pattern}")
            # Remove the dangerous pattern
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    
    # Additional character restrictions
    if re.search(r'[<>"\'\\/]', text):
        issues.append("Dangerous characters removed: < > \" ' \\ /")
        text = re.sub(r'[<>"\'\\/]', '', text)
    
    text = text.strip()
    
    if not text and original_text:
        return "", "Input contained only dangerous content and was completely removed"
    
    if issues:
        return text, f"Input sanitized with warnings: {'; '.join(issues)}"
    else:
        return text, "Input is safe"

print("Testing text sanitization:")

test_texts = [
    "Normal text input",
    "<script>alert('xss')</script>",
    "Text with    extra   whitespace",
    "Text\x00with\x1Fcontrol\x7Fcharacters",
    "Text with <b>HTML</b> tags",
    "",
    "   ",
    "Very long text that exceeds normal limits and should be truncated appropriately"
]

for text in test_texts:
    sanitized, message = sanitize_text_input(text, max_length=50)
    print(f"  Input: '{text[:30]}{'...' if len(text) > 30 else ''}'")
    print(f"  Output: '{sanitized}'")
    print(f"  Message: {message}")
    print()

print("Testing SQL injection prevention:")

sql_test_inputs = [
    "normal_username",
    "'; DROP TABLE users; --",
    "admin' OR '1'='1",
    "user<script>alert('xss')</script>",
    "UNION SELECT * FROM passwords",
    "test_user",
    ""
]

for sql_input in sql_test_inputs:
    sanitized, message = sanitize_sql_input(sql_input)
    print(f"  Input: '{sql_input}'")
    print(f"  Output: '{sanitized}'")
    print(f"  Message: {message}")
    print()

# BUSINESS RULE VALIDATION
print("=== BUSINESS RULE VALIDATION ===")
print()

class BusinessRuleValidator:
    """
    Framework for implementing complex business rules.
    """
    
    def __init__(self):
        self.rules = []
    
    def add_rule(self, rule_name, rule_func, error_message):
        """Add a business rule to the validator."""
        self.rules.append({
            'name': rule_name,
            'function': rule_func,
            'error_message': error_message
        })
    
    def validate(self, data):
        """Validate data against all business rules."""
        violations = []
        
        for rule in self.rules:
            try:
                if not rule['function'](data):
                    violations.append({
                        'rule': rule['name'],
                        'message': rule['error_message']
                    })
            except Exception as e:
                violations.append({
                    'rule': rule['name'],
                    'message': f"Rule validation error: {str(e)}"
                })
        
        return len(violations) == 0, violations

# Example: E-commerce order validation
def create_order_validator():
    """Create a business rule validator for e-commerce orders."""
    validator = BusinessRuleValidator()
    
    # Rule 1: Order must have at least one item
    validator.add_rule(
        "minimum_items",
        lambda data: len(data.get('items', [])) > 0,
        "Order must contain at least one item"
    )
    
    # Rule 2: Order total must match sum of item prices
    def validate_order_total(data):
        items = data.get('items', [])
        calculated_total = sum(item.get('price', 0) * item.get('quantity', 0) for item in items)
        declared_total = data.get('total', 0)
        return abs(calculated_total - declared_total) < 0.01  # Allow for rounding
    
    validator.add_rule(
        "total_matches_items",
        validate_order_total,
        "Order total does not match sum of item prices"
    )
    
    # Rule 3: Customer age validation for restricted items
    def validate_age_restrictions(data):
        customer_age = data.get('customer', {}).get('age', 0)
        items = data.get('items', [])
        
        for item in items:
            if item.get('age_restricted', False) and customer_age < 21:
                return False
        return True
    
    validator.add_rule(
        "age_restrictions",
        validate_age_restrictions,
        "Customer must be 21+ to purchase age-restricted items"
    )
    
    # Rule 4: Shipping address required for physical items
    def validate_shipping_address(data):
        items = data.get('items', [])
        has_physical_items = any(not item.get('digital', False) for item in items)
        has_shipping_address = bool(data.get('shipping_address', {}).get('street'))
        
        if has_physical_items and not has_shipping_address:
            return False
        return True
    
    validator.add_rule(
        "shipping_address_required",
        validate_shipping_address,
        "Shipping address required for physical items"
    )
    
    return validator

print("Testing business rule validation:")

order_validator = create_order_validator()

test_orders = [
    {
        # Valid order
        'items': [
            {'name': 'Book', 'price': 19.99, 'quantity': 2, 'digital': False},
            {'name': 'E-book', 'price': 9.99, 'quantity': 1, 'digital': True}
        ],
        'total': 49.97,
        'customer': {'age': 25},
        'shipping_address': {'street': '123 Main St', 'city': 'Anytown'}
    },
    {
        # Invalid: no items
        'items': [],
        'total': 0,
        'customer': {'age': 25},
        'shipping_address': {'street': '123 Main St'}
    },
    {
        # Invalid: total mismatch
        'items': [
            {'name': 'Book', 'price': 19.99, 'quantity': 1, 'digital': False}
        ],
        'total': 25.00,  # Wrong total
        'customer': {'age': 25},
        'shipping_address': {'street': '123 Main St'}
    },
    {
        # Invalid: age restriction
        'items': [
            {'name': 'Wine', 'price': 29.99, 'quantity': 1, 'age_restricted': True, 'digital': False}
        ],
        'total': 29.99,
        'customer': {'age': 18},  # Too young
        'shipping_address': {'street': '123 Main St'}
    },
    {
        # Invalid: missing shipping address
        'items': [
            {'name': 'Book', 'price': 19.99, 'quantity': 1, 'digital': False}
        ],
        'total': 19.99,
        'customer': {'age': 25}
        # Missing shipping_address
    }
]

for i, order in enumerate(test_orders, 1):
    print(f"\n--- Order {i} ---")
    is_valid, violations = order_validator.validate(order)
    
    if is_valid:
        print("✅ Order is valid")
    else:
        print("❌ Order has violations:")
        for violation in violations:
            print(f"  • {violation['rule']}: {violation['message']}")

print()

# CROSS-FIELD VALIDATION
print("=== CROSS-FIELD VALIDATION ===")
print()

def validate_date_range(start_date_str, end_date_str):
    """
    Validate that start date is before end date.
    """
    try:
        start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
        
        if start_date > end_date:
            return False, "Start date must be before end date"
        
        if start_date == end_date:
            return False, "Start date and end date cannot be the same"
        
        # Check for reasonable date range
        date_diff = (end_date - start_date).days
        if date_diff > 365:
            return False, "Date range cannot exceed 365 days"
        
        return True, f"Valid date range: {date_diff} days"
        
    except ValueError as e:
        return False, f"Invalid date format: {str(e)}"

def validate_password_confirmation(password, confirm_password):
    """
    Validate password confirmation matches.
    """
    if password != confirm_password:
        return False, "Password confirmation does not match"
    
    if not password:
        return False, "Password cannot be empty"
    
    return True, "Password confirmation matches"

def validate_address_consistency(data):
    """
    Validate consistency between address fields.
    """
    country = data.get('country', '').upper()
    postal_code = data.get('postal_code', '')
    state = data.get('state', '').upper()
    
    # US-specific validation
    if country == 'US' or country == 'USA':
        # ZIP code validation
        if not re.match(r'^\d{5}(-\d{4})?$', postal_code):
            return False, "US postal code must be in format 12345 or 12345-6789"
        
        # State validation (simplified)
        us_states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 
                     'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                     'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                     'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                     'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        
        if state not in us_states:
            return False, f"'{state}' is not a valid US state code"
    
    # Canada-specific validation
    elif country == 'CA' or country == 'CANADA':
        # Postal code validation
        if not re.match(r'^[A-Z]\d[A-Z] \d[A-Z]\d$', postal_code.upper()):
            return False, "Canadian postal code must be in format A1A 1A1"
        
        # Province validation (simplified)
        ca_provinces = ['AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
        if state not in ca_provinces:
            return False, f"'{state}' is not a valid Canadian province code"
    
    return True, "Address fields are consistent"

print("Testing cross-field validation:")

print("\nDate range validation:")
date_tests = [
    ("2023-01-01", "2023-12-31"),  # Valid
    ("2023-12-31", "2023-01-01"),  # Invalid: reversed
    ("2023-01-01", "2023-01-01"),  # Invalid: same date
    ("2023-01-01", "2024-12-31"),  # Invalid: too long
    ("invalid-date", "2023-12-31"), # Invalid: bad format
]

for start, end in date_tests:
    is_valid, message = validate_date_range(start, end)
    status = "✅" if is_valid else "❌"
    print(f"  {start} to {end}: {status} {message}")

print("\nPassword confirmation validation:")
password_tests = [
    ("MyPassword123!", "MyPassword123!"),  # Valid
    ("MyPassword123!", "MyPassword456!"),  # Invalid: don't match
    ("", ""),  # Invalid: empty
    ("Pass123!", "pass123!"),  # Invalid: case sensitive
]

for password, confirm in password_tests:
    is_valid, message = validate_password_confirmation(password, confirm)
    status = "✅" if is_valid else "❌"
    print(f"  Password match: {status} {message}")

print("\nAddress consistency validation:")
address_tests = [
    {'country': 'US', 'state': 'CA', 'postal_code': '90210'},  # Valid US
    {'country': 'US', 'state': 'XX', 'postal_code': '90210'},  # Invalid state
    {'country': 'US', 'state': 'CA', 'postal_code': 'invalid'},  # Invalid ZIP
    {'country': 'CA', 'state': 'ON', 'postal_code': 'K1A 0A6'},  # Valid Canada
    {'country': 'CA', 'state': 'XX', 'postal_code': 'K1A 0A6'},  # Invalid province
]

for address in address_tests:
    is_valid, message = validate_address_consistency(address)
    status = "✅" if is_valid else "❌"
    print(f"  {address}: {status} {message}")

print()

# VALIDATION PIPELINE
print("=== VALIDATION PIPELINE FRAMEWORK ===")
print()

class ValidationPipeline:
    """
    A framework for chaining multiple validation steps.
    """
    
    def __init__(self, name="Validation Pipeline"):
        self.name = name
        self.steps = []
    
    def add_step(self, step_name, validator_func, required=True, depends_on=None):
        """Add a validation step to the pipeline."""
        self.steps.append({
            'name': step_name,
            'validator': validator_func,
            'required': required,
            'depends_on': depends_on
        })
    
    def validate(self, data):
        """Run the complete validation pipeline."""
        results = {}
        overall_valid = True
        
        for step in self.steps:
            step_name = step['name']
            validator = step['validator']
            required = step['required']
            depends_on = step['depends_on']
            
            # Check dependencies
            if depends_on:
                if isinstance(depends_on, str):
                    depends_on = [depends_on]
                
                dependency_failed = False
                for dep in depends_on:
                    if dep not in results or not results[dep]['valid']:
                        dependency_failed = True
                        break
                
                if dependency_failed:
                    results[step_name] = {
                        'valid': False,
                        'message': f"Skipped due to failed dependency: {depends_on}",
                        'skipped': True
                    }
                    if required:
                        overall_valid = False
                    continue
            
            # Run validation step
            try:
                is_valid, message = validator(data)
                results[step_name] = {
                    'valid': is_valid,
                    'message': message,
                    'skipped': False
                }
                
                if not is_valid and required:
                    overall_valid = False
                    
            except Exception as e:
                results[step_name] = {
                    'valid': False,
                    'message': f"Validation error: {str(e)}",
                    'skipped': False
                }
                if required:
                    overall_valid = False
        
        return overall_valid, results

# Create user registration validation pipeline
def create_user_registration_pipeline():
    """Create a comprehensive user registration validation pipeline."""
    pipeline = ValidationPipeline("User Registration")
    
    # Step 1: Basic data presence
    def check_required_fields(data):
        required = ['username', 'email', 'password', 'confirm_password', 'age']
        missing = [field for field in required if not data.get(field)]
        
        if missing:
            return False, f"Missing required fields: {', '.join(missing)}"
        return True, "All required fields present"
    
    pipeline.add_step("required_fields", check_required_fields, required=True)
    
    # Step 2: Username validation
    def validate_username(data):
        username = data.get('username', '')
        
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if len(username) > 20:
            return False, "Username cannot exceed 20 characters"
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        
        # Simulate checking if username is taken
        taken_usernames = ['admin', 'root', 'test', 'user123']
        if username.lower() in taken_usernames:
            return False, "Username is already taken"
        
        return True, f"Username '{username}' is available"
    
    pipeline.add_step("username", validate_username, required=True, depends_on="required_fields")
    
    # Step 3: Email validation
    def validate_email_step(data):
        email = data.get('email', '')
        # Using our previous email validation function
        return validate_email_regex(email)
    
    pipeline.add_step("email", validate_email_step, required=True, depends_on="required_fields")
    
    # Step 4: Password validation
    def validate_password_step(data):
        password = data.get('password', '')
        from validate_password_strength import validate_password_strength  # Would import from previous function
        
        # Simplified password validation for this example
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        if not (has_upper and has_lower and has_digit):
            return False, "Password must contain uppercase, lowercase, and digit"
        
        return True, "Password meets requirements"
    
    pipeline.add_step("password", validate_password_step, required=True, depends_on="required_fields")
    
    # Step 5: Password confirmation
    def validate_password_confirmation_step(data):
        password = data.get('password', '')
        confirm = data.get('confirm_password', '')
        return validate_password_confirmation(password, confirm)
    
    pipeline.add_step("password_confirm", validate_password_confirmation_step, 
                     required=True, depends_on=["required_fields", "password"])
    
    # Step 6: Age validation
    def validate_age_step(data):
        try:
            age = int(data.get('age', 0))
            if age < 13:
                return False, "Must be at least 13 years old"
            if age > 120:
                return False, "Age cannot exceed 120"
            return True, f"Age {age} is valid"
        except (ValueError, TypeError):
            return False, "Age must be a valid number"
    
    pipeline.add_step("age", validate_age_step, required=True, depends_on="required_fields")
    
    return pipeline

print("Testing validation pipeline:")

registration_pipeline = create_user_registration_pipeline()

test_registrations = [
    {
        # Valid registration
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'SecurePass123',
        'confirm_password': 'SecurePass123',
        'age': '25'
    },
    {
        # Invalid: missing fields
        'username': 'incomplete',
        'email': 'user@example.com'
        # Missing password, confirm_password, age
    },
    {
        # Invalid: password issues
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'weak',
        'confirm_password': 'different',
        'age': '30'
    },
    {
        # Invalid: taken username
        'username': 'admin',  # Taken username
        'email': 'admin@example.com',
        'password': 'SecurePass123',
        'confirm_password': 'SecurePass123',
        'age': '25'
    }
]

for i, registration in enumerate(test_registrations, 1):
    print(f"\n--- Registration {i} ---")
    print(f"Data: {registration}")
    
    is_valid, results = registration_pipeline.validate(registration)
    
    print(f"Overall Result: {'✅ VALID' if is_valid else '❌ INVALID'}")
    
    for step_name, result in results.items():
        if result['skipped']:
            print(f"  {step_name}: ⏭️ {result['message']}")
        else:
            status = "✅" if result['valid'] else "❌"
            print(f"  {step_name}: {status} {result['message']}")

print()

print("=== SUMMARY ===")
print()
print("Advanced Validation Best Practices:")
print("1. Sanitize all input data to prevent security vulnerabilities")
print("2. Implement business rule validation for domain-specific constraints")
print("3. Use cross-field validation for interdependent data")
print("4. Create validation pipelines for complex, multi-step processes")
print("5. Provide comprehensive error reporting and feedback")
print("6. Consider security implications of all validation logic")
print("7. Test with malicious and edge-case inputs")
print("8. Use dependency management in validation workflows")

"""
KEY TAKEAWAYS:
==============
1. Advanced validation encompasses security, business rules, and data integrity
2. Data sanitization prevents security vulnerabilities like XSS and SQL injection
3. Business rule validation enforces domain-specific constraints and logic
4. Cross-field validation ensures consistency between related data fields
5. Validation pipelines manage complex, multi-step validation processes
6. Comprehensive error reporting helps users understand and fix issues
7. Security considerations must be built into every validation layer

ADVANCED VALIDATION PATTERNS:
=============================
• Sanitization: Clean input data while preserving valid content
• Business Rules: Domain-specific validation logic and constraints
• Cross-Field: Validate relationships and dependencies between fields
• Pipelines: Chain validation steps with dependency management
• Security: Prevent injection attacks and malicious input
• Error Reporting: Comprehensive feedback for complex validation failures

SECURITY CONSIDERATIONS:
========================
• Always sanitize user input before processing or storage
• Use whitelist approaches when possible (allowed vs disallowed)
• Escape HTML/XML content to prevent XSS attacks  
• Validate SQL input to prevent injection (use parameterized queries)
• Check for malicious patterns and suspicious content
• Implement rate limiting and input length restrictions
• Log validation failures for security monitoring

BUSINESS APPLICATIONS:
======================
• E-commerce: Order validation, payment processing, inventory checks
• User Management: Registration, profile updates, permission validation
• Financial: Transaction validation, compliance checks, audit trails
• Healthcare: Patient data validation, regulatory compliance
• Education: Student records, grade validation, enrollment rules

NEXT STEP:
Go to 06-complete-program.py to see all validation concepts in one comprehensive system!
"""