"""
Assignment 7 - Example 1: 2D Array Basics
=========================================

This program introduces fundamental concepts of two-dimensional arrays (matrices)
in Python. 2D arrays are collections of arrays arranged in rows and columns,
forming a grid-like structure essential for many advanced programming applications.
Understanding 2D arrays is crucial for game development, scientific computing,
image processing, and data analysis.

Key Concepts Demonstrated:
- 2D array creation and initialization methods
- Safe access patterns and bounds checking
- Row and column operations
- Matrix traversal techniques
- Memory layout understanding
- Common manipulation operations
- Performance considerations
"""

import random
import time

print("=== 2D ARRAY BASICS ===")
print()

print("2D arrays (matrices) are fundamental data structures for advanced programming:")
print("• Organize data in rows and columns for grid-based operations")
print("• Essential for game development, image processing, and scientific computing")
print("• Enable matrix mathematics and linear algebra operations")
print("• Support complex data relationships and spatial information")
print("• Form the foundation for multidimensional data analysis")
print()

# 2D ARRAY CREATION METHODS
print("=== 2D ARRAY CREATION METHODS ===")
print()

print("Method 1: List of Lists (Manual Creation)")
# Manual creation - simple but limited
matrix_manual = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(f"Manual 3x4 matrix:")
for row in matrix_manual:
    print(f"  {row}")
print()

print("Method 2: Nested List Comprehension (Recommended)")
# Using nested list comprehension - flexible and efficient
rows, cols = 4, 5
matrix_comprehension = [[row * cols + col for col in range(cols)] for row in range(rows)]
print(f"4x5 matrix using list comprehension:")
for row in matrix_comprehension:
    print(f"  {row}")
print()

print("Method 3: Nested Loops (Explicit Control)")
# Using nested loops - most readable for complex initialization
rows, cols = 3, 4
matrix_loops = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i + j)  # Some pattern or calculation
    matrix_loops.append(row)

print(f"3x4 matrix using nested loops:")
for row in matrix_loops:
    print(f"  {row}")
print()

print("Method 4: Fill with Specific Values")
# Creating matrices filled with specific values
def create_matrix(rows, cols, fill_value=0):
    """Create a matrix filled with a specific value."""
    return [[fill_value for _ in range(cols)] for _ in range(rows)]

def create_identity_matrix(size):
    """Create an identity matrix (1s on diagonal, 0s elsewhere)."""
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def create_random_matrix(rows, cols, min_val=0, max_val=10):
    """Create a matrix filled with random values."""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Demonstrate different fill methods
zero_matrix = create_matrix(3, 3, 0)
print("3x3 Zero matrix:")
for row in zero_matrix:
    print(f"  {row}")
print()

identity_matrix = create_identity_matrix(4)
print("4x4 Identity matrix:")
for row in identity_matrix:
    print(f"  {row}")
print()

random.seed(42)  # For reproducible results
random_matrix = create_random_matrix(3, 4, 1, 9)
print("3x4 Random matrix (values 1-9):")
for row in random_matrix:
    print(f"  {row}")
print()

# COMMON 2D ARRAY PITFALL - SHALLOW COPY
print("=== AVOIDING COMMON PITFALLS ===")
print()

print("❌ WRONG WAY - Shallow Copy Problem:")
# This creates multiple references to the same list!
wrong_matrix = [[0] * 3] * 3
print("Created using [[0] * 3] * 3:")
for row in wrong_matrix:
    print(f"  {row}")

print("Modifying [0][0] = 99:")
wrong_matrix[0][0] = 99
print("Result (all rows affected!):")
for row in wrong_matrix:
    print(f"  {row}")
print()

print("✅ CORRECT WAY - Proper Creation:")
correct_matrix = [[0] * 3 for _ in range(3)]
print("Created using [[0] * 3 for _ in range(3)]:")
for row in correct_matrix:
    print(f"  {row}")

print("Modifying [0][0] = 99:")
correct_matrix[0][0] = 99
print("Result (only intended row affected):")
for row in correct_matrix:
    print(f"  {row}")
print()

# MATRIX DIMENSIONS AND PROPERTIES
print("=== MATRIX DIMENSIONS AND PROPERTIES ===")
print()

def analyze_matrix(matrix, name="Matrix"):
    """Analyze and display matrix properties."""
    if not matrix:
        print(f"{name}: Empty matrix")
        return
    
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    
    # Check if it's rectangular (all rows same length)
    is_rectangular = all(len(row) == cols for row in matrix)
    
    # Calculate total elements
    total_elements = sum(len(row) for row in matrix)
    
    # Find min and max values
    all_values = [value for row in matrix for value in row]
    min_val = min(all_values) if all_values else None
    max_val = max(all_values) if all_values else None
    
    print(f"{name} Analysis:")
    print(f"  Dimensions: {rows} rows × {cols} columns")
    print(f"  Is rectangular: {is_rectangular}")
    print(f"  Total elements: {total_elements}")
    print(f"  Value range: {min_val} to {max_val}")
    
    if rows == cols:
        print(f"  Square matrix: Yes ({rows}×{rows})")
    else:
        print(f"  Square matrix: No")
    
    print()

# Analyze different matrices
analyze_matrix(matrix_manual, "Manual Matrix")
analyze_matrix(identity_matrix, "Identity Matrix")
analyze_matrix(random_matrix, "Random Matrix")

# Jagged array (non-rectangular)
jagged_array = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9, 10],
    [11]
]
analyze_matrix(jagged_array, "Jagged Array")

# SAFE MATRIX ACCESS
print("=== SAFE MATRIX ACCESS PATTERNS ===")
print()

def safe_get(matrix, row, col, default=None):
    """Safely get a value from matrix with bounds checking."""
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return matrix[row][col]
    return default

def safe_set(matrix, row, col, value):
    """Safely set a value in matrix with bounds checking."""
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        matrix[row][col] = value
        return True
    return False

def get_matrix_bounds(matrix):
    """Get the bounds (min/max valid indices) of a matrix."""
    if not matrix:
        return None
    
    max_row = len(matrix) - 1
    max_col = max(len(row) - 1 for row in matrix) if matrix else -1
    
    return {
        'min_row': 0,
        'max_row': max_row,
        'min_col': 0,
        'max_col': max_col
    }

# Demonstrate safe access
test_matrix = create_matrix(3, 4, 0)
# Fill with some test data
for i in range(len(test_matrix)):
    for j in range(len(test_matrix[i])):
        test_matrix[i][j] = i * 10 + j

print("Test matrix:")
for i, row in enumerate(test_matrix):
    print(f"  Row {i}: {row}")
print()

# Test safe access
test_cases = [
    (1, 2),    # Valid
    (0, 0),    # Valid (corner)
    (2, 3),    # Valid (corner)
    (-1, 0),   # Invalid (negative row)
    (0, -1),   # Invalid (negative col)
    (3, 0),    # Invalid (row out of bounds)
    (0, 4),    # Invalid (col out of bounds)
    (5, 5)     # Invalid (both out of bounds)
]

print("Safe access tests:")
for row, col in test_cases:
    value = safe_get(test_matrix, row, col, "OUT_OF_BOUNDS")
    print(f"  get({row}, {col}) = {value}")
print()

# Get matrix bounds
bounds = get_matrix_bounds(test_matrix)
print(f"Matrix bounds: {bounds}")
print()

# MATRIX TRAVERSAL PATTERNS
print("=== MATRIX TRAVERSAL PATTERNS ===")
print()

def traverse_row_major(matrix):
    """Traverse matrix row by row (standard order)."""
    result = []
    for row in matrix:
        for value in row:
            result.append(value)
    return result

def traverse_column_major(matrix):
    """Traverse matrix column by column."""
    if not matrix:
        return []
    
    result = []
    rows, cols = len(matrix), len(matrix[0])
    
    for col in range(cols):
        for row in range(rows):
            if col < len(matrix[row]):  # Handle jagged arrays
                result.append(matrix[row][col])
    
    return result

def traverse_diagonal_main(matrix):
    """Traverse main diagonal (top-left to bottom-right)."""
    result = []
    size = min(len(matrix), len(matrix[0]) if matrix else 0)
    
    for i in range(size):
        if i < len(matrix[i]):
            result.append(matrix[i][i])
    
    return result

def traverse_diagonal_anti(matrix):
    """Traverse anti-diagonal (top-right to bottom-left)."""
    result = []
    rows = len(matrix)
    
    for i in range(rows):
        col = rows - 1 - i
        if col < len(matrix[i]):
            result.append(matrix[i][col])
    
    return result

def traverse_spiral_clockwise(matrix):
    """Traverse matrix in spiral order (clockwise)."""
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Go right along top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Go down along right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Go left along bottom row (if we still have rows)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Go up along left column (if we still have columns)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

# Demonstrate traversal patterns
demo_matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Demo 4x4 matrix:")
for row in demo_matrix:
    print(f"  {row}")
print()

print("Traversal patterns:")
print(f"  Row-major: {traverse_row_major(demo_matrix)}")
print(f"  Column-major: {traverse_column_major(demo_matrix)}")
print(f"  Main diagonal: {traverse_diagonal_main(demo_matrix)}")
print(f"  Anti-diagonal: {traverse_diagonal_anti(demo_matrix)}")
print(f"  Spiral clockwise: {traverse_spiral_clockwise(demo_matrix)}")
print()

# ROW AND COLUMN OPERATIONS
print("=== ROW AND COLUMN OPERATIONS ===")
print()

def get_row(matrix, row_index):
    """Extract a specific row from matrix."""
    if 0 <= row_index < len(matrix):
        return matrix[row_index][:]  # Return copy, not reference
    return None

def get_column(matrix, col_index):
    """Extract a specific column from matrix."""
    column = []
    for row in matrix:
        if col_index < len(row):
            column.append(row[col_index])
    return column if column else None

def set_row(matrix, row_index, new_row):
    """Replace a specific row in matrix."""
    if 0 <= row_index < len(matrix):
        matrix[row_index] = new_row[:]  # Copy the new row
        return True
    return False

def set_column(matrix, col_index, new_column):
    """Replace a specific column in matrix."""
    if not matrix or col_index < 0:
        return False
    
    for i, value in enumerate(new_column):
        if i < len(matrix) and col_index < len(matrix[i]):
            matrix[i][col_index] = value
    return True

def calculate_row_sum(matrix, row_index):
    """Calculate sum of a specific row."""
    row = get_row(matrix, row_index)
    return sum(row) if row else None

def calculate_column_sum(matrix, col_index):
    """Calculate sum of a specific column."""
    column = get_column(matrix, col_index)
    return sum(column) if column else None

def calculate_matrix_sums(matrix):
    """Calculate all row sums and column sums."""
    if not matrix:
        return [], []
    
    row_sums = [sum(row) for row in matrix]
    
    col_sums = []
    max_cols = max(len(row) for row in matrix) if matrix else 0
    for col in range(max_cols):
        col_sum = sum(row[col] for row in matrix if col < len(row))
        col_sums.append(col_sum)
    
    return row_sums, col_sums

# Demonstrate row and column operations
operations_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

print("Operations matrix:")
for i, row in enumerate(operations_matrix):
    print(f"  Row {i}: {row}")
print()

# Extract operations
print("Row and column extraction:")
row_2 = get_row(operations_matrix, 2)
col_3 = get_column(operations_matrix, 3)
print(f"  Row 2: {row_2}")
print(f"  Column 3: {col_3}")
print()

# Sum calculations
row_sums, col_sums = calculate_matrix_sums(operations_matrix)
print("Sum calculations:")
print(f"  Row sums: {row_sums}")
print(f"  Column sums: {col_sums}")
print(f"  Total sum: {sum(row_sums)}")
print()

# MATRIX COPYING AND CLONING
print("=== MATRIX COPYING AND CLONING ===")
print()

def shallow_copy_matrix(matrix):
    """Create a shallow copy of matrix (copies row references)."""
    return matrix[:]

def deep_copy_matrix(matrix):
    """Create a deep copy of matrix (copies all data)."""
    return [row[:] for row in matrix]

def copy_matrix_manual(matrix):
    """Manual deep copy using nested loops."""
    if not matrix:
        return []
    
    copied = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value)
        copied.append(new_row)
    
    return copied

# Demonstrate copying differences
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original matrix:")
for row in original:
    print(f"  {row}")

# Create copies
shallow = shallow_copy_matrix(original)
deep = deep_copy_matrix(original)

print("\nModifying original[0][0] from 1 to 99...")
original[0][0] = 99

print("After modification:")
print(f"  Original: {original[0]}")
print(f"  Shallow copy: {shallow[0]}")  # Also affected!
print(f"  Deep copy: {deep[0]}")        # Not affected
print()

# PERFORMANCE CONSIDERATIONS
print("=== PERFORMANCE CONSIDERATIONS ===")
print()

def performance_test_creation():
    """Test performance of different matrix creation methods."""
    size = 100
    
    # Method 1: List comprehension
    start_time = time.time()
    matrix1 = [[0 for _ in range(size)] for _ in range(size)]
    time1 = time.time() - start_time
    
    # Method 2: Nested loops
    start_time = time.time()
    matrix2 = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matrix2.append(row)
    time2 = time.time() - start_time
    
    # Method 3: Pre-allocate and fill
    start_time = time.time()
    matrix3 = [[None] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            matrix3[i][j] = 0
    time3 = time.time() - start_time
    
    return time1, time2, time3

def performance_test_access():
    """Test performance of different access patterns."""
    matrix = [[i * 100 + j for j in range(100)] for i in range(100)]
    
    # Row-major access
    start_time = time.time()
    total_row_major = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total_row_major += matrix[i][j]
    time_row_major = time.time() - start_time
    
    # Column-major access
    start_time = time.time()
    total_col_major = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            total_col_major += matrix[i][j]
    time_col_major = time.time() - start_time
    
    return time_row_major, time_col_major, total_row_major, total_col_major

print("Performance testing matrix creation methods:")
creation_times = performance_test_creation()
print(f"  List comprehension: {creation_times[0]:.6f} seconds")
print(f"  Nested loops: {creation_times[1]:.6f} seconds")
print(f"  Pre-allocate: {creation_times[2]:.6f} seconds")
print()

print("Performance testing access patterns:")
access_results = performance_test_access()
print(f"  Row-major access: {access_results[0]:.6f} seconds")
print(f"  Column-major access: {access_results[1]:.6f} seconds")
print(f"  Row-major sum: {access_results[2]}")
print(f"  Column-major sum: {access_results[3]}")
print(f"  Speedup factor: {access_results[1]/access_results[0]:.2f}x")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")
print()

def create_multiplication_table(size):
    """Create a multiplication table matrix."""
    return [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]

def create_pascal_triangle(rows):
    """Create Pascal's triangle as a jagged 2D array."""
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def create_checkerboard(size, char1='■', char2='□'):
    """Create a checkerboard pattern."""
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j) % 2 == 0:
                row.append(char1)
            else:
                row.append(char2)
        board.append(row)
    return board

def find_matrix_pattern(matrix, pattern):
    """Find all occurrences of a pattern in a matrix."""
    if not matrix or not pattern:
        return []
    
    positions = []
    pattern_rows, pattern_cols = len(pattern), len(pattern[0])
    matrix_rows, matrix_cols = len(matrix), len(matrix[0])
    
    for i in range(matrix_rows - pattern_rows + 1):
        for j in range(matrix_cols - pattern_cols + 1):
            # Check if pattern matches at position (i, j)
            match = True
            for pi in range(pattern_rows):
                for pj in range(pattern_cols):
                    if matrix[i + pi][j + pj] != pattern[pi][pj]:
                        match = False
                        break
                if not match:
                    break
            
            if match:
                positions.append((i, j))
    
    return positions

# Demonstrate practical examples
print("Multiplication table (5x5):")
mult_table = create_multiplication_table(5)
for row in mult_table:
    print(f"  {row}")
print()

print("Pascal's triangle (6 rows):")
pascal = create_pascal_triangle(6)
for i, row in enumerate(pascal):
    spaces = " " * (6 - i)
    print(f"  {spaces}{' '.join(str(x) for x in row)}")
print()

print("Checkerboard (8x8):")
checkerboard = create_checkerboard(8)
for row in checkerboard:
    print(f"  {' '.join(row)}")
print()

# Pattern finding example
print("Pattern finding example:")
test_matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 1, 2, 15],
    [16, 17, 6, 7, 20]
]
search_pattern = [[1, 2], [6, 7]]

print("Matrix to search:")
for row in test_matrix:
    print(f"  {row}")

print(f"Pattern to find:")
for row in search_pattern:
    print(f"  {row}")

matches = find_matrix_pattern(test_matrix, search_pattern)
print(f"Pattern found at positions: {matches}")
print()

print("=== SUMMARY ===")
print()
print("2D Array Basics Summary:")
print("1. Use list comprehensions for efficient matrix creation")
print("2. Always create deep copies to avoid reference issues")
print("3. Implement bounds checking for safe access")
print("4. Row-major access is typically faster than column-major")
print("5. Choose appropriate traversal patterns for your use case")
print("6. Consider memory usage for large matrices")
print("7. Test edge cases like empty matrices and jagged arrays")
print("8. Understand the difference between shallow and deep copying")

"""
KEY TAKEAWAYS:
==============
1. 2D arrays are arrays of arrays, creating grid-like structures
2. List comprehensions are the preferred method for matrix creation
3. Bounds checking is essential to prevent index errors
4. Different traversal patterns serve different algorithmic needs
5. Memory layout affects performance - row-major is typically faster
6. Deep copying is necessary to avoid shared reference issues
7. Matrix operations form the foundation for advanced algorithms
8. Understanding these basics enables complex applications

CREATION PATTERNS:
==================
• List Comprehension: [[expr for j in range(cols)] for i in range(rows)]
• Nested Loops: More control but typically slower
• Pre-allocation: Good for known patterns
• Identity Matrix: [[1 if i==j else 0 for j in range(n)] for i in range(n)]

ACCESS PATTERNS:
================
• Direct Access: matrix[row][col]
• Safe Access: Check bounds before accessing
• Row Operations: Work with entire rows as lists
• Column Operations: Extract columns with list comprehension

TRAVERSAL METHODS:
==================
• Row-Major: Process row by row (standard)
• Column-Major: Process column by column
• Diagonal: Main diagonal and anti-diagonal
• Spiral: Clockwise or counterclockwise patterns

PERFORMANCE TIPS:
=================
• Use list comprehensions for creation
• Access memory in row-major order when possible
• Pre-allocate matrices when size is known
• Consider sparse representations for mostly empty matrices
• Profile your code to identify bottlenecks

COMMON MISTAKES:
================
• Shallow copy: [[0] * cols] * rows (WRONG!)
• Index confusion: Remember [row][col] order
• Missing bounds checks: Always validate indices
• Reference sharing: Use deep copy when needed

NEXT STEP:
Go to 02-matrix-operations.py to learn about mathematical operations on matrices!
"""