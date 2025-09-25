# Assignment 2: Selection Constructs (12%)

## 🎯 Learning Objectives

By the end of this assignment, you will understand:
- Conditional statements (if, elif, else)
- Boolean expressions and logical operators
- Comparison operators
- Nested conditional statements
- Decision-making in programs

## 📖 What are Selection Constructs?

Selection constructs allow programs to make **decisions** and choose different paths based on conditions. Instead of executing every line sequentially, your program can "branch" and execute different code blocks depending on the situation.

Think of it like a flowchart with decision points:
- "IF the weather is rainy, take an umbrella"
- "IF your grade is above 80, you get an A, ELSE you get a B"
- "IF temperature < 0, it's freezing, ELIF temperature < 20, it's cold, ELSE it's warm"

### Key Concepts:

1. **if statements** - Execute code only when a condition is true
2. **else statements** - Execute code when the if condition is false
3. **elif statements** - Test multiple conditions in sequence
4. **Boolean expressions** - Expressions that evaluate to True or False
5. **Comparison operators** - Compare values (==, !=, <, >, <=, >=)
6. **Logical operators** - Combine conditions (and, or, not)

## 📁 Files in This Assignment

- `examples/` - Commented code examples
- `exercises/` - Practice problems
- `solutions/` - Detailed solutions

## 🚀 Start Here

Begin with the examples in the `examples/` folder:
1. `01-basic-if-statements.py` - Simple conditional logic
2. `02-if-else-statements.py` - Two-way decisions
3. `03-elif-statements.py` - Multiple conditions
4. `04-boolean-logic.py` - Logical operators and complex conditions
5. `05-nested-conditions.py` - Conditions inside conditions
6. `06-complete-program.py` - Real-world decision-making program

## 💡 Key Programming Concepts

### Basic if Statement
```python
if condition:
    # Code to execute if condition is True
    print("Condition was true!")
```

### if-else Statement
```python
if condition:
    print("Condition is true")
else:
    print("Condition is false")
```

### if-elif-else Statement
```python
if condition1:
    print("First condition is true")
elif condition2:
    print("Second condition is true")
else:
    print("No conditions were true")
```

### Comparison Operators
- `==` Equal to
- `!=` Not equal to  
- `<` Less than
- `>` Greater than
- `<=` Less than or equal to
- `>=` Greater than or equal to

### Logical Operators
- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Reverses the condition

## ⚠️ Common Mistakes to Avoid

1. **Using = instead of ==**: Remember = assigns, == compares
2. **Forgetting colons**: if statements need a colon (:) at the end
3. **Indentation errors**: Code inside if blocks must be indented
4. **Logical operator confusion**: Understand difference between `and` and `or`
5. **Floating point comparisons**: Be careful comparing decimal numbers

## 🎯 Success Criteria

You'll know you understand selection constructs when you can:
- Write if statements that make decisions based on conditions
- Use elif to handle multiple possible conditions
- Combine conditions using and, or, not
- Create programs that respond differently to different inputs
- Debug logical errors in conditional statements

Ready to start making decisions in code? Head to the `examples/` folder! 🚀