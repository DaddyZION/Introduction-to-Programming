"""
Assignment 1 - Example 4: String Operations
=========================================

This program demonstrates working with STRINGS (text data).
Strings are sequences of characters and are fundamental to most programs.
You'll learn how to manipulate, combine, and format text effectively.

Key Concepts Demonstrated:
- String creation and basic operations
- String concatenation (joining)
- String methods for manipulation
- String formatting and presentation
- String indexing and slicing
- Common string operations in real programs
"""

print("=== STRING BASICS ===")
print()

# CREATING STRINGS
# Strings can be created with single or double quotes
first_name = "Alice"              # Double quotes
last_name = 'Johnson'            # Single quotes - works the same
university = "Tech University"    # Use consistent style in your programs

print("Basic string variables:")
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"University: {university}")
print()

# MULTI-LINE STRINGS
# Triple quotes allow strings to span multiple lines
poem = """Programming is fun,
Code runs line by line,
Variables store our data,
Everything works fine!"""

print("Multi-line string:")
print(poem)
print()

# STRING CONCATENATION - Joining strings together
print("=== STRING CONCATENATION ===")
print()

# Method 1: Using + operator
full_name = first_name + " " + last_name
print(f"Using + operator: {full_name}")

# Method 2: Using f-strings (recommended - most readable)
greeting = f"Hello, {first_name} {last_name}!"
print(f"Using f-string: {greeting}")

# Method 3: Using .format() method
introduction = "My name is {} and I study at {}".format(full_name, university)
print(f"Using .format(): {introduction}")

# Method 4: Using % formatting (older style)
student_info = "Student: %s, Age: %d" % (full_name, 20)
print(f"Using % formatting: {student_info}")
print()

# STRING LENGTH
print("=== STRING LENGTH ===")
print()

message = "Programming is awesome!"
length = len(message)
print(f"Message: '{message}'")
print(f"Length: {length} characters")
print()

# STRING METHODS - Built-in functions for string manipulation
print("=== USEFUL STRING METHODS ===")
print()

sample_text = "   Hello World Programming   "
print(f"Original: '{sample_text}'")

# Case conversion methods
print(f"Upper case: '{sample_text.upper()}'")
print(f"Lower case: '{sample_text.lower()}'")
print(f"Title case: '{sample_text.title()}'")
print(f"Capitalize: '{sample_text.capitalize()}'")

# Whitespace removal methods
print(f"Strip whitespace: '{sample_text.strip()}'")
print(f"Left strip: '{sample_text.lstrip()}'")
print(f"Right strip: '{sample_text.rstrip()}'")

# Replacement and checking methods
print(f"Replace 'World' with 'Python': '{sample_text.replace('World', 'Python')}'")
print(f"Contains 'Programming': {sample_text.__contains__('Programming')}")
print(f"Starts with 'Hello': {sample_text.strip().startswith('Hello')}")
print(f"Ends with 'ing': {sample_text.strip().endswith('ing')}")
print()

# STRING INDEXING - Accessing individual characters
print("=== STRING INDEXING ===")
print()

word = "PYTHON"
print(f"Word: {word}")
print("Index positions: 0=P, 1=Y, 2=T, 3=H, 4=O, 5=N")

# Positive indexing (from left, starting at 0)
print(f"First character [0]: {word[0]}")
print(f"Third character [2]: {word[2]}")
print(f"Last character [5]: {word[5]}")

# Negative indexing (from right, starting at -1)
print(f"Last character [-1]: {word[-1]}")
print(f"Second last [-2]: {word[-2]}")
print(f"First character [-6]: {word[-6]}")
print()

# STRING SLICING - Extracting parts of strings
print("=== STRING SLICING ===")
print()

sentence = "Programming is fun"
print(f"Full sentence: '{sentence}'")

# Slicing syntax: string[start:end]  (end is not included)
print(f"First 11 characters [0:11]: '{sentence[0:11]}'")
print(f"From index 12 to end [12:]: '{sentence[12:]}'")
print(f"First 4 characters [:4]: '{sentence[:4]}'")
print(f"Last 3 characters [-3:]: '{sentence[-3:]}'")
print(f"Middle part [12:14]: '{sentence[12:14]}'")
print()

# PRACTICAL EXAMPLE 1: NAME PROCESSING
print("=== PRACTICAL EXAMPLE 1: NAME PROCESSING ===")
print()

print("Enter your full name (first and last):")
full_name = input("Full name: ").strip()  # Remove extra spaces

# Split the name into parts
names = full_name.split()  # Splits on whitespace
if len(names) >= 2:
    first = names[0]
    last = names[-1]  # Last element (handles middle names)
    
    print(f"\nName processing results:")
    print(f"Full name: {full_name}")
    print(f"First name: {first}")
    print(f"Last name: {last}")
    print(f"Initials: {first[0]}.{last[0]}.")
    print(f"Formal: {last}, {first}")
    print(f"Username suggestion: {first.lower()}.{last.lower()}")
else:
    print("Please enter both first and last name")
print()

# PRACTICAL EXAMPLE 2: EMAIL VALIDATION BASICS
print("=== PRACTICAL EXAMPLE 2: BASIC EMAIL PROCESSING ===")
print()

email = input("Enter your email address: ").strip().lower()

if "@" in email and "." in email:
    # Split email into parts
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]
    
    print(f"\nEmail analysis:")
    print(f"Full email: {email}")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Email length: {len(email)} characters")
    
    # Check domain
    if domain.endswith('.edu'):
        print("This appears to be an educational email address")
    elif domain.endswith('.com'):
        print("This appears to be a commercial email address")
    elif domain.endswith('.org'):
        print("This appears to be an organizational email address")
else:
    print("Email format doesn't look correct (missing @ or .)")
print()

# PRACTICAL EXAMPLE 3: TEXT FORMATTING
print("=== PRACTICAL EXAMPLE 3: REPORT FORMATTING ===")
print()

# Get student information
student_name = input("Student name: ").title()  # Capitalize properly
student_id = input("Student ID: ").upper()     # Make uppercase
course_name = input("Course name: ").title()
grade = input("Grade: ").upper()

# Create a formatted report
print("\n" + "="*50)
print("STUDENT GRADE REPORT".center(50))
print("="*50)
print(f"Student: {student_name:<20} ID: {student_id}")
print(f"Course:  {course_name}")
print(f"Grade:   {grade}")
print("="*50)
print("Report generated successfully!")
print()

# STRING COMPARISON
print("=== STRING COMPARISON ===")
print()

password = "SecretPass123"
user_input = input("Enter the password: ")

# String comparison is case-sensitive
if user_input == password:
    print("✅ Password correct!")
else:
    print("❌ Password incorrect!")
    print(f"You entered: '{user_input}'")
    print(f"Expected: '{password}'")
    
    # Show case-insensitive comparison
    if user_input.lower() == password.lower():
        print("Note: Password matches if we ignore case differences")
print()

# ESCAPE CHARACTERS - Special characters in strings
print("=== ESCAPE CHARACTERS ===")
print()

# Common escape characters
print("Escape character examples:")
print("New line: Line 1\\nLine 2 becomes:")
print("Line 1\nLine 2")
print()
print("Tab character: Name\\tAge becomes:")
print("Name\tAge")
print("Alice\t25")
print("Bob\t30")
print()
print("Quotes in strings: \"Hello,\" he said")
print("Single quote in string: 'It\\'s a nice day'")
print()

# RAW STRINGS - For file paths and regular expressions
print("=== RAW STRINGS ===")
print()

# Regular string (escape characters are processed)
file_path1 = "C:\\Users\\Alice\\Documents\\file.txt"
print(f"Regular string: {file_path1}")

# Raw string (escape characters are treated literally)
file_path2 = r"C:\Users\Alice\Documents\file.txt"
print(f"Raw string: {file_path2}")
print()

print("=== SUMMARY ===")
print()
print("Key String Operations:")
print("1. Create strings with quotes: 'text' or \"text\"")
print("2. Join strings: + operator or f-strings")
print("3. String methods: .upper(), .lower(), .strip(), .replace()")
print("4. Access characters: string[index]")
print("5. Extract parts: string[start:end]")
print("6. Check content: 'substring' in string")
print("7. Length: len(string)")
print()
print("Best Practices:")
print("- Use f-strings for readable formatting")
print("- Use .strip() when getting user input")
print("- Remember string comparison is case-sensitive")
print("- Use meaningful variable names for strings")

"""
KEY TAKEAWAYS:
==============
1. Strings store text data and are created with quotes
2. Use f-strings for clean, readable string formatting
3. Many useful methods: .upper(), .lower(), .strip(), .replace()
4. String indexing starts at 0: string[0] is first character
5. Slicing extracts parts: string[start:end]
6. Strings are immutable - methods return new strings
7. String comparison is case-sensitive

COMMON MISTAKES:
================
- Forgetting that indexing starts at 0, not 1
- Not using .strip() when processing user input
- Case sensitivity in string comparisons
- Confusing string slicing syntax

NEXT STEP:
Go to 05-complete-program.py to see everything working together!
"""