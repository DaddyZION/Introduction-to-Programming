"""
Assignment 6 - Example 3: Searching and Sorting
===============================================

This program demonstrates fundamental searching and sorting algorithms
that are essential for working with arrays and strings. These algorithms
form the foundation of many data processing tasks and help understand
computational complexity and algorithm efficiency.

Key Concepts Demonstrated:
- Linear search and binary search algorithms
- Bubble sort, selection sort, and insertion sort
- Built-in sorting functions and custom sort keys
- Searching in strings and text processing
- Algorithm complexity and performance analysis
- Practical applications of search and sort operations
"""

import time
import random

print("=== SEARCHING AND SORTING ALGORITHMS ===")
print()

print("Search and sort algorithms are fundamental building blocks:")
print("• Enable efficient data retrieval and organization")
print("• Form the basis for more complex algorithms")
print("• Understanding complexity helps choose appropriate methods")
print("• Essential for database operations and data analysis")
print("• Critical for optimizing program performance")
print()

# LINEAR SEARCH ALGORITHM
print("=== LINEAR SEARCH ALGORITHM ===")
print()

def linear_search(arr, target):
    """
    Linear search: Check each element sequentially until target is found.
    Time Complexity: O(n) - worst case checks every element
    Space Complexity: O(1) - uses constant extra space
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index where target was found
    return -1  # Target not found

def linear_search_all(arr, target):
    """Find all occurrences of target in array."""
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

def linear_search_with_comparison_count(arr, target):
    """Linear search that counts comparisons made."""
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Demonstrate linear search
print("Linear Search Demonstration:")
sample_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50]
print(f"Sample array: {sample_array}")
print()

search_targets = [22, 90, 99, 64]
for target in search_targets:
    index = linear_search(sample_array, target)
    if index != -1:
        print(f"  Found {target} at index {index}")
    else:
        print(f"  {target} not found in array")

# Search with comparison counting
print()
print("Linear search with comparison counting:")
for target in [22, 99]:  # One found, one not found
    index, comparisons = linear_search_with_comparison_count(sample_array, target)
    if index != -1:
        print(f"  Found {target} at index {index} after {comparisons} comparisons")
    else:
        print(f"  {target} not found after {comparisons} comparisons")
print()

# Find all occurrences
duplicate_array = [1, 3, 5, 3, 7, 3, 9, 3, 11]
print(f"Array with duplicates: {duplicate_array}")
all_occurrences = linear_search_all(duplicate_array, 3)
print(f"All occurrences of 3: {all_occurrences}")
print()

# BINARY SEARCH ALGORITHM
print("=== BINARY SEARCH ALGORITHM ===")
print()

def binary_search(arr, target):
    """
    Binary search: Efficiently search in sorted array by halving search space.
    Prerequisite: Array must be sorted
    Time Complexity: O(log n) - much faster than linear search
    Space Complexity: O(1) - iterative version uses constant space
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Target not found

def binary_search_with_steps(arr, target):
    """Binary search that shows each step of the process."""
    left = 0
    right = len(arr) - 1
    step = 0
    
    print(f"  Searching for {target} in sorted array {arr}")
    
    while left <= right:
        step += 1
        mid = (left + right) // 2
        
        print(f"    Step {step}: left={left}, right={right}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            print(f"    Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"    {arr[mid]} < {target}, search right half")
            left = mid + 1
        else:
            print(f"    {arr[mid]} > {target}, search left half")
            right = mid - 1
    
    print(f"    {target} not found after {step} steps")
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive implementation of binary search."""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1  # Base case: target not found
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Demonstrate binary search
print("Binary Search Demonstration:")
sorted_array = [11, 12, 22, 25, 34, 50, 64, 76, 88, 90]
print(f"Sorted array: {sorted_array}")
print()

# Show detailed search steps
binary_search_with_steps(sorted_array, 34)
print()
binary_search_with_steps(sorted_array, 99)
print()

# Compare linear vs binary search performance
print("Performance comparison (Linear vs Binary Search):")
large_sorted_array = list(range(0, 10000, 2))  # Even numbers 0 to 9998
search_target = 5000

# Time linear search
start_time = time.time()
linear_result = linear_search(large_sorted_array, search_target)
linear_time = time.time() - start_time

# Time binary search
start_time = time.time()
binary_result = binary_search(large_sorted_array, search_target)
binary_time = time.time() - start_time

print(f"  Array size: {len(large_sorted_array)}")
print(f"  Target: {search_target}")
print(f"  Linear search: found at index {linear_result}, time: {linear_time:.6f} seconds")
print(f"  Binary search: found at index {binary_result}, time: {binary_time:.6f} seconds")
print(f"  Binary search is {linear_time/binary_time:.1f}x faster")
print()

# SORTING ALGORITHMS - BUBBLE SORT
print("=== SORTING ALGORITHMS - BUBBLE SORT ===")
print()

def bubble_sort(arr):
    """
    Bubble sort: Repeatedly compare adjacent elements and swap if wrong order.
    Time Complexity: O(n²) - inefficient for large datasets
    Space Complexity: O(1) - sorts in place
    Stable: Yes - maintains relative order of equal elements
    """
    n = len(arr)
    arr_copy = arr.copy()  # Don't modify original
    
    for i in range(n):
        # Flag to optimize: if no swaps made, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                # Swap elements
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr_copy

def bubble_sort_with_visualization(arr):
    """Bubble sort with step-by-step visualization."""
    n = len(arr)
    arr_copy = arr.copy()
    
    print(f"  Sorting {arr_copy} using Bubble Sort:")
    
    for i in range(n):
        swapped = False
        print(f"    Pass {i + 1}:")
        
        for j in range(0, n - i - 1):
            print(f"      Compare {arr_copy[j]} and {arr_copy[j + 1]}", end="")
            
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                print(" -> Swap!")
            else:
                print(" -> No swap")
        
        print(f"      After pass {i + 1}: {arr_copy}")
        
        if not swapped:
            print(f"      No swaps made, array is sorted!")
            break
    
    return arr_copy

# Demonstrate bubble sort
print("Bubble Sort Demonstration:")
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_result = bubble_sort_with_visualization(unsorted)
print()

# SORTING ALGORITHMS - SELECTION SORT
print("=== SORTING ALGORITHMS - SELECTION SORT ===")
print()

def selection_sort(arr):
    """
    Selection sort: Find minimum element and place it at beginning, repeat.
    Time Complexity: O(n²) - always makes the same number of comparisons
    Space Complexity: O(1) - sorts in place
    Stable: No - may change relative order of equal elements
    """
    n = len(arr)
    arr_copy = arr.copy()
    
    for i in range(n):
        # Find minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        
        # Swap found minimum with first element
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    
    return arr_copy

def selection_sort_with_visualization(arr):
    """Selection sort with step-by-step visualization."""
    n = len(arr)
    arr_copy = arr.copy()
    
    print(f"  Sorting {arr_copy} using Selection Sort:")
    
    for i in range(n):
        min_idx = i
        print(f"    Step {i + 1}: Finding minimum in {arr_copy[i:]}")
        
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        
        print(f"      Minimum is {arr_copy[min_idx]} at index {min_idx}")
        
        if min_idx != i:
            print(f"      Swap {arr_copy[i]} and {arr_copy[min_idx]}")
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
        else:
            print(f"      {arr_copy[i]} already in correct position")
        
        print(f"      After step {i + 1}: {arr_copy}")
    
    return arr_copy

# Demonstrate selection sort
print("Selection Sort Demonstration:")
unsorted = [29, 10, 14, 37, 13]
sorted_result = selection_sort_with_visualization(unsorted)
print()

# SORTING ALGORITHMS - INSERTION SORT
print("=== SORTING ALGORITHMS - INSERTION SORT ===")
print()

def insertion_sort(arr):
    """
    Insertion sort: Build sorted array one element at a time by inserting
    each element into its correct position.
    Time Complexity: O(n²) worst case, O(n) best case (already sorted)
    Space Complexity: O(1) - sorts in place
    Stable: Yes - maintains relative order of equal elements
    Adaptive: Yes - performs better on partially sorted data
    """
    arr_copy = arr.copy()
    
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        
        # Place key in its correct position
        arr_copy[j + 1] = key
    
    return arr_copy

def insertion_sort_with_visualization(arr):
    """Insertion sort with step-by-step visualization."""
    arr_copy = arr.copy()
    
    print(f"  Sorting {arr_copy} using Insertion Sort:")
    print(f"    Start: {arr_copy}")
    
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        
        print(f"    Step {i}: Insert {key} into sorted portion {arr_copy[:i]}")
        
        # Move elements and show each shift
        while j >= 0 and arr_copy[j] > key:
            print(f"      {arr_copy[j]} > {key}, shift right")
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        
        arr_copy[j + 1] = key
        print(f"      Insert {key} at position {j + 1}")
        print(f"      After step {i}: {arr_copy}")
    
    return arr_copy

# Demonstrate insertion sort
print("Insertion Sort Demonstration:")
unsorted = [12, 11, 13, 5, 6]
sorted_result = insertion_sort_with_visualization(unsorted)
print()

# ALGORITHM PERFORMANCE COMPARISON
print("=== ALGORITHM PERFORMANCE COMPARISON ===")
print()

def measure_sort_performance(sort_func, arr, name):
    """Measure execution time of sorting algorithm."""
    start_time = time.time()
    result = sort_func(arr)
    end_time = time.time()
    return end_time - start_time, result

def compare_sorting_algorithms(arr):
    """Compare performance of different sorting algorithms."""
    algorithms = [
        (bubble_sort, "Bubble Sort"),
        (selection_sort, "Selection Sort"),
        (insertion_sort, "Insertion Sort"),
        (lambda x: sorted(x), "Built-in Sort")
    ]
    
    print(f"Performance comparison for array of size {len(arr)}:")
    print(f"Array: {arr if len(arr) <= 20 else str(arr[:10]) + '...' + str(arr[-10:])}")
    print()
    
    results = []
    for sort_func, name in algorithms:
        time_taken, sorted_arr = measure_sort_performance(sort_func, arr, name)
        results.append((name, time_taken))
        
        # Verify sorting is correct
        is_sorted = all(sorted_arr[i] <= sorted_arr[i+1] for i in range(len(sorted_arr)-1))
        print(f"  {name:15}: {time_taken:.6f} seconds (Correct: {is_sorted})")
    
    print()
    return results

# Compare with small array
print("Small array comparison:")
small_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 35, 42]
compare_sorting_algorithms(small_array)

# Compare with larger array
print("Larger array comparison:")
large_array = [random.randint(1, 1000) for _ in range(100)]
compare_sorting_algorithms(large_array)

# SEARCHING IN STRINGS
print("=== SEARCHING IN STRINGS ===")
print()

def find_all_occurrences(text, pattern):
    """Find all occurrences of pattern in text."""
    occurrences = []
    start = 0
    
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break
        occurrences.append(pos)
        start = pos + 1
    
    return occurrences

def find_words(text, word):
    """Find whole word occurrences in text (case-insensitive)."""
    import re
    pattern = r'\b' + re.escape(word.lower()) + r'\b'
    matches = []
    
    for match in re.finditer(pattern, text.lower()):
        matches.append(match.start())
    
    return matches

def search_multiple_patterns(text, patterns):
    """Search for multiple patterns in text simultaneously."""
    results = {}
    
    for pattern in patterns:
        results[pattern] = find_all_occurrences(text.lower(), pattern.lower())
    
    return results

# Demonstrate string searching
print("String Search Demonstration:")
sample_text = """
Python is a powerful programming language. Python is easy to learn,
and Python is great for beginners. Many developers choose Python
because Python has excellent libraries and Python is versatile.
"""

print(f"Sample text: {repr(sample_text[:100])}...")
print()

# Find all occurrences of "Python"
python_occurrences = find_all_occurrences(sample_text, "Python")
print(f"All occurrences of 'Python': {python_occurrences}")

# Find word occurrences (whole words only)
python_words = find_words(sample_text, "python")
print(f"Whole word 'python' occurrences: {python_words}")

# Search for multiple patterns
patterns = ["Python", "is", "and", "programming"]
multiple_results = search_multiple_patterns(sample_text, patterns)
print(f"Multiple pattern search:")
for pattern, positions in multiple_results.items():
    print(f"  '{pattern}': {len(positions)} occurrences at positions {positions}")
print()

# STRING SORTING AND ORGANIZATION
print("=== STRING SORTING AND ORGANIZATION ===")
print()

def sort_words_by_length(words):
    """Sort words by length, then alphabetically."""
    return sorted(words, key=lambda word: (len(word), word.lower()))

def sort_case_insensitive(words):
    """Sort words case-insensitively."""
    return sorted(words, key=str.lower)

def sort_by_custom_criteria(words, criteria):
    """Sort words by custom criteria."""
    if criteria == "length":
        return sorted(words, key=len)
    elif criteria == "alphabetical":
        return sorted(words)
    elif criteria == "reverse_alphabetical":
        return sorted(words, reverse=True)
    elif criteria == "vowel_count":
        return sorted(words, key=lambda w: sum(1 for c in w.lower() if c in 'aeiou'))
    else:
        return words

# Demonstrate string sorting
print("String Sorting Demonstration:")
word_list = ["Python", "java", "JavaScript", "C++", "Go", "Rust", "programming", "code"]
print(f"Original words: {word_list}")
print()

# Different sorting methods
print("Sort by length then alphabetically:")
length_sorted = sort_words_by_length(word_list)
print(f"  {length_sorted}")
print()

print("Sort case-insensitive:")
case_insensitive = sort_case_insensitive(word_list)
print(f"  {case_insensitive}")
print()

print("Sort by vowel count:")
vowel_sorted = sort_by_custom_criteria(word_list, "vowel_count")
print(f"  {vowel_sorted}")
print()

# PRACTICAL APPLICATIONS
print("=== PRACTICAL APPLICATIONS ===")
print()

def find_anagrams(words):
    """Find groups of anagrams in a list of words."""
    anagram_groups = {}
    
    for word in words:
        # Sort letters to create a key
        sorted_letters = ''.join(sorted(word.lower()))
        
        if sorted_letters not in anagram_groups:
            anagram_groups[sorted_letters] = []
        anagram_groups[sorted_letters].append(word)
    
    # Return only groups with more than one word
    return {key: group for key, group in anagram_groups.items() if len(group) > 1}

def binary_search_strings(strings, target):
    """Binary search in sorted list of strings."""
    left, right = 0, len(strings) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if strings[mid] == target:
            return mid
        elif strings[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def find_closest_matches(word, word_list, max_distance=2):
    """Find words with similar spelling (simple edit distance)."""
    def simple_edit_distance(s1, s2):
        """Calculate simple edit distance between two strings."""
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        
        distances = list(range(len(s1) + 1))
        
        for i2, c2 in enumerate(s2):
            new_distances = [i2 + 1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    new_distances.append(distances[i1])
                else:
                    new_distances.append(1 + min(distances[i1], distances[i1 + 1], new_distances[-1]))
            distances = new_distances
        
        return distances[-1]
    
    matches = []
    for candidate in word_list:
        distance = simple_edit_distance(word.lower(), candidate.lower())
        if distance <= max_distance and candidate.lower() != word.lower():
            matches.append((candidate, distance))
    
    return sorted(matches, key=lambda x: x[1])

# Demonstrate practical applications
print("Practical Applications:")
print()

# Find anagrams
print("Anagram detection:")
word_list = ["listen", "silent", "enlist", "hello", "world", "act", "cat", "tac", "dog"]
anagrams = find_anagrams(word_list)
for sorted_key, group in anagrams.items():
    print(f"  Anagrams: {group}")
print()

# Binary search in strings
print("Binary search in sorted strings:")
sorted_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
search_name = "David"
index = binary_search_strings(sorted_names, search_name)
print(f"  Searching for '{search_name}' in {sorted_names}")
print(f"  Found at index: {index}")
print()

# Find similar words (spell checking concept)
print("Find similar words (spell checking):")
dictionary = ["python", "program", "programming", "algorithm", "function", "variable", "method"]
misspelled = "programing"  # Missing 'm'
similar = find_closest_matches(misspelled, dictionary, max_distance=2)
print(f"  Word: '{misspelled}'")
print(f"  Similar words: {similar}")
print()

print("=== SUMMARY ===")
print()
print("Searching and Sorting Summary:")
print("1. Linear search: O(n) - simple but slower for large datasets")
print("2. Binary search: O(log n) - much faster but requires sorted data")
print("3. Bubble sort: O(n²) - simple but inefficient")
print("4. Selection sort: O(n²) - makes fewer swaps than bubble sort")
print("5. Insertion sort: O(n²) - efficient for small or nearly sorted data")
print("6. Built-in sort: O(n log n) - highly optimized, use when possible")
print("7. String searching requires careful consideration of case and word boundaries")
print("8. Algorithm choice depends on data size, sorting requirements, and performance needs")

"""
KEY TAKEAWAYS:
==============
1. Choose algorithms based on data size and performance requirements
2. Binary search is much faster but requires sorted data
3. Built-in sorting functions are highly optimized - use them when possible
4. String searching has special considerations (case, word boundaries)
5. Understanding Big O notation helps choose appropriate algorithms
6. Simple algorithms are fine for small datasets
7. Consider stability and adaptiveness for specialized needs

SEARCH ALGORITHM COMPARISON:
============================
• Linear Search: O(n) time, works on any array
• Binary Search: O(log n) time, requires sorted array
• String Search: Consider case sensitivity and word boundaries

SORT ALGORITHM COMPARISON:
==========================
• Bubble Sort: O(n²), stable, adaptive
• Selection Sort: O(n²), not stable, makes fewest swaps
• Insertion Sort: O(n²), stable, adaptive, good for small arrays
• Built-in Sort: O(n log n), highly optimized

WHEN TO USE WHAT:
=================
• Small arrays (< 50): Any simple algorithm works
• Large arrays: Use built-in sort() or sorted()
• Need stability: Insertion sort or built-in sort
• Memory constrained: In-place algorithms (bubble, selection, insertion)
• Partially sorted: Insertion sort (adaptive)
• String data: Consider case-insensitive sorting

PRACTICAL APPLICATIONS:
=======================
• Database queries: Indexing uses binary search principles
• Autocomplete: Prefix searching in sorted lists
• Spell checking: Edit distance and fuzzy matching
• Data analysis: Sorting enables efficient grouping and searching
• File systems: Directory listings and file searching

PERFORMANCE TIPS:
=================
• Use built-in functions when possible (they're optimized)
• Sort once, search many times
• Consider data preprocessing for frequent operations
• Profile your code to identify actual bottlenecks
• Choose algorithms based on real-world data characteristics

NEXT STEP:
Go to 04-data-manipulation.py to learn about advanced data processing techniques!
"""