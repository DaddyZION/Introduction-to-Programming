"""
Assignment 4 - Exercise 3: Range and Boundary Validation
Difficulty: 🟡 Intermediate

TODO: Implement validation functions that check numeric ranges and boundaries.

This exercise focuses on validating numbers within specific ranges.
"""

# ==================== FUNCTION 1: Temperature Range Validation ====================
def validate_temperature(temp, unit='C'):
    """
    Validate temperature is within realistic range.
    
    Requirements:
    - If Celsius (C): -50 to 50
    - If Fahrenheit (F): -58 to 122
    - If Kelvin (K): 223 to 323
    - Must be a number
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_temperature(25, 'C') → (True, "Valid temperature")
    - validate_temperature(150, 'F') → (False, "Temperature out of range")
    - validate_temperature(-100, 'C') → (False, "Temperature too low")
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Credit Card Number Validation ====================
def validate_credit_card_length(card_number):
    """
    Validate credit card number length (simplified).
    
    Requirements:
    - Must be a string
    - Remove spaces and dashes
    - Length must be 13, 15, or 16 digits
    - Must contain only digits
    - Return (is_valid, card_type, message) tuple
    - Card types: 13=Visa, 15=Amex, 16=Visa/Mastercard
    
    Test Cases:
    - validate_credit_card_length("4532-1234-5678-9010") → (True, "Visa/Mastercard", "Valid")
    - validate_credit_card_length("1234567890123") → (True, "Visa", "Valid")
    - validate_credit_card_length("12345") → (False, "Unknown", "Invalid length")
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Time Validation ====================
def validate_time(hours, minutes, seconds=0):
    """
    Validate time components.
    
    Requirements:
    - Hours: 0-23
    - Minutes: 0-59
    - Seconds: 0-59 (optional, defaults to 0)
    - All must be integers
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_time(14, 30, 45) → (True, "Valid time: 14:30:45")
    - validate_time(25, 30) → (False, "Invalid hours (must be 0-23)")
    - validate_time(12, 61) → (False, "Invalid minutes (must be 0-59)")
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Percentage Validation ====================
def validate_percentage(value, allow_over_100=False):
    """
    Validate a percentage value.
    
    Requirements:
    - Must be a number (int or float)
    - If allow_over_100 is False: must be 0-100
    - If allow_over_100 is True: must be >= 0
    - Return (is_valid, message) tuple
    
    Test Cases:
    - validate_percentage(75.5) → (True, "Valid percentage")
    - validate_percentage(150) → (False, "Percentage cannot exceed 100")
    - validate_percentage(150, allow_over_100=True) → (True, "Valid percentage")
    - validate_percentage(-10) → (False, "Percentage cannot be negative")
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Score Range Validation ====================
def validate_score_range(score, min_score=0, max_score=100):
    """
    Validate a score is within a customizable range.
    
    Requirements:
    - Score must be a number
    - Score must be between min_score and max_score (inclusive)
    - Return (is_valid, percentage, message) tuple
    - Calculate percentage: (score / max_score) * 100
    
    Test Cases:
    - validate_score_range(85, 0, 100) → (True, 85.0, "Valid score")
    - validate_score_range(45, 0, 50) → (True, 90.0, "Valid score")
    - validate_score_range(110, 0, 100) → (False, 0, "Score exceeds maximum")
    """
    # TODO: Implement this function
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Range and Boundary Validation ===\n")
    
    # Test temperature validation
    print("Test 1: Temperature Validation")
    test_temps = [(25, 'C'), (150, 'F'), (-100, 'C'), (273, 'K')]
    for temp, unit in test_temps:
        result = validate_temperature(temp, unit)
        print(f"  {temp}°{unit}: {result}")
    
    # Test credit card validation
    print("\nTest 2: Credit Card Length")
    test_cards = ["4532-1234-5678-9010", "1234567890123", "12345", "123456789012345"]
    for card in test_cards:
        result = validate_credit_card_length(card)
        print(f"  {card}: {result}")
    
    # Test time validation
    print("\nTest 3: Time Validation")
    test_times = [(14, 30, 45), (25, 30), (12, 61), (0, 0, 0), (23, 59, 59)]
    for time_vals in test_times:
        result = validate_time(*time_vals)
        print(f"  {time_vals}: {result}")
    
    # Test percentage validation
    print("\nTest 4: Percentage Validation")
    test_percentages = [(75.5, False), (150, False), (150, True), (-10, False), (100, False)]
    for value, allow_over in test_percentages:
        result = validate_percentage(value, allow_over)
        print(f"  {value} (allow_over={allow_over}): {result}")
    
    # Test score range validation
    print("\nTest 5: Score Range Validation")
    test_scores = [(85, 0, 100), (45, 0, 50), (110, 0, 100), (50, 25, 75)]
    for score, min_s, max_s in test_scores:
        result = validate_score_range(score, min_s, max_s)
        print(f"  Score {score} (range {min_s}-{max_s}): {result}")
