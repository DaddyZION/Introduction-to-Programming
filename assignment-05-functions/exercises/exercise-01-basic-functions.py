"""
Assignment 5 - Exercise 1: Basic Function Operations
Difficulty: 🟢 Beginner

TODO: Implement basic calculator and utility functions.

This exercise practices function definition, parameters, and return values.
"""

# ==================== FUNCTION 1: Add Numbers ====================
def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Requirements:
    - Accept two numeric parameters
    - Return their sum
    - Handle both integers and floats
    
    Test Cases:
    - add_numbers(5, 3) → 8
    - add_numbers(2.5, 1.5) → 4.0
    - add_numbers(-10, 15) → 5
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Calculate Average ====================
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Requirements:
    - Accept a list of numbers
    - Return the average as a float
    - Return 0 if the list is empty
    - Handle edge cases gracefully
    
    Test Cases:
    - calculate_average([1, 2, 3, 4, 5]) → 3.0
    - calculate_average([10, 20, 30]) → 20.0
    - calculate_average([]) → 0.0
    - calculate_average([5]) → 5.0
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Find Maximum ====================
def find_maximum(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Requirements:
    - Accept a list of numbers
    - Return the maximum value
    - Return None if the list is empty
    - Don't use the built-in max() function
    
    Test Cases:
    - find_maximum([1, 5, 3, 9, 2]) → 9
    - find_maximum([-1, -5, -3]) → -1
    - find_maximum([]) → None
    - find_maximum([42]) → 42
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Count Occurrences ====================
def count_occurrences(items, target):
    """
    Count how many times target appears in items list.
    
    Requirements:
    - Accept a list and a target value
    - Return the count
    - Return 0 if list is empty
    
    Test Cases:
    - count_occurrences([1, 2, 3, 2, 4, 2], 2) → 3
    - count_occurrences(['a', 'b', 'a', 'c'], 'a') → 2
    - count_occurrences([], 5) → 0
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Is Even ====================
def is_even(number):
    """
    Check if a number is even.
    
    Requirements:
    - Accept an integer
    - Return True if even, False if odd
    
    Test Cases:
    - is_even(4) → True
    - is_even(7) → False
    - is_even(0) → True
    - is_even(-2) → True
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Factorial ====================
def factorial(n):
    """
    Calculate factorial of n (n!).
    
    Requirements:
    - Accept a non-negative integer
    - Return factorial value
    - factorial(0) should return 1
    - Use a loop (not recursion for this exercise)
    
    Test Cases:
    - factorial(0) → 1
    - factorial(5) → 120
    - factorial(3) → 6
    """
    # TODO: Implement this function
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Basic Function Operations ===\n")
    
    # Test add_numbers
    print("Test 1: Add Numbers")
    print(f"  add_numbers(5, 3) = {add_numbers(5, 3)}")
    print(f"  add_numbers(2.5, 1.5) = {add_numbers(2.5, 1.5)}")
    print(f"  add_numbers(-10, 15) = {add_numbers(-10, 15)}")
    
    # Test calculate_average
    print("\nTest 2: Calculate Average")
    print(f"  calculate_average([1, 2, 3, 4, 5]) = {calculate_average([1, 2, 3, 4, 5])}")
    print(f"  calculate_average([]) = {calculate_average([])}")
    
    # Test find_maximum
    print("\nTest 3: Find Maximum")
    print(f"  find_maximum([1, 5, 3, 9, 2]) = {find_maximum([1, 5, 3, 9, 2])}")
    print(f"  find_maximum([]) = {find_maximum([])}")
    
    # Test count_occurrences
    print("\nTest 4: Count Occurrences")
    print(f"  count_occurrences([1, 2, 3, 2, 4, 2], 2) = {count_occurrences([1, 2, 3, 2, 4, 2], 2)}")
    
    # Test is_even
    print("\nTest 5: Is Even")
    print(f"  is_even(4) = {is_even(4)}")
    print(f"  is_even(7) = {is_even(7)}")
    
    # Test factorial
    print("\nTest 6: Factorial")
    print(f"  factorial(0) = {factorial(0)}")
    print(f"  factorial(5) = {factorial(5)}")
