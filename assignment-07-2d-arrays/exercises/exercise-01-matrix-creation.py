"""
Assignment 7 - Exercise 1: Matrix Creation and Display
=====================================================

DIFFICULTY: Beginner ⭐
ESTIMATED TIME: 30-45 minutes
CONCEPTS: 2D array creation, initialization, display formatting

PROBLEM DESCRIPTION:
===================
Create a comprehensive matrix creation and display system that can:
1. Create matrices of different sizes with various initialization patterns
2. Display matrices in a well-formatted, readable way
3. Implement different matrix creation methods (zeros, ones, identity, random, pattern-based)
4. Support different data types and ranges
5. Provide matrix information and statistics

REQUIREMENTS:
============
1. Implement a Matrix class with the following methods:
   - __init__(rows, cols): Initialize matrix with given dimensions
   - create_zeros(): Fill matrix with zeros
   - create_ones(): Fill matrix with ones
   - create_identity(): Create identity matrix (1s on diagonal, 0s elsewhere)
   - create_random(min_val, max_val): Fill with random integers in range
   - create_pattern(pattern_type): Create various patterns (checkerboard, spiral, etc.)
   - display(): Show matrix in formatted way
   - get_info(): Return matrix dimensions and statistics
   - set_value(row, col, value): Set specific cell value
   - get_value(row, col): Get specific cell value

2. Pattern types to implement:
   - Checkerboard pattern (alternating 0s and 1s)
   - Diagonal pattern (values increase along diagonals)
   - Spiral pattern (numbers arranged in spiral from outside in)
   - Random pattern with seed for reproducibility

3. Display features:
   - Proper alignment of numbers
   - Row and column headers
   - Border lines for clarity
   - Support for different number formats (integers, floats)

LEARNING OBJECTIVES:
===================
- Understand 2D array structure and indexing
- Practice nested loops for matrix operations
- Learn proper code organization with classes
- Implement various initialization algorithms
- Master formatted output and display techniques

STARTER CODE:
============
"""

import random
import math

class Matrix:
    """A comprehensive matrix class for creating and displaying 2D arrays."""
    
    def __init__(self, rows, cols):
        """
        Initialize matrix with given dimensions.
        
        Args:
            rows (int): Number of rows
            cols (int): Number of columns
        """
        # TODO: Implement matrix initialization
        # Hints:
        # - Validate that rows and cols are positive integers
        # - Create a 2D list structure
        # - Initialize all values to 0
        # - Store rows and cols as instance variables
        pass
    
    def create_zeros(self):
        """Fill the entire matrix with zeros."""
        # TODO: Set all matrix elements to 0
        pass
    
    def create_ones(self):
        """Fill the entire matrix with ones."""
        # TODO: Set all matrix elements to 1
        pass
    
    def create_identity(self):
        """
        Create an identity matrix (1s on main diagonal, 0s elsewhere).
        Note: Only works for square matrices.
        """
        # TODO: Implement identity matrix creation
        # Hints:
        # - Check if matrix is square (rows == cols)
        # - Set diagonal elements to 1
        # - Set all other elements to 0
        pass
    
    def create_random(self, min_val=0, max_val=100, seed=None):
        """
        Fill matrix with random integers in the specified range.
        
        Args:
            min_val (int): Minimum random value
            max_val (int): Maximum random value
            seed (int): Random seed for reproducibility
        """
        # TODO: Implement random matrix creation
        # Hints:
        # - Use random.seed(seed) if seed is provided
        # - Use random.randint(min_val, max_val) for each cell
        pass
    
    def create_pattern(self, pattern_type):
        """
        Create various patterns in the matrix.
        
        Args:
            pattern_type (str): Type of pattern to create
                - 'checkerboard': Alternating 0s and 1s
                - 'diagonal': Values increase along diagonals
                - 'spiral': Numbers arranged in spiral pattern
                - 'border': Frame pattern with border
        """
        # TODO: Implement pattern creation
        # This is the most challenging part - start with checkerboard
        
        if pattern_type == 'checkerboard':
            # TODO: Create checkerboard pattern
            # Hint: Use (row + col) % 2 to determine if cell should be 0 or 1
            pass
        
        elif pattern_type == 'diagonal':
            # TODO: Create diagonal pattern
            # Hint: Value could be row + col, or distance from corner
            pass
        
        elif pattern_type == 'spiral':
            # TODO: Create spiral pattern (ADVANCED - save for last)
            # This is complex - start with other patterns first
            pass
        
        elif pattern_type == 'border':
            # TODO: Create border pattern
            # Hint: Check if row/col is on edge of matrix
            pass
    
    def display(self, title="Matrix", cell_width=4):
        """
        Display the matrix in a formatted way.
        
        Args:
            title (str): Title to display above matrix
            cell_width (int): Width of each cell for formatting
        """
        # TODO: Implement matrix display
        # Hints:
        # - Print title
        # - Print column headers (0, 1, 2, ...)
        # - Print horizontal separator line
        # - For each row: print row header, then all values in that row
        # - Use string formatting for proper alignment
        pass
    
    def get_info(self):
        """
        Get information about the matrix.
        
        Returns:
            dict: Dictionary containing matrix statistics
        """
        # TODO: Calculate and return matrix information
        # Should include:
        # - dimensions (rows, cols)
        # - total number of elements
        # - minimum value
        # - maximum value
        # - sum of all elements
        # - average value
        pass
    
    def set_value(self, row, col, value):
        """
        Set value at specific position.
        
        Args:
            row (int): Row index
            col (int): Column index
            value: Value to set
        
        Returns:
            bool: True if successful, False if invalid position
        """
        # TODO: Implement value setting with bounds checking
        pass
    
    def get_value(self, row, col):
        """
        Get value at specific position.
        
        Args:
            row (int): Row index
            col (int): Column index
        
        Returns:
            Value at position, or None if invalid position
        """
        # TODO: Implement value getting with bounds checking
        pass

def test_matrix_operations():
    """Test function to demonstrate matrix operations."""
    
    print("=== MATRIX CREATION AND DISPLAY TESTING ===")
    print()
    
    # Test 1: Basic matrix creation
    print("Test 1: Creating a 4x5 matrix")
    matrix1 = Matrix(4, 5)
    matrix1.display("Newly Created Matrix")
    print()
    
    # Test 2: Zeros matrix
    print("Test 2: Zeros matrix")
    matrix1.create_zeros()
    matrix1.display("Zeros Matrix")
    print()
    
    # Test 3: Ones matrix
    print("Test 3: Ones matrix")
    matrix1.create_ones()
    matrix1.display("Ones Matrix")
    print()
    
    # Test 4: Identity matrix (square)
    print("Test 4: Identity matrix")
    matrix2 = Matrix(5, 5)
    matrix2.create_identity()
    matrix2.display("Identity Matrix")
    print()
    
    # Test 5: Random matrix
    print("Test 5: Random matrix")
    matrix3 = Matrix(3, 6)
    matrix3.create_random(1, 20, seed=42)  # Use seed for reproducible results
    matrix3.display("Random Matrix (1-20)")
    print()
    
    # Test 6: Matrix information
    print("Test 6: Matrix information")
    info = matrix3.get_info()
    print("Matrix Information:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()
    
    # Test 7: Checkerboard pattern
    print("Test 7: Checkerboard pattern")
    matrix4 = Matrix(6, 8)
    matrix4.create_pattern('checkerboard')
    matrix4.display("Checkerboard Pattern")
    print()
    
    # Test 8: Diagonal pattern
    print("Test 8: Diagonal pattern")
    matrix5 = Matrix(5, 5)
    matrix5.create_pattern('diagonal')
    matrix5.display("Diagonal Pattern")
    print()
    
    # Test 9: Border pattern
    print("Test 9: Border pattern")
    matrix6 = Matrix(7, 10)
    matrix6.create_pattern('border')
    matrix6.display("Border Pattern")
    print()
    
    # Test 10: Individual cell operations
    print("Test 10: Individual cell operations")
    matrix7 = Matrix(3, 3)
    matrix7.create_zeros()
    
    # Set some specific values
    matrix7.set_value(0, 0, 10)
    matrix7.set_value(1, 1, 20)
    matrix7.set_value(2, 2, 30)
    matrix7.set_value(0, 2, 5)
    matrix7.set_value(2, 0, 15)
    
    matrix7.display("Custom Values")
    
    # Get specific values
    print("Getting specific values:")
    print(f"  Value at (0,0): {matrix7.get_value(0, 0)}")
    print(f"  Value at (1,1): {matrix7.get_value(1, 1)}")
    print(f"  Value at (2,2): {matrix7.get_value(2, 2)}")
    print()

# BONUS CHALLENGES (Optional):
def bonus_challenges():
    """Additional challenges for advanced students."""
    
    print("=== BONUS CHALLENGES ===")
    print()
    
    # Challenge 1: Implement spiral pattern
    print("Challenge 1: Create a spiral pattern matrix")
    # TODO: This is advanced - create numbers 1, 2, 3... in spiral pattern
    
    # Challenge 2: Create matrix with mathematical functions
    print("Challenge 2: Mathematical function matrices")
    # TODO: Create matrices where each cell is sin(row*col), or row^col, etc.
    
    # Challenge 3: Implement matrix comparison
    print("Challenge 3: Matrix comparison")
    # TODO: Add methods to compare two matrices for equality
    
    # Challenge 4: Matrix copying and cloning
    print("Challenge 4: Matrix copying")
    # TODO: Implement deep copy functionality

if __name__ == "__main__":
    # Run the test function
    test_matrix_operations()
    
    # Uncomment to try bonus challenges
    # bonus_challenges()

"""
SOLUTION HINTS:
==============

1. Matrix Initialization:
   - Use list comprehension: [[0 for _ in range(cols)] for _ in range(rows)]
   - Remember to validate input parameters

2. Display Formatting:
   - Use f-strings for formatting: f"{value:>{width}}"
   - Create separator lines with "-" characters
   - Consider using enumerate() for row numbers

3. Pattern Creation:
   - Checkerboard: (row + col) % 2 determines pattern
   - Diagonal: row + col gives diagonal values
   - Border: check if row == 0 or row == max_row or col == 0 or col == max_col

4. Error Handling:
   - Always check bounds before accessing array elements
   - Use try/except for robust error handling

5. Information Calculation:
   - Flatten the 2D array to calculate min, max, sum
   - Use nested loops to iterate through all elements

EXPECTED OUTPUT EXAMPLE:
=======================
Matrix Information:
  dimensions: (3, 6)
  elements: 18
  minimum: 1
  maximum: 20
  sum: 186
  average: 10.33

Checkerboard Pattern:
   0 1 2 3 4 5 6 7
  +-+-+-+-+-+-+-+-+
0 | 0 1 0 1 0 1 0 1
1 | 1 0 1 0 1 0 1 0
2 | 0 1 0 1 0 1 0 1
3 | 1 0 1 0 1 0 1 0
4 | 0 1 0 1 0 1 0 1
5 | 1 0 1 0 1 0 1 0

LEARNING OUTCOMES:
==================
After completing this exercise, you should understand:
- How to create and initialize 2D arrays
- Nested loop patterns for matrix operations
- String formatting for display purposes
- Basic algorithm implementation (patterns)
- Error handling and bounds checking
- Object-oriented programming with matrices

This exercise forms the foundation for all subsequent 2D array work!
"""