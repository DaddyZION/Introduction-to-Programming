"""
Assignment 2 - Exercise 3: Nested Decisions
Difficulty: 🟡 Intermediate

TODO: Practice multi-level decision making with nested if statements.

This exercise contains 4 mini-programs to practice nested conditions.
"""

# ==================== PROGRAM 1: University Admission System ====================
"""
TODO: Determine if a student is admitted to a university program.

Requirements:
- Ask for GPA (0.0-4.0) and SAT score (400-1600)
- Automatic admission: GPA >= 3.5 AND SAT >= 1200
- Conditional admission: GPA >= 3.0 AND SAT >= 1000
- If GPA >= 3.0 but SAT < 1000: "Consider retaking SAT"
- Otherwise: Not admitted

Example:
    Enter your GPA: 3.6
    Enter your SAT score: 1250
    Congratulations! You are automatically admitted!
"""

# TODO: Write your code here for Program 1


# ==================== PROGRAM 2: Insurance Premium Calculator ====================
"""
TODO: Calculate insurance premium based on age and driving record.

Requirements:
- Ask for age and number of accidents in past 3 years
- Base premium: $500
- If age < 25:
    - No accidents: add $200
    - 1 accident: add $400
    - 2+ accidents: add $800
- If age >= 25:
    - No accidents: add $0
    - 1 accident: add $150
    - 2+ accidents: add $400
- Display total premium

Example:
    Enter your age: 22
    Number of accidents in past 3 years: 0
    Your insurance premium: $700
"""

# TODO: Write your code here for Program 2


# ==================== PROGRAM 3: Game Character Stats System ====================
"""
TODO: Evaluate a game character's combat effectiveness.

Requirements:
- Ask for strength (1-100) and agility (1-100)
- If strength >= 70:
    - If agility >= 70: "Warrior Elite"
    - Else: "Heavy Fighter"
- Else if strength >= 40:
    - If agility >= 70: "Agile Fighter"
    - Else: "Balanced Fighter"
- Else:
    - If agility >= 70: "Scout"
    - Else: "Novice"

Example:
    Enter strength: 75
    Enter agility: 85
    Character class: Warrior Elite
"""

# TODO: Write your code here for Program 3


# ==================== PROGRAM 4: Medical Diagnosis Helper ====================
"""
TODO: Provide basic health recommendations based on symptoms.

Requirements:
- Ask if they have fever (yes/no) and cough (yes/no)
- If fever:
    - If cough: "See doctor - possible respiratory infection"
    - Else: "Rest and monitor - possible flu"
- Else (no fever):
    - If cough: "Take cough medicine - likely common cold"
    - Else: "No major symptoms detected"

Example:
    Do you have a fever? (yes/no): yes
    Do you have a cough? (yes/no): yes
    Recommendation: See doctor - possible respiratory infection
"""

# TODO: Write your code here for Program 4
