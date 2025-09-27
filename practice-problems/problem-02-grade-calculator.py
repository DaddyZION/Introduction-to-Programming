"""
Practice Problem 02: Grade Calculator System
===========================================

DIFFICULTY: Beginner-Intermediate ⭐⭐
CONCEPTS: Selection, Functions, Data Validation
ASSIGNMENTS: 2 (Selection), 4 (Validation), 5 (Functions)
ESTIMATED TIME: 60-90 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive grade calculation system for students and teachers.
The system should handle multiple assessment types, calculate weighted averages,
determine letter grades, provide statistical analysis, and generate progress reports.

This problem combines conditional logic, input validation, mathematical calculations,
and formatted output to create a practical educational tool.

REQUIREMENTS:
============
1. Support multiple grading schemes (percentage, points, letter grades)
2. Handle different assessment categories (tests, assignments, participation, etc.)
3. Calculate weighted averages based on category importance
4. Convert between different grading systems
5. Provide statistical analysis (mean, median, grade distribution)
6. Generate detailed progress reports
7. Include grade prediction and "what-if" analysis
8. Validate all inputs and handle errors gracefully

LEARNING OBJECTIVES:
===================
- Master conditional logic and decision structures
- Practice input validation techniques
- Implement mathematical calculations and statistics
- Design modular, reusable functions
- Create professional formatted output
- Handle complex data structures and calculations

STARTER CODE:
============
"""

import statistics
from datetime import datetime

class GradeCalculator:
    """Comprehensive grade calculation and analysis system."""
    
    def __init__(self):
        """Initialize the grade calculator with default settings."""
        # Grading scale (can be customized)
        self.grading_scale = {
            'A+': (97, 100), 'A': (93, 96), 'A-': (90, 92),
            'B+': (87, 89), 'B': (83, 86), 'B-': (80, 82),
            'C+': (77, 79), 'C': (73, 76), 'C-': (70, 72),
            'D+': (67, 69), 'D': (63, 66), 'D-': (60, 62),
            'F': (0, 59)
        }
        
        # Assessment categories and their default weights
        self.categories = {
            'tests': 40,           # 40% of final grade
            'assignments': 30,     # 30% of final grade
            'participation': 10,   # 10% of final grade
            'final_exam': 20       # 20% of final grade
        }
        
        # Student data storage
        self.students = {}
    
    def display_main_menu(self):
        """Display the main menu options."""
        print("=" * 60)
        print("             GRADE CALCULATOR SYSTEM")
        print("=" * 60)
        print("1. Add Student")
        print("2. Enter Grades for Student")
        print("3. Calculate Final Grade")
        print("4. Generate Progress Report")
        print("5. Class Statistics")
        print("6. Grade Distribution Analysis")
        print("7. What-If Grade Calculator")
        print("8. Customize Grading Scale")
        print("9. Customize Category Weights")
        print("10. Export Grade Report")
        print("0. Exit")
        print("=" * 60)
    
    def get_menu_choice(self):
        """Get and validate user's menu selection."""
        while True:
            try:
                choice = int(input("Enter your choice (0-10): "))
                if 0 <= choice <= 10:
                    return choice
                else:
                    print("❌ Please enter a number between 0 and 10.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def add_student(self):
        """Add a new student to the system."""
        print("\n👨‍🎓 ADD NEW STUDENT")
        print("-" * 30)
        
        while True:
            student_id = input("Enter Student ID: ").strip()
            if student_id:
                if student_id not in self.students:
                    break
                else:
                    print("❌ Student ID already exists! Please use a different ID.")
            else:
                print("❌ Student ID cannot be empty!")
        
        student_name = input("Enter Student Name: ").strip()
        while not student_name:
            print("❌ Student name cannot be empty!")
            student_name = input("Enter Student Name: ").strip()
        
        # Initialize student record
        self.students[student_id] = {
            'name': student_name,
            'grades': {category: [] for category in self.categories},
            'final_grade': None,
            'letter_grade': None,
            'created_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        print(f"✅ Student '{student_name}' (ID: {student_id}) added successfully!")
    
    def enter_grades(self):
        """Enter grades for a specific student."""
        if not self.students:
            print("❌ No students in the system. Please add a student first.")
            return
        
        print("\n📝 ENTER GRADES")
        print("-" * 20)
        
        # Display available students
        print("Available Students:")
        for student_id, student_data in self.students.items():
            print(f"  {student_id}: {student_data['name']}")
        
        student_id = input("\nEnter Student ID: ").strip()
        if student_id not in self.students:
            print("❌ Student not found!")
            return
        
        student = self.students[student_id]
        print(f"\nEntering grades for: {student['name']}")
        
        # Display categories
        print("\nAvailable Categories:")
        for i, (category, weight) in enumerate(self.categories.items(), 1):
            print(f"  {i}. {category.replace('_', ' ').title()} (Weight: {weight}%)")
        
        try:
            choice = int(input("\nSelect category (1-{}): ".format(len(self.categories))))
            if 1 <= choice <= len(self.categories):
                category = list(self.categories.keys())[choice - 1]
            else:
                print("❌ Invalid category selection!")
                return
        except ValueError:
            print("❌ Please enter a valid number!")
            return
        
        # Enter grade
        grade = self.get_valid_grade("Enter grade (0-100): ")
        if grade is not None:
            student['grades'][category].append(grade)
            print(f"✅ Grade {grade} added to {category.replace('_', ' ').title()}")
            
            # Show current grades in this category
            grades_in_category = student['grades'][category]
            if len(grades_in_category) > 1:
                avg = sum(grades_in_category) / len(grades_in_category)
                print(f"📊 Current average in {category.replace('_', ' ').title()}: {avg:.1f}")
    
    def get_valid_grade(self, prompt):
        """Get a valid grade from user input."""
        while True:
            try:
                grade = float(input(prompt))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("❌ Grade must be between 0 and 100!")
            except ValueError:
                print("❌ Please enter a valid number!")
                retry = input("Try again? (y/n): ").lower()
                if retry != 'y':
                    return None
    
    def calculate_final_grade(self):
        """Calculate final grade for a student."""
        if not self.students:
            print("❌ No students in the system.")
            return
        
        print("\n🧮 CALCULATE FINAL GRADE")
        print("-" * 25)
        
        # Display available students
        print("Available Students:")
        for student_id, student_data in self.students.items():
            print(f"  {student_id}: {student_data['name']}")
        
        student_id = input("\nEnter Student ID: ").strip()
        if student_id not in self.students:
            print("❌ Student not found!")
            return
        
        student = self.students[student_id]
        print(f"\nCalculating final grade for: {student['name']}")
        print("-" * 40)
        
        total_weighted_score = 0
        total_weight = 0
        category_details = []
        
        for category, weight in self.categories.items():
            grades = student['grades'][category]
            if grades:
                category_average = sum(grades) / len(grades)
                weighted_score = category_average * weight / 100
                total_weighted_score += weighted_score
                total_weight += weight
                
                category_details.append({
                    'category': category,
                    'grades': grades,
                    'average': category_average,
                    'weight': weight,
                    'weighted_score': weighted_score
                })
                
                print(f"{category.replace('_', ' ').title():<15}: {category_average:6.1f}% "
                      f"(Weight: {weight:2d}%, Contribution: {weighted_score:5.2f})")
        
        if total_weight == 0:
            print("❌ No grades entered for this student!")
            return
        
        # Calculate final grade
        if total_weight < 100:
            print(f"\n⚠️  Warning: Only {total_weight}% of total weight has grades entered.")
            final_grade = total_weighted_score * 100 / total_weight
        else:
            final_grade = total_weighted_score
        
        letter_grade = self.get_letter_grade(final_grade)
        
        # Store results
        student['final_grade'] = final_grade
        student['letter_grade'] = letter_grade
        
        print("-" * 40)
        print(f"FINAL GRADE: {final_grade:.2f}% ({letter_grade})")
        
        # Show grade analysis
        self.show_grade_analysis(final_grade, letter_grade)
    
    def get_letter_grade(self, percentage):
        """Convert percentage to letter grade."""
        for letter, (min_score, max_score) in self.grading_scale.items():
            if min_score <= percentage <= max_score:
                return letter
        return 'F'  # Default fallback
    
    def show_grade_analysis(self, grade, letter_grade):
        """Show detailed analysis of the grade."""
        print("\n📊 GRADE ANALYSIS")
        print("-" * 20)
        
        # Grade interpretation
        if grade >= 90:
            performance = "Excellent"
            emoji = "🏆"
        elif grade >= 80:
            performance = "Good"
            emoji = "👍"
        elif grade >= 70:
            performance = "Satisfactory"
            emoji = "👌"
        elif grade >= 60:
            performance = "Needs Improvement"
            emoji = "📈"
        else:
            performance = "Failing"
            emoji = "⚠️"
        
        print(f"{emoji} Performance Level: {performance}")
        
        # Distance from grade boundaries
        current_range = None
        for letter, (min_score, max_score) in self.grading_scale.items():
            if min_score <= grade <= max_score:
                current_range = (letter, min_score, max_score)
                break
        
        if current_range:
            letter, min_score, max_score = current_range
            if letter != 'A+':  # Not the highest grade
                # Find next higher grade
                grade_letters = list(self.grading_scale.keys())
                current_index = grade_letters.index(letter)
                if current_index > 0:
                    next_grade = grade_letters[current_index - 1]
                    next_min = self.grading_scale[next_grade][0]
                    points_needed = next_min - grade
                    print(f"📈 Points needed for {next_grade}: {points_needed:.1f}")
    
    def generate_progress_report(self):
        """Generate a comprehensive progress report for a student."""
        if not self.students:
            print("❌ No students in the system.")
            return
        
        print("\n📋 GENERATE PROGRESS REPORT")
        print("-" * 30)
        
        # Display available students
        print("Available Students:")
        for student_id, student_data in self.students.items():
            print(f"  {student_id}: {student_data['name']}")
        
        student_id = input("\nEnter Student ID: ").strip()
        if student_id not in self.students:
            print("❌ Student not found!")
            return
        
        student = self.students[student_id]
        
        print("\n" + "=" * 60)
        print(f"           PROGRESS REPORT")
        print(f"           {student['name']} (ID: {student_id})")
        print("=" * 60)
        
        # Report generation date
        print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Student Added: {student['created_date']}")
        print()
        
        # Detailed breakdown by category
        print("DETAILED BREAKDOWN BY CATEGORY")
        print("-" * 40)
        
        all_grades = []
        for category, weight in self.categories.items():
            grades = student['grades'][category]
            print(f"\n{category.replace('_', ' ').title()} (Weight: {weight}%):")
            
            if grades:
                print(f"  Grades: {', '.join(map(str, grades))}")
                category_avg = sum(grades) / len(grades)
                print(f"  Average: {category_avg:.1f}%")
                print(f"  Count: {len(grades)} grade(s)")
                
                # Grade trend (if multiple grades)
                if len(grades) > 1:
                    if grades[-1] > grades[0]:
                        trend = "Improving 📈"
                    elif grades[-1] < grades[0]:
                        trend = "Declining 📉"
                    else:
                        trend = "Stable ➡️"
                    print(f"  Trend: {trend}")
                
                all_grades.extend(grades)
            else:
                print("  No grades entered")
        
        # Overall statistics
        if all_grades:
            print("\n" + "=" * 40)
            print("OVERALL STATISTICS")
            print("=" * 40)
            print(f"Total Grades Entered: {len(all_grades)}")
            print(f"Highest Grade: {max(all_grades):.1f}%")
            print(f"Lowest Grade: {min(all_grades):.1f}%")
            print(f"Average of All Grades: {statistics.mean(all_grades):.1f}%")
            if len(all_grades) > 1:
                print(f"Standard Deviation: {statistics.stdev(all_grades):.1f}")
        
        # Final grade summary
        if student['final_grade'] is not None:
            print("\n" + "=" * 40)
            print("FINAL GRADE SUMMARY")
            print("=" * 40)
            print(f"Final Grade: {student['final_grade']:.2f}%")
            print(f"Letter Grade: {student['letter_grade']}")
        
        print("\n" + "=" * 60)
        print("           END OF REPORT")
        print("=" * 60)
    
    def class_statistics(self):
        """Display statistics for the entire class."""
        if not self.students:
            print("❌ No students in the system.")
            return
        
        print("\n📊 CLASS STATISTICS")
        print("-" * 25)
        
        # Collect all final grades
        final_grades = []
        students_with_grades = 0
        
        for student_data in self.students.values():
            if student_data['final_grade'] is not None:
                final_grades.append(student_data['final_grade'])
                students_with_grades += 1
        
        if not final_grades:
            print("❌ No students have calculated final grades yet.")
            return
        
        # Basic statistics
        print(f"Total Students: {len(self.students)}")
        print(f"Students with Final Grades: {students_with_grades}")
        print()
        
        print("FINAL GRADE STATISTICS")
        print("-" * 25)
        print(f"Highest Grade: {max(final_grades):.1f}%")
        print(f"Lowest Grade: {min(final_grades):.1f}%")
        print(f"Class Average: {statistics.mean(final_grades):.1f}%")
        print(f"Median Grade: {statistics.median(final_grades):.1f}%")
        
        if len(final_grades) > 1:
            print(f"Standard Deviation: {statistics.stdev(final_grades):.1f}")
        
        # Grade distribution
        print("\nGRADE DISTRIBUTION")
        print("-" * 20)
        
        grade_counts = {}
        for grade in final_grades:
            letter = self.get_letter_grade(grade)
            grade_counts[letter] = grade_counts.get(letter, 0) + 1
        
        for letter in self.grading_scale.keys():
            count = grade_counts.get(letter, 0)
            percentage = (count / len(final_grades)) * 100 if final_grades else 0
            bar = "█" * int(percentage / 5)  # Visual bar
            print(f"{letter:2s}: {count:2d} students ({percentage:4.1f}%) {bar}")
    
    def grade_distribution_analysis(self):
        """Provide detailed grade distribution analysis."""
        if not self.students:
            print("❌ No students in the system.")
            return
        
        print("\n📈 GRADE DISTRIBUTION ANALYSIS")
        print("-" * 35)
        
        # Collect data for each category
        category_stats = {}
        
        for category in self.categories:
            all_grades_in_category = []
            for student_data in self.students.values():
                grades = student_data['grades'][category]
                all_grades_in_category.extend(grades)
            
            if all_grades_in_category:
                category_stats[category] = {
                    'grades': all_grades_in_category,
                    'count': len(all_grades_in_category),
                    'average': statistics.mean(all_grades_in_category),
                    'median': statistics.median(all_grades_in_category),
                    'std_dev': statistics.stdev(all_grades_in_category) if len(all_grades_in_category) > 1 else 0
                }
        
        # Display analysis
        for category, stats in category_stats.items():
            print(f"\n{category.replace('_', ' ').title()}:")
            print(f"  Total Grades: {stats['count']}")
            print(f"  Average: {stats['average']:.1f}%")
            print(f"  Median: {stats['median']:.1f}%")
            print(f"  Std Deviation: {stats['std_dev']:.1f}")
            
            # Performance analysis
            high_performers = sum(1 for grade in stats['grades'] if grade >= 90)
            struggling = sum(1 for grade in stats['grades'] if grade < 70)
            
            print(f"  High Performers (≥90%): {high_performers} ({high_performers/stats['count']*100:.1f}%)")
            print(f"  Struggling (<70%): {struggling} ({struggling/stats['count']*100:.1f}%)")
    
    def what_if_calculator(self):
        """Calculate what grade is needed to achieve a target final grade."""
        if not self.students:
            print("❌ No students in the system.")
            return
        
        print("\n🎯 WHAT-IF GRADE CALCULATOR")
        print("-" * 30)
        
        # Display available students
        print("Available Students:")
        for student_id, student_data in self.students.items():
            print(f"  {student_id}: {student_data['name']}")
        
        student_id = input("\nEnter Student ID: ").strip()
        if student_id not in self.students:
            print("❌ Student not found!")
            return
        
        student = self.students[student_id]
        
        # Get target grade
        target_grade = self.get_valid_grade("Enter target final grade (0-100): ")
        if target_grade is None:
            return
        
        print(f"\nAnalyzing what's needed to achieve {target_grade}% final grade...")
        print("-" * 50)
        
        # Calculate current weighted score
        current_weighted_score = 0
        current_weight = 0
        remaining_categories = []
        
        for category, weight in self.categories.items():
            grades = student['grades'][category]
            if grades:
                category_average = sum(grades) / len(grades)
                weighted_score = category_average * weight / 100
                current_weighted_score += weighted_score
                current_weight += weight
                print(f"{category.replace('_', ' ').title()}: {category_average:.1f}% (completed)")
            else:
                remaining_categories.append((category, weight))
                print(f"{category.replace('_', ' ').title()}: Not completed yet")
        
        if not remaining_categories:
            print("\n❌ All categories have grades. Final grade is already determined.")
            current_final = current_weighted_score
            print(f"Current final grade: {current_final:.2f}%")
            return
        
        # Calculate what's needed
        remaining_weight = sum(weight for _, weight in remaining_categories)
        needed_weighted_score = target_grade - current_weighted_score
        
        print(f"\nCURRENT STATUS:")
        print(f"Current weighted score: {current_weighted_score:.2f}")
        print(f"Remaining weight: {remaining_weight}%")
        print(f"Needed weighted score from remaining categories: {needed_weighted_score:.2f}")
        
        if remaining_weight == 0:
            print("❌ No remaining categories to improve grade!")
        elif needed_weighted_score <= 0:
            print("✅ Target grade already achieved!")
        elif needed_weighted_score > remaining_weight:
            print("❌ Target grade is impossible to achieve!")
            max_possible = current_weighted_score + remaining_weight
            print(f"Maximum possible final grade: {max_possible:.2f}%")
        else:
            # Calculate required average
            required_average = (needed_weighted_score / remaining_weight) * 100
            print(f"\nREQUIRED PERFORMANCE:")
            print(f"Average needed in remaining categories: {required_average:.1f}%")
            
            if required_average > 100:
                print("❌ Required average is above 100%! Target is impossible.")
            elif required_average < 0:
                print("✅ Target is easily achievable!")
            else:
                difficulty = ""
                if required_average >= 95:
                    difficulty = "(Very Challenging) 🔥"
                elif required_average >= 85:
                    difficulty = "(Challenging) 💪"
                elif required_average >= 75:
                    difficulty = "(Achievable) 👍"
                else:
                    difficulty = "(Easily Achievable) 😊"
                
                print(f"Difficulty Assessment: {difficulty}")
    
    def customize_grading_scale(self):
        """Allow customization of the grading scale."""
        print("\n⚙️  CUSTOMIZE GRADING SCALE")
        print("-" * 30)
        
        print("Current Grading Scale:")
        for letter, (min_score, max_score) in self.grading_scale.items():
            print(f"  {letter}: {min_score}-{max_score}%")
        
        print("\nWould you like to:")
        print("1. Use standard 10-point scale (90-100=A, 80-89=B, etc.)")
        print("2. Use standard 7-point scale (93-100=A, 85-92=B, etc.)")
        print("3. Keep current scale")
        
        try:
            choice = int(input("Enter choice (1-3): "))
            
            if choice == 1:
                # 10-point scale
                self.grading_scale = {
                    'A': (90, 100), 'B': (80, 89), 'C': (70, 79),
                    'D': (60, 69), 'F': (0, 59)
                }
                print("✅ Switched to 10-point grading scale!")
            
            elif choice == 2:
                # 7-point scale
                self.grading_scale = {
                    'A': (93, 100), 'B': (85, 92), 'C': (77, 84),
                    'D': (70, 76), 'F': (0, 69)
                }
                print("✅ Switched to 7-point grading scale!")
            
            elif choice == 3:
                print("✅ Keeping current grading scale.")
            
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def customize_category_weights(self):
        """Allow customization of category weights."""
        print("\n⚙️  CUSTOMIZE CATEGORY WEIGHTS")
        print("-" * 35)
        
        print("Current Category Weights:")
        for category, weight in self.categories.items():
            print(f"  {category.replace('_', ' ').title()}: {weight}%")
        
        total_current = sum(self.categories.values())
        print(f"\nTotal Weight: {total_current}%")
        
        if total_current != 100:
            print("⚠️  Warning: Weights don't add up to 100%!")
        
        print("\nEnter new weights (must total 100%):")
        new_weights = {}
        total_new = 0
        
        for category in self.categories:
            while True:
                try:
                    weight = float(input(f"{category.replace('_', ' ').title()}: "))
                    if 0 <= weight <= 100:
                        new_weights[category] = weight
                        total_new += weight
                        break
                    else:
                        print("❌ Weight must be between 0 and 100!")
                except ValueError:
                    print("❌ Please enter a valid number!")
        
        if abs(total_new - 100) < 0.01:  # Allow for small floating point errors
            self.categories = new_weights
            print("✅ Category weights updated successfully!")
        else:
            print(f"❌ Weights total {total_new}%, must total 100%!")
            print("Changes not saved.")
    
    def export_grade_report(self):
        """Export grade reports to a text file."""
        if not self.students:
            print("❌ No students in the system.")
            return
        
        print("\n💾 EXPORT GRADE REPORT")
        print("-" * 25)
        
        filename = f"grade_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(filename, 'w') as file:
                file.write("GRADE CALCULATOR SYSTEM - EXPORT REPORT\n")
                file.write("=" * 60 + "\n")
                file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total Students: {len(self.students)}\n\n")
                
                # Grading scale
                file.write("GRADING SCALE:\n")
                file.write("-" * 15 + "\n")
                for letter, (min_score, max_score) in self.grading_scale.items():
                    file.write(f"{letter}: {min_score}-{max_score}%\n")
                file.write("\n")
                
                # Category weights
                file.write("CATEGORY WEIGHTS:\n")
                file.write("-" * 20 + "\n")
                for category, weight in self.categories.items():
                    file.write(f"{category.replace('_', ' ').title()}: {weight}%\n")
                file.write("\n")
                
                # Individual student reports
                for student_id, student_data in self.students.items():
                    file.write("=" * 60 + "\n")
                    file.write(f"STUDENT: {student_data['name']} (ID: {student_id})\n")
                    file.write("=" * 60 + "\n")
                    
                    for category, weight in self.categories.items():
                        grades = student_data['grades'][category]
                        file.write(f"\n{category.replace('_', ' ').title()} (Weight: {weight}%):\n")
                        if grades:
                            file.write(f"  Grades: {', '.join(map(str, grades))}\n")
                            avg = sum(grades) / len(grades)
                            file.write(f"  Average: {avg:.1f}%\n")
                        else:
                            file.write("  No grades entered\n")
                    
                    if student_data['final_grade'] is not None:
                        file.write(f"\nFINAL GRADE: {student_data['final_grade']:.2f}% ({student_data['letter_grade']})\n")
                    
                    file.write("\n")
            
            print(f"✅ Grade report exported to: {filename}")
        
        except IOError:
            print("❌ Error writing to file!")
    
    def run(self):
        """Main program loop."""
        print("🎓 Welcome to the Grade Calculator System!")
        print("This comprehensive tool helps calculate and analyze student grades.")
        
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n👋 Thank you for using the Grade Calculator System!")
                break
            elif choice == 1:
                self.add_student()
            elif choice == 2:
                self.enter_grades()
            elif choice == 3:
                self.calculate_final_grade()
            elif choice == 4:
                self.generate_progress_report()
            elif choice == 5:
                self.class_statistics()
            elif choice == 6:
                self.grade_distribution_analysis()
            elif choice == 7:
                self.what_if_calculator()
            elif choice == 8:
                self.customize_grading_scale()
            elif choice == 9:
                self.customize_category_weights()
            elif choice == 10:
                self.export_grade_report()
            
            print("\n" + "=" * 60)
            input("Press Enter to continue...")

def main():
    """Main entry point for the program."""
    calculator = GradeCalculator()
    calculator.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Complete class-based design with all methods implemented
2. ✅ Proper input validation for all user inputs
3. ✅ Mathematical accuracy in grade calculations
4. ✅ Comprehensive error handling
5. ✅ Professional formatted reports
6. ✅ Statistical analysis capabilities
7. ✅ File export functionality
8. ✅ Customizable grading schemes

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Complex conditional logic and decision making
• Input validation and error handling techniques
• Mathematical calculations and statistical analysis  
• Object-oriented programming principles
• File handling and data export
• Professional report generation
• User interface design
• Data management and organization

EXTENSION IDEAS:
===============
1. Add database storage for persistent data
2. Implement grade curves and scaling
3. Add assignment due dates and late penalties
4. Create graphical grade trends
5. Implement grade import from CSV files
6. Add email report functionality
7. Create web interface
8. Add grade prediction using machine learning

This problem provides excellent practice with conditional logic,
data validation, mathematical calculations, and professional
software design principles!
"""