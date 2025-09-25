"""
Assignment 3 - Example 2: FOR Loops with Sequences
=================================================

This program demonstrates how to use for loops with sequences like
lists, strings, and other collections. This is incredibly powerful
for processing data collections efficiently.

Key Concepts Demonstrated:
- Iterating over lists, tuples, and strings
- Accessing both index and value with enumerate()
- Processing collections of data
- String character-by-character processing
- Real-world data processing examples
"""

print("=== FOR LOOPS WITH SEQUENCES ===")
print()

# ITERATING OVER LISTS
print("=== ITERATING OVER LISTS ===")
print()

# Example 1: Simple list iteration
print("Example 1: Iterating over a list of names")

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(f"Student list: {students}")
print()

print("Greeting each student:")
for student in students:        # 'student' takes each value in the list
    print(f"Hello, {student}! Welcome to class.")

print()

# Example 2: Processing numbers in a list
print("Example 2: Processing a list of test scores")

test_scores = [85, 92, 78, 96, 88, 73, 91]
print(f"Test scores: {test_scores}")
print()

# Calculate statistics
total = 0
highest = test_scores[0]        # Initialize with first score
lowest = test_scores[0]         # Initialize with first score

print("Processing each score:")
for score in test_scores:
    print(f"Processing score: {score}")
    
    # Update total
    total = total + score
    print(f"  Running total: {total}")
    
    # Check if this is the highest score so far
    if score > highest:
        highest = score
        print(f"  New highest score: {highest}")
    
    # Check if this is the lowest score so far
    if score < lowest:
        lowest = score
        print(f"  New lowest score: {lowest}")

# Calculate average
average = total / len(test_scores)

print(f"\n=== STATISTICS ===")
print(f"Number of scores: {len(test_scores)}")
print(f"Total points: {total}")
print(f"Average score: {average:.2f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print()

# USING ENUMERATE() TO GET INDEX AND VALUE
print("=== USING ENUMERATE() FOR INDEX AND VALUE ===")
print()

# enumerate() gives you both the index (position) and the value
colors = ["red", "green", "blue", "yellow", "purple"]

print("List with positions:")
for index, color in enumerate(colors):
    print(f"Position {index}: {color}")

print()

# Practical example: numbered list
print("Creating a numbered menu:")
menu_items = ["Pizza", "Burger", "Salad", "Pasta", "Sandwich"]

for position, item in enumerate(menu_items, 1):  # Start numbering at 1
    print(f"{position}. {item}")

print()

# ITERATING OVER STRINGS
print("=== ITERATING OVER STRINGS ===")
print()

# Example 1: Character-by-character processing
print("Example 1: Analyzing characters in a string")

word = input("Enter a word to analyze: ")
print(f"Analyzing the word: '{word}'")
print()

vowel_count = 0
consonant_count = 0
vowels = "aeiouAEIOU"

print("Character analysis:")
for position, character in enumerate(word):
    print(f"Position {position}: '{character}'", end="")
    
    if character.isalpha():     # Check if it's a letter
        if character in vowels:
            vowel_count += 1
            print(" (vowel)")
        else:
            consonant_count += 1
            print(" (consonant)")
    else:
        print(" (not a letter)")

print(f"\n=== WORD ANALYSIS RESULTS ===")
print(f"Word: '{word}'")
print(f"Total characters: {len(word)}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print(f"Non-letters: {len(word) - vowel_count - consonant_count}")
print()

# Example 2: String transformation
print("Example 2: Building a new string from characters")

original = "Python Programming"
print(f"Original string: '{original}'")

# Build various transformations
uppercase_chars = ""
lowercase_chars = ""
no_spaces = ""
only_letters = ""

for char in original:
    uppercase_chars += char.upper()
    lowercase_chars += char.lower()
    
    if char != " ":             # Skip spaces
        no_spaces += char
    
    if char.isalpha():          # Only letters
        only_letters += char

print("Transformations:")
print(f"All uppercase: '{uppercase_chars}'")
print(f"All lowercase: '{lowercase_chars}'")
print(f"No spaces: '{no_spaces}'")
print(f"Only letters: '{only_letters}'")
print()

# PROCESSING LISTS OF DIFFERENT DATA TYPES
print("=== PROCESSING MIXED DATA TYPES ===")
print()

# Example: Student information processing
students_info = [
    ["Alice", 20, 85.5],
    ["Bob", 19, 92.3],
    ["Charlie", 21, 78.9],
    ["Diana", 20, 88.7]
]

print("Student Information Processing:")
print("Name     | Age | Grade")
print("---------|-----|-------")

total_grade = 0
for student_data in students_info:
    name = student_data[0]
    age = student_data[1]
    grade = student_data[2]
    
    print(f"{name:<8} | {age:2d}  | {grade:5.1f}")
    total_grade += grade

class_average = total_grade / len(students_info)
print("---------|-----|-------")
print(f"Class Average:   {class_average:5.1f}")
print()

# PRACTICAL EXAMPLE: SHOPPING CART
print("=== PRACTICAL EXAMPLE: SHOPPING CART PROCESSOR ===")
print()

# Shopping cart with items and prices
shopping_cart = [
    ("Apples", 3.50),
    ("Bread", 2.25),
    ("Milk", 4.80),
    ("Eggs", 3.25),
    ("Cheese", 6.75)
]

print("SHOPPING CART RECEIPT")
print("=" * 30)

subtotal = 0
for item, price in shopping_cart:      # Unpack tuple into two variables
    print(f"{item:<15} £{price:6.2f}")
    subtotal += price

# Calculate tax and total
tax_rate = 0.20  # 20% VAT
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print("-" * 30)
print(f"Subtotal:       £{subtotal:6.2f}")
print(f"Tax (20%):      £{tax_amount:6.2f}")
print(f"TOTAL:          £{total:6.2f}")
print("=" * 30)
print()

# FINDING ITEMS IN SEQUENCES
print("=== SEARCHING IN SEQUENCES ===")
print()

# Example 1: Find specific items
inventory = ["laptop", "mouse", "keyboard", "monitor", "speakers", "webcam"]

print("Current inventory:", inventory)
search_item = input("What item are you looking for? ").lower()

found = False
position = 0

print(f"\nSearching for '{search_item}'...")
for index, item in enumerate(inventory):
    if item == search_item:
        found = True
        position = index
        break                   # Exit loop when found

if found:
    print(f"✅ Found '{search_item}' at position {position}")
else:
    print(f"❌ '{search_item}' not found in inventory")

print()

# Example 2: Count occurrences
print("Example 2: Count letter occurrences")
sentence = input("Enter a sentence: ")
target_letter = input("Enter a letter to count: ").lower()

count = 0
positions = []

for index, char in enumerate(sentence.lower()):
    if char == target_letter:
        count += 1
        positions.append(index)

print(f"\nResults for letter '{target_letter}':")
print(f"Occurrences: {count}")
if positions:
    print(f"Found at positions: {positions}")
else:
    print("Letter not found in the sentence")

print()

# FILTERING AND TRANSFORMING DATA
print("=== FILTERING AND TRANSFORMING DATA ===")
print()

# Example: Grade filtering
all_grades = [95, 67, 88, 45, 92, 78, 56, 89, 91, 34, 76, 82]

print(f"All grades: {all_grades}")

# Filter grades into categories
excellent_grades = []  # 90+
good_grades = []       # 80-89
average_grades = []    # 70-79
poor_grades = []       # Below 70

for grade in all_grades:
    if grade >= 90:
        excellent_grades.append(grade)
    elif grade >= 80:
        good_grades.append(grade)
    elif grade >= 70:
        average_grades.append(grade)
    else:
        poor_grades.append(grade)

print("\n=== GRADE DISTRIBUTION ===")
print(f"Excellent (90+): {excellent_grades}")
print(f"Good (80-89):    {good_grades}")
print(f"Average (70-79): {average_grades}")
print(f"Poor (<70):      {poor_grades}")

print(f"\nDistribution counts:")
print(f"Excellent: {len(excellent_grades)} students")
print(f"Good:      {len(good_grades)} students")
print(f"Average:   {len(average_grades)} students")
print(f"Poor:      {len(poor_grades)} students")
print()

# WORKING WITH USER INPUT LISTS
print("=== WORKING WITH USER-GENERATED LISTS ===")
print()

print("Dynamic list creation from user input")
numbers = []
num_items = int(input("How many numbers do you want to enter? "))

print(f"Please enter {num_items} numbers:")
for i in range(num_items):
    number = float(input(f"Number {i+1}: "))
    numbers.append(number)

print(f"\nYou entered: {numbers}")

# Process the user's numbers
print("\nProcessing your numbers:")
for i, number in enumerate(numbers):
    square = number ** 2
    cube = number ** 3
    print(f"Number {i+1}: {number}")
    print(f"  Square: {square}")
    print(f"  Cube: {cube}")
    print()

print("=== SUMMARY ===")
print()
print("Key Points about FOR loops with sequences:")
print("1. Use 'for item in sequence:' to iterate over collections")
print("2. The loop variable takes each value in the sequence")
print("3. Use enumerate() to get both index and value")
print("4. Works with lists, tuples, strings, and other sequences")
print("5. Perfect for processing collections of data")
print("6. Can filter, transform, and analyze data efficiently")
print("7. No need to manually manage indexes or counters")

"""
KEY TAKEAWAYS:
==============
1. for loops work naturally with sequences (lists, strings, tuples)
2. Loop variables automatically take each value in the sequence
3. enumerate() provides both index and value when you need position info
4. String iteration processes characters one by one
5. Perfect for data processing, analysis, and transformation
6. More Pythonic than manually indexing with range(len(sequence))

POWERFUL PATTERNS:
==================
- Data filtering: separate items into categories
- Data transformation: modify each item in a collection
- Searching: find specific items or count occurrences
- Statistics: calculate sums, averages, min/max
- String processing: analyze or modify text character by character

COMMON MISTAKES:
================
- Using range(len(sequence)) when you could iterate directly
- Forgetting that strings are sequences of characters
- Not understanding tuple unpacking with enumerate()
- Modifying a list while iterating over it (can cause issues)

NEXT STEP:
Go to 03-while-loops.py to learn about condition-based repetition!
"""