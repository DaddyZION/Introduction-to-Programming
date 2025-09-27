"""
Practice Problem 01: Number Pattern Generator
============================================

DIFFICULTY: Beginner ⭐
CONCEPTS: Sequences, Iteration, Patterns
ASSIGNMENTS: 1 (Sequences), 3 (Iteration)
ESTIMATED TIME: 45-60 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive number pattern generator that can create various mathematical
and visual patterns using numbers. This problem combines basic arithmetic operations,
loops, and formatted output to create interesting visual patterns.

Your program should be able to generate:
1. Arithmetic sequences (linear patterns)
2. Geometric sequences (exponential patterns)
3. Fibonacci sequences
4. Prime number sequences
5. Visual number pyramids and triangles
6. Number spirals and grids

REQUIREMENTS:
============
1. Create functions for each pattern type
2. Allow user to specify pattern parameters (size, starting values, etc.)
3. Display patterns in a well-formatted way
4. Include a menu system for pattern selection
5. Validate user input and handle errors gracefully
6. Provide clear explanations of each pattern type

LEARNING OBJECTIVES:
===================
- Practice with arithmetic operations and number sequences
- Master nested loops for pattern creation
- Implement user input validation
- Design clean, modular functions
- Create formatted output displays
- Understand mathematical sequences and their properties

STARTER CODE:
============
"""

import math

def display_menu():
    """Display the main menu for pattern selection."""
    print("=" * 50)
    print("        NUMBER PATTERN GENERATOR")
    print("=" * 50)
    print("1. Arithmetic Sequence")
    print("2. Geometric Sequence") 
    print("3. Fibonacci Sequence")
    print("4. Prime Number Sequence")
    print("5. Number Pyramid")
    print("6. Number Triangle")
    print("7. Multiplication Table")
    print("8. Number Spiral (Advanced)")
    print("9. Pascal's Triangle")
    print("0. Exit")
    print("=" * 50)

def get_user_choice():
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = int(input("Enter your choice (0-9): "))
            if 0 <= choice <= 9:
                return choice
            else:
                print("❌ Please enter a number between 0 and 9.")
        except ValueError:
            print("❌ Please enter a valid number.")

def arithmetic_sequence():
    """Generate and display an arithmetic sequence."""
    print("\n📊 ARITHMETIC SEQUENCE GENERATOR")
    print("Formula: a(n) = first_term + (n-1) × common_difference")
    
    try:
        first_term = float(input("Enter the first term: "))
        common_diff = float(input("Enter the common difference: "))
        num_terms = int(input("Enter the number of terms: "))
        
        if num_terms <= 0:
            print("❌ Number of terms must be positive!")
            return
        
        print(f"\nArithmetic sequence with first term {first_term} and common difference {common_diff}:")
        print("Position | Term    | Calculation")
        print("-" * 35)
        
        total = 0
        for i in range(num_terms):
            term = first_term + i * common_diff
            total += term
            print(f"{i+1:8d} | {term:7.2f} | {first_term} + {i} × {common_diff}")
        
        print("-" * 35)
        print(f"Sum of all terms: {total:.2f}")
        print(f"Average of terms: {total/num_terms:.2f}")
        
    except ValueError:
        print("❌ Please enter valid numbers!")

def geometric_sequence():
    """Generate and display a geometric sequence."""
    print("\n📈 GEOMETRIC SEQUENCE GENERATOR")
    print("Formula: a(n) = first_term × common_ratio^(n-1)")
    
    try:
        first_term = float(input("Enter the first term: "))
        common_ratio = float(input("Enter the common ratio: "))
        num_terms = int(input("Enter the number of terms (max 20): "))
        
        if num_terms <= 0 or num_terms > 20:
            print("❌ Number of terms must be between 1 and 20!")
            return
        
        if common_ratio == 0:
            print("❌ Common ratio cannot be zero!")
            return
        
        print(f"\nGeometric sequence with first term {first_term} and common ratio {common_ratio}:")
        print("Position | Term        | Calculation")
        print("-" * 40)
        
        total = 0
        for i in range(num_terms):
            term = first_term * (common_ratio ** i)
            total += term
            print(f"{i+1:8d} | {term:11.3f} | {first_term} × {common_ratio}^{i}")
        
        print("-" * 40)
        print(f"Sum of all terms: {total:.3f}")
        
        # Calculate sum using formula for geometric series
        if common_ratio != 1:
            formula_sum = first_term * (1 - common_ratio**num_terms) / (1 - common_ratio)
            print(f"Sum using formula: {formula_sum:.3f}")
        
    except ValueError:
        print("❌ Please enter valid numbers!")
    except OverflowError:
        print("❌ Numbers too large to calculate!")

def fibonacci_sequence():
    """Generate and display a Fibonacci sequence."""
    print("\n🌀 FIBONACCI SEQUENCE GENERATOR")
    print("Formula: F(n) = F(n-1) + F(n-2), where F(0)=0, F(1)=1")
    
    try:
        num_terms = int(input("Enter the number of terms (max 30): "))
        
        if num_terms <= 0 or num_terms > 30:
            print("❌ Number of terms must be between 1 and 30!")
            return
        
        print(f"\nFirst {num_terms} Fibonacci numbers:")
        print("Position | Term      | Ratio to Previous")
        print("-" * 40)
        
        # Initialize first two terms
        if num_terms >= 1:
            fib_prev = 0
            print(f"{1:8d} | {fib_prev:9d} | N/A")
        
        if num_terms >= 2:
            fib_curr = 1
            print(f"{2:8d} | {fib_curr:9d} | N/A")
        
        # Generate remaining terms
        for i in range(2, num_terms):
            fib_next = fib_prev + fib_curr
            ratio = fib_next / fib_curr if fib_curr != 0 else 0
            print(f"{i+1:8d} | {fib_next:9d} | {ratio:13.6f}")
            
            fib_prev = fib_curr
            fib_curr = fib_next
        
        # Show golden ratio approximation
        if num_terms > 2:
            golden_ratio = (1 + math.sqrt(5)) / 2
            print(f"\nGolden Ratio: {golden_ratio:.6f}")
            print("Notice how the ratio approaches the Golden Ratio!")
        
    except ValueError:
        print("❌ Please enter a valid number!")

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_sequence():
    """Generate and display a sequence of prime numbers."""
    print("\n🔢 PRIME NUMBER SEQUENCE GENERATOR")
    print("Prime numbers are natural numbers greater than 1 that have no positive divisors other than 1 and themselves.")
    
    try:
        limit = int(input("Enter the maximum number to check (up to 1000): "))
        
        if limit < 2 or limit > 1000:
            print("❌ Please enter a number between 2 and 1000!")
            return
        
        print(f"\nPrime numbers up to {limit}:")
        primes = []
        
        for num in range(2, limit + 1):
            if is_prime(num):
                primes.append(num)
        
        # Display primes in rows of 10
        for i, prime in enumerate(primes):
            print(f"{prime:4d}", end=" ")
            if (i + 1) % 10 == 0:
                print()  # New line after every 10 primes
        
        if len(primes) % 10 != 0:
            print()  # Final new line if needed
        
        print(f"\nFound {len(primes)} prime numbers up to {limit}")
        
        # Show some interesting facts
        if len(primes) > 0:
            print(f"Smallest prime: {primes[0]}")
            print(f"Largest prime: {primes[-1]}")
            if len(primes) > 1:
                gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
                print(f"Average gap between primes: {sum(gaps)/len(gaps):.2f}")
        
    except ValueError:
        print("❌ Please enter a valid number!")

def number_pyramid():
    """Generate and display various number pyramids."""
    print("\n🔺 NUMBER PYRAMID GENERATOR")
    
    try:
        height = int(input("Enter the height of the pyramid (max 15): "))
        
        if height <= 0 or height > 15:
            print("❌ Height must be between 1 and 15!")
            return
        
        print("\nChoose pyramid type:")
        print("1. Sequential numbers")
        print("2. Row numbers")
        print("3. Powers of 2")
        print("4. Multiplication pyramid")
        
        pyramid_type = int(input("Enter choice (1-4): "))
        
        if pyramid_type == 1:
            # Sequential numbers pyramid
            print(f"\nSequential Numbers Pyramid (height {height}):")
            num = 1
            for row in range(1, height + 1):
                # Print leading spaces
                print(" " * (height - row) * 2, end="")
                
                # Print numbers for this row
                for col in range(row):
                    print(f"{num:3d} ", end="")
                    num += 1
                print()
        
        elif pyramid_type == 2:
            # Row numbers pyramid
            print(f"\nRow Numbers Pyramid (height {height}):")
            for row in range(1, height + 1):
                print(" " * (height - row) * 2, end="")
                for col in range(row):
                    print(f"{row:3d} ", end="")
                print()
        
        elif pyramid_type == 3:
            # Powers of 2 pyramid
            print(f"\nPowers of 2 Pyramid (height {height}):")
            for row in range(1, height + 1):
                print(" " * (height - row) * 3, end="")
                for col in range(row):
                    power_val = 2 ** (col)
                    print(f"{power_val:4d} ", end="")
                print()
        
        elif pyramid_type == 4:
            # Multiplication pyramid
            print(f"\nMultiplication Pyramid (height {height}):")
            for row in range(1, height + 1):
                print(" " * (height - row) * 2, end="")
                for col in range(1, row + 1):
                    product = row * col
                    print(f"{product:3d} ", end="")
                print()
        
        else:
            print("❌ Invalid pyramid type!")
        
    except ValueError:
        print("❌ Please enter valid numbers!")

def number_triangle():
    """Generate and display various number triangles."""
    print("\n📐 NUMBER TRIANGLE GENERATOR")
    
    try:
        size = int(input("Enter the size of the triangle (max 10): "))
        
        if size <= 0 or size > 10:
            print("❌ Size must be between 1 and 10!")
            return
        
        print("\nChoose triangle type:")
        print("1. Right triangle (ascending)")
        print("2. Right triangle (descending)")
        print("3. Floyd's triangle")
        print("4. Binary triangle")
        
        triangle_type = int(input("Enter choice (1-4): "))
        
        if triangle_type == 1:
            # Right triangle ascending
            print(f"\nRight Triangle - Ascending (size {size}):")
            for row in range(1, size + 1):
                for col in range(1, row + 1):
                    print(f"{col:2d} ", end="")
                print()
        
        elif triangle_type == 2:
            # Right triangle descending
            print(f"\nRight Triangle - Descending (size {size}):")
            for row in range(size, 0, -1):
                for col in range(1, row + 1):
                    print(f"{col:2d} ", end="")
                print()
        
        elif triangle_type == 3:
            # Floyd's triangle
            print(f"\nFloyd's Triangle (size {size}):")
            num = 1
            for row in range(1, size + 1):
                for col in range(row):
                    print(f"{num:3d} ", end="")
                    num += 1
                print()
        
        elif triangle_type == 4:
            # Binary triangle
            print(f"\nBinary Triangle (size {size}):")
            for row in range(size):
                for col in range(row + 1):
                    bit = (row + col) % 2
                    print(f"{bit} ", end="")
                print()
        
        else:
            print("❌ Invalid triangle type!")
        
    except ValueError:
        print("❌ Please enter valid numbers!")

def multiplication_table():
    """Generate and display multiplication tables."""
    print("\n✖️  MULTIPLICATION TABLE GENERATOR")
    
    try:
        size = int(input("Enter the size of the table (max 15): "))
        
        if size <= 0 or size > 15:
            print("❌ Size must be between 1 and 15!")
            return
        
        print(f"\nMultiplication Table ({size} × {size}):")
        
        # Print column headers
        print("   |", end="")
        for col in range(1, size + 1):
            print(f"{col:4d}", end="")
        print()
        
        # Print separator line
        print("---+" + "----" * size)
        
        # Print table rows
        for row in range(1, size + 1):
            print(f"{row:2d} |", end="")
            for col in range(1, size + 1):
                product = row * col
                print(f"{product:4d}", end="")
            print()
        
        # Show some interesting properties
        print(f"\nInteresting facts:")
        print(f"• Total numbers in table: {size * size}")
        print(f"• Sum of first row: {sum(range(1, size + 1))}")
        print(f"• Largest product: {size * size}")
        
        # Count perfect squares
        perfect_squares = 0
        for row in range(1, size + 1):
            for col in range(1, size + 1):
                product = row * col
                sqrt_product = int(math.sqrt(product))
                if sqrt_product * sqrt_product == product:
                    perfect_squares += 1
        
        print(f"• Perfect squares in table: {perfect_squares}")
        
    except ValueError:
        print("❌ Please enter a valid number!")

def pascals_triangle():
    """Generate and display Pascal's triangle."""
    print("\n🔺 PASCAL'S TRIANGLE GENERATOR")
    print("Pascal's triangle shows binomial coefficients where each number is the sum of the two numbers above it.")
    
    try:
        height = int(input("Enter the height (max 15): "))
        
        if height <= 0 or height > 15:
            print("❌ Height must be between 1 and 15!")
            return
        
        print(f"\nPascal's Triangle (height {height}):")
        
        for row in range(height):
            # Print leading spaces for centering
            print(" " * (height - row - 1) * 2, end="")
            
            # Calculate and print values for this row
            for col in range(row + 1):
                # Calculate binomial coefficient C(row, col)
                value = 1
                for i in range(col):
                    value = value * (row - i) // (i + 1)
                
                print(f"{value:3d} ", end="")
            print()
        
        # Show some properties
        print(f"\nProperties of Pascal's Triangle:")
        print(f"• Each row represents binomial coefficients")
        print(f"• Sum of row n = 2^n")
        print(f"• Contains many number sequences (Fibonacci, triangular numbers, etc.)")
        
        # Show row sums
        print(f"\nRow sums (powers of 2):")
        for row in range(min(height, 8)):
            row_sum = 2 ** row
            print(f"  Row {row}: {row_sum}")
        
    except ValueError:
        print("❌ Please enter a valid number!")

def number_spiral():
    """Generate and display a number spiral (Advanced)."""
    print("\n🌀 NUMBER SPIRAL GENERATOR (ADVANCED)")
    print("Creates a spiral pattern of numbers starting from the center and moving outward.")
    
    try:
        size = int(input("Enter the size (odd number, max 9): "))
        
        if size <= 0 or size > 9 or size % 2 == 0:
            print("❌ Size must be an odd number between 1 and 9!")
            return
        
        # Create the spiral grid
        grid = [[0 for _ in range(size)] for _ in range(size)]
        
        # Starting position (center)
        row = size // 2
        col = size // 2
        num = 1
        
        # Place the first number
        grid[row][col] = num
        num += 1
        
        # Direction vectors: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_dir = 0
        
        steps = 1
        
        while num <= size * size:
            for _ in range(2):  # Two sides per step length
                for _ in range(steps):
                    if num > size * size:
                        break
                    
                    # Move in current direction
                    dr, dc = directions[current_dir]
                    row += dr
                    col += dc
                    
                    # Check bounds
                    if 0 <= row < size and 0 <= col < size:
                        grid[row][col] = num
                        num += 1
                
                # Change direction
                current_dir = (current_dir + 1) % 4
                
                if num > size * size:
                    break
            
            steps += 1
        
        # Display the spiral
        print(f"\nNumber Spiral ({size} × {size}):")
        for row in grid:
            for val in row:
                print(f"{val:3d} ", end="")
            print()
        
        print(f"\nSpiral created with numbers 1 to {size * size}")
        
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    """Main program loop."""
    print("🎉 Welcome to the Number Pattern Generator!")
    print("This program creates various mathematical and visual patterns using numbers.")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 0:
            print("\n👋 Thank you for using the Number Pattern Generator!")
            print("Keep exploring the wonderful world of mathematical patterns!")
            break
        elif choice == 1:
            arithmetic_sequence()
        elif choice == 2:
            geometric_sequence()
        elif choice == 3:
            fibonacci_sequence()
        elif choice == 4:
            prime_sequence()
        elif choice == 5:
            number_pyramid()
        elif choice == 6:
            number_triangle()
        elif choice == 7:
            multiplication_table()
        elif choice == 8:
            number_spiral()
        elif choice == 9:
            pascals_triangle()
        
        print("\n" + "=" * 50)
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ All menu functions working correctly
2. ✅ Proper input validation for all user inputs
3. ✅ Clear, formatted output for all patterns
4. ✅ Mathematical accuracy in calculations
5. ✅ Proper error handling for edge cases
6. ✅ Well-documented code with comments
7. ✅ Efficient algorithms for pattern generation

LEARNING OUTCOMES:
==================
After completing this problem, you will have practiced:
• Basic arithmetic and mathematical sequences
• Nested loops for pattern creation
• User input validation and error handling
• Function design and modularity
• String formatting for display
• Mathematical concepts (primes, Fibonacci, Pascal's triangle)
• Problem decomposition and algorithm design

EXTENSION IDEAS:
===============
1. Add more sequence types (factorial, square numbers, etc.)
2. Implement pattern export to text file
3. Add colored output for better visualization
4. Create interactive pattern customization
5. Add mathematical analysis of sequences
6. Implement pattern recognition challenges
7. Create animated pattern generation

This problem provides excellent practice with fundamental programming
concepts while creating visually interesting and mathematically
meaningful output!
"""