"""
Practice Problem 03: Password Security Analyzer
===============================================

DIFFICULTY: Intermediate ⭐⭐
CONCEPTS: Strings, Validation, Security, Functions
ASSIGNMENTS: 4 (Validation), 5 (Functions), 6 (Strings)
ESTIMATED TIME: 60-75 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive password security analysis system that evaluates password
strength, provides security recommendations, and helps users create strong passwords.
The system should analyze various aspects of password security including length,
character variety, common patterns, and dictionary attacks.

This problem combines string processing, security concepts, validation techniques,
and user-friendly feedback to create a practical cybersecurity tool.

REQUIREMENTS:
============
1. Analyze password strength using multiple criteria
2. Check against common passwords and dictionary words
3. Detect common patterns and weaknesses
4. Generate secure password suggestions
5. Provide detailed security recommendations
6. Calculate estimated crack times
7. Support different security levels (basic, standard, high)
8. Include a password generation tool with customizable options

LEARNING OBJECTIVES:
===================
- Master string processing and analysis techniques
- Understand cybersecurity principles and best practices
- Practice complex validation logic
- Implement pattern recognition algorithms
- Design user-friendly feedback systems
- Work with character sets and encoding

STARTER CODE:
============
"""

import random
import string
import math
import re
from datetime import timedelta

class PasswordAnalyzer:
    """Comprehensive password security analysis and generation system."""
    
    def __init__(self):
        """Initialize the password analyzer with security rules and data."""
        
        # Common passwords (top 100 most common - partial list)
        self.common_passwords = {
            '123456', 'password', '123456789', '12345678', '12345', '1234567',
            'qwerty', 'abc123', '111111', 'dragon', 'master', 'monkey',
            'letmein', 'login', 'princess', 'qwertyuiop', 'solo', 'passw0rd',
            'starwars', 'hello', 'welcome', 'admin', 'iloveyou', 'football',
            'baseball', 'basketball', 'superman', 'batman', 'trustno1',
            'shadow', 'michael', 'jennifer', 'jordan', 'michelle', 'daniel',
            'anthony', 'lisa', 'ronald', 'kimberly', 'david', 'jessica',
            'sunshine', 'ashley', '123123', '654321', 'jesus', 'password1',
            'superman', 'hello123', 'charlie', 'aa123456', 'donald', 'password123'
        }
        
        # Common patterns to detect
        self.keyboard_patterns = [
            'qwerty', 'qwertyuiop', 'asdf', 'asdfgh', 'asdfghjkl',
            'zxcv', 'zxcvbn', 'zxcvbnm', '1234', '12345', '123456',
            '1234567890', 'abcd', 'abcdef', 'abcdefgh'
        ]
        
        # Character sets
        self.lowercase = set(string.ascii_lowercase)
        self.uppercase = set(string.ascii_uppercase)
        self.digits = set(string.digits)
        self.special_chars = set('!@#$%^&*()_+-=[]{}|;:,.<>?')
        
        # Security level requirements
        self.security_levels = {
            'basic': {
                'min_length': 8,
                'required_sets': 2,  # At least 2 different character types
                'max_common_patterns': 2,
                'description': 'Basic security for low-risk accounts'
            },
            'standard': {
                'min_length': 12,
                'required_sets': 3,
                'max_common_patterns': 1,
                'description': 'Standard security for most accounts'
            },
            'high': {
                'min_length': 16,
                'required_sets': 4,
                'max_common_patterns': 0,
                'description': 'High security for sensitive accounts'
            }
        }
    
    def display_main_menu(self):
        """Display the main menu options."""
        print("=" * 60)
        print("           PASSWORD SECURITY ANALYZER")
        print("=" * 60)
        print("1. Analyze Password Strength")
        print("2. Generate Secure Password")
        print("3. Compare Multiple Passwords") 
        print("4. Security Education Center")
        print("5. Batch Password Analysis")
        print("6. Password Policy Creator")
        print("7. Security Tips & Best Practices")
        print("0. Exit")
        print("=" * 60)
    
    def get_menu_choice(self):
        """Get and validate user's menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (0-7): "))
                if 0 <= choice <= 7:
                    return choice
                else:
                    print("❌ Please enter a number between 0 and 7.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def get_password_securely(self, prompt="Enter password: "):
        """Get password input (visible for analysis purposes)."""
        print("⚠️  Note: Password will be visible on screen for analysis")
        password = input(prompt).strip()
        return password
    
    def analyze_password_strength(self):
        """Analyze and display comprehensive password strength analysis."""
        print("\n🔍 PASSWORD STRENGTH ANALYZER")
        print("-" * 35)
        
        password = self.get_password_securely()
        if not password:
            print("❌ Password cannot be empty!")
            return
        
        print(f"\nAnalyzing password: {'*' * len(password)} (length: {len(password)})")
        print("=" * 50)
        
        # Perform comprehensive analysis
        analysis = self.perform_full_analysis(password)
        
        # Display results
        self.display_analysis_results(analysis)
    
    def perform_full_analysis(self, password):
        """Perform comprehensive password analysis."""
        analysis = {
            'password': password,
            'length': len(password),
            'character_analysis': self.analyze_characters(password),
            'pattern_analysis': self.analyze_patterns(password),
            'common_password_check': self.check_common_passwords(password),
            'entropy': self.calculate_entropy(password),
            'crack_time': self.estimate_crack_time(password),
            'strength_score': 0,
            'security_level': 'weak',
            'recommendations': []
        }
        
        # Calculate overall strength score
        analysis['strength_score'] = self.calculate_strength_score(analysis)
        analysis['security_level'] = self.determine_security_level(analysis['strength_score'])
        analysis['recommendations'] = self.generate_recommendations(analysis)
        
        return analysis
    
    def analyze_characters(self, password):
        """Analyze character composition of password."""
        char_analysis = {
            'lowercase_count': sum(1 for c in password if c in self.lowercase),
            'uppercase_count': sum(1 for c in password if c in self.uppercase),
            'digit_count': sum(1 for c in password if c in self.digits),
            'special_count': sum(1 for c in password if c in self.special_chars),
            'unique_chars': len(set(password)),
            'repeated_chars': len(password) - len(set(password)),
            'character_sets_used': 0
        }
        
        # Count character set variety
        if char_analysis['lowercase_count'] > 0:
            char_analysis['character_sets_used'] += 1
        if char_analysis['uppercase_count'] > 0:
            char_analysis['character_sets_used'] += 1
        if char_analysis['digit_count'] > 0:
            char_analysis['character_sets_used'] += 1
        if char_analysis['special_count'] > 0:
            char_analysis['character_sets_used'] += 1
        
        return char_analysis
    
    def analyze_patterns(self, password):
        """Analyze password for common patterns and weaknesses."""
        password_lower = password.lower()
        patterns = {
            'keyboard_patterns': [],
            'repeated_sequences': [],
            'sequential_numbers': False,
            'sequential_letters': False,
            'common_substitutions': [],
            'year_patterns': [],
            'simple_patterns': []
        }
        
        # Check for keyboard patterns
        for pattern in self.keyboard_patterns:
            if pattern in password_lower:
                patterns['keyboard_patterns'].append(pattern)
        
        # Check for repeated sequences
        for i in range(len(password) - 2):
            sequence = password[i:i+3]
            if len(set(sequence)) == 1:  # All same character
                patterns['repeated_sequences'].append(sequence)
        
        # Check for sequential numbers
        for i in range(len(password) - 2):
            if password[i:i+3].isdigit():
                nums = [int(password[i+j]) for j in range(3)]
                if nums[1] == nums[0] + 1 and nums[2] == nums[1] + 1:
                    patterns['sequential_numbers'] = True
                    break
        
        # Check for sequential letters
        for i in range(len(password) - 2):
            if password[i:i+3].isalpha():
                letters = password[i:i+3].lower()
                if ord(letters[1]) == ord(letters[0]) + 1 and ord(letters[2]) == ord(letters[1]) + 1:
                    patterns['sequential_letters'] = True
                    break
        
        # Check for year patterns (1900-2030)
        year_matches = re.findall(r'\b(19|20)\d{2}\b', password)
        patterns['year_patterns'] = year_matches
        
        # Check for common substitutions (e.g., @ for a, 3 for e, 0 for o, 1 for i)
        substitutions = {'@': 'a', '3': 'e', '0': 'o', '1': 'i', '5': 's', '7': 't'}
        for sub_char, orig_char in substitutions.items():
            if sub_char in password:
                patterns['common_substitutions'].append(f"{sub_char} for {orig_char}")
        
        return patterns
    
    def check_common_passwords(self, password):
        """Check if password is in common passwords list."""
        password_lower = password.lower()
        
        # Direct match
        if password_lower in self.common_passwords:
            return {'is_common': True, 'type': 'exact_match'}
        
        # Check with simple modifications (very basic)
        variations = [
            password_lower + '1',
            password_lower + '123',
            '123' + password_lower,
            password_lower + '!',
        ]
        
        for variation in variations:
            if variation in self.common_passwords:
                return {'is_common': True, 'type': 'simple_variation'}
        
        return {'is_common': False, 'type': 'unique'}
    
    def calculate_entropy(self, password):
        """Calculate password entropy (bits of randomness)."""
        charset_size = 0
        
        # Determine character set size
        if any(c in self.lowercase for c in password):
            charset_size += 26
        if any(c in self.uppercase for c in password):
            charset_size += 26
        if any(c in self.digits for c in password):
            charset_size += 10
        if any(c in self.special_chars for c in password):
            charset_size += len(self.special_chars)
        
        if charset_size == 0:
            return 0
        
        # Entropy = log2(charset_size) * password_length
        entropy = math.log2(charset_size) * len(password)
        return entropy
    
    def estimate_crack_time(self, password):
        """Estimate time to crack password using brute force."""
        entropy = self.calculate_entropy(password)
        
        # Assume 1 billion guesses per second (modern hardware)
        guesses_per_second = 1_000_000_000
        
        # Total possible combinations
        total_combinations = 2 ** entropy
        
        # Average time to crack (half the search space)
        seconds_to_crack = total_combinations / (2 * guesses_per_second)
        
        # Convert to human-readable format
        if seconds_to_crack < 60:
            return f"{seconds_to_crack:.1f} seconds"
        elif seconds_to_crack < 3600:
            return f"{seconds_to_crack/60:.1f} minutes"
        elif seconds_to_crack < 86400:
            return f"{seconds_to_crack/3600:.1f} hours"
        elif seconds_to_crack < 31536000:
            return f"{seconds_to_crack/86400:.1f} days"
        elif seconds_to_crack < 31536000000:
            return f"{seconds_to_crack/31536000:.1f} years"
        else:
            return f"{seconds_to_crack/31536000:.0e} years"
    
    def calculate_strength_score(self, analysis):
        """Calculate overall password strength score (0-100)."""
        score = 0
        password = analysis['password']
        char_analysis = analysis['character_analysis']
        pattern_analysis = analysis['pattern_analysis']
        common_check = analysis['common_password_check']
        
        # Length scoring (0-25 points)
        if len(password) >= 16:
            score += 25
        elif len(password) >= 12:
            score += 20
        elif len(password) >= 8:
            score += 15
        elif len(password) >= 6:
            score += 10
        else:
            score += 5
        
        # Character variety (0-25 points)
        score += char_analysis['character_sets_used'] * 6
        if char_analysis['unique_chars'] / len(password) > 0.8:
            score += 5  # Bonus for high character uniqueness
        
        # Pattern analysis (0-25 points)
        pattern_penalties = 0
        if pattern_analysis['keyboard_patterns']:
            pattern_penalties += 10
        if pattern_analysis['sequential_numbers'] or pattern_analysis['sequential_letters']:
            pattern_penalties += 8
        if pattern_analysis['repeated_sequences']:
            pattern_penalties += 5
        if pattern_analysis['year_patterns']:
            pattern_penalties += 3
        
        score += max(0, 25 - pattern_penalties)
        
        # Common password check (0-25 points)
        if common_check['is_common']:
            if common_check['type'] == 'exact_match':
                score += 0  # No points for common passwords
            else:
                score += 5  # Slight credit for variation
        else:
            score += 25
        
        return min(100, max(0, score))
    
    def determine_security_level(self, score):
        """Determine security level based on score."""
        if score >= 80:
            return 'very_strong'
        elif score >= 65:
            return 'strong'
        elif score >= 45:
            return 'moderate'
        elif score >= 25:
            return 'weak'
        else:
            return 'very_weak'
    
    def generate_recommendations(self, analysis):
        """Generate personalized recommendations for password improvement."""
        recommendations = []
        password = analysis['password']
        char_analysis = analysis['character_analysis']
        pattern_analysis = analysis['pattern_analysis']
        common_check = analysis['common_password_check']
        
        # Length recommendations
        if len(password) < 8:
            recommendations.append("📏 Use at least 8 characters (12+ recommended)")
        elif len(password) < 12:
            recommendations.append("📏 Consider using 12+ characters for better security")
        
        # Character variety recommendations
        if char_analysis['character_sets_used'] < 3:
            missing = []
            if char_analysis['lowercase_count'] == 0:
                missing.append("lowercase letters")
            if char_analysis['uppercase_count'] == 0:
                missing.append("uppercase letters")
            if char_analysis['digit_count'] == 0:
                missing.append("numbers")
            if char_analysis['special_count'] == 0:
                missing.append("special characters (!@#$%^&*)")
            
            recommendations.append(f"🔤 Add {', '.join(missing)}")
        
        # Pattern recommendations
        if pattern_analysis['keyboard_patterns']:
            recommendations.append("⌨️ Avoid keyboard patterns like 'qwerty' or '123456'")
        
        if pattern_analysis['sequential_numbers'] or pattern_analysis['sequential_letters']:
            recommendations.append("🔢 Avoid sequential characters (abc, 123, etc.)")
        
        if pattern_analysis['repeated_sequences']:
            recommendations.append("🔁 Avoid repeated characters or sequences")
        
        if pattern_analysis['year_patterns']:
            recommendations.append("📅 Avoid using years or dates")
        
        # Common password recommendations
        if common_check['is_common']:
            recommendations.append("🚫 This is a commonly used password - choose something unique")
        
        # Positive recommendations
        recommendations.append("💡 Use a passphrase with random words")
        recommendations.append("🔐 Consider using a password manager")
        recommendations.append("🔄 Enable two-factor authentication when available")
        
        return recommendations[:6]  # Limit to top 6 recommendations
    
    def display_analysis_results(self, analysis):
        """Display comprehensive analysis results."""
        password = analysis['password']
        char_analysis = analysis['character_analysis']
        pattern_analysis = analysis['pattern_analysis']
        common_check = analysis['common_password_check']
        
        # Overall strength display
        score = analysis['strength_score']
        level = analysis['security_level']
        
        print("🛡️  OVERALL STRENGTH")
        print("-" * 25)
        
        # Visual strength bar
        filled = int(score / 10)
        bar = "█" * filled + "░" * (10 - filled)
        
        level_colors = {
            'very_weak': '🔴',
            'weak': '🟠', 
            'moderate': '🟡',
            'strong': '🟢',
            'very_strong': '💚'
        }
        
        level_names = {
            'very_weak': 'Very Weak',
            'weak': 'Weak',
            'moderate': 'Moderate', 
            'strong': 'Strong',
            'very_strong': 'Very Strong'
        }
        
        print(f"Score: {score}/100 [{bar}]")
        print(f"Level: {level_colors[level]} {level_names[level]}")
        print(f"Entropy: {analysis['entropy']:.1f} bits")
        print(f"Estimated crack time: {analysis['crack_time']}")
        
        # Character analysis
        print(f"\n📊 CHARACTER ANALYSIS")
        print("-" * 25)
        print(f"Length: {analysis['length']} characters")
        print(f"Character sets used: {char_analysis['character_sets_used']}/4")
        print(f"  • Lowercase letters: {char_analysis['lowercase_count']}")
        print(f"  • Uppercase letters: {char_analysis['uppercase_count']}")
        print(f"  • Numbers: {char_analysis['digit_count']}")
        print(f"  • Special characters: {char_analysis['special_count']}")
        print(f"Unique characters: {char_analysis['unique_chars']}/{analysis['length']}")
        
        # Pattern analysis
        print(f"\n🔍 PATTERN ANALYSIS")
        print("-" * 20)
        
        issues_found = []
        if pattern_analysis['keyboard_patterns']:
            issues_found.append(f"Keyboard patterns: {', '.join(pattern_analysis['keyboard_patterns'])}")
        if pattern_analysis['repeated_sequences']:
            issues_found.append(f"Repeated sequences: {len(pattern_analysis['repeated_sequences'])}")
        if pattern_analysis['sequential_numbers']:
            issues_found.append("Sequential numbers detected")
        if pattern_analysis['sequential_letters']:
            issues_found.append("Sequential letters detected")
        if pattern_analysis['year_patterns']:
            issues_found.append(f"Year patterns: {', '.join(pattern_analysis['year_patterns'])}")
        if pattern_analysis['common_substitutions']:
            issues_found.append(f"Common substitutions: {', '.join(pattern_analysis['common_substitutions'])}")
        
        if issues_found:
            print("⚠️  Issues found:")
            for issue in issues_found:
                print(f"  • {issue}")
        else:
            print("✅ No common patterns detected")
        
        # Common password check
        print(f"\n🗂️  COMMON PASSWORD CHECK")
        print("-" * 30)
        if common_check['is_common']:
            print(f"❌ This password is commonly used ({common_check['type']})")
        else:
            print("✅ Not found in common passwords database")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS")
        print("-" * 20)
        for i, rec in enumerate(analysis['recommendations'], 1):
            print(f"{i}. {rec}")
        
        # Security level compliance
        print(f"\n📋 SECURITY LEVEL COMPLIANCE")
        print("-" * 35)
        for level_name, requirements in self.security_levels.items():
            meets_length = analysis['length'] >= requirements['min_length']
            meets_sets = char_analysis['character_sets_used'] >= requirements['required_sets']
            
            pattern_issues = len(pattern_analysis['keyboard_patterns']) + \
                           (1 if pattern_analysis['sequential_numbers'] else 0) + \
                           (1 if pattern_analysis['sequential_letters'] else 0)
            meets_patterns = pattern_issues <= requirements['max_common_patterns']
            
            compliance = meets_length and meets_sets and meets_patterns
            status = "✅" if compliance else "❌"
            
            print(f"{status} {level_name.title()}: {requirements['description']}")
    
    def generate_secure_password(self):
        """Generate secure passwords with customizable options."""
        print("\n🔐 SECURE PASSWORD GENERATOR")
        print("-" * 35)
        
        print("Choose generation method:")
        print("1. Random character password")
        print("2. Memorable passphrase")
        print("3. Custom pattern password")
        
        try:
            method = int(input("Enter choice (1-3): "))
            
            if method == 1:
                self.generate_random_password()
            elif method == 2:
                self.generate_passphrase()
            elif method == 3:
                self.generate_pattern_password()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def generate_random_password(self):
        """Generate random character password."""
        print("\nRandom Password Options:")
        
        # Get length
        while True:
            try:
                length = int(input("Enter password length (8-128): "))
                if 8 <= length <= 128:
                    break
                else:
                    print("❌ Length must be between 8 and 128!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Get character set preferences
        print("\nInclude character types:")
        include_lower = input("Lowercase letters (y/n)? ").lower().startswith('y')
        include_upper = input("Uppercase letters (y/n)? ").lower().startswith('y')
        include_digits = input("Numbers (y/n)? ").lower().startswith('y')
        include_special = input("Special characters (y/n)? ").lower().startswith('y')
        
        if not any([include_lower, include_upper, include_digits, include_special]):
            print("❌ Must include at least one character type!")
            return
        
        # Build character set
        charset = ""
        if include_lower:
            charset += string.ascii_lowercase
        if include_upper:
            charset += string.ascii_uppercase
        if include_digits:
            charset += string.digits
        if include_special:
            charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Generate passwords
        print(f"\n🎲 Generated Passwords (length {length}):")
        print("-" * 40)
        
        for i in range(5):  # Generate 5 options
            password = ''.join(random.choice(charset) for _ in range(length))
            analysis = self.perform_full_analysis(password)
            score = analysis['strength_score']
            level = analysis['security_level']
            
            level_emoji = {'very_weak': '🔴', 'weak': '🟠', 'moderate': '🟡', 'strong': '🟢', 'very_strong': '💚'}
            
            print(f"{i+1}. {password}")
            print(f"   Strength: {score}/100 {level_emoji.get(level, '⚪')}")
            print()
    
    def generate_passphrase(self):
        """Generate memorable passphrase."""
        # Simple word list (in practice, use a larger dictionary)
        words = [
            'apple', 'brave', 'chair', 'dance', 'eagle', 'flame', 'grape', 'house',
            'island', 'jungle', 'knight', 'lemon', 'magic', 'north', 'ocean', 'piano',
            'queen', 'river', 'storm', 'tiger', 'uncle', 'violet', 'whale', 'xenon',
            'yellow', 'zebra', 'anchor', 'bridge', 'castle', 'dragon', 'engine', 'forest',
            'golden', 'hammer', 'iceberg', 'jacket', 'kettle', 'ladder', 'mountain', 'ninja',
            'orange', 'purple', 'quartz', 'rocket', 'silver', 'thunder', 'universe', 'valley'
        ]
        
        print("\nPassphrase Options:")
        
        # Get number of words
        while True:
            try:
                num_words = int(input("Enter number of words (3-8): "))
                if 3 <= num_words <= 8:
                    break
                else:
                    print("❌ Number of words must be between 3 and 8!")
            except ValueError:
                print("❌ Please enter a valid number!")
        
        # Get separator
        print("\nSeparator options:")
        print("1. Hyphen (-)")
        print("2. Space ( )")
        print("3. Numbers (random)")
        print("4. Special characters (!@#)")
        
        try:
            sep_choice = int(input("Choose separator (1-4): "))
            if sep_choice == 1:
                separator = '-'
            elif sep_choice == 2:
                separator = ' '
            elif sep_choice == 3:
                separator = str(random.randint(0, 9))
            elif sep_choice == 4:
                separator = random.choice('!@#$%^&*')
            else:
                separator = '-'
        except ValueError:
            separator = '-'
        
        # Capitalization option
        capitalize = input("Capitalize first letter of each word (y/n)? ").lower().startswith('y')
        
        # Generate passphrases
        print(f"\n🎭 Generated Passphrases ({num_words} words):")
        print("-" * 45)
        
        for i in range(5):
            selected_words = random.sample(words, num_words)
            
            if capitalize:
                selected_words = [word.capitalize() for word in selected_words]
            
            passphrase = separator.join(selected_words)
            
            # Add numbers at the end for extra security
            if input("Add numbers at the end (y/n)? ").lower().startswith('y') if i == 0 else True:
                passphrase += str(random.randint(10, 999))
            
            analysis = self.perform_full_analysis(passphrase)
            score = analysis['strength_score']
            level = analysis['security_level']
            
            level_emoji = {'very_weak': '🔴', 'weak': '🟠', 'moderate': '🟡', 'strong': '🟢', 'very_strong': '💚'}
            
            print(f"{i+1}. {passphrase}")
            print(f"   Length: {len(passphrase)}, Strength: {score}/100 {level_emoji.get(level, '⚪')}")
            print()
    
    def generate_pattern_password(self):
        """Generate password based on custom patterns."""
        print("\nPattern-Based Password Generator:")
        print("Create passwords using patterns like:")
        print("  • Word + Numbers + Symbols")
        print("  • Base word with transformations")
        print("  • Structured formats")
        
        base_word = input("\nEnter a base word or phrase: ").strip()
        if not base_word:
            print("❌ Base word cannot be empty!")
            return
        
        print("\nTransformation options:")
        print("1. Add numbers before and after")
        print("2. Replace letters with numbers/symbols")
        print("3. Alternate upper/lower case")
        print("4. Add special characters")
        print("5. Reverse and combine")
        
        transformations = []
        choice = input("Select transformations (comma-separated, e.g., 1,3,4): ").strip()
        
        try:
            selected = [int(x.strip()) for x in choice.split(',') if x.strip().isdigit()]
            
            # Generate patterns
            print(f"\n🎨 Pattern-based passwords from '{base_word}':")
            print("-" * 50)
            
            for i in range(5):
                password = base_word
                
                # Apply transformations
                if 1 in selected:  # Add numbers
                    password = str(random.randint(10, 99)) + password + str(random.randint(10, 999))
                
                if 2 in selected:  # Replace letters
                    replacements = {'a': '@', 'e': '3', 'i': '!', 'o': '0', 's': '$'}
                    for old, new in replacements.items():
                        password = password.replace(old, new)
                
                if 3 in selected:  # Alternate case
                    password = ''.join(c.upper() if i % 2 == 0 else c.lower() 
                                     for i, c in enumerate(password))
                
                if 4 in selected:  # Add special characters
                    special = random.choice('!@#$%^&*')
                    password += special * random.randint(1, 3)
                
                if 5 in selected:  # Reverse and combine
                    password = password + password[::-1]
                
                analysis = self.perform_full_analysis(password)
                score = analysis['strength_score']
                level = analysis['security_level']
                
                level_emoji = {'very_weak': '🔴', 'weak': '🟠', 'moderate': '🟡', 'strong': '🟢', 'very_strong': '💚'}
                
                print(f"{i+1}. {password}")
                print(f"   Strength: {score}/100 {level_emoji.get(level, '⚪')}")
                print()
        
        except ValueError:
            print("❌ Invalid transformation selection!")
    
    def compare_passwords(self):
        """Compare strength of multiple passwords."""
        print("\n⚖️  PASSWORD COMPARISON")
        print("-" * 30)
        
        passwords = []
        
        print("Enter passwords to compare (press Enter on empty line to finish):")
        
        while len(passwords) < 10:  # Limit to 10 passwords
            password = input(f"Password {len(passwords) + 1}: ").strip()
            if not password:
                break
            passwords.append(password)
        
        if len(passwords) < 2:
            print("❌ Please enter at least 2 passwords to compare!")
            return
        
        print(f"\n📊 COMPARISON RESULTS ({len(passwords)} passwords)")
        print("=" * 60)
        
        analyses = []
        for i, password in enumerate(passwords, 1):
            analysis = self.perform_full_analysis(password)
            analyses.append((i, analysis))
        
        # Sort by strength score (descending)
        analyses.sort(key=lambda x: x[1]['strength_score'], reverse=True)
        
        print(f"{'Rank':<4} {'Password':<20} {'Score':<6} {'Level':<12} {'Length':<6}")
        print("-" * 60)
        
        level_emoji = {
            'very_weak': '🔴', 'weak': '🟠', 'moderate': '🟡', 
            'strong': '🟢', 'very_strong': '💚'
        }
        
        for rank, (original_num, analysis) in enumerate(analyses, 1):
            password_display = analysis['password'][:18] + ".." if len(analysis['password']) > 20 else analysis['password']
            score = analysis['strength_score']
            level = analysis['security_level']
            length = analysis['length']
            
            emoji = level_emoji.get(level, '⚪')
            
            print(f"{rank:<4} {password_display:<20} {score:<6} {emoji} {level:<10} {length:<6}")
        
        # Show detailed analysis for top password
        if analyses:
            print(f"\n🏆 STRONGEST PASSWORD ANALYSIS:")
            print("-" * 40)
            best_analysis = analyses[0][1]
            self.display_analysis_results(best_analysis)
    
    def security_education(self):
        """Provide cybersecurity education and tips."""
        print("\n🎓 SECURITY EDUCATION CENTER")
        print("-" * 35)
        
        print("1. Password Security Fundamentals")
        print("2. Common Attack Methods")
        print("3. Best Practices Guide")
        print("4. Two-Factor Authentication")
        print("5. Password Manager Benefits")
        print("6. Security Myths & Facts")
        
        try:
            choice = int(input("Select topic (1-6): "))
            
            if choice == 1:
                self.explain_password_fundamentals()
            elif choice == 2:
                self.explain_attack_methods()
            elif choice == 3:
                self.show_best_practices()
            elif choice == 4:
                self.explain_two_factor()
            elif choice == 5:
                self.explain_password_managers()
            elif choice == 6:
                self.debunk_security_myths()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def explain_password_fundamentals(self):
        """Explain password security fundamentals."""
        print("\n🔐 PASSWORD SECURITY FUNDAMENTALS")
        print("-" * 40)
        
        fundamentals = [
            ("Length Matters", "Longer passwords are exponentially harder to crack. Every additional character dramatically increases security."),
            ("Character Variety", "Using different types of characters (upper, lower, numbers, symbols) increases the search space for attackers."),
            ("Avoid Patterns", "Keyboard patterns, sequential characters, and predictable substitutions are easily detected by cracking tools."),
            ("Uniqueness", "Each account should have a unique password. Reusing passwords means one breach compromises multiple accounts."),
            ("Regular Updates", "Important passwords should be changed periodically, especially after security incidents."),
            ("Entropy", "True randomness in password creation makes passwords much stronger than human-generated patterns.")
        ]
        
        for title, explanation in fundamentals:
            print(f"\n📌 {title}")
            print(f"   {explanation}")
        
        print(f"\n💡 Quick Tips:")
        print("   • Aim for 12+ characters minimum")
        print("   • Use all 4 character types when possible")
        print("   • Avoid personal information")
        print("   • Consider passphrases for memorability")
    
    def explain_attack_methods(self):
        """Explain common password attack methods."""
        print("\n⚔️ COMMON ATTACK METHODS")
        print("-" * 30)
        
        attacks = [
            ("Brute Force", "Systematic trying of every possible combination. Effectiveness decreases exponentially with password length and complexity."),
            ("Dictionary Attack", "Using lists of common passwords and words. Most basic passwords fall to this method within seconds."),
            ("Credential Stuffing", "Using leaked passwords from other breaches. This is why password reuse is so dangerous."),
            ("Social Engineering", "Tricking users into revealing passwords. Often more effective than technical attacks."),
            ("Phishing", "Fake websites or emails designed to steal credentials. Always verify the authenticity of login pages."),
            ("Keyloggers", "Malware that records keystrokes. Two-factor authentication helps mitigate this risk.")
        ]
        
        for attack, description in attacks:
            print(f"\n🎯 {attack}")
            print(f"   {description}")
        
        print(f"\n🛡️ Defense Strategies:")
        print("   • Use strong, unique passwords")
        print("   • Enable two-factor authentication")
        print("   • Keep software updated")
        print("   • Be cautious with suspicious links/emails")
        print("   • Use reputable antivirus software")
    
    def show_best_practices(self):
        """Show password security best practices."""
        print("\n✅ PASSWORD BEST PRACTICES")
        print("-" * 35)
        
        practices = [
            "Create Strong Passwords",
            "• Use 12+ characters minimum",
            "• Include all character types (upper, lower, numbers, symbols)",
            "• Avoid common patterns and personal information",
            "• Consider using passphrases with random words",
            "",
            "Manage Passwords Securely",
            "• Use a unique password for each account", 
            "• Use a password manager to generate and store passwords",
            "• Never share passwords via email or text",
            "• Don't write passwords on sticky notes",
            "",
            "Account Security",
            "• Enable two-factor authentication whenever possible",
            "• Review account permissions and connected apps regularly",
            "• Monitor accounts for suspicious activity",
            "• Update passwords after security breaches",
            "",
            "Digital Hygiene",
            "• Keep devices and software updated",
            "• Use secure networks for sensitive activities",
            "• Log out of accounts on shared computers",
            "• Be cautious with password recovery options"
        ]
        
        for practice in practices:
            print(practice)
    
    def explain_two_factor(self):
        """Explain two-factor authentication."""
        print("\n🔐 TWO-FACTOR AUTHENTICATION (2FA)")
        print("-" * 40)
        
        print("What is 2FA?")
        print("Two-factor authentication adds an extra layer of security by requiring")
        print("two different types of verification:")
        print("1. Something you know (password)")
        print("2. Something you have (phone, authenticator app, hardware key)")
        
        print("\n🔑 Types of 2FA:")
        print("• SMS codes - Convenient but vulnerable to SIM swapping")
        print("• Authenticator apps - More secure, works offline")
        print("• Hardware keys - Most secure, but requires physical device")
        print("• Biometrics - Fingerprint, face recognition")
        
        print("\n✅ Benefits:")
        print("• Protects against password breaches")
        print("• Prevents most automated attacks")
        print("• Provides notification of unauthorized access attempts")
        print("• Required by many security compliance standards")
        
        print("\n💡 Best Practices:")
        print("• Enable 2FA on all important accounts")
        print("• Use authenticator apps over SMS when possible")
        print("• Keep backup codes in a secure location")
        print("• Use multiple 2FA methods when available")
    
    def explain_password_managers(self):
        """Explain benefits of password managers."""
        print("\n🗝️ PASSWORD MANAGER BENEFITS")
        print("-" * 35)
        
        print("Why Use a Password Manager?")
        print("Password managers solve the fundamental problem of creating,")
        print("remembering, and using strong, unique passwords for every account.")
        
        print("\n🎯 Key Benefits:")
        benefits = [
            "Generate strong, random passwords automatically",
            "Store unlimited passwords securely",
            "Auto-fill login forms to prevent phishing",
            "Sync passwords across all devices",
            "Identify weak, reused, or compromised passwords",
            "Secure sharing of passwords with team members",
            "Backup and recovery options"
        ]
        
        for benefit in benefits:
            print(f"• {benefit}")
        
        print("\n🔒 Security Features:")
        features = [
            "End-to-end encryption",
            "Zero-knowledge architecture",
            "Two-factor authentication",
            "Security audits and certifications",
            "Breach monitoring and alerts"
        ]
        
        for feature in features:
            print(f"• {feature}")
        
        print("\n💡 Popular Options:")
        print("• 1Password - Great for families and teams")
        print("• Bitwarden - Open-source with free tier")
        print("• LastPass - User-friendly interface")
        print("• Dashlane - Includes VPN and dark web monitoring")
        print("• KeePass - Self-hosted, fully offline option")
    
    def debunk_security_myths(self):
        """Debunk common security myths."""
        print("\n🔍 SECURITY MYTHS & FACTS")
        print("-" * 30)
        
        myths = [
            {
                'myth': "Changing passwords frequently makes them more secure",
                'fact': "Regular changes can lead to weaker passwords. Focus on strength and uniqueness instead.",
                'explanation': "Frequent changes often result in predictable patterns (password1, password2, etc.) or weaker passwords because users struggle to remember new complex ones."
            },
            {
                'myth': "Complex password requirements always improve security", 
                'fact': "Overly complex requirements can backfire by encouraging predictable patterns.",
                'explanation': "Requirements like 'must contain uppercase, lowercase, number, and symbol' often lead to passwords like 'Password1!' which follow predictable patterns."
            },
            {
                'myth': "Password strength meters are always accurate",
                'fact': "Many meters have flaws and may give false confidence in weak passwords.",
                'explanation': "Some meters only check basic rules and miss common patterns, dictionary words, or contextual weaknesses."
            },
            {
                'myth': "Storing passwords in browsers is always unsafe",
                'fact': "Modern browser password managers are reasonably secure for most users.",
                'explanation': "While dedicated password managers are better, browser storage is much safer than reusing simple passwords."
            },
            {
                'myth': "Hackers only target important people or companies",
                'fact': "Most attacks are automated and target anyone with valuable accounts.",
                'explanation': "Cybercriminals use automated tools that scan for vulnerabilities regardless of who you are."
            }
        ]
        
        for i, myth_fact in enumerate(myths, 1):
            print(f"\n❌ Myth {i}: {myth_fact['myth']}")
            print(f"✅ Fact: {myth_fact['fact']}")
            print(f"📝 Explanation: {myth_fact['explanation']}")
    
    def run(self):
        """Main program loop."""
        print("🔐 Welcome to the Password Security Analyzer!")
        print("This tool helps you create and analyze secure passwords.")
        
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n👋 Stay secure! Remember to use strong, unique passwords!")
                break
            elif choice == 1:
                self.analyze_password_strength()
            elif choice == 2:
                self.generate_secure_password()
            elif choice == 3:
                self.compare_passwords()
            elif choice == 4:
                self.security_education()
            elif choice == 5:
                print("🚧 Batch analysis feature coming soon!")
            elif choice == 6:
                print("🚧 Policy creator feature coming soon!")
            elif choice == 7:
                self.show_best_practices()
            
            print("\n" + "=" * 60)
            input("Press Enter to continue...")

def main():
    """Main entry point for the program."""
    analyzer = PasswordAnalyzer()
    analyzer.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Complete password strength analysis with multiple criteria
2. ✅ Pattern detection and security flaw identification
3. ✅ Password generation with customizable options
4. ✅ Educational content about cybersecurity
5. ✅ Professional user interface and clear feedback
6. ✅ Comprehensive error handling and input validation
7. ✅ Security best practices implementation
8. ✅ Real-world applicability and usefulness

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Advanced string processing and pattern recognition
• Security principles and best practices
• Complex validation logic and criteria evaluation
• Algorithm design for strength calculation
• User interface design for security tools
• Educational content presentation
• Cybersecurity awareness and implementation
• Professional software development practices

EXTENSION IDEAS:
===============
1. Add multi-language support for international users
2. Implement password breach checking via HaveIBeenPwned API
3. Create visual strength indicators and charts
4. Add password policy compliance checking
5. Implement secure password storage simulation
6. Create password audit tools for organizations
7. Add machine learning for smarter pattern detection
8. Integrate with popular password managers

This problem provides comprehensive practice with string processing,
security concepts, validation techniques, and professional software
design while creating a genuinely useful cybersecurity tool!
"""