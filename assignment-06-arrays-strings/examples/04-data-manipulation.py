"""
Assignment 6 - Example 4: Data Manipulation
==========================================

This program demonstrates advanced data manipulation techniques using
arrays and strings. These techniques are essential for processing real-world
data, transforming information, and solving complex programming problems.
The focus is on practical operations you'll encounter in data analysis,
file processing, and application development.

Key Concepts Demonstrated:
- Array transformations and filtering
- Data aggregation and statistical operations
- String parsing and data extraction
- Data cleaning and preprocessing
- Multi-dimensional data handling
- Data validation and error handling
- Performance optimization techniques
"""

import re
import json
from datetime import datetime

print("=== DATA MANIPULATION TECHNIQUES ===")
print()

print("Data manipulation is essential for real-world programming:")
print("• Transform raw data into useful information")
print("• Clean and validate data before processing")
print("• Extract insights through aggregation and analysis")
print("• Handle different data formats and structures")
print("• Optimize operations for performance and memory usage")
print()

# ARRAY TRANSFORMATIONS
print("=== ARRAY TRANSFORMATIONS ===")
print()

def transform_array(arr, operation):
    """Apply transformation operation to array elements."""
    operations = {
        'square': lambda x: x ** 2,
        'cube': lambda x: x ** 3,
        'absolute': lambda x: abs(x),
        'double': lambda x: x * 2,
        'sqrt': lambda x: x ** 0.5 if x >= 0 else 0,
        'reciprocal': lambda x: 1/x if x != 0 else 0,
        'normalize': lambda x: (x - min(arr)) / (max(arr) - min(arr)) if max(arr) != min(arr) else 0
    }
    
    if operation not in operations:
        return arr
    
    return [operations[operation](x) for x in arr]

def map_values(arr, mapping_func):
    """Apply custom mapping function to array elements."""
    return [mapping_func(x) for x in arr]

def conditional_transform(arr, condition, transform_func, else_func=None):
    """Transform elements that meet condition, optionally transform others."""
    result = []
    for item in arr:
        if condition(item):
            result.append(transform_func(item))
        elif else_func:
            result.append(else_func(item))
        else:
            result.append(item)
    return result

# Demonstrate array transformations
print("Array Transformation Examples:")
numbers = [1, -2, 3, -4, 5, 6, -7, 8, 9, -10]
print(f"Original array: {numbers}")
print()

# Basic transformations
transformations = ['square', 'absolute', 'double']
for operation in transformations:
    result = transform_array(numbers, operation)
    print(f"  {operation}: {result}")
print()

# Custom mapping
print("Custom mapping examples:")
fahrenheit_temps = [32, 68, 86, 104, 122]
celsius_temps = map_values(fahrenheit_temps, lambda f: round((f - 32) * 5/9, 1))
print(f"  Fahrenheit: {fahrenheit_temps}")
print(f"  Celsius: {celsius_temps}")

# Grade letter conversion
scores = [95, 87, 92, 78, 85, 91, 88, 76]
def score_to_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

grades = map_values(scores, score_to_grade)
print(f"  Scores: {scores}")
print(f"  Grades: {grades}")
print()

# Conditional transformation
print("Conditional transformation:")
mixed_numbers = [-5, 12, -3, 8, -1, 15, -9, 4]
# Make negative numbers positive, keep positive as is
result = conditional_transform(mixed_numbers, lambda x: x < 0, lambda x: -x)
print(f"  Original: {mixed_numbers}")
print(f"  Negatives made positive: {result}")
print()

# DATA FILTERING AND SELECTION
print("=== DATA FILTERING AND SELECTION ===")
print()

def filter_by_condition(arr, condition):
    """Filter array elements based on condition."""
    return [item for item in arr if condition(item)]

def filter_by_multiple_conditions(arr, *conditions):
    """Filter by multiple conditions (all must be true)."""
    return [item for item in arr if all(condition(item) for condition in conditions)]

def partition_data(arr, condition):
    """Partition data into two groups based on condition."""
    true_items = []
    false_items = []
    
    for item in arr:
        if condition(item):
            true_items.append(item)
        else:
            false_items.append(item)
    
    return true_items, false_items

def find_extremes(arr, key_func=None):
    """Find minimum, maximum, and their positions."""
    if not arr:
        return None
    
    if key_func is None:
        key_func = lambda x: x
    
    min_item = min(arr, key=key_func)
    max_item = max(arr, key=key_func)
    min_index = arr.index(min_item)
    max_index = arr.index(max_item)
    
    return {
        'min': {'value': min_item, 'index': min_index},
        'max': {'value': max_item, 'index': max_index}
    }

# Demonstrate filtering
print("Data Filtering Examples:")
student_scores = [95, 67, 89, 92, 78, 85, 91, 72, 88, 94]
print(f"Student scores: {student_scores}")
print()

# Basic filtering
high_scores = filter_by_condition(student_scores, lambda x: x >= 90)
failing_scores = filter_by_condition(student_scores, lambda x: x < 70)
print(f"High scores (≥90): {high_scores}")
print(f"Failing scores (<70): {failing_scores}")
print()

# Multiple condition filtering
product_data = [
    {'name': 'Laptop', 'price': 1200, 'category': 'Electronics', 'rating': 4.5},
    {'name': 'Book', 'price': 15, 'category': 'Education', 'rating': 4.2},
    {'name': 'Phone', 'price': 800, 'category': 'Electronics', 'rating': 4.7},
    {'name': 'Desk', 'price': 300, 'category': 'Furniture', 'rating': 4.1},
    {'name': 'Tablet', 'price': 500, 'category': 'Electronics', 'rating': 4.3}
]

# Filter electronics under $600 with rating > 4.0
filtered_products = filter_by_multiple_conditions(
    product_data,
    lambda p: p['category'] == 'Electronics',
    lambda p: p['price'] < 600,
    lambda p: p['rating'] > 4.0
)

print("Filtered products (Electronics, <$600, rating >4.0):")
for product in filtered_products:
    print(f"  {product['name']}: ${product['price']}, rating {product['rating']}")
print()

# Partition data
print("Data partitioning:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens, odds = partition_data(numbers, lambda x: x % 2 == 0)
print(f"  Numbers: {numbers}")
print(f"  Evens: {evens}")
print(f"  Odds: {odds}")
print()

# DATA AGGREGATION AND STATISTICS
print("=== DATA AGGREGATION AND STATISTICS ===")
print()

def calculate_statistics(arr):
    """Calculate comprehensive statistics for numerical array."""
    if not arr:
        return {}
    
    n = len(arr)
    total = sum(arr)
    mean = total / n
    
    # Variance and standard deviation
    variance = sum((x - mean) ** 2 for x in arr) / n
    std_dev = variance ** 0.5
    
    # Median
    sorted_arr = sorted(arr)
    if n % 2 == 0:
        median = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        median = sorted_arr[n//2]
    
    # Mode (most frequent value)
    frequency = {}
    for value in arr:
        frequency[value] = frequency.get(value, 0) + 1
    mode = max(frequency.keys(), key=lambda k: frequency[k])
    
    # Quartiles
    q1 = sorted_arr[n//4] if n >= 4 else sorted_arr[0]
    q3 = sorted_arr[3*n//4] if n >= 4 else sorted_arr[-1]
    
    return {
        'count': n,
        'sum': total,
        'mean': round(mean, 2),
        'median': median,
        'mode': mode,
        'min': min(arr),
        'max': max(arr),
        'range': max(arr) - min(arr),
        'variance': round(variance, 2),
        'std_dev': round(std_dev, 2),
        'q1': q1,
        'q3': q3
    }

def group_by(arr, key_func):
    """Group array elements by key function result."""
    groups = {}
    for item in arr:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups

def aggregate_by_group(arr, group_key, aggregate_key, operation):
    """Aggregate values by group using specified operation."""
    groups = group_by(arr, group_key)
    result = {}
    
    operations = {
        'sum': sum,
        'avg': lambda x: sum(x) / len(x) if x else 0,
        'min': min,
        'max': max,
        'count': len
    }
    
    if operation not in operations:
        return result
    
    for group_name, items in groups.items():
        values = [aggregate_key(item) for item in items]
        result[group_name] = operations[operation](values)
    
    return result

# Demonstrate aggregation
print("Statistical Analysis Examples:")
test_scores = [85, 92, 78, 96, 88, 91, 87, 82, 95, 89, 93, 86, 90, 84, 97]
stats = calculate_statistics(test_scores)

print(f"Test scores: {test_scores}")
print("Statistical summary:")
for key, value in stats.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")
print()

# Group analysis
sales_data = [
    {'salesperson': 'Alice', 'region': 'North', 'amount': 1200, 'month': 'Jan'},
    {'salesperson': 'Bob', 'region': 'South', 'amount': 1500, 'month': 'Jan'},
    {'salesperson': 'Alice', 'region': 'North', 'amount': 1300, 'month': 'Feb'},
    {'salesperson': 'Charlie', 'region': 'East', 'amount': 1100, 'month': 'Jan'},
    {'salesperson': 'Bob', 'region': 'South', 'amount': 1600, 'month': 'Feb'},
    {'salesperson': 'Charlie', 'region': 'East', 'amount': 1250, 'month': 'Feb'},
]

print("Sales data analysis:")
# Group by region
region_groups = group_by(sales_data, lambda x: x['region'])
for region, sales in region_groups.items():
    total = sum(sale['amount'] for sale in sales)
    print(f"  {region}: {len(sales)} sales, total ${total}")
print()

# Aggregate by salesperson
salesperson_totals = aggregate_by_group(
    sales_data, 
    lambda x: x['salesperson'],
    lambda x: x['amount'],
    'sum'
)
print("Total sales by salesperson:")
for person, total in salesperson_totals.items():
    print(f"  {person}: ${total}")
print()

# STRING DATA MANIPULATION
print("=== STRING DATA MANIPULATION ===")
print()

def parse_structured_text(text, delimiter=','):
    """Parse structured text data (CSV-like)."""
    lines = text.strip().split('\n')
    if not lines:
        return []
    
    # Use first line as headers
    headers = [header.strip() for header in lines[0].split(delimiter)]
    data = []
    
    for line in lines[1:]:
        values = [value.strip() for value in line.split(delimiter)]
        if len(values) == len(headers):
            record = dict(zip(headers, values))
            data.append(record)
    
    return data

def extract_patterns(text, patterns):
    """Extract multiple patterns from text using regex."""
    results = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        results[name] = matches
    return results

def clean_text_data(text):
    """Clean text data by normalizing whitespace and removing special chars."""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove leading/trailing whitespace
    text = text.strip()
    
    # Remove special characters but keep letters, numbers, spaces, basic punctuation
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    
    return text

def normalize_names(names):
    """Normalize person names to consistent format."""
    normalized = []
    for name in names:
        # Clean and split name
        clean_name = clean_text_data(name)
        parts = clean_name.split()
        
        # Capitalize each part
        normalized_parts = [part.capitalize() for part in parts if part]
        normalized.append(' '.join(normalized_parts))
    
    return normalized

# Demonstrate string manipulation
print("String Data Manipulation Examples:")

# Parse CSV-like data
csv_text = """
Name, Age, City, Salary
Alice Johnson, 28, New York, 75000
Bob Smith, 35, Los Angeles, 82000
Charlie Brown, 42, Chicago, 68000
Diana Prince, 31, Boston, 79000
"""

parsed_data = parse_structured_text(csv_text)
print("Parsed employee data:")
for record in parsed_data:
    print(f"  {record}")
print()

# Extract patterns from text
log_text = """
2024-01-15 10:30:25 ERROR: Failed login attempt for user@example.com from IP 192.168.1.100
2024-01-15 10:35:10 INFO: Successful login for admin@company.com from IP 10.0.0.50
2024-01-15 11:20:45 WARNING: High memory usage detected on server web-01
2024-01-15 11:25:30 ERROR: Database connection timeout for user john@domain.org
"""

patterns = {
    'timestamps': r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
    'emails': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    'ip_addresses': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
    'log_levels': r'\b(INFO|WARNING|ERROR)\b'
}

extracted = extract_patterns(log_text, patterns)
print("Extracted patterns from log file:")
for pattern_name, matches in extracted.items():
    print(f"  {pattern_name}: {matches}")
print()

# Clean and normalize names
messy_names = ["  ALICE johnson  ", "bob   SMITH", "Charlie-Brown", "diana  prince-wilson"]
clean_names = normalize_names(messy_names)
print("Name normalization:")
for original, cleaned in zip(messy_names, clean_names):
    print(f"  '{original}' -> '{cleaned}'")
print()

# DATA VALIDATION AND ERROR HANDLING
print("=== DATA VALIDATION AND ERROR HANDLING ===")
print()

def validate_data_types(data, schema):
    """Validate data against expected types and constraints."""
    errors = []
    
    for key, constraints in schema.items():
        if key not in data:
            if constraints.get('required', False):
                errors.append(f"Missing required field: {key}")
            continue
        
        value = data[key]
        expected_type = constraints.get('type')
        
        # Type validation
        if expected_type and not isinstance(value, expected_type):
            try:
                # Try to convert
                if expected_type == int:
                    data[key] = int(value)
                elif expected_type == float:
                    data[key] = float(value)
                elif expected_type == str:
                    data[key] = str(value)
            except (ValueError, TypeError):
                errors.append(f"Invalid type for {key}: expected {expected_type.__name__}, got {type(value).__name__}")
                continue
        
        # Range validation
        if 'min' in constraints and data[key] < constraints['min']:
            errors.append(f"{key} below minimum: {data[key]} < {constraints['min']}")
        
        if 'max' in constraints and data[key] > constraints['max']:
            errors.append(f"{key} above maximum: {data[key]} > {constraints['max']}")
        
        # Length validation
        if 'min_length' in constraints and len(str(data[key])) < constraints['min_length']:
            errors.append(f"{key} too short: minimum {constraints['min_length']} characters")
        
        if 'max_length' in constraints and len(str(data[key])) > constraints['max_length']:
            errors.append(f"{key} too long: maximum {constraints['max_length']} characters")
    
    return len(errors) == 0, errors

def sanitize_input(input_string, max_length=100, allowed_chars=None):
    """Sanitize user input for security and consistency."""
    if allowed_chars is None:
        allowed_chars = r'[A-Za-z0-9\s.,!?-]'
    
    # Remove disallowed characters
    sanitized = re.sub(f'[^{allowed_chars[1:-1]}]', '', input_string)
    
    # Trim to max length
    sanitized = sanitized[:max_length]
    
    # Clean whitespace
    sanitized = ' '.join(sanitized.split())
    
    return sanitized

def handle_missing_data(arr, strategy='remove'):
    """Handle missing data in array with different strategies."""
    if strategy == 'remove':
        return [x for x in arr if x is not None and str(x).strip()]
    
    elif strategy == 'replace_mean':
        # Calculate mean of non-None numeric values
        numeric_values = [x for x in arr if x is not None and isinstance(x, (int, float))]
        if not numeric_values:
            return arr
        mean_value = sum(numeric_values) / len(numeric_values)
        return [x if x is not None else mean_value for x in arr]
    
    elif strategy == 'replace_mode':
        # Find most common non-None value
        from collections import Counter
        non_none_values = [x for x in arr if x is not None]
        if not non_none_values:
            return arr
        mode_value = Counter(non_none_values).most_common(1)[0][0]
        return [x if x is not None else mode_value for x in arr]
    
    elif strategy == 'replace_default':
        return [x if x is not None else 0 for x in arr]
    
    return arr

# Demonstrate validation and error handling
print("Data Validation Examples:")

# Validate user data
user_schema = {
    'name': {'type': str, 'required': True, 'min_length': 2, 'max_length': 50},
    'age': {'type': int, 'required': True, 'min': 0, 'max': 150},
    'email': {'type': str, 'required': True},
    'salary': {'type': float, 'min': 0}
}

test_data = [
    {'name': 'John Doe', 'age': '30', 'email': 'john@example.com', 'salary': 50000.0},
    {'name': 'J', 'age': -5, 'email': 'invalid-email', 'salary': -1000},
    {'age': 25, 'email': 'missing@name.com', 'salary': 45000},
    {'name': 'Valid User', 'age': 28, 'email': 'valid@user.com'}
]

for i, data in enumerate(test_data):
    is_valid, errors = validate_data_types(data, user_schema)
    print(f"  Record {i + 1}: Valid={is_valid}")
    if errors:
        for error in errors:
            print(f"    - {error}")
    print()

# Handle missing data
print("Missing data handling:")
data_with_missing = [10, 20, None, 30, None, 40, 50, None, 60]
print(f"Original data: {data_with_missing}")

strategies = ['remove', 'replace_mean', 'replace_mode', 'replace_default']
for strategy in strategies:
    cleaned = handle_missing_data(data_with_missing, strategy)
    print(f"  {strategy}: {cleaned}")
print()

# PERFORMANCE OPTIMIZATION
print("=== PERFORMANCE OPTIMIZATION ===")
print()

def process_large_array_optimized(arr, batch_size=1000):
    """Process large array in batches to optimize memory usage."""
    results = []
    total_batches = (len(arr) + batch_size - 1) // batch_size
    
    print(f"Processing {len(arr)} items in {total_batches} batches of {batch_size}")
    
    for i in range(0, len(arr), batch_size):
        batch = arr[i:i + batch_size]
        # Simulate processing (square each number)
        batch_result = [x ** 2 for x in batch]
        results.extend(batch_result)
        
        if (i // batch_size + 1) % 10 == 0:  # Progress every 10 batches
            progress = (i + len(batch)) / len(arr) * 100
            print(f"  Progress: {progress:.1f}%")
    
    return results

def use_generator_for_memory_efficiency(n):
    """Generator function for memory-efficient processing."""
    for i in range(n):
        yield i ** 2

def compare_list_vs_generator():
    """Compare memory usage of list vs generator."""
    n = 1000000
    
    # List comprehension (creates all items in memory)
    print(f"Creating list of {n} squares...")
    start_time = time.time()
    list_squares = [x ** 2 for x in range(n)]
    list_time = time.time() - start_time
    
    # Generator (creates items on demand)
    print(f"Creating generator of {n} squares...")
    start_time = time.time()
    gen_squares = use_generator_for_memory_efficiency(n)
    gen_time = time.time() - start_time
    
    print(f"  List creation time: {list_time:.4f} seconds")
    print(f"  Generator creation time: {gen_time:.6f} seconds")
    print(f"  Generator is {list_time/gen_time:.0f}x faster to create")
    
    # Process first 10 items
    list_sample = list_squares[:10]
    gen_sample = [next(gen_squares) for _ in range(10)]
    
    print(f"  First 10 list items: {list_sample}")
    print(f"  First 10 generator items: {gen_sample}")

# Demonstrate performance optimization
print("Performance Optimization Examples:")
import time

# Batch processing simulation
large_data = list(range(5000))
processed_data = process_large_array_optimized(large_data, batch_size=1000)
print(f"Processed {len(processed_data)} items")
print()

# Memory efficiency comparison
compare_list_vs_generator()
print()

print("=== SUMMARY ===")
print()
print("Data Manipulation Summary:")
print("1. Array transformations enable flexible data processing")
print("2. Filtering and selection help extract relevant information")
print("3. Statistical analysis provides insights into data patterns")
print("4. String manipulation is essential for text processing")
print("5. Data validation prevents errors and security issues")
print("6. Performance optimization is crucial for large datasets")
print("7. Error handling ensures robust data processing")
print("8. Choose appropriate data structures and algorithms based on needs")

"""
KEY TAKEAWAYS:
==============
1. Data transformation is a fundamental programming skill
2. Always validate and clean data before processing
3. Use appropriate data structures for different operations
4. Consider memory and performance implications
5. Handle missing and invalid data gracefully
6. Regular expressions are powerful for text processing
7. Batch processing helps handle large datasets efficiently
8. Generators can provide memory-efficient alternatives to lists

TRANSFORMATION TECHNIQUES:
==========================
• Map: Apply function to each element
• Filter: Select elements meeting criteria
• Reduce: Aggregate elements to single value
• Group: Organize elements by key
• Sort: Order elements by criteria

DATA CLEANING WORKFLOW:
=======================
1. Validate data types and formats
2. Handle missing or null values
3. Remove or correct invalid entries
4. Normalize formats and encodings
5. Remove duplicates if necessary
6. Apply business rules and constraints

PERFORMANCE CONSIDERATIONS:
===========================
• Use list comprehensions for simple transformations
• Consider generators for memory-efficient processing
• Process large datasets in batches
• Cache expensive calculations
• Choose appropriate algorithms for data size
• Profile code to identify bottlenecks

STRING PROCESSING PATTERNS:
===========================
• Regular expressions for pattern matching
• Split and join for parsing and formatting
• String methods for common operations
• Unicode handling for international text
• Validation for security and consistency

ERROR HANDLING STRATEGIES:
==========================
• Validate input data early
• Provide meaningful error messages
• Use try-catch for expected failures
• Log errors for debugging
• Graceful degradation when possible
• Unit test edge cases

REAL-WORLD APPLICATIONS:
========================
• Data analysis and reporting
• File processing and transformation
• Web scraping and parsing
• Database operations
• API data processing
• Machine learning preprocessing

NEXT STEP:
Go to 05-text-analysis.py to learn about advanced text processing and analysis!
"""