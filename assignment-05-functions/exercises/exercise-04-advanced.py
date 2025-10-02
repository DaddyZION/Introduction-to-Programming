"""
Assignment 5 - Exercise 4: Advanced Functions
Difficulty: 🟠 Advanced

TODO: Practice advanced function concepts including lambda, map, filter, and recursion.

This exercise covers more sophisticated function programming techniques.
"""

# ==================== FUNCTION 1: Lambda Functions ====================
"""
TODO: Create lambda functions for the following operations:

1. square: takes a number and returns its square
2. is_positive: takes a number and returns True if positive
3. full_name: takes first and last name, returns "First Last"
"""

# Example:
# square = lambda x: x ** 2

# TODO: Create the three lambda functions here
square = None  # Replace with lambda
is_positive = None  # Replace with lambda
full_name = None  # Replace with lambda


# ==================== FUNCTION 2: Map and Filter ====================
def process_numbers(numbers):
    """
    Process a list of numbers using map and filter.
    
    Requirements:
    - Filter out negative numbers
    - Square the remaining numbers
    - Return the result as a list
    - Use filter() and map() functions
    
    Test Cases:
    - process_numbers([1, -2, 3, -4, 5]) → [1, 9, 25]
    - process_numbers([-1, -2, -3]) → []
    - process_numbers([2, 4, 6]) → [4, 16, 36]
    """
    # TODO: Implement using filter() and map()
    pass


# ==================== FUNCTION 3: Recursive Factorial ====================
def factorial_recursive(n):
    """
    Calculate factorial using recursion.
    
    Requirements:
    - Use recursion (function calls itself)
    - Base case: factorial(0) = 1
    - Recursive case: n * factorial(n-1)
    
    Test Cases:
    - factorial_recursive(0) → 1
    - factorial_recursive(5) → 120
    - factorial_recursive(3) → 6
    """
    # TODO: Implement recursively
    pass


# ==================== FUNCTION 4: Fibonacci ====================
def fibonacci(n):
    """
    Calculate nth Fibonacci number using recursion.
    
    Requirements:
    - Use recursion
    - Base cases: fib(0) = 0, fib(1) = 1
    - Recursive case: fib(n-1) + fib(n-2)
    
    Test Cases:
    - fibonacci(0) → 0
    - fibonacci(1) → 1
    - fibonacci(6) → 8
    - fibonacci(10) → 55
    """
    # TODO: Implement recursively
    pass


# ==================== FUNCTION 5: Higher-Order Function ====================
def apply_operation(numbers, operation):
    """
    Apply a given operation to all numbers in a list.
    
    Requirements:
    - Accept a list of numbers and a function
    - Apply the function to each number
    - Return list of results
    - This is a higher-order function (takes function as parameter)
    
    Test Cases:
    - apply_operation([1, 2, 3], lambda x: x * 2) → [2, 4, 6]
    - apply_operation([1, 2, 3], lambda x: x ** 2) → [1, 4, 9]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Function Composition ====================
def compose(f, g):
    """
    Create a new function that is the composition of f and g.
    
    Requirements:
    - Return a new function that applies g first, then f
    - The returned function should accept one argument
    - Result: f(g(x))
    
    Example:
    double = lambda x: x * 2
    add_one = lambda x: x + 1
    double_then_add = compose(add_one, double)
    double_then_add(3) → 7  # (3 * 2) + 1
    """
    # TODO: Implement function composition
    pass


# ==================== FUNCTION 7: Reduce Implementation ====================
def custom_reduce(function, sequence, initial=None):
    """
    Implement your own version of reduce (fold).
    
    Requirements:
    - Apply function cumulatively to sequence items
    - Start with initial value if provided
    - Otherwise start with first two elements
    - Return final accumulated value
    
    Test Cases:
    - custom_reduce(lambda x, y: x + y, [1, 2, 3, 4]) → 10
    - custom_reduce(lambda x, y: x * y, [1, 2, 3, 4], 1) → 24
    """
    # TODO: Implement reduce
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Advanced Functions ===\n")
    
    # Test lambda functions
    print("Test 1: Lambda Functions")
    if square:
        print(f"  square(5) = {square(5)}")
    if is_positive:
        print(f"  is_positive(5) = {is_positive(5)}")
        print(f"  is_positive(-3) = {is_positive(-3)}")
    if full_name:
        print(f"  full_name('John', 'Doe') = {full_name('John', 'Doe')}")
    
    # Test process_numbers
    print("\nTest 2: Map and Filter")
    # print(f"  process_numbers([1, -2, 3, -4, 5]) = {process_numbers([1, -2, 3, -4, 5])}")
    
    # Test factorial_recursive
    print("\nTest 3: Recursive Factorial")
    # print(f"  factorial_recursive(5) = {factorial_recursive(5)}")
    
    # Test fibonacci
    print("\nTest 4: Fibonacci")
    # print(f"  fibonacci(10) = {fibonacci(10)}")
    
    # Test apply_operation
    print("\nTest 5: Apply Operation (Higher-Order)")
    # result = apply_operation([1, 2, 3], lambda x: x * 2)
    # print(f"  apply_operation([1,2,3], double) = {result}")
    
    # Test compose
    print("\nTest 6: Function Composition")
    # double = lambda x: x * 2
    # add_one = lambda x: x + 1
    # composed = compose(add_one, double)
    # print(f"  compose(add_one, double)(3) = {composed(3)}")
    
    # Test custom_reduce
    print("\nTest 7: Custom Reduce")
    # result = custom_reduce(lambda x, y: x + y, [1, 2, 3, 4])
    # print(f"  custom_reduce(add, [1,2,3,4]) = {result}")
