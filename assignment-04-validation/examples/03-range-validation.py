"""
Assignment 4 - Example 3: Range Validation and Boundary Checking
================================================================

This program demonstrates how to validate that numeric values fall within
acceptable ranges. Range validation is crucial for ensuring data makes sense
in your application's context and preventing logical errors.

Key Concepts Demonstrated:
- Numeric range validation (min/max bounds)
- Age validation with realistic limits
- Price and currency validation
- Percentage and ratio validation
- Date and time range checking
- Custom range validation functions
- Boundary condition testing
- Error messaging for range violations
"""

print("=== RANGE VALIDATION AND BOUNDARY CHECKING ===")
print()

print("Range validation ensures numbers are within acceptable limits:")
print("• Age: 0-120 years (realistic human lifespan)")
print("• Price: $0.01-$999,999.99 (reasonable product prices)")
print("• Percentage: 0-100% (valid percentage range)")
print("• Grade: 0-100 points (standard grading scale)")
print()

# BASIC RANGE VALIDATION PATTERNS
print("=== BASIC RANGE VALIDATION PATTERNS ===")
print()

def validate_age(age):
    """
    Validate age with realistic human limits.
    Returns: (is_valid, error_message)
    """
    try:
        age_num = float(age)
        
        # Check if it's a whole number (ages are typically integers)
        if age_num != int(age_num):
            return False, "Age must be a whole number"
        
        age_int = int(age_num)
        
        # Range validation
        if age_int < 0:
            return False, "Age cannot be negative"
        elif age_int > 120:
            return False, "Age cannot exceed 120 years"
        elif age_int == 0:
            return False, "Age must be at least 1 year"
        else:
            return True, f"Valid age: {age_int}"
            
    except (ValueError, TypeError):
        return False, "Age must be a number"

# Test age validation
print("Testing age validation:")

test_ages = ["25", "0", "-5", "150", "30.5", "abc", "18", ""]

for test_age in test_ages:
    is_valid, message = validate_age(test_age)
    status = "✅" if is_valid else "❌"
    print(f"  Age '{test_age}': {status} {message}")

print()

# PRICE RANGE VALIDATION
print("=== PRICE RANGE VALIDATION ===")
print()

def validate_price(price_str):
    """
    Validate price with reasonable commercial limits.
    Returns: (is_valid, cleaned_price, error_message)
    """
    try:
        # Remove common price formatting
        cleaned = price_str.strip().replace('$', '').replace(',', '')
        
        if not cleaned:
            return False, 0, "Price cannot be empty"
        
        price = float(cleaned)
        
        # Range validation
        if price < 0:
            return False, price, "Price cannot be negative"
        elif price == 0:
            return False, price, "Price must be greater than $0.00"
        elif price < 0.01:
            return False, price, "Price must be at least $0.01 (minimum currency unit)"
        elif price > 999999.99:
            return False, price, "Price cannot exceed $999,999.99"
        else:
            # Round to 2 decimal places for currency
            rounded_price = round(price, 2)
            return True, rounded_price, f"Valid price: ${rounded_price:.2f}"
            
    except (ValueError, TypeError):
        return False, 0, "Price must be a valid number"

print("Testing price validation:")

test_prices = ["$19.99", "0", "-10.50", "$1,234.56", "999999", "1000000", "abc", "0.001"]

for test_price in test_prices:
    is_valid, price, message = validate_price(test_price)
    status = "✅" if is_valid else "❌"
    print(f"  Price '{test_price}': {status} {message}")

print()

# PERCENTAGE VALIDATION
print("=== PERCENTAGE VALIDATION ===")
print()

def validate_percentage(percent_str, allow_over_100=False):
    """
    Validate percentage values.
    allow_over_100: Some contexts allow percentages over 100% (like growth rates)
    """
    try:
        # Remove % symbol if present
        cleaned = percent_str.strip().replace('%', '')
        
        if not cleaned:
            return False, 0, "Percentage cannot be empty"
        
        percent = float(cleaned)
        
        # Range validation
        if percent < 0:
            return False, percent, "Percentage cannot be negative"
        elif not allow_over_100 and percent > 100:
            return False, percent, "Percentage cannot exceed 100%"
        elif allow_over_100 and percent > 1000:  # Reasonable upper limit for growth
            return False, percent, "Percentage seems unreasonably high (>1000%)"
        else:
            return True, percent, f"Valid percentage: {percent}%"
            
    except (ValueError, TypeError):
        return False, 0, "Percentage must be a valid number"

print("Testing percentage validation (standard 0-100%):")

test_percentages = ["85%", "100", "0", "105", "-10", "abc", "50.5"]

for test_percent in test_percentages:
    is_valid, percent, message = validate_percentage(test_percent)
    status = "✅" if is_valid else "❌"
    print(f"  Percentage '{test_percent}': {status} {message}")

print("\nTesting percentage validation (allowing over 100%):")

growth_rates = ["150%", "200", "500", "1200", "75"]

for rate in growth_rates:
    is_valid, percent, message = validate_percentage(rate, allow_over_100=True)
    status = "✅" if is_valid else "❌"
    print(f"  Growth rate '{rate}': {status} {message}")

print()

# GRADE VALIDATION WITH DIFFERENT SCALES
print("=== GRADE VALIDATION WITH DIFFERENT SCALES ===")
print()

def validate_grade(grade_str, scale="100"):
    """
    Validate grades on different scales.
    Supported scales: "100" (0-100), "4.0" (0.0-4.0), "letter" (A,B,C,D,F)
    """
    if scale == "100":
        try:
            grade = float(grade_str)
            
            if grade < 0:
                return False, "Grade cannot be negative"
            elif grade > 100:
                return False, "Grade cannot exceed 100 points"
            else:
                return True, f"Valid grade: {grade}/100"
                
        except (ValueError, TypeError):
            return False, "Grade must be a number"
    
    elif scale == "4.0":
        try:
            grade = float(grade_str)
            
            if grade < 0.0:
                return False, "GPA cannot be negative"
            elif grade > 4.0:
                return False, "GPA cannot exceed 4.0"
            else:
                return True, f"Valid GPA: {grade:.2f}/4.0"
                
        except (ValueError, TypeError):
            return False, "GPA must be a number"
    
    elif scale == "letter":
        grade_upper = grade_str.strip().upper()
        valid_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
        
        if grade_upper in valid_grades:
            return True, f"Valid letter grade: {grade_upper}"
        else:
            return False, f"Invalid letter grade. Valid grades: {', '.join(valid_grades)}"
    
    else:
        return False, "Unknown grading scale"

print("Testing grade validation on 100-point scale:")
test_grades_100 = ["85", "100", "0", "105", "-10", "92.5"]

for grade in test_grades_100:
    is_valid, message = validate_grade(grade, "100")
    status = "✅" if is_valid else "❌"
    print(f"  Grade '{grade}': {status} {message}")

print("\nTesting GPA validation on 4.0 scale:")
test_gpas = ["3.7", "4.0", "0.0", "4.5", "-1.0", "2.85"]

for gpa in test_gpas:
    is_valid, message = validate_grade(gpa, "4.0")
    status = "✅" if is_valid else "❌"
    print(f"  GPA '{gpa}': {status} {message}")

print("\nTesting letter grade validation:")
test_letters = ["A", "B+", "C-", "F", "Z", "a", "D+"]

for letter in test_letters:
    is_valid, message = validate_grade(letter, "letter")
    status = "✅" if is_valid else "❌"
    print(f"  Letter '{letter}': {status} {message}")

print()

# DATE RANGE VALIDATION
print("=== DATE RANGE VALIDATION ===")
print()

def validate_year(year_str, min_year=1900, max_year=2030):
    """
    Validate year within reasonable bounds.
    """
    try:
        year = int(year_str)
        
        if year < min_year:
            return False, f"Year cannot be before {min_year}"
        elif year > max_year:
            return False, f"Year cannot be after {max_year}"
        else:
            return True, f"Valid year: {year}"
            
    except (ValueError, TypeError):
        return False, "Year must be a valid integer"

def validate_month(month_str):
    """
    Validate month (1-12).
    """
    try:
        month = int(month_str)
        
        if month < 1:
            return False, "Month must be at least 1"
        elif month > 12:
            return False, "Month cannot exceed 12"
        else:
            month_names = ["", "January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]
            return True, f"Valid month: {month} ({month_names[month]})"
            
    except (ValueError, TypeError):
        return False, "Month must be a valid integer"

def validate_day(day_str, month=None, year=None):
    """
    Validate day with consideration for month/year (simplified).
    """
    try:
        day = int(day_str)
        
        if day < 1:
            return False, "Day must be at least 1"
        
        # Simplified day validation - in practice, you'd check for leap years, etc.
        if month:
            days_in_month = {
                1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
            }
            
            max_day = days_in_month.get(month, 31)
            if day > max_day:
                return False, f"Day cannot exceed {max_day} for the given month"
        else:
            if day > 31:
                return False, "Day cannot exceed 31"
        
        return True, f"Valid day: {day}"
        
    except (ValueError, TypeError):
        return False, "Day must be a valid integer"

print("Testing date component validation:")

print("\nYears:")
test_years = ["2023", "1899", "2031", "abc", "2000"]
for year in test_years:
    is_valid, message = validate_year(year)
    status = "✅" if is_valid else "❌"
    print(f"  Year '{year}': {status} {message}")

print("\nMonths:")
test_months = ["6", "0", "13", "12", "abc"]
for month in test_months:
    is_valid, message = validate_month(month)
    status = "✅" if is_valid else "❌"
    print(f"  Month '{month}': {status} {message}")

print("\nDays:")
test_days = ["15", "0", "32", "31", "29"]
for day in test_days:
    is_valid, message = validate_day(day)
    status = "✅" if is_valid else "❌"
    print(f"  Day '{day}': {status} {message}")

print()

# CUSTOM RANGE VALIDATION FRAMEWORK
print("=== CUSTOM RANGE VALIDATION FRAMEWORK ===")
print()

class RangeValidator:
    """
    A flexible class for creating custom range validators.
    """
    
    def __init__(self, min_value, max_value, field_name="value", allow_decimals=True):
        self.min_value = min_value
        self.max_value = max_value
        self.field_name = field_name
        self.allow_decimals = allow_decimals
    
    def validate(self, value_str):
        """
        Validate a value against the configured range.
        """
        try:
            # Convert to appropriate numeric type
            if self.allow_decimals:
                value = float(value_str)
            else:
                value = int(value_str)
                
                # Check if original was decimal when decimals not allowed
                if self.allow_decimals == False and '.' in str(value_str):
                    return False, f"{self.field_name} must be a whole number"
            
            # Range checking
            if value < self.min_value:
                return False, f"{self.field_name} must be at least {self.min_value}"
            elif value > self.max_value:
                return False, f"{self.field_name} cannot exceed {self.max_value}"
            else:
                return True, f"Valid {self.field_name}: {value}"
                
        except (ValueError, TypeError):
            return False, f"{self.field_name} must be a valid number"

# Create specialized validators
print("Creating specialized validators:")

temperature_validator = RangeValidator(-50, 50, "Temperature (°C)")
speed_validator = RangeValidator(0, 200, "Speed (mph)", allow_decimals=False)
rating_validator = RangeValidator(1, 5, "Rating")

validators = [
    (temperature_validator, ["25", "-60", "100", "22.5"]),
    (speed_validator, ["65", "250", "-10", "55.5"]),
    (rating_validator, ["4", "0", "6", "3.8"])
]

for validator, test_values in validators:
    print(f"\nTesting {validator.field_name}:")
    for test_val in test_values:
        is_valid, message = validator.validate(test_val)
        status = "✅" if is_valid else "❌"
        print(f"  Value '{test_val}': {status} {message}")

print()

# INTERACTIVE RANGE VALIDATION EXAMPLE
print("=== INTERACTIVE RANGE VALIDATION EXAMPLE ===")
print()

def get_valid_input(prompt, validator_func):
    """
    Generic function to get valid input using any validation function.
    """
    while True:
        user_input = input(prompt).strip()
        
        if not user_input:
            print("❌ Input cannot be empty. Please try again.")
            continue
        
        is_valid, message = validator_func(user_input)
        
        if is_valid:
            print(f"✅ {message}")
            return user_input
        else:
            print(f"❌ {message} Please try again.")

print("🎯 Interactive Product Entry System")
print("Let's collect valid product information:")

# Example interactive session (using simulated input)
print("\n--- Simulated Product Entry ---")
print("Enter product price: $25.99")
is_valid, price, message = validate_price("$25.99")
print(f"✅ {message}")

print("Enter customer age: 28")
is_valid, message = validate_age("28")
print(f"✅ {message}")

print("Enter discount percentage: 15%")
is_valid, percent, message = validate_percentage("15%")
print(f"✅ {message}")

print("\n🎉 All product information validated successfully!")

print()

# BOUNDARY CONDITION TESTING
print("=== BOUNDARY CONDITION TESTING ===")
print()

print("Testing boundary conditions is crucial for robust validation:")
print("• Test minimum and maximum allowed values")
print("• Test values just below and above limits")
print("• Test zero and negative values")
print("• Test decimal precision limits")
print()

def test_boundaries(validator_func, test_name, boundary_values):
    """
    Test a validator function with boundary conditions.
    """
    print(f"Boundary testing for {test_name}:")
    
    for description, value in boundary_values:
        is_valid, *result = validator_func(value)
        status = "✅" if is_valid else "❌"
        message = result[-1] if result else "No message"  # Get the last element (message)
        print(f"  {description}: {status} {message}")
    
    print()

# Test age validation boundaries
age_boundaries = [
    ("Minimum valid age", "1"),
    ("Just below minimum", "0"),
    ("Maximum valid age", "120"),
    ("Just above maximum", "121"),
    ("Typical adult", "30"),
    ("Edge case decimal", "25.0")
]

test_boundaries(validate_age, "Age Validation", age_boundaries)

# Test percentage validation boundaries
percent_boundaries = [
    ("Minimum valid", "0"),
    ("Just below minimum", "-0.1"),
    ("Maximum valid", "100"),
    ("Just above maximum", "100.1"),
    ("Mid-range", "50"),
    ("High precision", "99.99")
]

test_boundaries(lambda x: validate_percentage(x), "Percentage Validation", percent_boundaries)

print()

print("=== SUMMARY ===")
print()
print("Range Validation Best Practices:")
print("1. Define realistic minimum and maximum bounds")
print("2. Consider the context and domain of your application")
print("3. Test boundary conditions thoroughly")
print("4. Provide clear error messages explaining limits")
print("5. Handle both inclusive and exclusive ranges appropriately")
print("6. Consider precision requirements (integers vs decimals)")
print("7. Validate related constraints (e.g., start date < end date)")
print("8. Use consistent validation patterns across your application")

"""
KEY TAKEAWAYS:
==============
1. Range validation ensures numeric values fall within acceptable bounds
2. Different domains require different range constraints (age, price, grade, etc.)
3. Boundary condition testing is essential for robust validation
4. Custom validator classes can make range validation reusable
5. Consider precision requirements (whole numbers vs decimals)
6. Provide clear, helpful error messages that explain the valid range
7. Test edge cases: minimum, maximum, just below/above limits

COMMON RANGE VALIDATION PATTERNS:
=================================
• Age: 0-120 years (or context-specific like 18-65 for employment)
• Price: $0.01-$999,999.99 (reasonable commercial limits)
• Percentage: 0-100% (or allow over 100% for growth rates)
• Grade: 0-100 points, 0.0-4.0 GPA, or A-F letters
• Year: 1900-2030 (reasonable historical/future range)
• Rating: 1-5 stars (or 1-10 scale)

IMPLEMENTATION STRATEGIES:
==========================
• Create reusable validator functions for common ranges
• Use validator classes for complex or configurable validation
• Implement boundary testing in your validation suite
• Consider domain-specific requirements and constraints
• Provide meaningful error messages with guidance

NEXT STEP:
Go to 04-format-validation.py to learn pattern matching and format validation!
"""