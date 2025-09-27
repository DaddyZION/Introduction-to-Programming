"""
Assignment 7 - Example 2: Matrix Operations
==========================================

This program demonstrates fundamental mathematical operations on matrices,
including addition, subtraction, multiplication, and transformations. These
operations form the core of linear algebra and are essential for scientific
computing, computer graphics, game development, and machine learning applications.

Key Concepts Demonstrated:
- Matrix arithmetic operations (add, subtract, multiply)
- Scalar operations and matrix transformations
- Transpose and matrix properties
- Linear algebra concepts and applications
- Performance optimization for matrix operations
- Practical applications in real-world scenarios
"""

import time
import math
import random

print("=== MATRIX OPERATIONS ===")
print()

print("Matrix operations are fundamental to advanced programming applications:")
print("• Linear algebra forms the basis of scientific computing")
print("• Computer graphics use matrices for transformations and projections")
print("• Machine learning relies heavily on matrix computations")
print("• Game engines use matrices for physics and rendering")
print("• Image processing applies matrix operations to pixel data")
print("• Economic modeling uses matrices for optimization problems")
print()

# MATRIX ARITHMETIC OPERATIONS
print("=== MATRIX ARITHMETIC OPERATIONS ===")
print()

def add_matrices(A, B):
    """
    Add two matrices element-wise.
    Requirement: Matrices must have the same dimensions.
    Time Complexity: O(rows × cols)
    Space Complexity: O(rows × cols)
    """
    # Check if matrices can be added
    if len(A) != len(B):
        raise ValueError("Matrices must have the same number of rows")
    
    if any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("Matrices must have the same number of columns in each row")
    
    # Perform element-wise addition
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    
    return result

def subtract_matrices(A, B):
    """
    Subtract matrix B from matrix A element-wise.
    Requirement: Matrices must have the same dimensions.
    """
    if len(A) != len(B):
        raise ValueError("Matrices must have the same number of rows")
    
    if any(len(A[i]) != len(B[i]) for i in range(len(A))):
        raise ValueError("Matrices must have the same number of columns in each row")
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    
    return result

def scalar_multiply(matrix, scalar):
    """
    Multiply every element of the matrix by a scalar value.
    """
    result = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        result.append(new_row)
    return result

def negate_matrix(matrix):
    """
    Negate all elements in the matrix (multiply by -1).
    """
    return scalar_multiply(matrix, -1)

# Demonstrate matrix arithmetic
print("Matrix Arithmetic Examples:")
print()

# Create sample matrices
matrix_A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix A:")
for row in matrix_A:
    print(f"  {row}")

print("Matrix B:")
for row in matrix_B:
    print(f"  {row}")
print()

# Addition
result_add = add_matrices(matrix_A, matrix_B)
print("A + B:")
for row in result_add:
    print(f"  {row}")
print()

# Subtraction
result_sub = subtract_matrices(matrix_A, matrix_B)
print("A - B:")
for row in result_sub:
    print(f"  {row}")
print()

# Scalar multiplication
result_scalar = scalar_multiply(matrix_A, 3)
print("3 × A:")
for row in result_scalar:
    print(f"  {row}")
print()

# MATRIX MULTIPLICATION
print("=== MATRIX MULTIPLICATION ===")
print()

def multiply_matrices(A, B):
    """
    Multiply two matrices using the standard algorithm.
    Requirement: Number of columns in A must equal number of rows in B.
    Time Complexity: O(n³) for square matrices
    Space Complexity: O(n²) for result matrix
    """
    # Check compatibility
    if not A or not B:
        raise ValueError("Matrices cannot be empty")
    
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError(f"Cannot multiply {rows_A}×{cols_A} and {rows_B}×{cols_B} matrices")
    
    # Initialize result matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def multiply_matrices_optimized(A, B):
    """
    Optimized matrix multiplication with better cache performance.
    """
    if not A or not B:
        raise ValueError("Matrices cannot be empty")
    
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError(f"Cannot multiply {rows_A}×{cols_A} and {rows_B}×{cols_B} matrices")
    
    # Initialize result matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Optimized order: i-k-j instead of i-j-k for better cache locality
    for i in range(rows_A):
        for k in range(cols_A):
            if A[i][k] != 0:  # Skip zero multiplications
                for j in range(cols_B):
                    result[i][j] += A[i][k] * B[k][j]
    
    return result

def matrix_power(matrix, power):
    """
    Compute matrix raised to a power using repeated multiplication.
    """
    if power < 0:
        raise ValueError("Negative powers not supported")
    if power == 0:
        # Return identity matrix
        n = len(matrix)
        return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    if power == 1:
        return [row[:] for row in matrix]  # Deep copy
    
    # Use repeated squaring for efficiency
    result = matrix_power(matrix, power // 2)
    result = multiply_matrices(result, result)
    
    if power % 2 == 1:
        result = multiply_matrices(result, matrix)
    
    return result

# Demonstrate matrix multiplication
print("Matrix Multiplication Examples:")
print()

# Rectangular matrices for multiplication
matrix_C = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matrix_D = [
    [7, 8, 9],
    [10, 11, 12]
]

print("Matrix C (3×2):")
for row in matrix_C:
    print(f"  {row}")

print("Matrix D (2×3):")
for row in matrix_D:
    print(f"  {row}")
print()

# C × D (3×2) × (2×3) = (3×3)
result_CD = multiply_matrices(matrix_C, matrix_D)
print("C × D (3×3 result):")
for row in result_CD:
    print(f"  {row}")
print()

# D × C (2×3) × (3×2) = (2×2)
result_DC = multiply_matrices(matrix_D, matrix_C)
print("D × C (2×2 result):")
for row in result_DC:
    print(f"  {row}")
print()

# Square matrix power
square_matrix = [
    [1, 1],
    [1, 0]
]

print("Square matrix:")
for row in square_matrix:
    print(f"  {row}")

matrix_squared = matrix_power(square_matrix, 2)
print("Matrix² (squared):")
for row in matrix_squared:
    print(f"  {row}")

matrix_cubed = matrix_power(square_matrix, 3)
print("Matrix³ (cubed):")
for row in matrix_cubed:
    print(f"  {row}")
print()

# MATRIX TRANSPOSE AND PROPERTIES
print("=== MATRIX TRANSPOSE AND PROPERTIES ===")
print()

def transpose_matrix(matrix):
    """
    Compute the transpose of a matrix (flip rows and columns).
    """
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    
    # Create transposed matrix
    transposed = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
    
    return transposed

def is_square_matrix(matrix):
    """Check if matrix is square (equal rows and columns)."""
    if not matrix:
        return False
    return len(matrix) == len(matrix[0])

def is_symmetric_matrix(matrix):
    """Check if matrix is symmetric (A = A^T)."""
    if not is_square_matrix(matrix):
        return False
    
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_identity_matrix(matrix):
    """Check if matrix is an identity matrix."""
    if not is_square_matrix(matrix):
        return False
    
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            expected = 1 if i == j else 0
            if matrix[i][j] != expected:
                return False
    return True

def trace_matrix(matrix):
    """Calculate the trace of a matrix (sum of diagonal elements)."""
    if not is_square_matrix(matrix):
        raise ValueError("Trace is only defined for square matrices")
    
    return sum(matrix[i][i] for i in range(len(matrix)))

def matrix_determinant_2x2(matrix):
    """Calculate determinant of a 2×2 matrix."""
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("This function only works for 2×2 matrices")
    
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def matrix_determinant_3x3(matrix):
    """Calculate determinant of a 3×3 matrix using cofactor expansion."""
    if len(matrix) != 3 or len(matrix[0]) != 3:
        raise ValueError("This function only works for 3×3 matrices")
    
    # Using first row expansion
    a, b, c = matrix[0][0], matrix[0][1], matrix[0][2]
    
    # Calculate 2×2 minors
    minor1 = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
    minor2 = matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]
    minor3 = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
    
    return a * minor1 - b * minor2 + c * minor3

# Demonstrate matrix properties
print("Matrix Properties Examples:")
print()

# Test matrices
test_matrices = [
    ([[1, 2, 3], [4, 5, 6]], "Rectangular"),
    ([[1, 2], [3, 4]], "Square 2×2"),
    ([[1, 2, 3], [2, 4, 5], [3, 5, 6]], "Symmetric 3×3"),
    ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], "Identity 3×3"),
    ([[2, -1, 3], [1, 0, 4], [5, 2, -2]], "General 3×3")
]

for matrix, description in test_matrices:
    print(f"{description} matrix:")
    for row in matrix:
        print(f"  {row}")
    
    print(f"  Properties:")
    print(f"    Square: {is_square_matrix(matrix)}")
    
    if is_square_matrix(matrix):
        print(f"    Symmetric: {is_symmetric_matrix(matrix)}")
        print(f"    Identity: {is_identity_matrix(matrix)}")
        print(f"    Trace: {trace_matrix(matrix)}")
        
        if len(matrix) == 2:
            det = matrix_determinant_2x2(matrix)
            print(f"    Determinant: {det}")
        elif len(matrix) == 3:
            det = matrix_determinant_3x3(matrix)
            print(f"    Determinant: {det}")
    
    # Show transpose
    transposed = transpose_matrix(matrix)
    print(f"  Transpose:")
    for row in transposed:
        print(f"    {row}")
    print()

# TRANSFORMATION MATRICES
print("=== TRANSFORMATION MATRICES ===")
print()

def rotation_matrix_2d(angle_degrees):
    """Create a 2D rotation matrix for given angle in degrees."""
    angle_rad = math.radians(angle_degrees)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    
    return [
        [cos_a, -sin_a],
        [sin_a, cos_a]
    ]

def scaling_matrix_2d(scale_x, scale_y):
    """Create a 2D scaling matrix."""
    return [
        [scale_x, 0],
        [0, scale_y]
    ]

def shearing_matrix_2d(shear_x, shear_y):
    """Create a 2D shearing matrix."""
    return [
        [1, shear_x],
        [shear_y, 1]
    ]

def apply_transformation(points, transformation_matrix):
    """Apply transformation matrix to a list of 2D points."""
    transformed_points = []
    
    for point in points:
        # Convert point to column vector and multiply
        point_matrix = [[point[0]], [point[1]]]
        result = multiply_matrices(transformation_matrix, point_matrix)
        transformed_points.append([result[0][0], result[1][0]])
    
    return transformed_points

def round_matrix(matrix, decimals=2):
    """Round all elements in matrix to specified decimal places."""
    return [[round(element, decimals) for element in row] for row in matrix]

# Demonstrate transformation matrices
print("Transformation Matrices Examples:")
print()

# Original points (square)
original_points = [
    [1, 1],   # Top-right
    [-1, 1],  # Top-left
    [-1, -1], # Bottom-left
    [1, -1]   # Bottom-right
]

print("Original square points:")
for i, point in enumerate(original_points):
    print(f"  Point {i+1}: {point}")
print()

# Rotation transformation
rotation_45 = rotation_matrix_2d(45)
print("45° rotation matrix:")
for row in round_matrix(rotation_45, 3):
    print(f"  {row}")

rotated_points = apply_transformation(original_points, rotation_45)
print("Points after 45° rotation:")
for i, point in enumerate(rotated_points):
    print(f"  Point {i+1}: {[round(p, 3) for p in point]}")
print()

# Scaling transformation
scaling_2x = scaling_matrix_2d(2, 0.5)
print("Scaling matrix (2x in X, 0.5x in Y):")
for row in scaling_2x:
    print(f"  {row}")

scaled_points = apply_transformation(original_points, scaling_2x)
print("Points after scaling:")
for i, point in enumerate(scaled_points):
    print(f"  Point {i+1}: {point}")
print()

# Combined transformations
combined = multiply_matrices(rotation_45, scaling_2x)
print("Combined transformation (rotation then scaling):")
for row in round_matrix(combined, 3):
    print(f"  {row}")

combined_points = apply_transformation(original_points, combined)
print("Points after combined transformation:")
for i, point in enumerate(combined_points):
    print(f"  Point {i+1}: {[round(p, 3) for p in point]}")
print()

# MATRIX PERFORMANCE ANALYSIS
print("=== MATRIX PERFORMANCE ANALYSIS ===")
print()

def benchmark_matrix_multiplication():
    """Benchmark different matrix multiplication algorithms."""
    sizes = [10, 50, 100]
    
    print("Matrix multiplication performance comparison:")
    print(f"{'Size':<6} {'Standard':<12} {'Optimized':<12} {'Speedup':<10}")
    print("-" * 50)
    
    for size in sizes:
        # Create random matrices
        random.seed(42)
        A = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
        B = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
        
        # Time standard multiplication
        start_time = time.time()
        result1 = multiply_matrices(A, B)
        time_standard = time.time() - start_time
        
        # Time optimized multiplication
        start_time = time.time()
        result2 = multiply_matrices_optimized(A, B)
        time_optimized = time.time() - start_time
        
        # Calculate speedup
        speedup = time_standard / time_optimized if time_optimized > 0 else float('inf')
        
        print(f"{size:<6} {time_standard:<12.6f} {time_optimized:<12.6f} {speedup:<10.2f}x")
    
    print()

def analyze_matrix_memory_usage():
    """Analyze memory usage patterns for different matrix operations."""
    size = 100
    
    # Create test matrix
    matrix = [[i * size + j for j in range(size)] for i in range(size)]
    
    print(f"Memory usage analysis for {size}×{size} matrix:")
    
    # Calculate theoretical memory usage
    elements = size * size
    bytes_per_element = 28  # Approximate for Python integers
    total_bytes = elements * bytes_per_element
    
    print(f"  Elements: {elements:,}")
    print(f"  Estimated memory: {total_bytes:,} bytes ({total_bytes/1024/1024:.2f} MB)")
    
    # Test different operations
    operations = [
        ("Original matrix", lambda: matrix),
        ("Transpose", lambda: transpose_matrix(matrix)),
        ("Scalar multiply", lambda: scalar_multiply(matrix, 2)),
        ("Matrix addition", lambda: add_matrices(matrix, matrix)),
        ("Matrix multiplication", lambda: multiply_matrices(matrix, matrix))
    ]
    
    print("\n  Operation timing:")
    for name, operation in operations:
        start_time = time.time()
        result = operation()
        end_time = time.time()
        print(f"    {name:<18}: {end_time - start_time:.6f} seconds")
    
    print()

# Run performance benchmarks
benchmark_matrix_multiplication()
analyze_matrix_memory_usage()

# PRACTICAL APPLICATIONS
print("=== PRACTICAL APPLICATIONS ===")
print()

def solve_linear_system_2x2(A, b):
    """
    Solve 2×2 linear system Ax = b using Cramer's rule.
    A is coefficient matrix, b is constants vector.
    """
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("Matrix must be 2×2")
    if len(b) != 2:
        raise ValueError("Constants vector must have 2 elements")
    
    # Calculate determinant
    det_A = matrix_determinant_2x2(A)
    if abs(det_A) < 1e-10:  # Check for near-zero determinant
        raise ValueError("System has no unique solution (determinant ≈ 0)")
    
    # Create matrices for Cramer's rule
    A_x = [[b[0], A[0][1]], [b[1], A[1][1]]]  # Replace first column with b
    A_y = [[A[0][0], b[0]], [A[1][0], b[1]]]  # Replace second column with b
    
    # Calculate solutions
    x = matrix_determinant_2x2(A_x) / det_A
    y = matrix_determinant_2x2(A_y) / det_A
    
    return [x, y]

def calculate_distance_matrix(points):
    """Calculate distance matrix between all pairs of points."""
    n = len(points)
    distance_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate Euclidean distance
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            distance = math.sqrt(dx*dx + dy*dy)
            
            # Matrix is symmetric
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance
    
    return distance_matrix

def markov_chain_step(state_vector, transition_matrix):
    """
    Perform one step of a Markov chain simulation.
    state_vector is current probability distribution.
    transition_matrix contains transition probabilities.
    """
    # Convert state vector to column matrix
    state_matrix = [[prob] for prob in state_vector]
    
    # Multiply transition matrix by state vector
    result_matrix = multiply_matrices(transition_matrix, state_matrix)
    
    # Convert back to list
    return [result_matrix[i][0] for i in range(len(result_matrix))]

def simulate_markov_chain(initial_state, transition_matrix, steps):
    """Simulate multiple steps of a Markov chain."""
    states = [initial_state[:]]  # Start with copy of initial state
    current_state = initial_state[:]
    
    for step in range(steps):
        current_state = markov_chain_step(current_state, transition_matrix)
        states.append(current_state[:])
    
    return states

# Demonstrate practical applications
print("Practical Applications Examples:")
print()

# Solving linear equations
print("1. Solving Linear System:")
coefficient_matrix = [[2, 3], [1, -1]]
constants_vector = [7, 1]

print(f"System: {coefficient_matrix[0][0]}x + {coefficient_matrix[0][1]}y = {constants_vector[0]}")
print(f"        {coefficient_matrix[1][0]}x + {coefficient_matrix[1][1]}y = {constants_vector[1]}")

solution = solve_linear_system_2x2(coefficient_matrix, constants_vector)
print(f"Solution: x = {solution[0]}, y = {solution[1]}")

# Verify solution
verification = multiply_matrices(coefficient_matrix, [[solution[0]], [solution[1]]])
print(f"Verification: [{verification[0][0]}, {verification[1][0]}] = {constants_vector}")
print()

# Distance matrix
print("2. Distance Matrix Calculation:")
cities = [
    [0, 0],    # Origin
    [3, 4],    # Point A
    [6, 8],    # Point B
    [9, 12]    # Point C
]

city_names = ["Origin", "City A", "City B", "City C"]
distances = calculate_distance_matrix(cities)

print("City coordinates:")
for i, (name, coords) in enumerate(zip(city_names, cities)):
    print(f"  {name}: {coords}")

print("\nDistance matrix:")
print(f"{'':>8}", end="")
for name in city_names:
    print(f"{name:>8}", end="")
print()

for i, name in enumerate(city_names):
    print(f"{name:>8}", end="")
    for j in range(len(city_names)):
        print(f"{distances[i][j]:>8.2f}", end="")
    print()
print()

# Markov chain simulation
print("3. Markov Chain Simulation:")
# Simple weather model: [Sunny, Cloudy, Rainy]
transition_matrix = [
    [0.7, 0.2, 0.1],  # From Sunny
    [0.3, 0.4, 0.3],  # From Cloudy
    [0.2, 0.3, 0.5]   # From Rainy
]

initial_state = [1.0, 0.0, 0.0]  # Start sunny
weather_states = ["Sunny", "Cloudy", "Rainy"]

print("Weather transition matrix:")
print(f"{'From/To':>8}", end="")
for state in weather_states:
    print(f"{state:>8}", end="")
print()

for i, state in enumerate(weather_states):
    print(f"{state:>8}", end="")
    for j in range(len(weather_states)):
        print(f"{transition_matrix[i][j]:>8.2f}", end="")
    print()

# Simulate 7 days
simulation_steps = 7
states_over_time = simulate_markov_chain(initial_state, transition_matrix, simulation_steps)

print(f"\nWeather probability simulation ({simulation_steps} days):")
print(f"{'Day':>4}", end="")
for state in weather_states:
    print(f"{state:>10}", end="")
print()

for day, state in enumerate(states_over_time):
    print(f"{day:>4}", end="")
    for prob in state:
        print(f"{prob:>10.3f}", end="")
    print()
print()

print("=== SUMMARY ===")
print()
print("Matrix Operations Summary:")
print("1. Matrix arithmetic requires compatible dimensions")
print("2. Matrix multiplication is not commutative (AB ≠ BA)")
print("3. Transformation matrices enable geometric operations")
print("4. Matrix properties reveal structural information")
print("5. Performance optimization is crucial for large matrices")
print("6. Linear algebra concepts have broad practical applications")
print("7. Numerical stability considerations are important")
print("8. Choose appropriate algorithms based on matrix characteristics")

"""
KEY TAKEAWAYS:
==============
1. Matrix operations follow specific mathematical rules and requirements
2. Dimension compatibility is essential for operations
3. Matrix multiplication has O(n³) complexity for standard algorithm
4. Transformation matrices enable powerful geometric operations
5. Matrix properties provide insights into system behavior
6. Performance optimization becomes critical for large-scale operations
7. Real-world applications span from graphics to scientific computing

OPERATION REQUIREMENTS:
=======================
• Addition/Subtraction: Same dimensions required
• Multiplication: Columns in A = Rows in B
• Transpose: Always possible, flips dimensions
• Determinant: Only for square matrices
• Inverse: Square matrix with non-zero determinant

PERFORMANCE CONSIDERATIONS:
===========================
• Standard multiplication: O(n³) time complexity
• Cache-friendly access patterns improve performance
• Sparse matrices may benefit from specialized algorithms
• Memory usage grows quadratically with dimension
• Consider numerical libraries for production code

TRANSFORMATION MATRICES:
========================
• Rotation: Preserves distances and angles
• Scaling: Changes object size
• Shearing: Distorts shapes
• Translation: Requires homogeneous coordinates (3×3 for 2D)
• Composition: Multiply matrices to combine transformations

APPLICATIONS:
=============
• Computer Graphics: Object transformations, projections
• Machine Learning: Data transformations, neural networks
• Engineering: System analysis, optimization
• Economics: Input-output analysis, game theory
• Physics: Quantum mechanics, linear systems

NUMERICAL CONSIDERATIONS:
=========================
• Floating-point precision affects results
• Condition number indicates numerical stability
• Iterative methods may be preferred for large systems
• Regularization techniques handle ill-conditioned matrices

NEXT STEP:
Go to 03-grid-traversal.py to learn about navigation and pathfinding algorithms!
"""