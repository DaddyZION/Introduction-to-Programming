"""
Assignment 3 - Exercise 4: Menu Systems
Difficulty: 🟠 Advanced

TODO: Create interactive menu-driven programs with validation.

This exercise contains 2 comprehensive menu systems.
"""

# ==================== PROGRAM 1: Simple Calculator Menu ====================
"""
TODO: Create a calculator with a menu system.

Requirements:
- Display menu with options:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Exit
- Loop until user chooses Exit
- For each operation:
  * Get two numbers
  * Perform operation
  * Display result
- Validate input (menu choice must be 1-5)
- Handle division by zero

Example Output:
    === CALCULATOR MENU ===
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
    
    Enter choice (1-5): 1
    Enter first number: 10
    Enter second number: 5
    Result: 10 + 5 = 15
    
    Enter choice (1-5): 4
    Enter first number: 20
    Enter second number: 4
    Result: 20 / 4 = 5.0
    
    Enter choice (1-5): 5
    Thank you for using the calculator!
"""

# TODO: Write your code here for Program 1


# ==================== PROGRAM 2: Student Grade Manager ====================
"""
TODO: Create a student grade management system.

Requirements:
- Menu options:
  1. Add student grade
  2. View all grades
  3. Calculate class average
  4. Find highest grade
  5. Find lowest grade
  6. Exit
- Store student names and grades in lists
- Loop until user chooses Exit
- Validate all inputs:
  * Grade must be 0-100
  * Menu choice must be 1-6
  * Name cannot be empty
- Handle empty list (no grades entered yet)

Example Output:
    === GRADE MANAGER ===
    1. Add student grade
    2. View all grades
    3. Calculate class average
    4. Find highest grade
    5. Find lowest grade
    6. Exit
    
    Enter choice (1-6): 1
    Enter student name: Alice
    Enter grade (0-100): 85
    Grade added successfully!
    
    Enter choice (1-6): 1
    Enter student name: Bob
    Enter grade (0-100): 92
    Grade added successfully!
    
    Enter choice (1-6): 2
    === ALL GRADES ===
    Alice: 85
    Bob: 92
    
    Enter choice (1-6): 3
    Class average: 88.50
    
    Enter choice (1-6): 4
    Highest grade: Bob - 92
    
    Enter choice (1-6): 5
    Lowest grade: Alice - 85
    
    Enter choice (1-6): 6
    Goodbye!
"""

# TODO: Write your code here for Program 2
