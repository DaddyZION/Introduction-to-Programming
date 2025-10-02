"""
Assignment 6 - Exercise 1: Array Statistics Calculator
Difficulty: 🟢 Beginner

TODO: Create a program that calculates statistics for a list of numbers.

Requirements:
1. Takes a list of numbers from user input
2. Calculates and displays: sum, average, minimum, maximum
3. Count of positive, negative, and zero values
4. Range (max - min)
"""

# ==================== FUNCTION 1: Calculate Sum ====================
def calculate_sum(numbers):
    """
    Calculate the sum of all numbers in the list.
    
    Parameters:
    - numbers: list of numbers
    
    Returns: float
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Calculate Statistics ====================
def calculate_statistics(numbers):
    """
    Calculate comprehensive statistics for a list of numbers.
    
    Parameters:
    - numbers: list of numbers
    
    Returns: dictionary with keys:
    - sum, average, min, max, range
    - positive_count, negative_count, zero_count
    
    Example:
    calculate_statistics([5, -3, 8, 0, 12, -7, 4])
    → {'sum': 19, 'average': 2.71, 'min': -7, 'max': 12, 
       'range': 19, 'positive_count': 4, 'negative_count': 2, 'zero_count': 1}
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Display Statistics ====================
def display_statistics(stats):
    """
    Display statistics in a formatted manner.
    
    Format:
    === ARRAY STATISTICS ===
    Sum: 19
    Average: 2.71
    Min: -7, Max: 12
    Range: 19
    Positive: 4, Negative: 2, Zero: 1
    """
    # TODO: Implement this function
    pass


# ==================== MAIN PROGRAM ====================
def main():
    """
    Main program to collect input and display statistics.
    """
    print("=== Array Statistics Calculator ===\n")
    
    # TODO: Get numbers from user
    # Example: Enter numbers separated by spaces: 5 -3 8 0 12 -7 4
    
    # TODO: Calculate statistics
    
    # TODO: Display results
    
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    # Test with sample data
    test_data = [5, -3, 8, 0, 12, -7, 4]
    
    print("Testing with data:", test_data)
    # stats = calculate_statistics(test_data)
    # display_statistics(stats)
    
    print("\nTo run interactive program:")
    print("  Uncomment: main()")
    # main()
