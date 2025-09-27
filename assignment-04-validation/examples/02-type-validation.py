"""
Assignment 4 - Example 2: Type Validation and Conversion
=======================================================

This program demonstrates type validation - ensuring data is the correct
type and handling type conversion safely. Type validation is crucial because
Python is dynamically typed, meaning variables can hold any type of data.

Key Concepts Demonstrated:
- Type checking and validation
- Safe type conversion with try-catch
- Handling different numeric types
- String to number conversion
- Boolean validation and conversion
- Type coercion best practices
- Custom type validators
"""

print("=== TYPE VALIDATION AND CONVERSION ===")
print()

print("Python variables can hold any type of data:")
print("• Numbers: 42, 3.14, -7")
print("• Strings: 'hello', 'world'")
print("• Booleans: True, False")
print("• Lists, dictionaries, and more...")
print()

print("But your program often expects SPECIFIC types!")
print("Type validation ensures data is the right type before processing.")
print()

# UNDERSTANDING PYTHON TYPES
print("=== UNDERSTANDING PYTHON TYPES ===")
print()

# Demonstrate different types
sample_data = [
    42,           # int
    3.14,         # float
    "hello",      # str
    True,         # bool
    [1, 2, 3],    # list
    None,         # NoneType
    "42",         # str (looks like number)
    "3.14",       # str (looks like float)
    "true",       # str (looks like boolean)
    "",           # str (empty)
]

print("Sample data and their types:")
for data in sample_data:
    data_type = type(data).__name__
    print(f"  {repr(data):>10} -> {data_type}")

print()

# TYPE CHECKING FUNCTIONS
print("=== BUILT-IN TYPE CHECKING ===")
print()

print("Python provides built-in type checking functions:")

def demonstrate_type_checking():
    test_value = "42"
    
    print(f"Testing value: {repr(test_value)}")
    print(f"  type(value): {type(test_value)}")
    print(f"  isinstance(value, str): {isinstance(test_value, str)}")
    print(f"  isinstance(value, int): {isinstance(test_value, int)}")
    print(f"  str.isdigit(): {test_value.isdigit()}")
    print(f"  str.isnumeric(): {test_value.isnumeric()}")
    print(f"  str.isalpha(): {test_value.isalpha()}")
    print(f"  str.isalnum(): {test_value.isalnum()}")

demonstrate_type_checking()
print()

# SAFE INTEGER CONVERSION
print("=== SAFE INTEGER CONVERSION ===")
print()

def safe_int_conversion(value, default=None):
    """
    Safely convert a value to integer.
    Returns tuple: (success, converted_value, error_message)
    """
    
    # Handle None
    if value is None:
        return False, default, "Value is None"
    
    # If already an integer
    if isinstance(value, int):
        return True, value, "Already an integer"
    
    # If it's a float, check if it's a whole number
    if isinstance(value, float):
        if value.is_integer():
            return True, int(value), "Converted from whole number float"
        else:
            return False, default, f"Float {value} is not a whole number"
    
    # If it's a boolean
    if isinstance(value, bool):
        return True, int(value), f"Converted boolean {value} to {int(value)}"
    
    # Try to convert string
    if isinstance(value, str):
        # Remove whitespace
        value = value.strip()
        
        # Check for empty string
        if not value:
            return False, default, "Empty string cannot be converted to integer"
        
        # Try conversion
        try:
            result = int(value)
            return True, result, f"Converted string '{value}' to integer"
        except ValueError:
            # Maybe it's a float string?
            try:
                float_val = float(value)
                if float_val.is_integer():
                    return True, int(float_val), f"Converted float string '{value}' to integer"
                else:
                    return False, default, f"String '{value}' represents a non-whole number"
            except ValueError:
                return False, default, f"String '{value}' is not a valid number"
    
    # Unsupported type
    return False, default, f"Cannot convert {type(value).__name__} to integer"

# Test integer conversion
print("Testing safe integer conversion:")

test_values = [
    42,           # int
    3.0,          # whole number float
    3.14,         # decimal float
    True,         # boolean
    False,        # boolean
    "42",         # string number
    "  -17  ",    # string with whitespace
    "3.0",        # string float (whole)
    "3.14",       # string float (decimal)
    "abc",        # invalid string
    "",           # empty string
    None,         # None
    [1, 2, 3],    # list
]

for test_value in test_values:
    success, result, message = safe_int_conversion(test_value)
    status = "✅ SUCCESS" if success else "❌ FAILED"
    
    print(f"Input: {repr(test_value):>12}")
    print(f"  Status: {status}")
    print(f"  Result: {result}")
    print(f"  Message: {message}")
    print()

# SAFE FLOAT CONVERSION
print("=== SAFE FLOAT CONVERSION ===")
print()

def safe_float_conversion(value, default=None):
    """
    Safely convert a value to float.
    Returns tuple: (success, converted_value, error_message)
    """
    
    # Handle None
    if value is None:
        return False, default, "Value is None"
    
    # If already a float or int
    if isinstance(value, (int, float)):
        return True, float(value), f"Converted {type(value).__name__} to float"
    
    # If it's a boolean
    if isinstance(value, bool):
        return True, float(value), f"Converted boolean {value} to {float(value)}"
    
    # Try to convert string
    if isinstance(value, str):
        # Remove whitespace
        value = value.strip()
        
        # Check for empty string
        if not value:
            return False, default, "Empty string cannot be converted to float"
        
        # Try conversion
        try:
            result = float(value)
            # Check for special values
            if result == float('inf'):
                return False, default, "Value represents positive infinity"
            elif result == float('-inf'):
                return False, default, "Value represents negative infinity"
            elif result != result:  # NaN check
                return False, default, "Value represents NaN (Not a Number)"
            else:
                return True, result, f"Converted string '{value}' to float"
        except ValueError:
            return False, default, f"String '{value}' is not a valid number"
    
    # Unsupported type
    return False, default, f"Cannot convert {type(value).__name__} to float"

# Test float conversion
print("Testing safe float conversion:")

test_float_values = [
    42,           # int
    3.14,         # float
    True,         # boolean
    "3.14159",    # string float
    "  -42.5  ",  # string with whitespace
    "1.5e-10",    # scientific notation
    "inf",        # infinity
    "-inf",       # negative infinity
    "nan",        # not a number
    "abc",        # invalid string
    "",           # empty string
    None          # None
]

for test_value in test_float_values:
    success, result, message = safe_float_conversion(test_value)
    status = "✅ SUCCESS" if success else "❌ FAILED"
    
    print(f"Input: {repr(test_value):>12}")
    print(f"  Status: {status}")
    print(f"  Result: {result}")
    print(f"  Message: {message}")
    print()

# BOOLEAN VALIDATION
print("=== BOOLEAN VALIDATION ===")
print()

def safe_boolean_conversion(value, default=None):
    """
    Safely convert a value to boolean with intelligent interpretation.
    Returns tuple: (success, converted_value, error_message)
    """
    
    # Handle None
    if value is None:
        return False, default, "Value is None"
    
    # If already a boolean
    if isinstance(value, bool):
        return True, value, "Already a boolean"
    
    # If it's a number
    if isinstance(value, (int, float)):
        return True, bool(value), f"Converted number {value} to {bool(value)}"
    
    # String conversion with intelligent interpretation
    if isinstance(value, str):
        value = value.strip().lower()
        
        # Empty string
        if not value:
            return False, default, "Empty string cannot be converted to boolean"
        
        # True values
        if value in ['true', '1', 'yes', 'on', 'y', 't']:
            return True, True, f"String '{value}' interpreted as True"
        
        # False values
        if value in ['false', '0', 'no', 'off', 'n', 'f']:
            return True, False, f"String '{value}' interpreted as False"
        
        # Unknown string
        return False, default, f"String '{value}' cannot be interpreted as boolean"
    
    # Use Python's built-in truthiness for other types
    try:
        result = bool(value)
        return True, result, f"Used truthiness: {type(value).__name__} -> {result}"
    except:
        return False, default, f"Cannot convert {type(value).__name__} to boolean"

# Test boolean conversion
print("Testing safe boolean conversion:")

test_bool_values = [
    True,         # boolean
    False,        # boolean
    1,            # int (truthy)
    0,            # int (falsy)
    -1,           # int (truthy)
    3.14,         # float (truthy)
    0.0,          # float (falsy)
    "true",       # string true
    "TRUE",       # string true (uppercase)
    "false",      # string false
    "yes",        # string true variant
    "no",         # string false variant
    "1",          # string numeric true
    "0",          # string numeric false
    "maybe",      # ambiguous string
    "",           # empty string
    [1, 2, 3],    # non-empty list (truthy)
    [],           # empty list (falsy)
    None          # None
]

for test_value in test_bool_values:
    success, result, message = safe_boolean_conversion(test_value)
    status = "✅ SUCCESS" if success else "❌ FAILED"
    
    print(f"Input: {repr(test_value):>12}")
    print(f"  Status: {status}")
    print(f"  Result: {result}")
    print(f"  Message: {message}")
    print()

# COMPREHENSIVE TYPE VALIDATOR
print("=== COMPREHENSIVE TYPE VALIDATOR ===")
print()

class TypeValidator:
    """
    A comprehensive type validation class with multiple conversion methods.
    """
    
    @staticmethod
    def validate_and_convert(value, target_type, strict=False):
        """
        Validate and convert value to target type.
        
        Args:
            value: The value to validate/convert
            target_type: The target type (int, float, str, bool)
            strict: If True, only allow exact type matches
            
        Returns:
            tuple: (success, converted_value, error_message)
        """
        
        if target_type == int:
            if strict and not isinstance(value, int):
                return False, None, f"Strict mode: expected int, got {type(value).__name__}"
            return safe_int_conversion(value)
            
        elif target_type == float:
            if strict and not isinstance(value, float):
                return False, None, f"Strict mode: expected float, got {type(value).__name__}"
            return safe_float_conversion(value)
            
        elif target_type == bool:
            if strict and not isinstance(value, bool):
                return False, None, f"Strict mode: expected bool, got {type(value).__name__}"
            return safe_boolean_conversion(value)
            
        elif target_type == str:
            if strict and not isinstance(value, str):
                return False, None, f"Strict mode: expected str, got {type(value).__name__}"
            try:
                result = str(value)
                return True, result, f"Converted {type(value).__name__} to string"
            except:
                return False, None, f"Cannot convert {type(value).__name__} to string"
        
        else:
            return False, None, f"Unsupported target type: {target_type}"

# Test comprehensive type validator
print("Testing comprehensive type validator:")

validator = TypeValidator()

test_cases = [
    ("42", int, False),      # String to int (relaxed)
    ("42", int, True),       # String to int (strict) - should fail
    (42, int, True),         # Int to int (strict) - should pass
    ("3.14", float, False),  # String to float (relaxed)
    (True, int, False),      # Bool to int (relaxed)
    ("yes", bool, False),    # String to bool (relaxed)
    (123, str, False),       # Int to string (relaxed)
]

for value, target_type, strict_mode in test_cases:
    success, result, message = validator.validate_and_convert(value, target_type, strict_mode)
    status = "✅ SUCCESS" if success else "❌ FAILED"
    strict_text = " (STRICT)" if strict_mode else " (RELAXED)"
    
    print(f"Convert {repr(value)} to {target_type.__name__}{strict_text}")
    print(f"  Status: {status}")
    print(f"  Result: {repr(result)}")
    print(f"  Message: {message}")
    print()

# REAL-WORLD VALIDATION EXAMPLES
print("=== REAL-WORLD TYPE VALIDATION EXAMPLES ===")
print()

# Example 1: Age validation with type checking
print("Example 1: Age Validation with Type Checking")

def validate_age_with_types(age_input):
    """
    Validate age with comprehensive type checking.
    """
    
    # First, try to convert to integer
    success, age, message = safe_int_conversion(age_input)
    
    if not success:
        return False, None, f"Type error: {message}"
    
    # Now validate the range
    if age < 0:
        return False, None, "Age cannot be negative"
    elif age > 150:
        return False, None, "Age cannot exceed 150"
    elif age == 0:
        return True, age, "Valid age (newborn)"
    else:
        return True, age, "Valid age"

# Test age validation
print("\nTesting age validation with type checking:")

age_test_values = [
    "25",         # Valid string
    25,           # Valid int
    25.0,         # Valid float (whole)
    25.5,         # Invalid float (decimal)
    "-5",         # Invalid (negative)
    "abc",        # Invalid (not numeric)
    True,         # Converts to 1
    None          # Invalid
]

for test_age in age_test_values:
    success, result, message = validate_age_with_types(test_age)
    status = "✅ VALID" if success else "❌ INVALID"
    
    print(f"Input: {repr(test_age):>8} -> {status}")
    print(f"  Result: {result}")
    print(f"  Message: {message}")
    print()

# Example 2: Grade validation
print("Example 2: Grade Validation with Type Checking")

def validate_grade_with_types(grade_input):
    """
    Validate grade with type checking (supports both percentage and GPA).
    """
    
    # Try to convert to float
    success, grade, message = safe_float_conversion(grade_input)
    
    if not success:
        return False, None, f"Type error: {message}"
    
    # Determine if it's percentage (0-100) or GPA (0-4.0)
    if 0 <= grade <= 4.0:
        grade_type = "GPA"
        if grade > 4.0:
            return False, None, "GPA cannot exceed 4.0"
    elif 0 <= grade <= 100:
        grade_type = "Percentage"
        if grade > 100:
            return False, None, "Percentage cannot exceed 100%"
    else:
        if grade < 0:
            return False, None, "Grade cannot be negative"
        else:
            return False, None, "Grade seems invalid (>100 and >4.0)"
    
    return True, grade, f"Valid {grade_type}: {grade}"

# Test grade validation
print("\nTesting grade validation:")

grade_test_values = [
    "95",         # Percentage
    "3.7",        # GPA
    95,           # Int percentage
    3.7,          # Float GPA
    "105",        # Invalid percentage
    "4.5",        # Invalid GPA
    "-10",        # Negative
    "A+",         # Letter grade (invalid for this validator)
    None          # None
]

for test_grade in grade_test_values:
    success, result, message = validate_grade_with_types(test_grade)
    status = "✅ VALID" if success else "❌ INVALID"
    
    print(f"Input: {repr(test_grade):>8} -> {status}")
    print(f"  Result: {result}")
    print(f"  Message: {message}")
    print()

# ADVANCED TYPE VALIDATION PATTERNS
print("=== ADVANCED TYPE VALIDATION PATTERNS ===")
print()

# Example: Multi-type validator
print("Multi-Type Input Handler")

def handle_multi_type_input(value, allowed_types):
    """
    Handle input that could be one of several types.
    
    Args:
        value: Input value
        allowed_types: List of allowed types in order of preference
        
    Returns:
        tuple: (success, converted_value, detected_type, message)
    """
    
    for target_type in allowed_types:
        if target_type == int:
            success, result, message = safe_int_conversion(value)
        elif target_type == float:
            success, result, message = safe_float_conversion(value)
        elif target_type == bool:
            success, result, message = safe_boolean_conversion(value)
        elif target_type == str:
            success, result, message = True, str(value), "Converted to string"
        else:
            continue
        
        if success:
            return True, result, target_type, f"Converted to {target_type.__name__}: {message}"
    
    return False, None, None, f"Could not convert to any allowed type: {[t.__name__ for t in allowed_types]}"

# Test multi-type handler
print("\nTesting multi-type input handler:")

multi_type_tests = [
    ("42", [int, float, str]),        # Should convert to int
    ("3.14", [int, float, str]),      # Should convert to float (int fails)
    ("hello", [int, float, str]),     # Should convert to string (others fail)
    ("true", [bool, int, str]),       # Should convert to boolean
    ("invalid", [int, float]),        # Should fail (no string allowed)
]

for test_value, allowed_types in multi_type_tests:
    success, result, detected_type, message = handle_multi_type_input(test_value, allowed_types)
    status = "✅ SUCCESS" if success else "❌ FAILED"
    
    print(f"Input: {repr(test_value):>10}")
    print(f"  Allowed: {[t.__name__ for t in allowed_types]}")
    print(f"  Status: {status}")
    print(f"  Result: {repr(result)} ({detected_type.__name__ if detected_type else 'None'})")
    print(f"  Message: {message}")
    print()

# INPUT COLLECTION WITH TYPE VALIDATION
print("=== INPUT COLLECTION WITH TYPE VALIDATION ===")
print()

def get_typed_input(prompt, target_type, validator=None, max_attempts=3):
    """
    Get input from user with type validation and optional custom validator.
    
    Args:
        prompt: Input prompt to show user
        target_type: Expected type (int, float, str, bool)
        validator: Optional custom validation function
        max_attempts: Maximum number of attempts
        
    Returns:
        Validated and converted value, or None if failed
    """
    
    type_name = target_type.__name__
    
    for attempt in range(max_attempts):
        try:
            user_input = input(f"{prompt} (expected {type_name}): ")
            
            # Convert to target type
            if target_type == int:
                success, value, message = safe_int_conversion(user_input)
            elif target_type == float:
                success, value, message = safe_float_conversion(user_input)
            elif target_type == bool:
                success, value, message = safe_boolean_conversion(user_input)
            elif target_type == str:
                success, value, message = True, user_input, "String input"
            else:
                print(f"❌ Unsupported type: {type_name}")
                continue
            
            if not success:
                print(f"❌ {message}")
                if attempt < max_attempts - 1:
                    print(f"Please try again. ({max_attempts - attempt - 1} attempts remaining)")
                continue
            
            # Apply custom validator if provided
            if validator:
                try:
                    is_valid, error_msg = validator(value)
                    if not is_valid:
                        print(f"❌ {error_msg}")
                        if attempt < max_attempts - 1:
                            print(f"Please try again. ({max_attempts - attempt - 1} attempts remaining)")
                        continue
                except Exception as e:
                    print(f"❌ Validation error: {e}")
                    continue
            
            print(f"✅ Valid {type_name}: {value}")
            return value
            
        except KeyboardInterrupt:
            print("\n❌ Input cancelled by user")
            return None
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            continue
    
    print(f"❌ Failed to get valid input after {max_attempts} attempts")
    return None

# Example custom validators
def age_validator(age):
    """Custom validator for age"""
    if age < 0:
        return False, "Age cannot be negative"
    elif age > 150:
        return False, "Age cannot exceed 150"
    else:
        return True, "Valid age"

def grade_validator(grade):
    """Custom validator for percentage grades"""
    if grade < 0:
        return False, "Grade cannot be negative"
    elif grade > 100:
        return False, "Grade cannot exceed 100%"
    else:
        return True, "Valid grade"

print("Example: Type-validated input collection")
print("(This would normally be interactive)")

# Simulate the input collection process
print("\nExample usage:")
print("age = get_typed_input('Enter age', int, age_validator)")
print("grade = get_typed_input('Enter grade', float, grade_validator)")
print("name = get_typed_input('Enter name', str)")

print()

print("=== SUMMARY ===")
print()
print("Type Validation Key Points:")
print("1. Always validate types before processing data")
print("2. Use safe conversion functions that handle errors")
print("3. Provide meaningful error messages for type mismatches")
print("4. Consider what types are acceptable for each input")
print("5. Handle edge cases (None, empty strings, special floats)")
print("6. Use strict vs relaxed validation based on requirements")
print("7. Combine type validation with business rule validation")
print("8. Test with various input types and edge cases")

"""
KEY TAKEAWAYS:
==============
1. Type validation prevents runtime errors and data corruption
2. Safe conversion functions handle errors gracefully
3. Python's dynamic typing requires explicit type checking
4. Consider multiple acceptable input types (int/float for numbers)
5. Provide clear error messages for type conversion failures
6. Use isinstance() and type checking methods appropriately
7. Handle special cases (None, infinity, NaN) explicitly

TYPE CONVERSION STRATEGIES:
===========================
• Strict validation: Only allow exact type matches
• Relaxed validation: Allow reasonable conversions (string "42" -> int 42)
• Multi-type inputs: Accept several types and convert to best match
• Intelligent interpretation: "yes"/"no" -> boolean, etc.

COMMON PITFALLS:
================
• Not checking for None values
• Assuming string inputs are always valid numbers
• Forgetting about floating-point special values (inf, nan)
• Not handling empty strings appropriately  
• Mixing up truthiness with actual boolean values
• Not considering locale-specific number formats

NEXT STEP:
Go to 03-range-validation.py to learn about boundary and limit checking!
"""