"""
Assignment 2 - Example 5: Nested Conditions
==========================================

This program demonstrates nested conditional statements - conditions inside
other conditions. Nested conditions allow for sophisticated decision-making
with multiple levels of logic, enabling complex program behavior.

Key Concepts Demonstrated:
- Nested if statements (if inside if)
- Multi-level decision trees
- Proper indentation for nested blocks
- Complex decision-making scenarios
- When to use nested vs flat conditions
- Avoiding deep nesting with early returns
"""

print("=== NESTED CONDITIONS ===")
print()

print("Nested conditions are if statements inside other if statements.")
print("They allow for multi-level decision making where the inner decision")
print("only happens if the outer condition is already true.")
print()

# BASIC NESTED CONDITIONS
print("=== BASIC NESTED CONDITIONS ===")
print()

print("Structure:")
print("if outer_condition:")
print("    if inner_condition:")
print("        # This only runs if BOTH conditions are true")
print("    else:")
print("        # This runs if outer is true but inner is false")
print("else:")
print("    # This runs if outer is false")
print()

# Example 1: Weather and activity planning
print("Example 1: Activity planning based on weather")

weather = "sunny"
temperature = 75
has_free_time = True

print(f"Current conditions:")
print(f"  Weather: {weather}")
print(f"  Temperature: {temperature}°F")
print(f"  Has free time: {has_free_time}")
print()

print("Decision process:")

if weather == "sunny":
    print("✓ Weather is sunny - outdoor activities possible")
    
    if temperature >= 70:
        print("  ✓ Temperature is warm enough")
        
        if has_free_time:
            print("    ✓ Have free time available")
            print("    🏖️  Perfect! Let's go to the beach!")
        else:
            print("    ✗ No free time available")
            print("    📚 Too busy - maybe next time")
    else:
        print("  ✗ Temperature too cold for outdoor activities")
        print("  🏠 Let's stay inside where it's warm")
else:
    print("✗ Weather is not sunny")
    print("🌧️  Indoor activities only today")

print()

# Example 2: Banking system with nested validation
print("Example 2: Banking transaction validation")

account_balance = 1500
transaction_amount = 800
daily_limit = 1000
account_active = True
has_overdraft = False

print(f"Account information:")
print(f"  Balance: ${account_balance}")
print(f"  Transaction amount: ${transaction_amount}")
print(f"  Daily limit: ${daily_limit}")
print(f"  Account active: {account_active}")
print(f"  Has overdraft protection: {has_overdraft}")
print()

print("Transaction validation:")

if account_active:
    print("✓ Account is active")
    
    if transaction_amount <= daily_limit:
        print("  ✓ Transaction within daily limit")
        
        if transaction_amount <= account_balance:
            print("    ✓ Sufficient funds available")
            print("    💰 TRANSACTION APPROVED")
            new_balance = account_balance - transaction_amount
            print(f"    New balance: ${new_balance}")
        else:
            print("    ✗ Insufficient funds")
            
            if has_overdraft:
                print("      ✓ Overdraft protection available")
                print("      💰 TRANSACTION APPROVED (with overdraft)")
                overdraft_amount = transaction_amount - account_balance
                print(f"      Overdraft used: ${overdraft_amount}")
            else:
                print("      ✗ No overdraft protection")
                print("      ❌ TRANSACTION DENIED")
    else:
        print("  ✗ Transaction exceeds daily limit")
        print("  ❌ TRANSACTION DENIED")
else:
    print("✗ Account is not active")
    print("❌ TRANSACTION DENIED")

print()

# NESTED CONDITIONS VS LOGICAL OPERATORS
print("=== NESTED CONDITIONS vs LOGICAL OPERATORS ===")
print()

print("Sometimes you can choose between nested conditions and logical operators:")
print()

# Same logic implemented both ways
age = 25
has_license = True
has_car = True

print(f"Driver profile: Age {age}, License: {has_license}, Car: {has_car}")
print()

# Method 1: Nested conditions
print("Method 1: Using nested conditions")
if age >= 18:
    print("  ✓ Old enough to drive")
    if has_license:
        print("    ✓ Has valid license")
        if has_car:
            print("      ✓ Has access to car")
            print("      🚗 CAN DRIVE!")
        else:
            print("      ✗ No car available")
            print("      🚌 Need to find transportation")
    else:
        print("    ✗ No valid license")
        print("    📖 Need to get license first")
else:
    print("  ✗ Too young to drive")
    print("  ⏰ Wait until 18")

print()

# Method 2: Logical operators (flatter structure)
print("Method 2: Using logical operators")
can_drive = age >= 18 and has_license and has_car

if can_drive:
    print("✓ All requirements met")
    print("🚗 CAN DRIVE!")
else:
    print("✗ Missing requirements:")
    if age < 18:
        print("  - Too young")
    if not has_license:
        print("  - No license")
    if not has_car:
        print("  - No car")

print()
print("Both methods work! Choose based on:")
print("• Nested: Better for step-by-step validation with different messages")
print("• Logical: Better for simple all-or-nothing decisions")

print()

# COMPLEX NESTED DECISION TREE
print("=== COMPLEX NESTED DECISION TREE ===")
print()

print("Example: Student grade calculator with complex rules")

exam_score = 85
homework_avg = 92
attendance_rate = 0.95  # 95%
participation = True
extra_credit = 5

print(f"Student performance:")
print(f"  Exam score: {exam_score}")
print(f"  Homework average: {homework_avg}")
print(f"  Attendance rate: {attendance_rate * 100:.0f}%")
print(f"  Participation: {participation}")
print(f"  Extra credit points: {extra_credit}")
print()

print("Grade calculation process:")

# Start with base grade calculation
base_grade = (exam_score * 0.6) + (homework_avg * 0.4)
print(f"Base grade: ({exam_score} × 0.6) + ({homework_avg} × 0.4) = {base_grade:.1f}")

# Apply attendance and participation bonuses/penalties
if attendance_rate >= 0.9:  # 90% or better
    print("✓ Excellent attendance (≥90%)")
    
    if participation:
        print("  ✓ Good classroom participation")
        
        if extra_credit > 0:
            print(f"    ✓ Extra credit earned: +{extra_credit} points")
            final_grade = base_grade + extra_credit + 2  # Participation bonus
            print(f"    Final grade: {base_grade:.1f} + {extra_credit} + 2 = {final_grade:.1f}")
        else:
            print("    • No extra credit")
            final_grade = base_grade + 2  # Participation bonus only
            print(f"    Final grade: {base_grade:.1f} + 2 = {final_grade:.1f}")
    else:
        print("  ✗ Poor classroom participation")
        
        if extra_credit > 0:
            print(f"    ✓ Extra credit helps: +{extra_credit} points")
            final_grade = base_grade + extra_credit  # No participation bonus
            print(f"    Final grade: {base_grade:.1f} + {extra_credit} = {final_grade:.1f}")
        else:
            print("    • No extra credit to help")
            final_grade = base_grade  # No bonuses
            print(f"    Final grade: {base_grade:.1f} (no bonuses)")
            
elif attendance_rate >= 0.8:  # 80-89%
    print("⚠ Fair attendance (80-89%)")
    
    if participation:
        print("  ✓ Good participation helps offset attendance")
        final_grade = base_grade + extra_credit + 1  # Reduced bonus
        print(f"    Final grade: {base_grade:.1f} + {extra_credit} + 1 = {final_grade:.1f}")
    else:
        print("  ✗ Poor participation compounds attendance issues")
        final_grade = base_grade + extra_credit - 2  # Penalty applied
        print(f"    Final grade: {base_grade:.1f} + {extra_credit} - 2 = {final_grade:.1f}")
        
else:  # Below 80%
    print("✗ Poor attendance (<80%)")
    print("  Significant grade penalty applied")
    final_grade = base_grade * 0.9 + extra_credit  # 10% penalty
    print(f"    Final grade: ({base_grade:.1f} × 0.9) + {extra_credit} = {final_grade:.1f}")

# Ensure grade doesn't exceed 100
final_grade = min(100, final_grade)

# Determine letter grade using nested conditions
print(f"\nFinal numeric grade: {final_grade:.1f}")

if final_grade >= 90:
    letter_grade = "A"
    if final_grade >= 97:
        performance = "Exceptional"
    elif final_grade >= 94:
        performance = "Excellent"
    else:
        performance = "Very Good"
elif final_grade >= 80:
    letter_grade = "B"
    if final_grade >= 87:
        performance = "Good"
    else:
        performance = "Satisfactory"
elif final_grade >= 70:
    letter_grade = "C"
    if final_grade >= 77:
        performance = "Acceptable"
    else:
        performance = "Below Average"
elif final_grade >= 60:
    letter_grade = "D"
    performance = "Poor"
else:
    letter_grade = "F"
    performance = "Failing"

print(f"Letter grade: {letter_grade}")
print(f"Performance level: {performance}")

print()

# AVOIDING DEEP NESTING
print("=== AVOIDING DEEP NESTING ===")
print()

print("Deep nesting can make code hard to read. Here are better approaches:")
print()

# Example: User registration validation
print("Example: User registration validation")

username = "john_doe"
password = "SecurePass123!"
email = "john@example.com"
age = 25
agreed_terms = True

print(f"Registration attempt:")
print(f"  Username: {username}")
print(f"  Password: [hidden]")
print(f"  Email: {email}")
print(f"  Age: {age}")
print(f"  Agreed to terms: {agreed_terms}")
print()

# BAD: Deep nesting (hard to read)
print("❌ BAD APPROACH: Deep nesting")
print("if username:")
print("    if len(username) >= 3:")
print("        if password:")
print("            if len(password) >= 8:")
print("                if '@' in email:")
print("                    if age >= 13:")
print("                        if agreed_terms:")
print("                            print('Registration successful')")
print("This creates a 'pyramid of doom' - hard to read and maintain!")
print()

# BETTER: Early exit pattern (guard clauses)
print("✅ BETTER APPROACH: Early exit with guard clauses")

def validate_registration():
    # Check each requirement and exit early if failed
    if not username:
        return "❌ Username is required"
    
    if len(username) < 3:
        return "❌ Username must be at least 3 characters"
    
    if not password:
        return "❌ Password is required"
    
    if len(password) < 8:
        return "❌ Password must be at least 8 characters"
    
    if '@' not in email:
        return "❌ Valid email address required"
    
    if age < 13:
        return "❌ Must be at least 13 years old"
    
    if not agreed_terms:
        return "❌ Must agree to terms and conditions"
    
    # All validations passed
    return "✅ Registration successful!"

# Test the validation
result = validate_registration()
print(f"Result: {result}")

print()

# PRACTICAL NESTED CONDITIONS EXAMPLE
print("=== PRACTICAL EXAMPLE: GAME LOGIC ===")
print()

print("Example: RPG character action validation")

# Character stats
character_health = 75
character_mana = 30
character_level = 12
has_weapon = True
weapon_durability = 85
enemy_present = True
enemy_health = 40

print(f"Character status:")
print(f"  Health: {character_health}")
print(f"  Mana: {character_mana}")
print(f"  Level: {character_level}")
print(f"  Has weapon: {has_weapon}")
print(f"  Weapon durability: {weapon_durability}%")
print(f"  Enemy present: {enemy_present}")
print(f"  Enemy health: {enemy_health}")
print()

print("Determining available actions:")

# Combat actions
if enemy_present:
    print("⚔️ Enemy detected - combat options available")
    
    if character_health > 20:  # Healthy enough to fight
        print("  ✓ Character healthy enough for combat")
        
        if has_weapon:
            print("    ✓ Weapon equipped")
            
            if weapon_durability > 10:
                print("      ✓ Weapon in good condition")
                print("      🗡️ MELEE ATTACK available")
                
                if character_level >= 10:
                    print("      ✓ High level - special attacks unlocked")
                    print("      💥 POWER ATTACK available")
            else:
                print("      ✗ Weapon nearly broken")
                print("      🤛 UNARMED ATTACK available (reduced damage)")
        else:
            print("    ✗ No weapon equipped")
            print("    🤛 UNARMED ATTACK available")
            
        # Magic options
        if character_mana >= 20:
            print("    ✓ Sufficient mana for spells")
            print("    ✨ MAGIC ATTACK available")
            
            if character_mana >= 50:
                print("    ✓ High mana - powerful spells available")
                print("    🔥 FIREBALL SPELL available")
    else:
        print("  ✗ Character too injured for combat")
        print("  🏃 RETREAT recommended")
        
        if character_health > 5:
            print("    ⚗️ HEALING POTION option available")
else:
    print("🌳 No enemies - exploration options")
    print("  🚶 MOVE available")
    print("  🔍 SEARCH available")
    
    if character_health < 100:
        print("  💤 REST available (restore health)")
    
    if character_mana < 100:
        print("  🧘 MEDITATE available (restore mana)")

print()

# NESTED CONDITIONS FOR DATA PROCESSING
print("=== NESTED CONDITIONS FOR DATA PROCESSING ===")
print()

print("Example: Processing student records with complex rules")

students = [
    {"name": "Alice", "grade": 95, "attendance": 0.98, "homework_submitted": 15, "total_homework": 15},
    {"name": "Bob", "grade": 82, "attendance": 0.85, "homework_submitted": 12, "total_homework": 15},
    {"name": "Charlie", "grade": 78, "attendance": 0.75, "homework_submitted": 10, "total_homework": 15}
]

print("Processing student records:")

for student in students:
    name = student["name"]
    grade = student["grade"]
    attendance = student["attendance"]
    hw_completion = student["homework_submitted"] / student["total_homework"]
    
    print(f"\n📊 {name}:")
    print(f"   Grade: {grade}")
    print(f"   Attendance: {attendance * 100:.0f}%")
    print(f"   Homework completion: {hw_completion * 100:.0f}%")
    
    # Nested evaluation for awards and warnings
    if grade >= 90:
        print("   🏆 High academic achievement")
        
        if attendance >= 0.95:
            print("     ✅ Perfect attendance bonus")
            
            if hw_completion >= 0.95:
                print("       🌟 DEAN'S LIST - Exceptional student!")
            else:
                print("       📝 Good student - encourage homework completion")
        else:
            print("     ⚠️ Encourage better attendance for dean's list")
            
    elif grade >= 80:
        print("   📚 Good academic standing")
        
        if attendance < 0.85:
            print("     ⚠️ Attendance intervention recommended")
            
        if hw_completion < 0.8:
            print("     📋 Homework support needed")
            
    else:
        print("   🚨 Academic concern - intervention needed")
        
        if attendance < 0.8:
            print("     🔴 CRITICAL: Poor attendance")
            
        if hw_completion < 0.7:
            print("     🔴 CRITICAL: Failing to complete homework")
            
        print("     📞 Schedule parent meeting")

print()

print("=== SUMMARY ===")
print()
print("Nested Conditions Best Practices:")
print("1. Use indentation clearly to show nesting levels")
print("2. Limit nesting depth - prefer early returns/guard clauses")
print("3. Consider logical operators for simple combinations")
print("4. Use nested conditions for step-by-step validation")
print("5. Add comments for complex decision trees")
print("6. Test all possible paths through nested conditions")
print("7. Consider extracting complex logic into functions")

"""
KEY TAKEAWAYS:
==============
1. Nested conditions enable multi-level decision making
2. Inner conditions only execute if outer conditions are true
3. Proper indentation is crucial for readability
4. Avoid "pyramid of doom" - deep nesting is hard to read
5. Consider early exits/guard clauses for cleaner code
6. Use nested vs logical operators based on complexity
7. Test all possible execution paths

WHEN TO USE NESTED CONDITIONS:
==============================
• Step-by-step validation with different responses at each level
• Game logic with multiple state checks
• Complex business rules with hierarchical decisions
• Data processing with multi-level categorization
• User interface flows with conditional options

ALTERNATIVES TO DEEP NESTING:
==============================
• Guard clauses (early returns)
• Logical operators for simple combinations
• Function decomposition
• State machines for complex workflows
• Lookup tables for simple mappings

NEXT STEP:
Go to 06-complete-program.py to see all selection concepts in one comprehensive program!
"""