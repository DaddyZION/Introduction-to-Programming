"""
Assignment 3 - Example 6: COMMON LOOP PATTERNS
===============================================

This program demonstrates essential loop patterns that appear frequently
in programming. These patterns are building blocks for more complex
algorithms and are crucial for solving computational problems effectively.

Key Concepts Demonstrated:
- Accumulator patterns (sum, product, count)
- Find patterns (search, min/max, first/last)
- Filter patterns (collect valid items)
- Transform patterns (convert data)
- Validation patterns (check conditions)
- Counter patterns (frequency counting)
- Flag patterns (state tracking)
"""

print("=== ESSENTIAL LOOP PATTERNS ===")
print()

print("Loop patterns are reusable solutions to common programming problems.")
print("Master these patterns and you can solve many computational challenges!")
print()

# PATTERN 1: ACCUMULATOR PATTERNS
print("=== PATTERN 1: ACCUMULATOR PATTERNS ===")
print()

print("Accumulators build up a result by processing items one at a time.")
print()

# Sum accumulator
print("1A. SUM ACCUMULATOR - Add up all values")

numbers = [10, 25, 7, 33, 12, 8, 19]
total = 0                           # Initialize accumulator

print(f"Numbers: {numbers}")
print("Process:")

for number in numbers:
    print(f"  Adding {number}: {total} + {number} = {total + number}")
    total = total + number          # Accumulate the sum

print(f"Final sum: {total}")
print()

# Product accumulator  
print("1B. PRODUCT ACCUMULATOR - Multiply all values")

numbers = [2, 3, 4, 5]
product = 1                         # Initialize to 1 for multiplication

print(f"Numbers: {numbers}")
print("Process:")

for number in numbers:
    print(f"  Multiplying {number}: {product} × {number} = {product * number}")
    product = product * number      # Accumulate the product

print(f"Final product: {product}")
print()

# Count accumulator
print("1C. COUNT ACCUMULATOR - Count items meeting criteria")

words = ["apple", "banana", "apricot", "cherry", "avocado", "blueberry"]
count = 0                           # Initialize counter

print(f"Words: {words}")
print("Counting words that start with 'a':")

for word in words:
    if word.startswith('a'):
        count = count + 1           # Increment counter
        print(f"  '{word}' starts with 'a' - count now: {count}")
    else:
        print(f"  '{word}' doesn't start with 'a' - count still: {count}")

print(f"Total words starting with 'a': {count}")
print()

# String accumulator
print("1D. STRING ACCUMULATOR - Build strings character by character")

sentence = "Hello World"
vowels = ""                         # Initialize empty string
vowel_letters = "aeiouAEIOU"

print(f"Original: '{sentence}'")
print("Extracting vowels:")

for char in sentence:
    if char in vowel_letters:
        vowels = vowels + char      # Accumulate vowels
        print(f"  '{char}' is a vowel - vowels now: '{vowels}'")
    else:
        print(f"  '{char}' is not a vowel - vowels still: '{vowels}'")

print(f"All vowels found: '{vowels}'")
print()

# PATTERN 2: FIND PATTERNS
print("=== PATTERN 2: FIND PATTERNS ===")
print()

print("Find patterns locate specific items or values in data.")
print()

# Find minimum
print("2A. FIND MINIMUM - Locate the smallest value")

numbers = [45, 23, 67, 12, 89, 5, 34]
minimum = numbers[0]                # Start with first value

print(f"Numbers: {numbers}")
print(f"Starting with first value as minimum: {minimum}")

for number in numbers[1:]:          # Start from second value
    print(f"  Comparing {number} with current min {minimum}")
    if number < minimum:
        minimum = number
        print(f"    New minimum found: {minimum}")
    else:
        print(f"    {minimum} is still smaller")

print(f"Final minimum: {minimum}")
print()

# Find maximum with position
print("2B. FIND MAXIMUM with POSITION")

scores = [85, 92, 78, 96, 88, 91]
max_score = scores[0]
max_position = 0

print(f"Scores: {scores}")
print("Finding highest score and its position:")

for i in range(len(scores)):
    score = scores[i]
    print(f"  Position {i}: score {score}")
    
    if score > max_score:
        max_score = score
        max_position = i
        print(f"    New maximum: {max_score} at position {max_position}")

print(f"Highest score: {max_score} at position {max_position}")
print()

# Find first occurrence
print("2C. FIND FIRST OCCURRENCE")

items = ["cat", "dog", "bird", "cat", "fish", "cat"]
target = "cat"
position = -1                       # -1 means "not found"

print(f"Items: {items}")
print(f"Looking for first occurrence of '{target}':")

for i in range(len(items)):
    print(f"  Position {i}: '{items[i]}'")
    
    if items[i] == target:
        position = i
        print(f"    Found '{target}' at position {i}!")
        break                       # Stop at first occurrence
    else:
        print(f"    Not '{target}', continuing...")

if position != -1:
    print(f"First '{target}' found at position {position}")
else:
    print(f"'{target}' not found")

print()

# PATTERN 3: FILTER PATTERNS  
print("=== PATTERN 3: FILTER PATTERNS ===")
print()

print("Filter patterns collect items that meet specific criteria.")
print()

# Filter by condition
print("3A. FILTER BY CONDITION - Collect even numbers")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []                   # Initialize empty list

print(f"Original numbers: {numbers}")
print("Filtering for even numbers:")

for number in numbers:
    if number % 2 == 0:             # Check if even
        even_numbers.append(number)
        print(f"  {number} is even - added to list: {even_numbers}")
    else:
        print(f"  {number} is odd - skipped")

print(f"Even numbers: {even_numbers}")
print()

# Filter by multiple criteria
print("3B. FILTER BY MULTIPLE CRITERIA - Valid passwords")

passwords = ["abc", "password123", "12345", "StrongPass1!", "weak", "MySecret99"]
valid_passwords = []

print("Password requirements: At least 8 characters, contains digit")
print(f"Testing passwords: {passwords}")

for password in passwords:
    print(f"  Testing '{password}':")
    
    # Check length
    if len(password) < 8:
        print(f"    Too short ({len(password)} chars) - rejected")
        continue
    
    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    if not has_digit:
        print(f"    No digit found - rejected")
        continue
    
    # Password is valid
    valid_passwords.append(password)
    print(f"    Valid password - accepted!")

print(f"Valid passwords: {valid_passwords}")
print()

# PATTERN 4: TRANSFORM PATTERNS
print("=== PATTERN 4: TRANSFORM PATTERNS ===")
print()

print("Transform patterns convert data from one form to another.")
print()

# Transform values
print("4A. TRANSFORM VALUES - Convert temperatures")

celsius_temps = [0, 20, 37, 100, -10]
fahrenheit_temps = []

print(f"Celsius temperatures: {celsius_temps}")
print("Converting to Fahrenheit (F = C × 9/5 + 32):")

for celsius in celsius_temps:
    fahrenheit = celsius * 9/5 + 32
    fahrenheit_temps.append(fahrenheit)
    print(f"  {celsius}°C = {fahrenheit}°F")

print(f"Fahrenheit temperatures: {fahrenheit_temps}")
print()

# Transform strings
print("4B. TRANSFORM STRINGS - Capitalize names")

names = ["john doe", "mary SMITH", "bob johnson", "alice BROWN"]
proper_names = []

print(f"Original names: {names}")
print("Converting to proper case:")

for name in names:
    proper_name = name.title()      # Convert to Title Case
    proper_names.append(proper_name)
    print(f"  '{name}' → '{proper_name}'")

print(f"Proper names: {proper_names}")
print()

# PATTERN 5: VALIDATION PATTERNS
print("=== PATTERN 5: VALIDATION PATTERNS ===")
print()

print("Validation patterns check if data meets all required conditions.")
print()

# Validate all items
print("5A. VALIDATE ALL - Check if all numbers are positive")

test_cases = [
    [1, 2, 3, 4, 5],           # All positive
    [0, 1, 2, 3],              # Contains zero
    [-1, 2, 3, 4],             # Contains negative
    [10, 20, 30]               # All positive
]

for case_num, numbers in enumerate(test_cases, 1):
    print(f"Test case {case_num}: {numbers}")
    
    all_positive = True         # Assume true until proven false
    
    for number in numbers:
        print(f"  Checking {number}: ", end="")
        if number <= 0:
            all_positive = False
            print("not positive - validation failed")
            break           # No need to check further
        else:
            print("positive ✓")
    
    result = "✅ All positive" if all_positive else "❌ Not all positive"
    print(f"  Result: {result}")
    print()

# Validate any item
print("5B. VALIDATE ANY - Check if any word contains 'ing'")

sentences = [
    ["I", "am", "running", "fast"],
    ["The", "cat", "sleeps"],
    ["We", "are", "singing", "songs"],
    ["No", "match", "here"]
]

for case_num, words in enumerate(sentences, 1):
    print(f"Sentence {case_num}: {words}")
    
    has_ing = False
    
    for word in words:
        print(f"  Checking '{word}': ", end="")
        if "ing" in word:
            has_ing = True
            print("contains 'ing' ✓")
            break               # Found one, no need to continue
        else:
            print("no 'ing'")
    
    result = "✅ Contains 'ing'" if has_ing else "❌ No 'ing' found"
    print(f"  Result: {result}")
    print()

# PATTERN 6: COUNTER PATTERNS
print("=== PATTERN 6: COUNTER PATTERNS ===")
print()

print("Counter patterns count frequencies or occurrences.")
print()

# Count frequencies
print("6A. COUNT FREQUENCIES - Letter frequency analysis")

text = "hello world"
letter_counts = {}              # Dictionary to store counts

print(f"Analyzing text: '{text}'")
print("Counting each letter:")

for char in text:
    if char.isalpha():          # Only count letters
        char = char.lower()     # Convert to lowercase
        
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
        
        print(f"  '{char}': {letter_counts[char]} occurrences")

print(f"Final counts: {letter_counts}")
print()

# Count by categories
print("6B. COUNT BY CATEGORIES - Grade distribution")

grades = [85, 92, 78, 65, 88, 91, 72, 95, 84, 67]
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

print(f"Grades: {grades}")
print("Grade scale: A(90+), B(80-89), C(70-79), D(60-69), F(<60)")

for grade in grades:
    print(f"  Grade {grade}: ", end="")
    
    if grade >= 90:
        grade_counts["A"] += 1
        print("A")
    elif grade >= 80:
        grade_counts["B"] += 1
        print("B")
    elif grade >= 70:
        grade_counts["C"] += 1
        print("C")
    elif grade >= 60:
        grade_counts["D"] += 1
        print("D")
    else:
        grade_counts["F"] += 1
        print("F")

print(f"Grade distribution: {grade_counts}")
print()

# PATTERN 7: FLAG PATTERNS
print("=== PATTERN 7: FLAG PATTERNS ===")
print()

print("Flag patterns track states or conditions during processing.")
print()

# Single flag
print("7A. SINGLE FLAG - Check for duplicates")

numbers = [1, 2, 3, 4, 2, 5]
has_duplicates = False

print(f"Numbers: {numbers}")
print("Checking for duplicates:")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(f"  Comparing position {i}({numbers[i]}) with position {j}({numbers[j]})")
        
        if numbers[i] == numbers[j]:
            has_duplicates = True
            print(f"    Duplicate found: {numbers[i]}")
            break
    
    if has_duplicates:              # Exit outer loop too
        break

result = "✅ Duplicates found" if has_duplicates else "❌ No duplicates"
print(f"Result: {result}")
print()

# Multiple flags
print("7B. MULTIPLE FLAGS - Password strength checker")

password = "MyPassword123!"
flags = {
    "has_upper": False,
    "has_lower": False,
    "has_digit": False,
    "has_special": False,
    "long_enough": len(password) >= 8
}

print(f"Password: '{password}'")
print("Checking requirements:")

special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

for char in password:
    print(f"  Character '{char}': ", end="")
    
    checks = []
    if char.isupper():
        flags["has_upper"] = True
        checks.append("uppercase")
    if char.islower():
        flags["has_lower"] = True
        checks.append("lowercase")
    if char.isdigit():
        flags["has_digit"] = True
        checks.append("digit")
    if char in special_chars:
        flags["has_special"] = True
        checks.append("special")
    
    if checks:
        print(", ".join(checks))
    else:
        print("no special properties")

print(f"\nPassword requirements status:")
for requirement, status in flags.items():
    status_icon = "✅" if status else "❌"
    print(f"  {requirement}: {status_icon}")

all_met = all(flags.values())
strength = "Strong" if all_met else "Weak"
print(f"\nPassword strength: {strength}")
print()

# COMBINING PATTERNS
print("=== COMBINING PATTERNS ===")
print()

print("Real-world example: Student grade analysis")

students = [
    {"name": "Alice", "grades": [85, 92, 78, 96]},
    {"name": "Bob", "grades": [72, 85, 79, 88]},
    {"name": "Charlie", "grades": [95, 98, 92, 94]},
    {"name": "Diana", "grades": [68, 74, 71, 77]}
]

print("Analyzing student performance...")
print()

class_total = 0
class_count = 0
honor_roll = []                     # Filter pattern
grade_distribution = {"A": 0, "B": 0, "C": 0, "D": 0}  # Counter pattern

for student in students:
    name = student["name"]
    grades = student["grades"]
    
    print(f"Student: {name}")
    print(f"  Grades: {grades}")
    
    # Accumulator pattern - calculate average
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    
    print(f"  Average: {average:.1f}")
    
    # Transform pattern - assign letter grade
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    else:
        letter_grade = "D"
    
    print(f"  Letter Grade: {letter_grade}")
    
    # Counter pattern - track distribution
    grade_distribution[letter_grade] += 1
    
    # Filter pattern - identify honor roll (A average)
    if letter_grade == "A":
        honor_roll.append(name)
        print(f"  🏆 Honor Roll!")
    
    # Accumulator pattern - class statistics
    class_total += average
    class_count += 1
    
    print()

# Final analysis
class_average = class_total / class_count
print(f"=== CLASS SUMMARY ===")
print(f"Class average: {class_average:.1f}")
print(f"Grade distribution: {grade_distribution}")
print(f"Honor roll students: {honor_roll}")

print()

print("=== PATTERN SUMMARY ===")
print()
print("1. ACCUMULATOR: Build up results (sum, product, count, concatenate)")
print("2. FIND: Locate specific values (min, max, first, last)")
print("3. FILTER: Collect items meeting criteria")
print("4. TRANSFORM: Convert data to different format")
print("5. VALIDATION: Check if conditions are met")
print("6. COUNTER: Track frequencies and distributions")
print("7. FLAG: Monitor states and conditions")
print()
print("💡 Combine patterns to solve complex problems!")
print("💡 Most algorithms use multiple patterns together!")

"""
KEY TAKEAWAYS:
==============
1. Loop patterns are reusable solutions to common problems
2. Accumulator: Build results incrementally (sum, count, concatenate)
3. Find: Locate specific items (min/max, search, position)
4. Filter: Collect items meeting criteria
5. Transform: Convert data between formats
6. Validation: Check all/any conditions
7. Counter: Track frequencies and categories
8. Flag: Monitor states during processing
9. Combine patterns for complex solutions

MASTER THESE PATTERNS:
======================
• Accumulator: total = 0; for x in data: total += x
• Find Min: min_val = data[0]; for x in data[1:]: if x < min_val: min_val = x
• Filter: result = []; for x in data: if condition(x): result.append(x)
• Transform: result = []; for x in data: result.append(transform(x))
• Validate All: valid = True; for x in data: if not check(x): valid = False; break
• Count: count = 0; for x in data: if condition(x): count += 1
• Flag: found = False; for x in data: if condition(x): found = True; break

PROBLEM-SOLVING APPROACH:
=========================
1. Identify what type of result you need
2. Choose the appropriate pattern(s)
3. Initialize variables correctly
4. Process data item by item
5. Update accumulators/flags/counters as needed
6. Return or display final result

NEXT STEP:
Go to 07-complete-program.py to see all these concepts in one comprehensive program!
"""