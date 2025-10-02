"""
Assignment 6 - Exercise 2: String Formatter
Difficulty: 🟢 Beginner

TODO: Create a program that formats names properly.

Requirements:
1. Takes a person's full name and formats it properly
2. Handles various input formats (different cases, extra spaces)
3. Validates the input and provides error messages
4. Outputs the name in different formats
"""

# ==================== FUNCTION 1: Clean Name ====================
def clean_name(name):
    """
    Clean and normalize a name string.
    
    Requirements:
    - Remove extra whitespace
    - Trim leading/trailing spaces
    - Convert to title case
    
    Example:
    clean_name("  alice marie   JOHNSON  ") → "Alice Marie Johnson"
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Split Name ====================
def split_name(full_name):
    """
    Split a full name into components.
    
    Returns: dictionary with keys: first, middle, last
    - If 2 words: first and last only (middle is empty string)
    - If 3+ words: first, middle (joined), last
    
    Example:
    split_name("Alice Marie Johnson") 
    → {'first': 'Alice', 'middle': 'Marie', 'last': 'Johnson'}
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Format Name ====================
def format_name_variations(full_name):
    """
    Format name in multiple variations.
    
    Returns: dictionary with different formats:
    - 'standard': "First Middle Last"
    - 'last_first': "Last, First Middle"
    - 'first_initial': "First M. Last"
    - 'initials': "F. M. Last"
    
    Example:
    format_name_variations("Alice Marie Johnson")
    → {
        'standard': 'Alice Marie Johnson',
        'last_first': 'Johnson, Alice Marie',
        'first_initial': 'Alice M. Johnson',
        'initials': 'A. M. Johnson'
    }
    """
    # TODO: Implement this function
    # Hint: Use split_name() function
    pass


# ==================== FUNCTION 4: Validate Name ====================
def validate_name(name):
    """
    Validate that a name is properly formatted.
    
    Requirements:
    - Must have at least 2 words (first and last)
    - Each word must start with a letter
    - No numbers or special characters (except spaces, hyphens, apostrophes)
    
    Returns: (is_valid, message) tuple
    """
    # TODO: Implement this function
    pass


# ==================== MAIN PROGRAM ====================
def main():
    """
    Interactive name formatter.
    """
    print("=== Name Formatter ===\n")
    
    # TODO: Get name from user
    
    # TODO: Clean and validate name
    
    # TODO: Display formatted variations
    
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    test_names = [
        "  alice marie   JOHNSON  ",
        "john doe",
        "Dr. Susan B. Anthony",
        "123 Invalid",
        "Single"
    ]
    
    print("Testing name formatting:\n")
    for name in test_names:
        print(f"Input: '{name}'")
        cleaned = clean_name(name) if name else None
        # print(f"  Cleaned: {cleaned}")
        # validation = validate_name(cleaned) if cleaned else (False, "Empty name")
        # print(f"  Valid: {validation}")
        print()
    
    print("To run interactive program:")
    print("  Uncomment: main()")
    # main()
