"""
Assignment 3 - Example 4: LOOP CONTROL (break, continue, pass)
==============================================================

This program demonstrates advanced loop control statements that give you
precise control over loop execution. These tools help you handle special
cases, exit early, or skip iterations based on conditions.

Key Concepts Demonstrated:
- break statement (exit loop immediately)
- continue statement (skip to next iteration)
- pass statement (placeholder/do nothing)
- Loop control with flags
- Early termination strategies
- Exception handling in loops
"""

print("=== LOOP CONTROL STATEMENTS ===")
print()

# INTRODUCTION TO LOOP CONTROL
print("Loop control statements let you modify loop behavior:")
print("• break    - Exit the loop immediately")
print("• continue - Skip the rest of this iteration, go to next")
print("• pass     - Do nothing (placeholder)")
print()

# BREAK STATEMENT
print("=== THE BREAK STATEMENT ===")
print()

print("BREAK exits the loop immediately, no matter what")
print()

# Example 1: Finding a number in a sequence
print("Example 1: Find the first number greater than 50")

numbers = [12, 34, 67, 23, 89, 45, 78]
found_number = None
position = -1

print(f"Searching in: {numbers}")

for i in range(len(numbers)):
    number = numbers[i]
    print(f"Checking position {i}: {number}")
    
    if number > 50:
        found_number = number
        position = i
        print(f"Found it! {number} is greater than 50")
        break                   # Exit the loop immediately
        print("This line never executes")  # Unreachable code
    
    print(f"  {number} is not greater than 50, continuing...")

if found_number is not None:
    print(f"Result: Found {found_number} at position {position}")
else:
    print("Result: No number greater than 50 found")

print()

# Example 2: User input with early exit
print("Example 2: Password attempts with break")

correct_password = "secret123"
max_attempts = 3
attempts = 0

print("Please enter the password:")

for attempt in range(1, max_attempts + 1):
    password = input(f"Attempt {attempt}/{max_attempts}: ")
    attempts = attempt
    
    if password == correct_password:
        print("✅ Access granted! Breaking out of loop.")
        break                   # Exit immediately on success
        
    print(f"❌ Incorrect password.")
    
    if attempt == max_attempts:
        print("Maximum attempts reached.")
else:
    # This 'else' runs only if the loop completes WITHOUT break
    print("🔒 Access denied - loop completed normally")

# Check what happened
if password == correct_password:
    print(f"Success after {attempts} attempts!")
else:
    print(f"Failed after {attempts} attempts.")

print()

# CONTINUE STATEMENT
print("=== THE CONTINUE STATEMENT ===")
print()

print("CONTINUE skips the rest of the current iteration")
print("and jumps to the next iteration of the loop")
print()

# Example 1: Skip negative numbers
print("Example 1: Process only positive numbers")

numbers = [5, -2, 8, -7, 12, 0, -3, 15]
positive_sum = 0

print(f"Processing: {numbers}")
print("Skipping negative numbers and zero:")

for number in numbers:
    print(f"\nProcessing {number}:")
    
    if number <= 0:
        print(f"  {number} is not positive, skipping...")
        continue                # Skip to next iteration
        print("  This line never executes for non-positive numbers")
    
    # This code only runs for positive numbers
    positive_sum += number
    print(f"  {number} is positive, added to sum. New sum: {positive_sum}")

print(f"\nFinal sum of positive numbers: {positive_sum}")
print()

# Example 2: Skip specific values in data processing
print("Example 2: Clean data by skipping invalid values")

data = ["John", "", "Mary", None, "Bob", "   ", "Alice", ""]
cleaned_names = []

print("Raw data:", data)
print("Cleaning process:")

for item in data:
    print(f"\nProcessing: {repr(item)}")
    
    # Skip None values
    if item is None:
        print("  None value detected, skipping...")
        continue
    
    # Skip empty strings
    if item == "":
        print("  Empty string detected, skipping...")
        continue
    
    # Skip whitespace-only strings
    if item.strip() == "":
        print("  Whitespace-only string detected, skipping...")
        continue
    
    # If we get here, the data is valid
    cleaned_names.append(item.strip())
    print(f"  Valid name: '{item.strip()}' added to cleaned list")

print(f"\nOriginal data: {data}")
print(f"Cleaned data: {cleaned_names}")
print()

# COMBINING BREAK AND CONTINUE
print("=== COMBINING BREAK AND CONTINUE ===")
print()

print("Example: Process numbers until we hit a stop condition")

numbers = [3, 7, 2, -1, 9, 0, 4, -999, 6, 8]
processed = []
sum_positive = 0

print(f"Numbers to process: {numbers}")
print("Rules:")
print("• Skip negative numbers (except -999)")
print("• Add positive numbers to sum")
print("• Stop immediately when we see -999")
print()

for i, number in enumerate(numbers):
    print(f"Step {i+1}: Processing {number}")
    
    # Stop condition - break immediately
    if number == -999:
        print(f"  STOP SIGNAL (-999) detected! Breaking loop.")
        break
    
    # Skip condition - continue to next iteration
    if number < 0:
        print(f"  {number} is negative (not -999), skipping...")
        continue
    
    # Process valid positive numbers
    processed.append(number)
    sum_positive += number
    print(f"  {number} added. Running sum: {sum_positive}")

print(f"\nProcessed numbers: {processed}")
print(f"Sum of positive numbers: {sum_positive}")
print(f"Stopped at index: {i}")
print()

# PASS STATEMENT
print("=== THE PASS STATEMENT ===")
print()

print("PASS does nothing - it's a placeholder for future code")
print()

# Example 1: Placeholder in development
print("Example 1: Development placeholder")

for number in range(1, 6):
    if number % 2 == 0:
        # TODO: Implement even number processing later
        pass                    # Placeholder - does nothing
    else:
        print(f"{number} is odd")

print()

# Example 2: Empty exception handler
print("Example 2: Exception handling with pass")

numbers = ["5", "abc", "10", "3.14", "xyz"]
valid_numbers = []

for item in numbers:
    try:
        number = int(item)
        valid_numbers.append(number)
        print(f"✅ Converted '{item}' to {number}")
    except ValueError:
        # We know some conversions will fail, but that's okay
        pass                    # Ignore the error and continue
        print(f"❌ Skipped '{item}' (not a valid integer)")

print(f"Valid integers found: {valid_numbers}")
print()

# NESTED LOOPS WITH CONTROL STATEMENTS
print("=== LOOP CONTROL IN NESTED LOOPS ===")
print()

print("Important: break and continue only affect the innermost loop")
print()

# Example: Finding coordinates in a grid
print("Example: Search for value in a 2D grid")

grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

search_value = 7
found = False
found_row, found_col = -1, -1

print("Grid:")
for row in grid:
    print(row)

print(f"\nSearching for {search_value}:")

for row_index in range(len(grid)):
    print(f"\nSearching row {row_index}: {grid[row_index]}")
    
    for col_index in range(len(grid[row_index])):
        value = grid[row_index][col_index]
        print(f"  Checking position ({row_index},{col_index}): {value}")
        
        if value == search_value:
            found_row, found_col = row_index, col_index
            found = True
            print(f"  ✅ Found {search_value}!")
            break               # This only breaks the inner loop
    
    if found:                   # Need this to break outer loop
        print(f"Breaking out of outer loop too")
        break                   # This breaks the outer loop

if found:
    print(f"Result: {search_value} found at position ({found_row}, {found_col})")
else:
    print(f"Result: {search_value} not found in grid")

print()

# LOOP CONTROL WITH FLAGS
print("=== USING FLAGS FOR LOOP CONTROL ===")
print()

print("Flags are boolean variables that control loop behavior")
print()

# Example: Interactive menu with exit condition
print("Example: Restaurant ordering system")

menu = {
    1: ("Pizza", 12.99),
    2: ("Burger", 8.99),
    3: ("Salad", 7.49),
    4: ("Pasta", 11.49)
}

order = []
total = 0.0
ordering = True                 # Flag to control main loop

print("🍽️  Welcome to the Restaurant!")

while ordering:                 # Continue while flag is True
    print("\n=== MENU ===")
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - £{price:.2f}")
    print("5. View order")
    print("6. Checkout")
    print("7. Cancel order")
    
    try:
        choice = int(input("\nEnter your choice (1-7): "))
        
        if choice in menu:
            item, price = menu[choice]
            order.append((item, price))
            total += price
            print(f"✅ Added {item} (£{price:.2f}) to your order")
            
        elif choice == 5:
            if order:
                print("\n📋 Your Order:")
                for i, (item, price) in enumerate(order, 1):
                    print(f"  {i}. {item} - £{price:.2f}")
                print(f"Total: £{total:.2f}")
            else:
                print("Your order is empty")
                
        elif choice == 6:
            if order:
                print("\n🧾 Final Order:")
                for item, price in order:
                    print(f"  {item} - £{price:.2f}")
                print(f"Total: £{total:.2f}")
                print("Thank you for your order! 👋")
                ordering = False    # Set flag to exit loop
            else:
                print("Cannot checkout with empty order")
                
        elif choice == 7:
            print("Order cancelled. Thank you for visiting! 👋")
            ordering = False        # Set flag to exit loop
            
        else:
            print("❌ Invalid choice. Please try again.")
            
    except ValueError:
        print("❌ Please enter a valid number.")

print()

# ADVANCED PATTERN: LOOP WITH EARLY SUCCESS DETECTION
print("=== ADVANCED PATTERN: EARLY SUCCESS DETECTION ===")
print()

# Example: Testing network connections
print("Example: Testing connections to servers")

servers = [
    ("Server A", False),
    ("Server B", False),
    ("Server C", True),   # This one works
    ("Server D", True),
    ("Server E", False)
]

print("Testing server connections...")
working_servers = []
connection_found = False

for server_name, is_working in servers:
    print(f"\nTesting {server_name}...")
    
    if not is_working:
        print(f"  ❌ {server_name} is not responding")
        continue                # Skip to next server
    
    # Server is working
    print(f"  ✅ {server_name} is online!")
    working_servers.append(server_name)
    
    if not connection_found:    # First working server found
        print(f"  🎉 {server_name} will be our primary connection!")
        connection_found = True
        # Note: We continue testing instead of breaking
        # to find all working servers

print(f"\nResults:")
print(f"Working servers: {working_servers}")
print(f"Primary server: {working_servers[0] if working_servers else 'None'}")

if connection_found:
    print("✅ Successfully established connection!")
else:
    print("❌ No working servers found!")

print()

# PRACTICAL EXERCISE: DATA VALIDATION
print("=== PRACTICAL EXERCISE: DATA VALIDATION ===")
print()

print("Example: Validate and clean user data")

user_inputs = [
    "john.doe@email.com",
    "",                         # Empty
    "invalid-email",            # Invalid format
    "jane@company.co.uk",
    "   spaces@email.com   ",   # Has spaces
    "another@valid.org",
    "quit"                      # Stop signal
]

valid_emails = []
print("Processing email addresses:")
print("Rules: Skip empty, invalid format, or 'quit' signal")
print()

for i, email in enumerate(user_inputs):
    print(f"Input {i+1}: '{email}'")
    
    # Check for quit signal
    if email.strip().lower() == "quit":
        print("  🛑 Quit signal detected, stopping processing")
        break
    
    # Skip empty inputs
    if not email.strip():
        print("  ⚠️  Empty input, skipping")
        continue
    
    # Clean the email
    cleaned_email = email.strip()
    
    # Basic validation (contains @ and .)
    if "@" not in cleaned_email or "." not in cleaned_email:
        print(f"  ❌ Invalid format: '{cleaned_email}', skipping")
        continue
    
    # Valid email found
    valid_emails.append(cleaned_email)
    print(f"  ✅ Valid email added: '{cleaned_email}'")

print(f"\nProcessing complete!")
print(f"Valid emails collected: {valid_emails}")
print(f"Total valid emails: {len(valid_emails)}")

print()

print("=== SUMMARY ===")
print()
print("Loop Control Statements:")
print()
print("BREAK:")
print("• Exits the loop immediately")
print("• Useful for early termination")
print("• Only affects the innermost loop in nested loops")
print("• Common in search operations and error conditions")
print()
print("CONTINUE:")
print("• Skips the rest of the current iteration")
print("• Jumps to the next iteration")
print("• Great for filtering and data validation")
print("• Keeps the loop running")
print()
print("PASS:")
print("• Does nothing - placeholder statement")
print("• Useful during development")
print("• Required when syntax needs a statement but you want no action")
print("• Often used in exception handling")
print()
print("Best Practices:")
print("1. Use break for early success or failure detection")
print("2. Use continue for filtering invalid data")
print("3. Use flags for complex exit conditions")
print("4. Be careful with nested loops - break only affects innermost loop")
print("5. Consider using functions to avoid complex loop control")

"""
KEY TAKEAWAYS:
==============
1. break - Exit loop immediately, jump to code after loop
2. continue - Skip rest of iteration, go to next iteration  
3. pass - Do nothing, placeholder for future code
4. Loop control only affects the innermost loop in nested structures
5. Use flags for complex control logic
6. Great for search, validation, and early termination

COMMON USE CASES:
=================
• break: Search operations, early exit on error, user quit commands
• continue: Data filtering, skipping invalid inputs, conditional processing  
• pass: Development placeholders, empty exception handlers

ADVANCED PATTERNS:
==================
• Combine with flags for complex state management
• Use in validation pipelines for data cleaning
• Implement early success detection in testing scenarios
• Handle user interruption in interactive programs

NEXT STEP:
Go to 05-nested-loops.py to learn about loops inside loops!
"""