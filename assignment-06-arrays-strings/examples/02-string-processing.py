"""
Assignment 6 - Example 2: String Processing
===========================================

This program explores comprehensive string manipulation and text processing
techniques in Python. Strings are sequences of characters and share many
properties with arrays/lists, but have specialized methods for text operations.
Understanding string processing is crucial for handling user input, file
processing, and data manipulation tasks.

Key Concepts Demonstrated:
- String creation, access, and immutability
- String methods for case conversion, searching, and validation
- String formatting techniques
- Text parsing and manipulation
- Regular expression patterns (basic introduction)
- Character encoding and Unicode handling
"""

import re  # Regular expressions module

print("=== STRING PROCESSING ===")
print()

print("Strings are sequences of characters with specialized text operations:")
print("• Immutable - cannot be changed after creation")
print("• Indexed like arrays (zero-based indexing)")
print("• Rich set of built-in methods for text processing")
print("• Support for Unicode characters and encoding")
print("• Can be treated as arrays of characters")
print()

# STRING CREATION AND BASIC PROPERTIES
print("=== STRING CREATION AND BASIC PROPERTIES ===")
print()

# Different ways to create strings
single_quotes = 'Hello, World!'
double_quotes = "Hello, World!"
triple_quotes = """This is a
multi-line
string"""
raw_string = r"This is a raw string with \n not interpreted"
formatted_string = f"Current year: {2024}"

print("String creation methods:")
print(f"  Single quotes: {repr(single_quotes)}")
print(f"  Double quotes: {repr(double_quotes)}")
print(f"  Triple quotes: {repr(triple_quotes)}")
print(f"  Raw string: {repr(raw_string)}")
print(f"  F-string: {formatted_string}")
print()

# String properties and characteristics
sample_text = "Programming is fun!"
print(f"Sample string: '{sample_text}'")
print(f"Length: {len(sample_text)}")
print(f"Type: {type(sample_text)}")
print(f"First character: '{sample_text[0]}'")
print(f"Last character: '{sample_text[-1]}'")
print(f"Character at index 5: '{sample_text[5]}'")
print()

# String immutability demonstration
print("String immutability:")
original = "Hello"
print(f"Original string: '{original}'")
try:
    original[0] = "h"  # This will raise an error
except TypeError as e:
    print(f"  Cannot modify string: {e}")
print()

# STRING INDEXING AND SLICING
print("=== STRING INDEXING AND SLICING ===")
print()

text_sample = "Python Programming"
print(f"Sample text: '{text_sample}'")
print("Index positions:  0123456789012345678")
print("Negative indices: -17-16-15...  -2 -1")
print()

print("Character access:")
print(f"  text_sample[0] = '{text_sample[0]}'")
print(f"  text_sample[7] = '{text_sample[7]}'")
print(f"  text_sample[-1] = '{text_sample[-1]}'")
print(f"  text_sample[-11] = '{text_sample[-11]}'")
print()

print("String slicing:")
print(f"  text_sample[0:6] = '{text_sample[0:6]}'")    # "Python"
print(f"  text_sample[7:] = '{text_sample[7:]}'")      # "Programming"
print(f"  text_sample[:6] = '{text_sample[:6]}'")      # "Python"
print(f"  text_sample[::2] = '{text_sample[::2]}'")    # Every 2nd character
print(f"  text_sample[::-1] = '{text_sample[::-1]}'")  # Reverse string
print()

# Advanced slicing examples
print("Advanced slicing patterns:")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f"Alphabet: {alphabet}")
print(f"  First 5 letters: {alphabet[:5]}")
print(f"  Last 5 letters: {alphabet[-5:]}")
print(f"  Every 3rd letter: {alphabet[::3]}")
print(f"  Reverse every 2nd: {alphabet[::-2]}")
print(f"  Middle section: {alphabet[10:16]}")
print()

# STRING METHODS - CASE CONVERSION
print("=== STRING METHODS - CASE CONVERSION ===")
print()

mixed_case = "PyThOn PrOgRaMmInG iS AwEsOmE!"
print(f"Original: '{mixed_case}'")
print(f"  lower(): '{mixed_case.lower()}'")
print(f"  upper(): '{mixed_case.upper()}'")
print(f"  capitalize(): '{mixed_case.capitalize()}'")
print(f"  title(): '{mixed_case.title()}'")
print(f"  swapcase(): '{mixed_case.swapcase()}'")
print()

# Handling special cases
special_cases = "hello world 123 ñoël"
print(f"Special cases: '{special_cases}'")
print(f"  title(): '{special_cases.title()}'")
print(f"  capitalize(): '{special_cases.capitalize()}'")
print()

# Case checking methods
test_strings = ["HELLO", "hello", "Hello", "HeLLo", "123", "Hello123"]
print("Case checking methods:")
for string in test_strings:
    print(f"  '{string}': upper={string.isupper()}, lower={string.islower()}, "
          f"title={string.istitle()}")
print()

# STRING METHODS - SEARCHING AND FINDING
print("=== STRING METHODS - SEARCHING AND FINDING ===")
print()

search_text = "The quick brown fox jumps over the lazy dog"
print(f"Search text: '{search_text}'")
print()

# Basic searching methods
print("Basic searching:")
print(f"  'fox' in text: {'fox' in search_text}")
print(f"  'cat' in text: {'cat' in search_text}")
print(f"  find('fox'): {search_text.find('fox')}")
print(f"  find('cat'): {search_text.find('cat')}")  # Returns -1 if not found
print(f"  index('fox'): {search_text.index('fox')}")
print()

# Find with start and end positions
print("Find with position parameters:")
print(f"  find('the'): {search_text.find('the')}")  # First occurrence
print(f"  find('the', 10): {search_text.find('the', 10)}")  # After position 10
print(f"  rfind('the'): {search_text.rfind('the')}")  # Last occurrence
print()

# Count occurrences
print("Counting occurrences:")
print(f"  count('o'): {search_text.count('o')}")
print(f"  count('the'): {search_text.count('the')}")
print(f"  count('quick'): {search_text.count('quick')}")
print()

# Boolean search methods
search_examples = [
    ("startswith('The')", search_text.startswith('The')),
    ("startswith('the')", search_text.startswith('the')),
    ("endswith('dog')", search_text.endswith('dog')),
    ("endswith('cat')", search_text.endswith('cat')),
]

print("Boolean search methods:")
for description, result in search_examples:
    print(f"  {description}: {result}")
print()

# STRING METHODS - VALIDATION AND CLASSIFICATION
print("=== STRING METHODS - VALIDATION AND CLASSIFICATION ===")
print()

validation_samples = [
    "12345",      # All digits
    "hello",      # All letters
    "Hello123",   # Mixed alphanumeric
    "   ",        # All spaces
    "Hello World",# Contains space
    "",           # Empty string
    "user@email.com",  # Email format
    "Hello_World_123"  # With underscores
]

print("String validation methods:")
print(f"{'String':<15} {'isdigit':<8} {'isalpha':<8} {'isalnum':<8} "
      f"{'isspace':<8} {'islower':<8} {'isupper':<8}")
print("-" * 70)

for sample in validation_samples:
    display_sample = sample if sample else "(empty)"
    print(f"'{display_sample}':<15 {str(sample.isdigit()):<8} "
          f"{str(sample.isalpha()):<8} {str(sample.isalnum()):<8} "
          f"{str(sample.isspace()):<8} {str(sample.islower()):<8} "
          f"{str(sample.isupper()):<8}")
print()

# Additional validation methods
print("Additional validation methods:")
special_samples = [
    ("Hello World", "isascii"),
    ("café", "isascii"),
    ("Hello123", "isidentifier"),
    ("123hello", "isidentifier"),
    ("_valid_var", "isidentifier"),
    ("123.45", "isdecimal"),
    ("½", "isnumeric"),
]

for sample, method in special_samples:
    result = getattr(sample, method)()
    print(f"  '{sample}'.{method}(): {result}")
print()

# STRING METHODS - MODIFICATION (RETURN NEW STRINGS)
print("=== STRING METHODS - MODIFICATION ===")
print()

# Whitespace handling
whitespace_demo = "   Hello, World!   "
print(f"Whitespace handling:")
print(f"  Original: '{whitespace_demo}'")
print(f"  strip(): '{whitespace_demo.strip()}'")
print(f"  lstrip(): '{whitespace_demo.lstrip()}'")
print(f"  rstrip(): '{whitespace_demo.rstrip()}'")
print()

# Custom character stripping
custom_strip = "***Hello, World!***"
print(f"Custom character stripping:")
print(f"  Original: '{custom_strip}'")
print(f"  strip('*'): '{custom_strip.strip('*')}'")
print()

# String replacement
replacement_demo = "I love cats and cats love me"
print(f"String replacement:")
print(f"  Original: '{replacement_demo}'")
print(f"  replace('cats', 'dogs'): '{replacement_demo.replace('cats', 'dogs')}'")
print(f"  replace('cats', 'dogs', 1): '{replacement_demo.replace('cats', 'dogs', 1)}'")
print()

# String splitting and joining
print("=== STRING SPLITTING AND JOINING ===")
print()

# Basic splitting
sentence = "apple,banana,cherry,date,elderberry"
words = "The quick brown fox"
print(f"Basic splitting:")
print(f"  '{sentence}'.split(','): {sentence.split(',')}")
print(f"  '{words}'.split(): {words.split()}")  # Split on whitespace
print()

# Advanced splitting
multiline_text = """Line 1
Line 2
Line 3"""
print(f"Multiline splitting:")
print(f"  splitlines(): {multiline_text.splitlines()}")
print()

# Joining strings
fruits = ["apple", "banana", "cherry", "date"]
print(f"String joining:")
print(f"  Fruits list: {fruits}")
print(f"  ', '.join(fruits): '{', '.join(fruits)}'")
print(f"  ' | '.join(fruits): '{' | '.join(fruits)}'")
print(f"  ''.join(fruits): '{''.join(fruits)}'")
print()

# STRING FORMATTING
print("=== STRING FORMATTING ===")
print()

# Old-style % formatting
name = "Alice"
age = 30
score = 85.75
print("Old-style % formatting:")
old_style_result = "Hello, %s! You are %d years old." % (name, age)
print(f"  'Hello, %s! You are %d years old.' % (name, age):")
print(f"  '{old_style_result}'")
print()

# str.format() method
print("str.format() method:")
template = "Hello, {}! You scored {:.2f} points."
print(f"  Template: '{template}'")
print(f"  Result: '{template.format(name, score)}'")

# Named placeholders
named_template = "Hello, {name}! You are {age} years old and scored {score:.1f}."
print(f"  Named template: '{named_template}'")
print(f"  Result: '{named_template.format(name=name, age=age, score=score)}'")
print()

# F-string formatting (modern approach)
print("F-string formatting (Python 3.6+):")
print(f"  f'Hello, {name}! You are {age} years old.': '{f'Hello, {name}! You are {age} years old.'}'")
print(f"  f'Score: {score:.2f}': '{f'Score: {score:.2f}'}'")
print(f"  f'{name.upper()}: {score:.0f}%': '{f'{name.upper()}: {score:.0f}%'}'")
print()

# Advanced formatting options
print("Advanced formatting options:")
number = 1234.5678
print(f"  Number: {number}")
print(f"  f'{number:.2f}' (2 decimal places): '{number:.2f}'")
print(f"  f'{number:,.2f}' (with comma separator): '{number:,.2f}'")
print(f"  f'{number:>10.2f}' (right-aligned, width 10): '{number:>10.2f}'")
print(f"  f'{number:<10.2f}' (left-aligned, width 10): '{number:<10.2f}'")
print(f"  f'{number:^10.2f}' (center-aligned, width 10): '{number:^10.2f}'")
print()

# TEXT PARSING AND EXTRACTION
print("=== TEXT PARSING AND EXTRACTION ===")
print()

def parse_email(email):
    """Parse an email address into username and domain parts."""
    if '@' not in email:
        return None, None
    
    username, domain = email.split('@', 1)  # Split only at first @
    return username.strip(), domain.strip()

def extract_numbers(text):
    """Extract all numbers from a text string."""
    numbers = []
    current_number = ""
    
    for char in text:
        if char.isdigit() or char == '.':
            current_number += char
        else:
            if current_number:
                try:
                    # Try to convert to float, then to int if possible
                    num = float(current_number)
                    if num.is_integer():
                        numbers.append(int(num))
                    else:
                        numbers.append(num)
                except ValueError:
                    pass
                current_number = ""
    
    # Don't forget the last number
    if current_number:
        try:
            num = float(current_number)
            if num.is_integer():
                numbers.append(int(num))
            else:
                numbers.append(num)
        except ValueError:
            pass
    
    return numbers

def parse_csv_line(line):
    """Parse a simple CSV line (handles quoted fields)."""
    fields = []
    current_field = ""
    in_quotes = False
    
    for char in line:
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            fields.append(current_field.strip())
            current_field = ""
        else:
            current_field += char
    
    # Add the last field
    fields.append(current_field.strip())
    return fields

# Demonstrate parsing functions
print("Email parsing:")
email_examples = ["user@example.com", "invalid.email", "test@domain.co.uk"]
for email in email_examples:
    username, domain = parse_email(email)
    print(f"  '{email}' -> username: '{username}', domain: '{domain}'")
print()

print("Number extraction:")
text_with_numbers = "I have 5 apples, 3.5 oranges, and $12.99 in my wallet."
numbers = extract_numbers(text_with_numbers)
print(f"  Text: '{text_with_numbers}'")
print(f"  Numbers found: {numbers}")
print()

print("CSV parsing:")
csv_examples = [
    'John,25,Engineer',
    '"Smith, John",30,"Software Engineer"',
    'Alice,"Manager, Sales",35'
]
for csv_line in csv_examples:
    fields = parse_csv_line(csv_line)
    print(f"  '{csv_line}' -> {fields}")
print()

# REGULAR EXPRESSIONS (BASIC INTRODUCTION)
print("=== REGULAR EXPRESSIONS (BASIC INTRODUCTION) ===")
print()

print("Regular expressions provide powerful pattern matching for strings:")

# Basic pattern matching
text_sample = "Contact me at john@example.com or call (555) 123-4567"
print(f"Sample text: '{text_sample}'")
print()

# Find email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_pattern, text_sample)
print(f"Email pattern matches: {emails}")

# Find phone numbers
phone_pattern = r'\(\d{3}\)\s\d{3}-\d{4}'
phones = re.findall(phone_pattern, text_sample)
print(f"Phone pattern matches: {phones}")
print()

# Pattern substitution
print("Pattern substitution:")
sensitive_text = "My SSN is 123-45-6789 and my phone is (555) 123-4567"
# Mask SSN
masked_ssn = re.sub(r'\d{3}-\d{2}-\d{4}', 'XXX-XX-XXXX', sensitive_text)
print(f"  Original: '{sensitive_text}'")
print(f"  Masked SSN: '{masked_ssn}'")

# Mask phone numbers
masked_phone = re.sub(r'\(\d{3}\)\s\d{3}-\d{4}', '(XXX) XXX-XXXX', masked_ssn)
print(f"  Fully masked: '{masked_phone}'")
print()

# UNICODE AND CHARACTER ENCODING
print("=== UNICODE AND CHARACTER ENCODING ===")
print()

# Unicode characters and handling
unicode_examples = [
    "Hello",           # ASCII
    "Café",            # Latin characters
    "こんにちは",        # Japanese
    "🐍",              # Emoji
    "Ñoël",            # Accented characters
]

print("Unicode string handling:")
for text in unicode_examples:
    print(f"  '{text}': length={len(text)}, bytes={len(text.encode('utf-8'))}")
print()

# Character encoding and decoding
print("Character encoding/decoding:")
original = "Café with Ñoël 🐍"
encoded_utf8 = original.encode('utf-8')
encoded_ascii = original.encode('ascii', errors='ignore')
print(f"  Original: '{original}'")
print(f"  UTF-8 bytes: {encoded_utf8}")
print(f"  ASCII (errors ignored): {encoded_ascii}")
print(f"  Decoded UTF-8: '{encoded_utf8.decode('utf-8')}'")
print()

# PRACTICAL STRING PROCESSING FUNCTIONS
print("=== PRACTICAL STRING PROCESSING FUNCTIONS ===")
print()

def clean_text(text):
    """Clean text by removing extra whitespace and normalizing case."""
    # Remove leading/trailing whitespace
    cleaned = text.strip()
    
    # Replace multiple spaces with single spaces
    import re
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    # Normalize case (title case)
    cleaned = cleaned.title()
    
    return cleaned

def validate_password(password):
    """Validate password strength."""
    issues = []
    
    if len(password) < 8:
        issues.append("Must be at least 8 characters long")
    
    if not any(c.isupper() for c in password):
        issues.append("Must contain at least one uppercase letter")
    
    if not any(c.islower() for c in password):
        issues.append("Must contain at least one lowercase letter")
    
    if not any(c.isdigit() for c in password):
        issues.append("Must contain at least one digit")
    
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        issues.append("Must contain at least one special character")
    
    return len(issues) == 0, issues

def format_phone_number(phone):
    """Format a phone number to standard (XXX) XXX-XXXX format."""
    # Remove all non-digit characters
    digits = ''.join(c for c in phone if c.isdigit())
    
    # Check if we have exactly 10 digits
    if len(digits) != 10:
        return None
    
    # Format as (XXX) XXX-XXXX
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

def extract_words(text):
    """Extract words from text, handling punctuation and case."""
    # Convert to lowercase and split on non-word characters
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return words

def count_word_frequency(text):
    """Count frequency of words in text."""
    words = extract_words(text)
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    # Sort by frequency (descending)
    return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# Demonstrate practical functions
print("Text cleaning:")
messy_text = "   hello    WORLD   this   is   a   TEST   "
clean_result = clean_text(messy_text)
print(f"  Original: '{messy_text}'")
print(f"  Cleaned: '{clean_result}'")
print()

print("Password validation:")
password_tests = ["weak", "StrongPass123!", "NoDigits!", "no_upper123!", "SHORT1!"]
for pwd in password_tests:
    is_valid, issues = validate_password(pwd)
    print(f"  '{pwd}': Valid={is_valid}")
    if issues:
        for issue in issues:
            print(f"    - {issue}")
print()

print("Phone number formatting:")
phone_tests = ["5551234567", "(555) 123-4567", "555-123-4567", "1-555-123-4567", "555.123.4567"]
for phone in phone_tests:
    formatted = format_phone_number(phone)
    print(f"  '{phone}' -> '{formatted}'")
print()

print("Word frequency analysis:")
sample_text = """
Python is a great programming language. Python is easy to learn and Python
is powerful. Many developers love Python because Python is versatile and
Python has great libraries.
"""
frequencies = count_word_frequency(sample_text)
print("  Top 10 most frequent words:")
for word, count in frequencies[:10]:
    print(f"    '{word}': {count}")
print()

print("=== SUMMARY ===")
print()
print("String Processing Summary:")
print("1. Strings are immutable sequences of characters")
print("2. Rich set of built-in methods for text manipulation")
print("3. Multiple approaches to string formatting (%, format(), f-strings)")
print("4. Regular expressions provide powerful pattern matching")
print("5. Unicode support enables international text processing")
print("6. Proper validation and cleaning are essential for robust applications")
print("7. String methods return new strings (due to immutability)")

"""
KEY TAKEAWAYS:
==============
1. Strings are immutable - operations return new strings
2. Rich set of methods for searching, formatting, and validation
3. F-strings are the modern, preferred formatting method
4. Regular expressions provide powerful pattern matching
5. Always consider Unicode when processing text
6. Input validation and cleaning are critical for security
7. String slicing works exactly like array slicing

ESSENTIAL STRING METHODS:
=========================
• Case: lower(), upper(), title(), capitalize()
• Search: find(), index(), count(), in operator
• Validation: isdigit(), isalpha(), isalnum(), etc.
• Modification: strip(), replace(), split(), join()
• Boolean: startswith(), endswith()

STRING FORMATTING OPTIONS:
===========================
• Old style: "Hello, %s" % name
• format(): "Hello, {}".format(name)
• f-strings: f"Hello, {name}" (recommended)

COMMON PATTERNS:
================
• Email validation: regex patterns
• Phone formatting: digit extraction + formatting
• Text cleaning: strip() + regex for whitespace
• Word extraction: regex word boundaries
• CSV parsing: split() with quote handling

TEXT PROCESSING WORKFLOW:
=========================
1. Input validation and cleaning
2. Parsing and extraction
3. Processing and transformation
4. Output formatting
5. Error handling for edge cases

UNICODE CONSIDERATIONS:
=======================
• Use UTF-8 encoding for international text
• Be aware of byte vs character length differences
• Handle encoding errors gracefully
• Consider normalization for comparison operations

NEXT STEP:
Go to 03-searching-sorting.py to learn about search algorithms and sorting techniques!
"""