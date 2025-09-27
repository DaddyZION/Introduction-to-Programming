# Assignment 6 - Arrays and Strings Exercises
## 1D Data Structures Practice Problems

Welcome to Assignment 6 exercises! These problems will help you practice and master the concepts of arrays, strings, and 1D data structures. Each exercise builds upon the examples and includes varying difficulty levels.

## Exercise Categories

### 🟢 Basic Level (Exercises 1-5)
- Array creation and basic operations
- String manipulation fundamentals
- Simple searching and basic algorithms
- **Recommended for**: Students new to arrays and strings

### 🟡 Intermediate Level (Exercises 6-10)
- Complex data manipulation
- Algorithm implementation
- Multi-step problem solving
- **Recommended for**: Students comfortable with basic concepts

### 🔴 Advanced Level (Exercises 11-15)
- Sophisticated algorithms
- Performance optimization
- Real-world applications
- **Recommended for**: Students ready for challenging problems

---

## 🟢 Basic Level Exercises

### Exercise 1: Array Statistics Calculator
**File**: `exercise-01-array-stats.py`

Create a program that:
1. Takes a list of numbers from user input
2. Calculates and displays:
   - Sum, average, minimum, maximum
   - Count of positive, negative, and zero values
   - Range (max - min)

**Sample Input**: `[5, -3, 8, 0, 12, -7, 4]`
**Expected Output**:
```
Sum: 19
Average: 2.71
Min: -7, Max: 12
Range: 19
Positive: 4, Negative: 2, Zero: 1
```

---

### Exercise 2: String Formatter
**File**: `exercise-02-string-formatter.py`

Create a program that:
1. Takes a person's full name and formats it properly
2. Handles various input formats (different cases, extra spaces)
3. Validates the input and provides error messages
4. Outputs the name in different formats:
   - "Last, First Middle"
   - "First M. Last"
   - "F. M. Last"

**Sample Input**: `"  alice marie   JOHNSON  "`
**Expected Output**:
```
Formatted name: Alice Marie Johnson
Last, First: Johnson, Alice Marie
First Initial: Alice M. Johnson
Initials: A. M. Johnson
```

---

### Exercise 3: Simple Shopping List Manager
**File**: `exercise-03-shopping-list.py`

Create a shopping list manager that:
1. Allows adding items to a list
2. Removes items from the list
3. Displays the list in alphabetical order
4. Finds items containing specific text
5. Calculates total if prices are included

**Required Functions**:
- `add_item(shopping_list, item)`
- `remove_item(shopping_list, item)`
- `find_items(shopping_list, search_term)`
- `display_list(shopping_list)`

---

### Exercise 4: Password Validator
**File**: `exercise-04-password-validator.py`

Create a password validation system that:
1. Checks password strength based on multiple criteria
2. Provides specific feedback for each missing requirement
3. Suggests improvements
4. Rates password strength (Weak/Fair/Good/Strong)

**Validation Rules**:
- At least 8 characters long
- Contains uppercase and lowercase letters
- Contains at least one number
- Contains at least one special character
- No common dictionary words

---

### Exercise 5: Grade Book Analyzer
**File**: `exercise-05-gradebook.py`

Create a grade book system that:
1. Stores student names and their test scores
2. Calculates average score for each student
3. Finds the class average
4. Identifies top and bottom performers
5. Generates a simple report

**Data Structure**: Use a dictionary where keys are student names and values are lists of scores.

---

## 🟡 Intermediate Level Exercises

### Exercise 6: Text File Analyzer
**File**: `exercise-06-text-analyzer.py`

Create a comprehensive text analysis tool that:
1. Reads text from user input or simulated file content
2. Counts words, sentences, and paragraphs
3. Finds the most and least common words
4. Calculates average word and sentence length
5. Identifies potential readability level
6. Generates a word frequency histogram (text-based)

**Advanced Features**:
- Remove stopwords for better analysis
- Handle punctuation properly
- Calculate reading time estimate

---

### Exercise 7: Inventory Management System
**File**: `exercise-07-inventory.py`

Build an inventory management system that:
1. Manages product information (name, quantity, price)
2. Supports adding, updating, and removing products
3. Calculates total inventory value
4. Finds products by various criteria
5. Generates low-stock alerts
6. Sorts products by different attributes

**Data Structure**: List of dictionaries representing products.

---

### Exercise 8: Contact Directory
**File**: `exercise-08-contact-directory.py`

Create a contact management system that:
1. Stores contact information (name, phone, email, address)
2. Validates phone numbers and email addresses
3. Supports multiple search methods
4. Groups contacts by categories
5. Exports contact list in formatted text
6. Handles duplicate detection

**Features**:
- Phone number normalization
- Email validation using regex
- Fuzzy name searching

---

### Exercise 9: Data Cleaning Utility
**File**: `exercise-09-data-cleaning.py`

Build a data cleaning utility that:
1. Takes messy data arrays (mixed types, missing values, duplicates)
2. Identifies and handles different types of data issues
3. Provides cleaning options (remove, replace, normalize)
4. Generates a cleaning report
5. Validates data consistency

**Cleaning Tasks**:
- Remove duplicates
- Handle missing values
- Normalize formats (dates, phone numbers)
- Detect outliers
- Fix encoding issues

---

### Exercise 10: Survey Data Processor
**File**: `exercise-10-survey-processor.py`

Create a survey data processing system that:
1. Processes survey responses (multiple choice, ratings, text)
2. Calculates response statistics
3. Performs sentiment analysis on text responses
4. Groups responses by demographics
5. Generates summary charts (text-based)
6. Identifies trends and patterns

---

## 🔴 Advanced Level Exercises

### Exercise 11: Advanced Sorting Algorithms
**File**: `exercise-11-advanced-sorting.py`

Implement and compare advanced sorting algorithms:
1. Merge sort with visualization
2. Quick sort with different pivot strategies
3. Heap sort implementation
4. Performance comparison with timing
5. Hybrid sorting for different data types
6. Stable vs unstable sorting demonstration

**Requirements**:
- Visual step-by-step output
- Performance metrics
- Memory usage analysis
- Best/worst case demonstrations

---

### Exercise 12: Pattern Recognition Engine
**File**: `exercise-12-pattern-recognition.py`

Build a pattern recognition system that:
1. Finds patterns in numeric sequences
2. Detects trends and cycles
3. Predicts next values in sequences
4. Identifies anomalies and outliers
5. Generates pattern reports
6. Supports multiple pattern types (arithmetic, geometric, polynomial)

**Advanced Features**:
- Machine learning-style pattern detection
- Confidence scoring
- Multiple algorithm comparison

---

### Exercise 13: Text Similarity Analyzer
**File**: `exercise-13-similarity-analyzer.py`

Create a sophisticated text similarity system that:
1. Implements multiple similarity algorithms
2. Handles document preprocessing
3. Performs plagiarism detection
4. Groups similar documents
5. Generates similarity matrices
6. Supports multiple languages

**Algorithms to Implement**:
- Cosine similarity
- Jaccard coefficient
- Edit distance (Levenshtein)
- N-gram analysis

---

### Exercise 14: Performance Optimization Lab
**File**: `exercise-14-optimization-lab.py`

Create a performance testing and optimization laboratory:
1. Compare different array operations
2. Memory usage profiling
3. Algorithm complexity verification
4. Optimization technique demonstrations
5. Benchmarking suite
6. Performance regression testing

**Optimization Techniques**:
- List comprehensions vs loops
- Generator expressions
- Memory-efficient algorithms
- Caching strategies

---

### Exercise 15: Mini Database Engine
**File**: `exercise-15-database-engine.py`

Build a simple database engine using arrays and strings:
1. Table creation and management
2. Data insertion, updating, deletion
3. Query processing (SELECT, WHERE, ORDER BY)
4. Index creation for performance
5. Join operations between tables
6. Data persistence (save/load)

**Features**:
- SQL-like query language
- Transaction support
- Data validation
- Performance optimization

---

## Getting Started

### Prerequisites
- Complete understanding of Assignment 6 examples (01-06)
- Python basics (variables, functions, control structures)
- Basic understanding of algorithms and data structures

### How to Approach These Exercises

1. **Start with your level**: Begin with basic exercises if you're new to these concepts
2. **Read carefully**: Each exercise has specific requirements and expected outputs
3. **Plan first**: Think about your approach before coding
4. **Test thoroughly**: Create test cases for different scenarios
5. **Optimize**: After getting it working, consider improvements
6. **Document**: Add comments explaining your logic

### Exercise Structure Template

Each exercise file should follow this structure:

```python
"""
Exercise [Number]: [Title]
Level: [Basic/Intermediate/Advanced]

Description: [What the program does]

Requirements:
- [Requirement 1]
- [Requirement 2]
...

Author: [Your name]
Date: [Date]
"""

def main():
    \"\"\"Main program execution\"\"\"
    print("Exercise [Number]: [Title]")
    print("=" * 40)
    
    # Your implementation here
    
    # Test your functions
    test_functions()

def test_functions():
    \"\"\"Test your implementations\"\"\"
    print("\nTesting...")
    # Add your test cases here

if __name__ == "__main__":
    main()
```

### Submission Guidelines

1. **File naming**: Follow the exact naming convention provided
2. **Code quality**: Use proper indentation, comments, and variable names
3. **Testing**: Include test cases demonstrating your solution works
4. **Documentation**: Explain complex algorithms and design decisions
5. **Error handling**: Handle edge cases and invalid inputs gracefully

---

## Additional Resources

### Helpful References
- Python documentation for string methods
- Algorithm complexity reference
- Regular expression guide
- Performance profiling techniques

### Practice Data
You can generate test data for your exercises using these techniques:
- Random number generation for arrays
- Lorem ipsum text for string processing
- Mock datasets for real-world scenarios

### Challenge Yourself
- Implement solutions without using certain built-in functions
- Optimize for different constraints (memory, speed, readability)
- Add GUI interfaces to your console programs
- Extend exercises with additional features

---

## Assessment Criteria

Your exercises will be evaluated on:

### Functionality (40%)
- Correct implementation of requirements
- Proper handling of edge cases
- Robust error handling

### Code Quality (30%)
- Clean, readable code structure
- Appropriate use of functions and classes
- Proper naming conventions
- Adequate comments and documentation

### Algorithm Efficiency (20%)
- Appropriate choice of algorithms
- Time and space complexity considerations
- Performance optimization where relevant

### Testing and Examples (10%)
- Comprehensive test cases
- Clear demonstration of functionality
- Good example data and scenarios

---

Good luck with your exercises! Remember, the goal is to deepen your understanding of arrays, strings, and 1D data structures. Don't hesitate to experiment with different approaches and challenge yourself with the more advanced problems.

**Assignment 6 Weight**: 16% of total course grade
**Due Date**: [Check course schedule]
**Estimated Time**: 15-25 hours depending on chosen exercises

Happy coding! 🚀💻📊