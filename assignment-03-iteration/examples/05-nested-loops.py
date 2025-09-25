"""
Assignment 3 - Example 5: NESTED LOOPS
=======================================

This program demonstrates nested loops - loops inside other loops.
This is essential for working with 2D data structures, generating
patterns, and solving complex problems that require multiple levels
of iteration.

Key Concepts Demonstrated:
- Nested for loops and execution flow
- Inner vs outer loop variables
- 2D data structures (grids, matrices)
- Pattern generation
- Nested loops with different ranges
- Performance considerations
- Real-world applications
"""

print("=== UNDERSTANDING NESTED LOOPS ===")
print()

# WHAT ARE NESTED LOOPS?
print("Nested loops are loops inside other loops.")
print("The inner loop completes ALL its iterations")
print("for EACH iteration of the outer loop.")
print()

print("Structure:")
print("for outer_var in outer_sequence:")
print("    for inner_var in inner_sequence:")
print("        # This runs for every combination")
print("        # of outer_var and inner_var")
print()

# BASIC NESTED LOOP EXAMPLE
print("=== BASIC NESTED LOOP EXAMPLE ===")
print()

print("Example 1: Simple nested counting")
print("Outer loop: 1 to 3, Inner loop: A to C")
print()

for number in range(1, 4):         # Outer loop: 1, 2, 3
    print(f"Outer loop: {number}")
    
    for letter in ['A', 'B', 'C']: # Inner loop runs completely each time
        print(f"  Inner loop: {letter}")
        print(f"    Combination: {number}-{letter}")
    
    print(f"  Finished inner loop for {number}")
    print()

print("Notice: The inner loop runs 3 times for each outer loop iteration")
print("Total combinations: 3 × 3 = 9")
print()

# EXECUTION FLOW DEMONSTRATION
print("=== EXECUTION FLOW STEP-BY-STEP ===")
print()

print("Let's trace through a nested loop execution:")

step = 0
for i in range(1, 3):              # Outer: 1, 2
    for j in range(1, 3):          # Inner: 1, 2
        step += 1
        print(f"Step {step}: i={i}, j={j}")

print(f"Total steps: {step}")
print("Pattern: (1,1), (1,2), (2,1), (2,2)")
print()

# MULTIPLICATION TABLE EXAMPLE
print("=== PRACTICAL EXAMPLE: MULTIPLICATION TABLE ===")
print()

print("Creating a multiplication table using nested loops:")
print()

# Header row
print("   ", end="")                # Space for row labels
for col in range(1, 6):
    print(f"{col:4}", end="")       # Column headers
print()                            # New line

# Multiplication table rows
for row in range(1, 6):
    print(f"{row}  ", end="")       # Row label
    
    for col in range(1, 6):
        product = row * col
        print(f"{product:4}", end="")   # Print product with width 4
    
    print()                         # New line after each row

print()

# 2D GRID CREATION
print("=== WORKING WITH 2D GRIDS ===")
print()

print("Example 1: Creating and displaying a 2D grid")

# Create a 4x5 grid with coordinates
grid = []
rows, cols = 4, 5

print("Creating grid with nested loops:")

for row in range(rows):
    grid_row = []                   # Create new row
    
    for col in range(cols):
        # Each cell contains its coordinates as a tuple
        cell_value = (row, col)
        grid_row.append(cell_value)
        
    grid.append(grid_row)           # Add row to grid

# Display the grid
print("\nGrid contents:")
for row_index in range(len(grid)):
    for col_index in range(len(grid[row_index])):
        cell = grid[row_index][col_index]
        print(f"{cell}", end="  ")
    print()                         # New line after each row

print(f"\nGrid dimensions: {len(grid)} rows × {len(grid[0])} columns")
print()

# PATTERN GENERATION
print("=== PATTERN GENERATION ===")
print()

print("Example 1: Star triangle pattern")

height = 5
for row in range(1, height + 1):
    # Print spaces for alignment (optional)
    for space in range(height - row):
        print(" ", end="")
    
    # Print stars for this row
    for star in range(row):
        print("* ", end="")
    
    print()                         # New line after each row

print()

print("Example 2: Number square pattern")

size = 4
for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(f"{row}{col}", end=" ")
    print()

print()

print("Example 3: Checkerboard pattern")

board_size = 6
for row in range(board_size):
    for col in range(board_size):
        # Alternate between two patterns based on position
        if (row + col) % 2 == 0:
            print("⬜", end="")      # White square
        else:
            print("⬛", end="")      # Black square
    print()

print()

# SEARCHING IN 2D DATA
print("=== SEARCHING IN 2D DATA ===")
print()

print("Example: Find all positions of a value in a grid")

# Sample data grid
data_grid = [
    [1, 5, 3, 5],
    [2, 5, 7, 8],
    [9, 1, 5, 4],
    [6, 3, 2, 5]
]

search_value = 5
positions_found = []

print("Grid to search:")
for row in data_grid:
    print(row)

print(f"\nSearching for value: {search_value}")

for row_idx in range(len(data_grid)):
    for col_idx in range(len(data_grid[row_idx])):
        current_value = data_grid[row_idx][col_idx]
        
        print(f"Checking position ({row_idx},{col_idx}): {current_value}")
        
        if current_value == search_value:
            positions_found.append((row_idx, col_idx))
            print(f"  ✅ Found {search_value}!")
        else:
            print(f"  ❌ Not a match")

print(f"\nSearch complete!")
print(f"Value {search_value} found at positions: {positions_found}")
print(f"Total occurrences: {len(positions_found)}")

print()

# NESTED LOOPS WITH DIFFERENT RANGES
print("=== NESTED LOOPS WITH DIFFERENT RANGES ===")
print()

print("Example: Creating a right triangle of numbers")

max_rows = 5
for row in range(1, max_rows + 1):  # Row determines how many numbers
    print(f"Row {row}: ", end="")
    
    for num in range(1, row + 1):   # Inner range depends on outer variable
        print(num, end=" ")
        
    print()                         # New line after each row

print()

# PRACTICAL APPLICATION: COORDINATE SYSTEM
print("=== PRACTICAL APPLICATION: COORDINATE SYSTEM ===")
print()

print("Example: Generate all coordinates in a region")

# Define boundaries
min_x, max_x = 0, 3
min_y, max_y = 0, 2

all_coordinates = []

print(f"Generating coordinates from ({min_x},{min_y}) to ({max_x},{max_y}):")

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        coordinate = (x, y)
        all_coordinates.append(coordinate)
        print(f"Generated coordinate: {coordinate}")

print(f"\nAll coordinates: {all_coordinates}")
print(f"Total coordinates: {len(all_coordinates)}")

# Verify with formula: (max_x - min_x + 1) × (max_y - min_y + 1)
expected = (max_x - min_x + 1) * (max_y - min_y + 1)
print(f"Expected count: {expected} ✓" if len(all_coordinates) == expected else "❌ Count mismatch!")

print()

# NESTED LOOPS WITH BREAK AND CONTINUE
print("=== NESTED LOOPS WITH CONTROL STATEMENTS ===")
print()

print("Example: Find first occurrence of a target in 2D array")

matrix = [
    [1, 3, 5],
    [7, 2, 9],
    [4, 6, 8]
]

target = 6
found = False
found_position = None

print("Matrix:")
for row in matrix:
    print(row)

print(f"\nSearching for {target}:")

for row_idx in range(len(matrix)):
    print(f"\nSearching row {row_idx}: {matrix[row_idx]}")
    
    for col_idx in range(len(matrix[row_idx])):
        value = matrix[row_idx][col_idx]
        print(f"  Checking ({row_idx},{col_idx}): {value}")
        
        if value == target:
            found_position = (row_idx, col_idx)
            found = True
            print(f"  🎯 Found {target}!")
            break               # Break inner loop only
    
    if found:                   # Need this check to break outer loop
        print(f"Breaking out of outer loop")
        break                   # Break outer loop

if found:
    print(f"\nResult: {target} found at position {found_position}")
else:
    print(f"\nResult: {target} not found in matrix")

print()

# PERFORMANCE CONSIDERATIONS
print("=== PERFORMANCE CONSIDERATIONS ===")
print()

print("Nested loops multiply the number of operations!")
print()

# Demonstrate with timing
import time

print("Comparing single vs nested loop performance:")

# Single loop
start_time = time.time()
count_single = 0
for i in range(1000):
    count_single += 1
single_time = time.time() - start_time

print(f"Single loop (1,000 iterations): {count_single} operations")
print(f"Time: {single_time:.6f} seconds")

# Nested loop  
start_time = time.time()
count_nested = 0
for i in range(100):               # 100 × 100 = 10,000 operations
    for j in range(100):
        count_nested += 1
nested_time = time.time() - start_time

print(f"Nested loop (100×100): {count_nested} operations")
print(f"Time: {nested_time:.6f} seconds")
print(f"Ratio: {nested_time/single_time:.1f}x slower")

print()
print("Key insight: 100×100 nested loop does 10× more work than 1000 single loop!")

print()

# REAL-WORLD APPLICATION: IMAGE PROCESSING
print("=== REAL-WORLD APPLICATION: IMAGE PROCESSING ===")
print()

print("Example: Process pixels in an image (simulated)")

# Simulate a small 3x4 grayscale image (values 0-255)
image = [
    [100, 150, 200, 255],
    [50,  75,  125, 175],
    [25,  100, 150, 225]
]

print("Original image (grayscale values):")
for row in image:
    for pixel in row:
        print(f"{pixel:3}", end=" ")
    print()

print("\nApplying brightness adjustment (+50):")

# Process each pixel
adjusted_image = []
for row_idx in range(len(image)):
    adjusted_row = []
    
    for col_idx in range(len(image[row_idx])):
        original_value = image[row_idx][col_idx]
        adjusted_value = min(255, original_value + 50)  # Cap at 255
        adjusted_row.append(adjusted_value)
        
        print(f"Pixel ({row_idx},{col_idx}): {original_value} → {adjusted_value}")
    
    adjusted_image.append(adjusted_row)

print("\nAdjusted image:")
for row in adjusted_image:
    for pixel in row:
        print(f"{pixel:3}", end=" ")
    print()

print()

# GAME BOARD EXAMPLE
print("=== GAME BOARD EXAMPLE ===")
print()

print("Example: Initialize and display a Tic-Tac-Toe board")

# Initialize 3x3 board
board_size = 3
board = []

# Create empty board
for row in range(board_size):
    board_row = []
    for col in range(board_size):
        board_row.append(" ")       # Empty cell
    board.append(board_row)

print("Empty board:")
for row_idx in range(board_size):
    for col_idx in range(board_size):
        print(f"[{board[row_idx][col_idx]}]", end="")
        if col_idx < board_size - 1:
            print("|", end="")
    print()
    if row_idx < board_size - 1:
        print("---+---+---")

# Add some moves
board[0][0] = "X"
board[1][1] = "O"
board[2][2] = "X"

print("\nBoard with moves:")
for row_idx in range(board_size):
    for col_idx in range(board_size):
        print(f"[{board[row_idx][col_idx]}]", end="")
        if col_idx < board_size - 1:
            print("|", end="")
    print()
    if row_idx < board_size - 1:
        print("---+---+---")

print()

# ADVANCED PATTERN: VARIABLE INNER LOOP RANGE
print("=== ADVANCED: VARIABLE INNER RANGES ===")
print()

print("Example: Pascal's triangle (first 6 rows)")

rows = 6
for row in range(rows):
    # Print leading spaces for alignment
    for space in range(rows - row - 1):
        print("  ", end="")
    
    # Calculate and print values for this row
    for col in range(row + 1):
        # Pascal's triangle formula: C(row,col) = row! / (col! * (row-col)!)
        # Simplified calculation
        if col == 0 or col == row:
            value = 1
        else:
            # For demonstration, we'll calculate it step by step
            value = 1
            for k in range(col):
                value = value * (row - k) // (k + 1)
        
        print(f"{value:3} ", end="")
    
    print()

print()

print("=== SUMMARY ===")
print()
print("Nested Loops Key Points:")
print("1. Inner loop completes ALL iterations for EACH outer iteration")
print("2. Total operations = outer_iterations × inner_iterations")
print("3. Great for 2D data structures, grids, and matrices")
print("4. Essential for pattern generation and image processing")
print("5. Use break/continue carefully - they only affect the immediate loop")
print("6. Consider performance impact - operations multiply quickly")
print("7. Common in games, graphics, data analysis, and scientific computing")

"""
KEY TAKEAWAYS:
==============
1. Nested loops = loops inside loops
2. Inner loop runs completely for each outer loop iteration
3. Perfect for 2D data structures and coordinate systems
4. Operations multiply: 10×10 nested loops = 100 operations
5. Essential for matrix operations, pattern generation, image processing
6. Break/continue only affect the immediate containing loop
7. Use flags or functions to break out of multiple nested levels

COMMON PATTERNS:
================
• Grid/Matrix operations: for row... for col...
• Pattern generation: triangles, squares, shapes
• Coordinate generation: all (x,y) combinations
• Game boards: initialize and update 2D boards
• Image processing: process every pixel
• Search operations: find items in 2D data

PERFORMANCE TIPS:
=================
• Be aware of operation count: n×m operations for n×m nested loops
• Consider breaking early when possible
• Use appropriate data structures
• Profile performance for large datasets
• Sometimes single loops with math can replace nested loops

NEXT STEP:
Go to 06-loop-patterns.py to learn common loop patterns and algorithms!
"""