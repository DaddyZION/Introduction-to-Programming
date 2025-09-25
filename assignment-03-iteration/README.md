# Assignment 3: Iteration Constructs (13%)

## 🎯 Learning Objectives

By the end of this assignment, you will understand:
- For loops for counting and iterating over sequences
- While loops for condition-based repetition
- Loop control with break and continue
- Nested loops for complex patterns
- Common loop patterns and applications

## 📖 What are Iteration Constructs?

Iteration constructs (loops) allow programs to **repeat** code multiple times. Instead of writing the same code over and over, you can use loops to execute code blocks repeatedly based on conditions or for a specific number of times.

Think of loops like:
- "Count from 1 to 10"
- "Keep asking for input until the user enters 'quit'"
- "Process each student in the class list"
- "Repeat this calculation for every data point"

### Key Concepts:

1. **for loops** - Repeat code a specific number of times or for each item in a sequence
2. **while loops** - Repeat code as long as a condition remains true
3. **Loop control** - Using break to exit early, continue to skip iterations
4. **Nested loops** - Loops inside other loops for complex patterns
5. **Loop variables** - Counters and accumulators that change each iteration
6. **Infinite loops** - How to avoid them and when they might be useful

## 📁 Files in This Assignment

- `examples/` - Commented code examples
- `exercises/` - Practice problems
- `solutions/` - Detailed solutions

## 🚀 Start Here

Begin with the examples in the `examples/` folder:
1. `01-basic-for-loops.py` - Counting and basic iteration
2. `02-for-loops-with-sequences.py` - Iterating over lists and strings
3. `03-while-loops.py` - Condition-based repetition
4. `04-loop-control.py` - Break, continue, and loop management
5. `05-nested-loops.py` - Loops within loops
6. `06-loop-patterns.py` - Common programming patterns with loops
7. `07-complete-program.py` - Comprehensive loop-based application

## 💡 Key Programming Concepts

### Basic For Loop
```python
for i in range(5):          # Repeat 5 times (0, 1, 2, 3, 4)
    print(f"Count: {i}")
```

### For Loop with Sequences
```python
names = ["Alice", "Bob", "Charlie"]
for name in names:          # Iterate over each item
    print(f"Hello, {name}!")
```

### While Loop
```python
count = 0
while count < 5:            # Repeat while condition is True
    print(f"Count: {count}")
    count += 1              # Don't forget to update the condition!
```

### Loop Control
```python
for i in range(10):
    if i == 3:
        continue            # Skip this iteration
    if i == 7:
        break              # Exit the loop entirely
    print(i)
```

## ⚠️ Common Mistakes to Avoid

1. **Infinite while loops**: Forgetting to update the loop condition
2. **Off-by-one errors**: range(10) goes 0-9, not 1-10
3. **Modifying loop variables**: Don't change the loop counter inside a for loop
4. **Nested loop confusion**: Keep track of which loop does what
5. **Using wrong loop type**: Choose for vs while based on the problem

## 🎯 Success Criteria

You'll know you understand iteration constructs when you can:
- Write for loops to repeat code a specific number of times
- Use while loops for condition-based repetition
- Iterate over strings, lists, and ranges effectively
- Control loop execution with break and continue
- Create nested loops for complex patterns
- Choose the right type of loop for different problems

Ready to start repeating code efficiently? Head to the `examples/` folder! 🔄