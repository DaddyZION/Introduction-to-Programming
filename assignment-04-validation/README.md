# Assignment 4: Data Validation and Input Handling (13%)

## 🎯 Learning Objectives

By the end of this assignment, you will understand:
- Input validation techniques and best practices
- Error handling and exception management
- Data sanitization and cleaning methods
- User input validation patterns
- Robust program design principles
- Type checking and conversion
- Range validation and boundary checking
- Format validation (emails, phones, etc.)

## 📖 What is Data Validation?

Data validation is the process of **ensuring data quality** by checking that input meets specific criteria before processing. It's one of the most critical aspects of programming because:

- **Security**: Prevents malicious input from compromising your program
- **Reliability**: Ensures your program works correctly with clean data
- **User Experience**: Provides clear feedback when input is incorrect
- **Data Integrity**: Maintains consistency and accuracy in your data

Think of validation like a **quality control checkpoint**:
- "Is this email address in the correct format?"
- "Is this age between reasonable limits?"
- "Does this password meet security requirements?"
- "Is this credit card number valid?"

### Key Validation Concepts:

1. **Input Validation** - Check user input before processing
2. **Type Validation** - Ensure data is the correct type (int, float, string)
3. **Range Validation** - Verify values are within acceptable limits
4. **Format Validation** - Check patterns (email, phone, etc.)
5. **Business Rule Validation** - Enforce domain-specific rules
6. **Error Handling** - Gracefully manage invalid input
7. **Data Sanitization** - Clean and normalize input data

## 🏗️ Why Validation Matters

### Without Validation:
```python
age = int(input("Enter age: "))  # What if user enters "abc"? -> CRASH!
price = float(input("Price: "))  # What if negative? -> Logic errors!
```

### With Validation:
```python
while True:
    try:
        age = int(input("Enter age: "))
        if 0 <= age <= 150:
            break
        else:
            print("Age must be between 0 and 150")
    except ValueError:
        print("Please enter a valid number")
```

## 📁 Files in This Assignment

- `examples/` - Comprehensive code examples
- `exercises/` - Practice problems with solutions
- `README.md` - This overview document

## 🚀 Start Here

Begin with the examples in the `examples/` folder:

1. `01-basic-validation.py` - Introduction to input validation
2. `02-type-validation.py` - Type checking and conversion
3. `03-range-validation.py` - Boundary and limit checking
4. `04-format-validation.py` - Pattern matching and format checking
5. `05-exception-handling.py` - Error handling and recovery
6. `06-data-sanitization.py` - Cleaning and normalizing data
7. `07-complete-program.py` - Comprehensive validation system

## 💡 Key Programming Concepts

### Basic Validation Pattern
```python
def validate_input(value, validator_func, error_message):
    if validator_func(value):
        return value
    else:
        raise ValueError(error_message)
```

### Try-Except Pattern
```python
try:
    # Code that might fail
    result = risky_operation()
except SpecificError:
    # Handle the error
    print("Something went wrong")
```

### Validation Loop Pattern
```python
while True:
    user_input = input("Enter value: ")
    if is_valid(user_input):
        break
    print("Invalid input, try again")
```

## 🔧 Common Validation Types

### 1. Type Validation
- Converting strings to numbers
- Checking data types
- Handling conversion errors

### 2. Range Validation
- Minimum/maximum values
- Boundary checking
- Inclusive/exclusive ranges

### 3. Format Validation
- Email addresses
- Phone numbers
- Credit card numbers
- Postal codes

### 4. Business Rule Validation
- Age restrictions
- Password complexity
- Unique constraints
- Relationship validation

## 🛡️ Validation Best Practices

1. **Validate Early** - Check input as soon as possible
2. **Be Specific** - Provide clear error messages
3. **Fail Gracefully** - Don't crash on bad input
4. **Sanitize Data** - Clean input before processing
5. **Use Whitelisting** - Accept known good patterns
6. **Test Edge Cases** - Empty strings, extreme values
7. **Document Requirements** - Make validation rules clear

## 🎓 Real-World Applications

- **Web Forms**: User registration, contact forms
- **Financial Systems**: Transaction validation, account verification
- **Healthcare**: Patient data validation, dosage checking
- **E-commerce**: Product information, payment processing
- **Gaming**: Score validation, user input handling
- **Data Processing**: File validation, data cleaning

## 📊 Assignment Weight: 13%

This assignment represents 13% of your total course grade, reflecting the critical importance of validation in real-world programming. Mastering these concepts will make you a more professional and reliable programmer.

## 🏆 Success Criteria

You'll know you've mastered validation when you can:
- ✅ Design robust input validation systems
- ✅ Handle errors gracefully without crashing
- ✅ Validate different data types and formats
- ✅ Provide helpful user feedback
- ✅ Implement business rule validation
- ✅ Create reusable validation functions
- ✅ Test validation thoroughly with edge cases

## 🔗 Connection to Other Assignments

This assignment builds on:
- **Assignment 1**: Variable types and string handling
- **Assignment 2**: Conditional logic for validation rules
- **Assignment 3**: Loops for input retry mechanisms

And prepares you for:
- **Assignment 5**: Functions to organize validation logic
- **Assignment 6**: Validating array/list data
- **Assignment 7**: Complex data structure validation

---

**Ready to become a validation expert? Start with `01-basic-validation.py`! 🚀**

*Remember: Good validation is the foundation of professional software. Every input is untrusted until proven valid!*