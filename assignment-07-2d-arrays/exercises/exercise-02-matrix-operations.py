"""
Assignment 7 - Exercise 2: Basic Matrix Operations
Difficulty: 🟢 Beginner

TODO: Implement basic 2D array (matrix) operations.

Requirements:
1. Create and initialize matrices
2. Perform basic operations (add, multiply, transpose)
3. Calculate row and column sums
4. Find min/max values in matrix
"""

# ==================== FUNCTION 1: Create Matrix ====================
def create_matrix(rows, cols, initial_value=0):
    """
    Create a matrix with specified dimensions.
    
    Parameters:
    - rows: number of rows
    - cols: number of columns
    - initial_value: value to fill matrix with
    
    Returns: 2D list (matrix)
    
    Example:
    create_matrix(3, 4, 0) → 
    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 2: Display Matrix ====================
def display_matrix(matrix, title="Matrix"):
    """
    Display a matrix in a formatted manner.
    
    Format:
    === Matrix ===
    [  1,  2,  3 ]
    [  4,  5,  6 ]
    [  7,  8,  9 ]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 3: Get Matrix Dimensions ====================
def get_dimensions(matrix):
    """
    Get the dimensions of a matrix.
    
    Returns: (rows, cols) tuple
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 4: Add Matrices ====================
def add_matrices(matrix1, matrix2):
    """
    Add two matrices element-wise.
    
    Requirements:
    - Matrices must have same dimensions
    - Return new matrix with sum
    - Return None if dimensions don't match
    
    Example:
    [[1, 2], [3, 4]] + [[5, 6], [7, 8]] = [[6, 8], [10, 12]]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 5: Multiply Matrix by Scalar ====================
def scalar_multiply(matrix, scalar):
    """
    Multiply every element in matrix by a scalar value.
    
    Example:
    [[1, 2], [3, 4]] * 2 = [[2, 4], [6, 8]]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 6: Transpose Matrix ====================
def transpose(matrix):
    """
    Transpose a matrix (swap rows and columns).
    
    Example:
    [[1, 2, 3],     [[1, 4],
     [4, 5, 6]]  →   [2, 5],
                     [3, 6]]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 7: Calculate Row Sums ====================
def calculate_row_sums(matrix):
    """
    Calculate sum of each row.
    
    Returns: list of row sums
    
    Example:
    [[1, 2, 3], [4, 5, 6]] → [6, 15]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 8: Calculate Column Sums ====================
def calculate_column_sums(matrix):
    """
    Calculate sum of each column.
    
    Returns: list of column sums
    
    Example:
    [[1, 2, 3], [4, 5, 6]] → [5, 7, 9]
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 9: Find Matrix Min/Max ====================
def find_min_max(matrix):
    """
    Find minimum and maximum values in matrix.
    
    Returns: (min_value, max_value, min_position, max_position) tuple
    Position is (row, col) tuple
    
    Example:
    [[3, 1, 4], [1, 5, 9]] 
    → (1, 9, (0, 1), (1, 2))
    """
    # TODO: Implement this function
    pass


# ==================== FUNCTION 10: Create Identity Matrix ====================
def create_identity_matrix(size):
    """
    Create an identity matrix of given size.
    (1s on diagonal, 0s elsewhere)
    
    Example:
    create_identity_matrix(3) →
    [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]
    """
    # TODO: Implement this function
    pass


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing Basic Matrix Operations ===\n")
    
    # Test create and display
    print("Test 1: Create Matrix")
    # matrix1 = create_matrix(3, 4, 5)
    # display_matrix(matrix1, "3x4 Matrix filled with 5")
    
    # Test dimensions
    print("\nTest 2: Get Dimensions")
    test_matrix = [[1, 2, 3], [4, 5, 6]]
    # rows, cols = get_dimensions(test_matrix)
    # print(f"  Dimensions: {rows} rows x {cols} columns")
    
    # Test addition
    print("\nTest 3: Add Matrices")
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    # result = add_matrices(matrix_a, matrix_b)
    # display_matrix(result, "Sum")
    
    # Test scalar multiplication
    print("\nTest 4: Scalar Multiplication")
    # result = scalar_multiply(matrix_a, 2)
    # display_matrix(result, "Matrix × 2")
    
    # Test transpose
    print("\nTest 5: Transpose")
    matrix_c = [[1, 2, 3], [4, 5, 6]]
    # result = transpose(matrix_c)
    # display_matrix(result, "Transposed")
    
    # Test row/column sums
    print("\nTest 6: Row and Column Sums")
    # row_sums = calculate_row_sums(matrix_c)
    # col_sums = calculate_column_sums(matrix_c)
    # print(f"  Row sums: {row_sums}")
    # print(f"  Column sums: {col_sums}")
    
    # Test min/max
    print("\nTest 7: Find Min/Max")
    matrix_d = [[3, 1, 4], [1, 5, 9], [2, 6, 5]]
    # min_val, max_val, min_pos, max_pos = find_min_max(matrix_d)
    # print(f"  Min: {min_val} at {min_pos}")
    # print(f"  Max: {max_val} at {max_pos}")
    
    # Test identity matrix
    print("\nTest 8: Identity Matrix")
    # identity = create_identity_matrix(4)
    # display_matrix(identity, "4×4 Identity Matrix")
