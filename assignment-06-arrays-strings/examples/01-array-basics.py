"""
Assignment 6 - Example 1: Array/List Basics
============================================

This program introduces fundamental concepts of arrays and lists in Python.
Arrays (called lists in Python) are ordered collections that can store
multiple values of any type. Understanding array operations is essential
for data manipulation and algorithm implementation.

Key Concepts Demonstrated:
- Array/list creation and initialization
- Element access using indices
- Adding and removing elements
- Common list methods and operations
- Index-based manipulation
- Array iteration patterns
"""

print("=== ARRAY/LIST BASICS ===")
print()

print("Arrays (lists in Python) are ordered collections of elements:")
print("• Store multiple values in a single variable")
print("• Elements are ordered and indexed (starting from 0)")
print("• Can contain different data types")
print("• Mutable - can be modified after creation")
print("• Dynamic - can grow and shrink during runtime")
print()

# ARRAY CREATION AND INITIALIZATION
print("=== ARRAY CREATION AND INITIALIZATION ===")
print()

# Creating empty arrays
empty_list = []
empty_list_explicit = list()

print("Creating empty arrays:")
print(f"  empty_list = []: {empty_list}")
print(f"  empty_list_explicit = list(): {empty_list_explicit}")
print()

# Creating arrays with initial values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "date"]
mixed_data = [1, "hello", 3.14, True, None]
nested_list = [[1, 2], [3, 4], [5, 6]]

print("Creating arrays with initial values:")
print(f"  numbers = {numbers}")
print(f"  fruits = {fruits}")
print(f"  mixed_data = {mixed_data}")
print(f"  nested_list = {nested_list}")
print()

# Creating arrays using range and list comprehension
range_list = list(range(10))  # 0 to 9
range_custom = list(range(5, 16, 2))  # 5 to 15, step 2
squares = [x**2 for x in range(1, 6)]  # List comprehension
repeated_values = [0] * 5  # Repeat value 5 times

print("Creating arrays using different techniques:")
print(f"  range_list = list(range(10)): {range_list}")
print(f"  range_custom = list(range(5, 16, 2)): {range_custom}")
print(f"  squares = [x**2 for x in range(1, 6)]: {squares}")
print(f"  repeated_values = [0] * 5: {repeated_values}")
print()

# ELEMENT ACCESS AND MODIFICATION
print("=== ELEMENT ACCESS AND MODIFICATION ===")
print()

# Accessing elements by index
sample_list = ["zero", "one", "two", "three", "four"]
print(f"Sample list: {sample_list}")
print("Accessing elements by index:")
print(f"  sample_list[0] = {sample_list[0]}")  # First element
print(f"  sample_list[2] = {sample_list[2]}")  # Third element
print(f"  sample_list[-1] = {sample_list[-1]}")  # Last element
print(f"  sample_list[-2] = {sample_list[-2]}")  # Second to last
print()

# Modifying elements
print("Modifying elements:")
sample_list[1] = "ONE"
sample_list[-1] = "FOUR"
print(f"After modifications: {sample_list}")
print()

# Error handling for invalid indices
print("Handling invalid indices:")
try:
    invalid_access = sample_list[10]  # Index out of range
except IndexError as e:
    print(f"  IndexError caught: {e}")

try:
    invalid_negative = sample_list[-10]  # Negative index out of range
except IndexError as e:
    print(f"  Negative IndexError caught: {e}")
print()

# ARRAY LENGTH AND PROPERTIES
print("=== ARRAY LENGTH AND PROPERTIES ===")
print()

def analyze_array(arr, name):
    """Analyze and display array properties."""
    print(f"Analysis of {name}:")
    print(f"  Array: {arr}")
    print(f"  Length: {len(arr)}")
    print(f"  Type: {type(arr)}")
    print(f"  Is empty: {len(arr) == 0}")
    if arr:  # Non-empty array
        print(f"  First element: {arr[0]} (type: {type(arr[0])})")
        print(f"  Last element: {arr[-1]} (type: {type(arr[-1])})")
    print()

# Analyze different arrays
analyze_array([], "empty_array")
analyze_array(numbers, "numbers")
analyze_array(fruits, "fruits")
analyze_array(mixed_data, "mixed_data")

# ADDING ELEMENTS TO ARRAYS
print("=== ADDING ELEMENTS TO ARRAYS ===")
print()

# Using append() to add single elements
demo_list = [1, 2, 3]
print(f"Original list: {demo_list}")

demo_list.append(4)
print(f"After append(4): {demo_list}")

demo_list.append("hello")
print(f"After append('hello'): {demo_list}")
print()

# Using insert() to add elements at specific positions
demo_list.insert(0, "first")  # Insert at beginning
print(f"After insert(0, 'first'): {demo_list}")

demo_list.insert(3, "middle")  # Insert in middle
print(f"After insert(3, 'middle'): {demo_list}")

demo_list.insert(-1, "near_end")  # Insert before last element
print(f"After insert(-1, 'near_end'): {demo_list}")
print()

# Using extend() to add multiple elements
demo_list.extend([10, 20, 30])
print(f"After extend([10, 20, 30]): {demo_list}")

demo_list.extend("abc")  # Extends with individual characters
print(f"After extend('abc'): {demo_list}")
print()

# Using + operator for concatenation (creates new list)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"list1 + list2 = {list1} + {list2} = {combined}")
print(f"Original lists unchanged: list1={list1}, list2={list2}")
print()

# REMOVING ELEMENTS FROM ARRAYS
print("=== REMOVING ELEMENTS FROM ARRAYS ===")
print()

# Create sample list for removal demonstrations
removal_demo = ["apple", "banana", "cherry", "date", "elderberry", "banana"]
print(f"Original list: {removal_demo}")

# Using remove() to remove first occurrence of a value
removal_demo.remove("banana")  # Removes first "banana"
print(f"After remove('banana'): {removal_demo}")

# Using pop() to remove and return element at index
popped_element = removal_demo.pop()  # Remove last element
print(f"After pop(): {removal_demo}")
print(f"Popped element: {popped_element}")

popped_at_index = removal_demo.pop(1)  # Remove element at index 1
print(f"After pop(1): {removal_demo}")
print(f"Popped element at index 1: {popped_at_index}")
print()

# Using del statement to remove elements
del_demo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original list for del demo: {del_demo}")

del del_demo[0]  # Remove first element
print(f"After del del_demo[0]: {del_demo}")

del del_demo[-1]  # Remove last element
print(f"After del del_demo[-1]: {del_demo}")

del del_demo[2:5]  # Remove slice (elements at indices 2, 3, 4)
print(f"After del del_demo[2:5]: {del_demo}")
print()

# Using clear() to remove all elements
clear_demo = [1, 2, 3, 4, 5]
print(f"Before clear(): {clear_demo}")
clear_demo.clear()
print(f"After clear(): {clear_demo}")
print()

# Error handling for removal operations
print("Handling removal errors:")
error_demo = ["a", "b", "c"]

try:
    error_demo.remove("z")  # Value not in list
except ValueError as e:
    print(f"  ValueError in remove(): {e}")

try:
    error_demo.pop(10)  # Index out of range
except IndexError as e:
    print(f"  IndexError in pop(): {e}")
print()

# ARRAY SLICING
print("=== ARRAY SLICING ===")
print()

# Create sample array for slicing
slice_demo = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(f"Sample array: {slice_demo}")
print("Array indices: 0   1   2   3   4   5   6   7   8   9")
print("              -10 -9  -8  -7  -6  -5  -4  -3  -2  -1")
print()

# Basic slicing syntax: array[start:end:step]
print("Basic slicing examples:")
print(f"  slice_demo[2:6] = {slice_demo[2:6]}")      # Elements 2-5
print(f"  slice_demo[:4] = {slice_demo[:4]}")        # First 4 elements
print(f"  slice_demo[3:] = {slice_demo[3:]}")        # From index 3 to end
print(f"  slice_demo[:] = {slice_demo[:]}")          # Complete copy
print()

print("Slicing with step:")
print(f"  slice_demo[::2] = {slice_demo[::2]}")      # Every 2nd element
print(f"  slice_demo[1::2] = {slice_demo[1::2]}")    # Every 2nd, starting at 1
print(f"  slice_demo[::3] = {slice_demo[::3]}")      # Every 3rd element
print()

print("Negative indexing in slicing:")
print(f"  slice_demo[-3:] = {slice_demo[-3:]}")      # Last 3 elements
print(f"  slice_demo[:-2] = {slice_demo[:-2]}")      # All except last 2
print(f"  slice_demo[-5:-1] = {slice_demo[-5:-1]}")  # From -5 to -1
print()

print("Reverse slicing:")
print(f"  slice_demo[::-1] = {slice_demo[::-1]}")    # Reverse entire array
print(f"  slice_demo[5:1:-1] = {slice_demo[5:1:-1]}")# Reverse slice
print()

# Modifying slices
print("Modifying array slices:")
slice_modify = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {slice_modify}")

slice_modify[2:5] = [30, 40, 50]  # Replace slice with new values
print(f"After slice_modify[2:5] = [30, 40, 50]: {slice_modify}")

slice_modify[1:4] = [100]  # Replace multiple elements with single element
print(f"After slice_modify[1:4] = [100]: {slice_modify}")

slice_modify[2:2] = [200, 300]  # Insert elements at position 2
print(f"After slice_modify[2:2] = [200, 300]: {slice_modify}")
print()

# ARRAY METHODS AND OPERATIONS
print("=== ARRAY METHODS AND OPERATIONS ===")
print()

# Create sample data for method demonstrations
method_demo = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(f"Sample array: {method_demo}")

# Finding elements and their positions
print("Finding elements:")
print(f"  Count of 1: {method_demo.count(1)}")
print(f"  Count of 5: {method_demo.count(5)}")
print(f"  Count of 99: {method_demo.count(99)}")  # Not found
print()

print(f"  Index of first 5: {method_demo.index(5)}")
try:
    print(f"  Index of 99: {method_demo.index(99)}")  # Will raise ValueError
except ValueError as e:
    print(f"  ValueError finding 99: {e}")
print()

# Sorting arrays
unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"Unsorted array: {unsorted}")

sorted_copy = sorted(unsorted)  # Returns new sorted list
print(f"sorted(unsorted): {sorted_copy}")
print(f"Original unchanged: {unsorted}")

unsorted.sort()  # Sorts in place
print(f"After unsorted.sort(): {unsorted}")

# Reverse sorting
reverse_demo = [5, 2, 8, 1, 9]
print(f"Before reverse sort: {reverse_demo}")
reverse_demo.sort(reverse=True)
print(f"After sort(reverse=True): {reverse_demo}")
print()

# Reversing arrays
reverse_demo.reverse()  # Reverse in place
print(f"After reverse(): {reverse_demo}")

# Using reversed() function (returns iterator)
reverse_iter = list(reversed([1, 2, 3, 4, 5]))
print(f"list(reversed([1, 2, 3, 4, 5])): {reverse_iter}")
print()

# ARRAY ITERATION PATTERNS
print("=== ARRAY ITERATION PATTERNS ===")
print()

sample_data = ["red", "green", "blue", "yellow", "purple"]

# Basic iteration
print("Basic iteration:")
for item in sample_data:
    print(f"  Item: {item}")
print()

# Iteration with index using enumerate()
print("Iteration with index using enumerate():")
for index, item in enumerate(sample_data):
    print(f"  Index {index}: {item}")
print()

# Iteration with custom start index
print("Iteration with custom start index:")
for index, item in enumerate(sample_data, start=1):
    print(f"  Position {index}: {item}")
print()

# Iteration using range and len()
print("Iteration using range and len():")
for i in range(len(sample_data)):
    print(f"  sample_data[{i}] = {sample_data[i]}")
print()

# Reverse iteration
print("Reverse iteration:")
for item in reversed(sample_data):
    print(f"  Reverse item: {item}")
print()

# PRACTICAL EXAMPLES
print("=== PRACTICAL EXAMPLES ===")
print()

def calculate_statistics(numbers):
    """Calculate basic statistics for a list of numbers."""
    if not numbers:
        return {"error": "Empty list provided"}
    
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    
    # Find min and max
    minimum = min(numbers)
    maximum = max(numbers)
    
    # Calculate median
    sorted_numbers = sorted(numbers)
    if count % 2 == 0:
        median = (sorted_numbers[count//2 - 1] + sorted_numbers[count//2]) / 2
    else:
        median = sorted_numbers[count//2]
    
    return {
        "count": count,
        "sum": total,
        "mean": round(mean, 2),
        "median": median,
        "min": minimum,
        "max": maximum,
        "range": maximum - minimum
    }

def find_duplicates(items):
    """Find duplicate items in an array."""
    seen = []
    duplicates = []
    
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        elif item not in seen:
            seen.append(item)
    
    return duplicates

def remove_duplicates(items):
    """Remove duplicates from array while preserving order."""
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

def rotate_array(arr, positions):
    """Rotate array elements by given number of positions."""
    if not arr:
        return arr
    
    # Handle positions greater than array length
    positions = positions % len(arr)
    
    # Rotate by slicing
    return arr[positions:] + arr[:positions]

# Demonstrate practical functions
print("Statistics calculation:")
test_numbers = [85, 92, 78, 96, 88, 91, 87, 82, 95, 89]
stats = calculate_statistics(test_numbers)
print(f"  Numbers: {test_numbers}")
for key, value in stats.items():
    print(f"  {key.capitalize()}: {value}")
print()

print("Duplicate detection:")
test_duplicates = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]
duplicates = find_duplicates(test_duplicates)
unique = remove_duplicates(test_duplicates)
print(f"  Original: {test_duplicates}")
print(f"  Duplicates found: {duplicates}")
print(f"  After removing duplicates: {unique}")
print()

print("Array rotation:")
rotation_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"  Original: {rotation_test}")
print(f"  Rotate by 3: {rotate_array(rotation_test, 3)}")
print(f"  Rotate by -2: {rotate_array(rotation_test, -2)}")
print(f"  Rotate by 12: {rotate_array(rotation_test, 12)}")  # More than length
print()

# MEMORY CONSIDERATIONS
print("=== MEMORY AND PERFORMANCE CONSIDERATIONS ===")
print()

print("Understanding list copying:")
original = [1, 2, 3, 4, 5]
reference = original  # Same object reference
shallow_copy = original[:]  # Shallow copy using slicing
deep_copy = original.copy()  # Shallow copy using method

print(f"Original: {original}")
print(f"Reference: {reference}")
print(f"Shallow copy (slice): {shallow_copy}")
print(f"Deep copy (method): {deep_copy}")
print()

# Modify original and see effects
original[0] = 999
print("After modifying original[0] = 999:")
print(f"Original: {original}")
print(f"Reference: {reference}")  # Also changed (same object)
print(f"Shallow copy (slice): {shallow_copy}")  # Unchanged
print(f"Deep copy (method): {deep_copy}")  # Unchanged
print()

print("List comprehensions vs loops (performance):")
# List comprehension (generally faster)
squares_comprehension = [x**2 for x in range(1000)]

# Traditional loop (generally slower for simple operations)
squares_loop = []
for x in range(1000):
    squares_loop.append(x**2)

print(f"Both methods create lists of {len(squares_comprehension)} elements")
print("List comprehensions are generally faster for simple transformations")
print()

print("=== SUMMARY ===")
print()
print("Array/List Basics Summary:")
print("1. Arrays store ordered collections of elements")
print("2. Elements are accessed using zero-based indices")
print("3. Arrays are mutable and can grow/shrink dynamically")
print("4. Many built-in methods available for manipulation")
print("5. Slicing provides powerful ways to extract subarrays")
print("6. Multiple iteration patterns for different needs")
print("7. Consider memory implications when copying arrays")

"""
KEY TAKEAWAYS:
==============
1. Arrays (lists) are fundamental data structures for storing collections
2. Zero-based indexing is used to access elements
3. Negative indices count from the end of the array
4. Slicing syntax [start:end:step] provides flexible subarray extraction
5. Many built-in methods for adding, removing, and manipulating elements
6. List comprehensions offer concise syntax for creating new lists
7. Understanding shallow vs deep copying is important for memory management

ARRAY CREATION PATTERNS:
========================
• Literal: [1, 2, 3, 4, 5]
• Empty: [] or list()
• Range: list(range(10))
• Repetition: [0] * 5
• Comprehension: [x**2 for x in range(5)]

COMMON OPERATIONS:
==================
• Access: array[index]
• Modify: array[index] = value
• Add: append(), insert(), extend()
• Remove: remove(), pop(), del, clear()
• Find: index(), count(), in operator
• Sort: sort(), sorted()
• Reverse: reverse(), reversed()

SLICING SYNTAX:
===============
• array[start:end] - elements from start to end-1
• array[:n] - first n elements
• array[n:] - elements from n to end
• array[::step] - every step-th element
• array[::-1] - reverse array

BEST PRACTICES:
===============
• Use descriptive variable names for arrays
• Check for empty arrays before processing
• Handle IndexError for invalid indices
• Use appropriate methods (append vs extend vs insert)
• Consider list comprehensions for simple transformations
• Be aware of reference vs copy behavior
• Use enumerate() when you need both index and value

NEXT STEP:
Go to 02-string-processing.py to learn about string manipulation and text processing!
"""