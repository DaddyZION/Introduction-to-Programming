"""
Assignment 7 - Exercise 3: Grid Pattern Generation
Difficulty: 🟡 Intermediate

TODO: Generate various patterns in 2D grids.

Requirements:
1. Create different grid patterns (checkerboard, spiral, etc.)
2. Generate number patterns (multiplication tables, etc.)
3. Create geometric shapes in grids
"""

# ==================== FUNCTION 1: Checkerboard Pattern ====================
def create_checkerboard(size, char1='X', char2='O'):
    """
    Create a checkerboard pattern.
    
    Parameters:
    - size: grid size (size x size)
    - char1: character for "black" squares
    - char2: character for "white" squares
    
    Example (size=4):
    X O X O
    O X O X
    X O X O
    O X O X
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Multiplication Table ====================
def create_multiplication_table(size):
    """
    Create a multiplication table.
    
    Example (size=5):
    [[ 1,  2,  3,  4,  5],
     [ 2,  4,  6,  8, 10],
     [ 3,  6,  9, 12, 15],
     [ 4,  8, 12, 16, 20],
     [ 5, 10, 15, 20, 25]]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Diamond Pattern ====================
def create_diamond(size):
    """
    Create a diamond pattern with * and spaces.
    
    Example (size=5):
        *
       ***
      *****
       ***
        *
    
    Returns: 2D grid where * is 1 and space is 0
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Spiral Pattern ====================
def create_spiral(size):
    """
    Create a spiral pattern of numbers.
    
    Example (size=4):
    [[ 1,  2,  3,  4],
     [12, 13, 14,  5],
     [11, 16, 15,  6],
     [10,  9,  8,  7]]
    
    Numbers spiral inward clockwise from top-left.
    """
    # TODO: Implement this function (CHALLENGE!)
    pass


# ==================== FUNCTION 5: Border Pattern ====================
def create_border(rows, cols, border_char='#', fill_char=' '):
    """
    Create a grid with a border.
    
    Example (5x7):
    #######
    #     #
    #     #
    #     #
    #######
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Pascal's Triangle ====================
def create_pascals_triangle(rows):
    """
    Create Pascal's triangle as a 2D array.
    
    Example (5 rows):
    [[1],
     [1, 1],
     [1, 2, 1],
     [1, 3, 3, 1],
     [1, 4, 6, 4, 1]]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 7: Display Grid ====================
def display_grid(grid, spacing=3):
    """
    Display a 2D grid with proper formatting.
    
    Parameters:
    - grid: 2D list
    - spacing: space between elements
    """
    # TODO: Implement this function
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Grid Pattern Generation ===\n")
    
    print("Test 1: Checkerboard")
    # board = create_checkerboard(8)
    # display_grid(board, spacing=2)
    
    print("\nTest 2: Multiplication Table")
    # table = create_multiplication_table(10)
    # display_grid(table, spacing=4)
    
    print("\nTest 3: Diamond Pattern")
    # diamond = create_diamond(9)
    # display_grid(diamond, spacing=1)
    
    print("\nTest 4: Spiral Pattern")
    # spiral = create_spiral(5)
    # display_grid(spiral, spacing=3)
    
    print("\nTest 5: Border Pattern")
    # border = create_border(7, 15)
    # display_grid(border, spacing=1)
    
    print("\nTest 6: Pascal's Triangle")
    # triangle = create_pascals_triangle(8)
    # for row in triangle:
    #     print("  ", row)
