"""
Practice Problem 05: Personal Finance Management System
====================================================

DIFFICULTY: Advanced ⭐⭐⭐
CONCEPTS: Classes, File Management, Data Analysis, Financial Calculations
ASSIGNMENTS: 5 (Functions), 6 (Arrays/Strings), 7 (2D Arrays) + Advanced Concepts
ESTIMATED TIME: 90-120 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive personal finance management system that helps users track
their income, expenses, budgets, and financial goals. The system should provide
detailed financial analysis, budgeting tools, spending pattern recognition, and
financial planning features.

This problem combines object-oriented programming, financial calculations, data
analysis, and practical money management concepts to create a useful personal
finance application.

REQUIREMENTS:
============
1. Track income and expenses across multiple categories
2. Create and monitor budgets with alerts and recommendations
3. Analyze spending patterns and trends
4. Set and track financial goals (savings, debt reduction, etc.)
5. Generate detailed financial reports and insights
6. Provide investment tracking and portfolio analysis
7. Calculate loan payments, interest, and amortization schedules
8. Include financial planning tools and calculators

LEARNING OBJECTIVES:
===================
- Master object-oriented design and implementation
- Understand financial mathematics and calculations
- Practice data analysis and pattern recognition
- Implement complex validation and error handling
- Design user-friendly financial interfaces
- Work with date/time calculations and trends

STARTER CODE:
============
"""

import math
import random
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from enum import Enum

class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"

class Category:
    """Represents a financial category for transactions."""
    
    def __init__(self, name: str, type: TransactionType, budget_limit: float = 0.0):
        self.name = name
        self.type = type
        self.budget_limit = budget_limit
        self.transactions = []

class Transaction:
    """Represents a financial transaction."""
    
    def __init__(self, amount: float, category: str, description: str, 
                 date: str, transaction_type: TransactionType):
        self.transaction_id = self.generate_id()
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
        self.type = transaction_type
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def generate_id():
        """Generate a unique transaction ID."""
        return f"TXN{random.randint(100000, 999999)}"

class Account:
    """Represents a financial account (checking, savings, credit card, etc.)."""
    
    def __init__(self, name: str, account_type: str, initial_balance: float = 0.0):
        self.name = name
        self.type = account_type
        self.balance = initial_balance
        self.transactions = []
        self.created_date = datetime.now().strftime("%Y-%m-%d")

class FinancialGoal:
    """Represents a financial goal (savings target, debt reduction, etc.)."""
    
    def __init__(self, name: str, target_amount: float, deadline: str, 
                 goal_type: str, current_amount: float = 0.0):
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.deadline = deadline
        self.type = goal_type
        self.created_date = datetime.now().strftime("%Y-%m-%d")
        self.is_achieved = False

class PersonalFinanceSystem:
    """Comprehensive personal finance management system."""
    
    def __init__(self):
        """Initialize the personal finance system."""
        self.accounts = {}
        self.categories = {}
        self.transactions = []
        self.goals = {}
        self.budgets = {}
        
        # Financial constants
        self.annual_inflation_rate = 0.025  # 2.5% average inflation
        
        # Initialize default categories and accounts
        self.initialize_default_data()
    
    def initialize_default_data(self):
        """Initialize system with default categories and sample accounts."""
        # Default expense categories
        expense_categories = [
            ("Housing", 1500.0), ("Transportation", 400.0), ("Food & Dining", 500.0),
            ("Utilities", 200.0), ("Healthcare", 300.0), ("Entertainment", 200.0),
            ("Shopping", 300.0), ("Personal Care", 100.0), ("Education", 200.0),
            ("Insurance", 250.0), ("Taxes", 500.0), ("Savings", 1000.0), ("Other", 0.0)
        ]
        
        for name, budget in expense_categories:
            self.categories[name] = Category(name, TransactionType.EXPENSE, budget)
        
        # Default income categories
        income_categories = ["Salary", "Freelance", "Investments", "Other Income"]
        for name in income_categories:
            self.categories[name] = Category(name, TransactionType.INCOME, 0.0)
        
        # Default accounts
        self.accounts["Checking"] = Account("Main Checking", "checking", 2500.0)
        self.accounts["Savings"] = Account("Emergency Savings", "savings", 10000.0)
        self.accounts["Credit Card"] = Account("Main Credit Card", "credit", -1200.0)
        
        # Generate sample transactions for demonstration
        self.generate_sample_transactions()
        
        # Default financial goals
        self.goals["Emergency Fund"] = FinancialGoal(
            "Emergency Fund", 15000.0, "2024-12-31", "savings", 10000.0)
        self.goals["Vacation"] = FinancialGoal(
            "European Vacation", 5000.0, "2024-08-01", "savings", 1500.0)
    
    def generate_sample_transactions(self):
        """Generate realistic sample transactions for the last 3 months."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=90)
        
        # Sample transaction patterns
        monthly_salary = 5000.0
        
        current_date = start_date
        while current_date <= end_date:
            # Add monthly salary (first of each month)
            if current_date.day == 1:
                self.add_sample_transaction(
                    monthly_salary, "Salary", "Monthly Salary", 
                    current_date.strftime("%Y-%m-%d"), TransactionType.INCOME)
            
            # Add random expenses throughout the month
            if random.random() < 0.3:  # 30% chance of expense on any given day
                category_names = [name for name, cat in self.categories.items() 
                                if cat.type == TransactionType.EXPENSE and name != "Taxes"]
                category = random.choice(category_names)
                
                # Amount based on category
                amount_ranges = {
                    "Housing": (1200, 1800), "Transportation": (20, 100),
                    "Food & Dining": (10, 80), "Utilities": (50, 200),
                    "Healthcare": (25, 150), "Entertainment": (15, 100),
                    "Shopping": (20, 200), "Personal Care": (15, 60),
                    "Education": (30, 100), "Insurance": (100, 300),
                    "Savings": (200, 500), "Other": (10, 50)
                }
                
                min_amt, max_amt = amount_ranges.get(category, (10, 100))
                amount = random.uniform(min_amt, max_amt)
                
                description = f"{category} expense"
                self.add_sample_transaction(
                    amount, category, description,
                    current_date.strftime("%Y-%m-%d"), TransactionType.EXPENSE)
            
            current_date += timedelta(days=1)
    
    def add_sample_transaction(self, amount: float, category: str, description: str,
                             date: str, transaction_type: TransactionType):
        """Add a sample transaction to the system."""
        transaction = Transaction(amount, category, description, date, transaction_type)
        self.transactions.append(transaction)
        
        # Update account balances
        if transaction_type == TransactionType.INCOME:
            self.accounts["Checking"].balance += amount
        else:  # EXPENSE
            self.accounts["Checking"].balance -= amount
    
    def display_main_menu(self):
        """Display the main menu options."""
        print("=" * 60)
        print("         PERSONAL FINANCE MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. Account Management")
        print("2. Transaction Management")
        print("3. Budget Planning & Tracking")
        print("4. Financial Goals")
        print("5. Financial Reports & Analysis")
        print("6. Investment Portfolio")
        print("7. Loan & Debt Management")
        print("8. Financial Calculators")
        print("9. Settings & Categories")
        print("10. Data Import/Export")
        print("0. Exit")
        print("=" * 60)
    
    def get_menu_choice(self):
        """Get and validate user's menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (0-10): "))
                if 0 <= choice <= 10:
                    return choice
                else:
                    print("❌ Please enter a number between 0 and 10.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def manage_accounts(self):
        """Account management functionality."""
        print("\n💳 ACCOUNT MANAGEMENT")
        print("-" * 30)
        
        print("1. View All Accounts")
        print("2. Account Details")
        print("3. Add New Account")
        print("4. Transfer Between Accounts")
        print("5. Account Balance History")
        
        try:
            choice = int(input("Enter choice (1-5): "))
            
            if choice == 1:
                self.view_all_accounts()
            elif choice == 2:
                self.view_account_details()
            elif choice == 3:
                self.add_new_account()
            elif choice == 4:
                self.transfer_between_accounts()
            elif choice == 5:
                self.show_balance_history()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_all_accounts(self):
        """Display overview of all accounts."""
        print("\n💰 ACCOUNT OVERVIEW")
        print("-" * 35)
        
        if not self.accounts:
            print("❌ No accounts found!")
            return
        
        total_assets = 0
        total_liabilities = 0
        
        print(f"{'Account':<20} {'Type':<12} {'Balance':<15} {'Status'}")
        print("-" * 65)
        
        for account in self.accounts.values():
            balance = account.balance
            status = "✅ Good" if balance >= 0 else "⚠️ Negative"
            
            if account.type in ["checking", "savings"]:
                total_assets += max(0, balance)
                total_liabilities += max(0, -balance)
            elif account.type == "credit":
                total_liabilities += max(0, -balance)
            else:
                if balance > 0:
                    total_assets += balance
                else:
                    total_liabilities += -balance
            
            print(f"{account.name:<20} {account.type.title():<12} "
                  f"${balance:>10,.2f} {status}")
        
        print("-" * 65)
        net_worth = total_assets - total_liabilities
        print(f"{'Total Assets:':<35} ${total_assets:>10,.2f}")
        print(f"{'Total Liabilities:':<35} ${total_liabilities:>10,.2f}")
        print(f"{'Net Worth:':<35} ${net_worth:>10,.2f}")
        
        # Net worth analysis
        if net_worth > 0:
            print("💚 Positive net worth - Good financial position!")
        elif net_worth > -1000:
            print("🟡 Nearly balanced - Focus on reducing debt")
        else:
            print("🔴 Negative net worth - Priority: debt reduction")
    
    def add_new_account(self):
        """Add a new financial account."""
        print("\n➕ ADD NEW ACCOUNT")
        print("-" * 25)
        
        name = input("Account name: ").strip()
        if not name:
            print("❌ Account name cannot be empty!")
            return
        
        if name in self.accounts:
            print("❌ Account already exists!")
            return
        
        print("\nAccount types:")
        print("1. Checking")
        print("2. Savings") 
        print("3. Credit Card")
        print("4. Investment")
        print("5. Other")
        
        try:
            type_choice = int(input("Select type (1-5): "))
            account_types = ["", "checking", "savings", "credit", "investment", "other"]
            
            if 1 <= type_choice <= 5:
                account_type = account_types[type_choice]
            else:
                print("❌ Invalid choice!")
                return
            
            initial_balance = float(input("Initial balance: $"))
            
            self.accounts[name] = Account(name, account_type, initial_balance)
            print(f"✅ Account '{name}' created successfully!")
        
        except ValueError:
            print("❌ Please enter valid numbers!")
    
    def manage_transactions(self):
        """Transaction management functionality."""
        print("\n💸 TRANSACTION MANAGEMENT")
        print("-" * 35)
        
        print("1. Add New Transaction")
        print("2. View Recent Transactions")
        print("3. Search Transactions")
        print("4. Edit Transaction")
        print("5. Delete Transaction")
        print("6. Transaction Categories")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.add_new_transaction()
            elif choice == 2:
                self.view_recent_transactions()
            elif choice == 3:
                self.search_transactions()
            elif choice == 4:
                self.edit_transaction()
            elif choice == 5:
                self.delete_transaction()
            elif choice == 6:
                self.manage_categories()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def add_new_transaction(self):
        """Add a new financial transaction."""
        print("\n➕ ADD NEW TRANSACTION")
        print("-" * 30)
        
        # Transaction type
        print("Transaction type:")
        print("1. Income")
        print("2. Expense")
        
        try:
            type_choice = int(input("Select type (1-2): "))
            if type_choice == 1:
                trans_type = TransactionType.INCOME
            elif type_choice == 2:
                trans_type = TransactionType.EXPENSE
            else:
                print("❌ Invalid choice!")
                return
        except ValueError:
            print("❌ Please enter a valid number!")
            return
        
        # Amount
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
        except ValueError:
            print("❌ Please enter a valid amount!")
            return
        
        # Category
        available_categories = [name for name, cat in self.categories.items() 
                              if cat.type == trans_type]
        
        print("\nAvailable categories:")
        for i, category in enumerate(available_categories, 1):
            print(f"{i}. {category}")
        
        try:
            cat_choice = int(input(f"Select category (1-{len(available_categories)}): ")) - 1
            if 0 <= cat_choice < len(available_categories):
                category = available_categories[cat_choice]
            else:
                print("❌ Invalid category choice!")
                return
        except ValueError:
            print("❌ Please enter a valid number!")
            return
        
        # Description
        description = input("Description: ").strip()
        if not description:
            description = f"{trans_type.value.title()} - {category}"
        
        # Date
        date = input("Date (YYYY-MM-DD) or Enter for today: ").strip()
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        # Create transaction
        transaction = Transaction(amount, category, description, date, trans_type)
        self.transactions.append(transaction)
        
        # Update account balance (assuming checking account for simplicity)
        if trans_type == TransactionType.INCOME:
            self.accounts["Checking"].balance += amount
        else:
            self.accounts["Checking"].balance -= amount
        
        print(f"✅ Transaction added successfully! ID: {transaction.transaction_id}")
        
        # Check budget if it's an expense
        if trans_type == TransactionType.EXPENSE:
            self.check_budget_alert(category, amount)
    
    def check_budget_alert(self, category: str, amount: float):
        """Check if expense exceeds budget and show alert."""
        if category in self.categories:
            budget_limit = self.categories[category].budget_limit
            
            if budget_limit > 0:
                # Calculate current month spending in this category
                current_month = datetime.now().strftime("%Y-%m")
                monthly_spending = sum(
                    t.amount for t in self.transactions 
                    if (t.category == category and 
                        t.type == TransactionType.EXPENSE and
                        t.date.startswith(current_month))
                )
                
                percentage = (monthly_spending / budget_limit) * 100
                
                if percentage > 100:
                    print(f"🚨 BUDGET ALERT: {category} spending is {percentage:.1f}% of budget!")
                elif percentage > 80:
                    print(f"⚠️ Budget Warning: {category} spending is {percentage:.1f}% of budget")
    
    def view_recent_transactions(self):
        """Display recent transactions."""
        print("\n📋 RECENT TRANSACTIONS")
        print("-" * 30)
        
        if not self.transactions:
            print("❌ No transactions found!")
            return
        
        # Sort transactions by date (most recent first)
        recent_transactions = sorted(
            self.transactions, 
            key=lambda x: x.date + " " + x.created_at.split()[1], 
            reverse=True
        )[:20]  # Show last 20 transactions
        
        print(f"{'ID':<10} {'Date':<12} {'Type':<8} {'Category':<15} {'Amount':<12} {'Description'}")
        print("-" * 85)
        
        for transaction in recent_transactions:
            amount_str = f"${transaction.amount:,.2f}"
            if transaction.type == TransactionType.EXPENSE:
                amount_str = f"-{amount_str}"
            
            print(f"{transaction.transaction_id:<10} {transaction.date:<12} "
                  f"{transaction.type.value.title():<8} {transaction.category:<15} "
                  f"{amount_str:<12} {transaction.description[:25]}")
    
    def budget_planning(self):
        """Budget planning and tracking functionality."""
        print("\n📊 BUDGET PLANNING & TRACKING")
        print("-" * 40)
        
        print("1. Create/Edit Budget")
        print("2. View Current Budget Status")
        print("3. Budget vs Actual Comparison")
        print("4. Budget Recommendations")
        print("5. Spending Alerts Setup")
        
        try:
            choice = int(input("Enter choice (1-5): "))
            
            if choice == 1:
                self.create_edit_budget()
            elif choice == 2:
                self.view_budget_status()
            elif choice == 3:
                self.budget_vs_actual()
            elif choice == 4:
                self.budget_recommendations()
            elif choice == 5:
                self.setup_spending_alerts()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def view_budget_status(self):
        """Display current budget status and spending analysis."""
        print("\n💰 CURRENT BUDGET STATUS")
        print("-" * 35)
        
        current_month = datetime.now().strftime("%Y-%m")
        
        # Calculate monthly spending by category
        monthly_spending = {}
        for transaction in self.transactions:
            if (transaction.type == TransactionType.EXPENSE and 
                transaction.date.startswith(current_month)):
                
                category = transaction.category
                if category not in monthly_spending:
                    monthly_spending[category] = 0
                monthly_spending[category] += transaction.amount
        
        print(f"Budget Status for {datetime.now().strftime('%B %Y')}:")
        print()
        print(f"{'Category':<20} {'Budget':<12} {'Spent':<12} {'Remaining':<12} {'%':<6}")
        print("-" * 70)
        
        total_budget = 0
        total_spent = 0
        
        for category_name, category in self.categories.items():
            if category.type == TransactionType.EXPENSE and category.budget_limit > 0:
                budget = category.budget_limit
                spent = monthly_spending.get(category_name, 0)
                remaining = budget - spent
                percentage = (spent / budget * 100) if budget > 0 else 0
                
                total_budget += budget
                total_spent += spent
                
                # Color coding based on spending percentage
                status = "✅" if percentage <= 80 else "⚠️" if percentage <= 100 else "🚨"
                
                print(f"{category_name:<20} ${budget:<10,.0f} ${spent:<10,.0f} "
                      f"${remaining:<10,.0f} {percentage:<5.1f}% {status}")
        
        print("-" * 70)
        total_remaining = total_budget - total_spent
        total_percentage = (total_spent / total_budget * 100) if total_budget > 0 else 0
        
        print(f"{'TOTAL':<20} ${total_budget:<10,.0f} ${total_spent:<10,.0f} "
              f"${total_remaining:<10,.0f} {total_percentage:<5.1f}%")
        
        # Budget analysis
        print(f"\n📈 BUDGET ANALYSIS")
        print("-" * 25)
        
        if total_percentage <= 80:
            print("✅ Excellent! You're well within budget.")
        elif total_percentage <= 100:
            print("⚠️ Close to budget limit. Monitor spending carefully.")
        else:
            print("🚨 Over budget! Consider reducing expenses or adjusting budget.")
        
        # Identify problematic categories
        over_budget_categories = [
            name for name, cat in self.categories.items()
            if (cat.type == TransactionType.EXPENSE and cat.budget_limit > 0 and
                monthly_spending.get(name, 0) > cat.budget_limit)
        ]
        
        if over_budget_categories:
            print(f"\n🔴 Over-budget categories: {', '.join(over_budget_categories)}")
    
    def financial_reports(self):
        """Generate comprehensive financial reports."""
        print("\n📊 FINANCIAL REPORTS & ANALYSIS")
        print("-" * 40)
        
        print("1. Monthly Income Statement")
        print("2. Spending Analysis")
        print("3. Cash Flow Report")
        print("4. Net Worth Tracking")
        print("5. Financial Trends")
        print("6. Category Performance")
        print("7. Goal Progress Report")
        
        try:
            choice = int(input("Enter choice (1-7): "))
            
            if choice == 1:
                self.monthly_income_statement()
            elif choice == 2:
                self.spending_analysis()
            elif choice == 3:
                self.cash_flow_report()
            elif choice == 4:
                self.net_worth_tracking()
            elif choice == 5:
                self.financial_trends()
            elif choice == 6:
                self.category_performance()
            elif choice == 7:
                self.goal_progress_report()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def monthly_income_statement(self):
        """Generate monthly income statement."""
        print("\n📋 MONTHLY INCOME STATEMENT")
        print("-" * 35)
        
        current_month = datetime.now().strftime("%Y-%m")
        month_name = datetime.now().strftime("%B %Y")
        
        print(f"Income Statement for {month_name}")
        print("=" * 40)
        
        # Calculate income and expenses
        total_income = 0
        total_expenses = 0
        income_by_category = {}
        expenses_by_category = {}
        
        for transaction in self.transactions:
            if transaction.date.startswith(current_month):
                if transaction.type == TransactionType.INCOME:
                    total_income += transaction.amount
                    if transaction.category not in income_by_category:
                        income_by_category[transaction.category] = 0
                    income_by_category[transaction.category] += transaction.amount
                
                elif transaction.type == TransactionType.EXPENSE:
                    total_expenses += transaction.amount
                    if transaction.category not in expenses_by_category:
                        expenses_by_category[transaction.category] = 0
                    expenses_by_category[transaction.category] += transaction.amount
        
        # Display income section
        print("\n💰 INCOME")
        print("-" * 15)
        for category, amount in sorted(income_by_category.items()):
            print(f"{category:<20} ${amount:>10,.2f}")
        print("-" * 35)
        print(f"{'Total Income':<20} ${total_income:>10,.2f}")
        
        # Display expenses section
        print("\n💸 EXPENSES")
        print("-" * 16)
        for category, amount in sorted(expenses_by_category.items()):
            print(f"{category:<20} ${amount:>10,.2f}")
        print("-" * 35)
        print(f"{'Total Expenses':<20} ${total_expenses:>10,.2f}")
        
        # Net income
        net_income = total_income - total_expenses
        print("\n" + "=" * 35)
        print(f"{'NET INCOME':<20} ${net_income:>10,.2f}")
        
        # Analysis
        if net_income > 0:
            savings_rate = (net_income / total_income * 100) if total_income > 0 else 0
            print(f"\n✅ Positive cash flow! Savings rate: {savings_rate:.1f}%")
        else:
            print(f"\n🔴 Negative cash flow! Need to reduce expenses by ${-net_income:,.2f}")
    
    def spending_analysis(self):
        """Perform detailed spending pattern analysis."""
        print("\n🔍 SPENDING ANALYSIS")
        print("-" * 25)
        
        # Get time period
        print("Select analysis period:")
        print("1. Last 30 days")
        print("2. Last 3 months")
        print("3. Last 6 months")
        print("4. Current year")
        
        try:
            period_choice = int(input("Enter choice (1-4): "))
            
            end_date = datetime.now()
            if period_choice == 1:
                start_date = end_date - timedelta(days=30)
                period_name = "Last 30 Days"
            elif period_choice == 2:
                start_date = end_date - timedelta(days=90)
                period_name = "Last 3 Months"
            elif period_choice == 3:
                start_date = end_date - timedelta(days=180)
                period_name = "Last 6 Months"
            elif period_choice == 4:
                start_date = datetime(end_date.year, 1, 1)
                period_name = f"Year {end_date.year}"
            else:
                print("❌ Invalid choice!")
                return
        
        except ValueError:
            print("❌ Please enter a valid number!")
            return
        
        print(f"\n📊 Spending Analysis - {period_name}")
        print("=" * 40)
        
        # Filter transactions by date range
        period_transactions = []
        for transaction in self.transactions:
            if transaction.type == TransactionType.EXPENSE:
                try:
                    trans_date = datetime.strptime(transaction.date, "%Y-%m-%d")
                    if start_date <= trans_date <= end_date:
                        period_transactions.append(transaction)
                except ValueError:
                    continue
        
        if not period_transactions:
            print("❌ No expense data found for this period!")
            return
        
        # Calculate spending by category
        spending_by_category = {}
        for transaction in period_transactions:
            if transaction.category not in spending_by_category:
                spending_by_category[transaction.category] = 0
            spending_by_category[transaction.category] += transaction.amount
        
        total_spending = sum(spending_by_category.values())
        
        # Sort categories by spending amount
        sorted_categories = sorted(spending_by_category.items(), key=lambda x: x[1], reverse=True)
        
        print(f"{'Category':<20} {'Amount':<12} {'%':<6} {'Trend'}")
        print("-" * 50)
        
        for category, amount in sorted_categories:
            percentage = (amount / total_spending * 100) if total_spending > 0 else 0
            
            # Simple trend indicator (this could be enhanced with historical data)
            trend = "📈" if percentage > 10 else "➡️" if percentage > 5 else "📉"
            
            print(f"{category:<20} ${amount:<10,.2f} {percentage:<5.1f}% {trend}")
        
        print("-" * 50)
        print(f"{'TOTAL':<20} ${total_spending:<10,.2f} 100.0%")
        
        # Spending insights
        print(f"\n💡 SPENDING INSIGHTS")
        print("-" * 25)
        
        top_category = sorted_categories[0] if sorted_categories else None
        if top_category:
            print(f"• Largest expense: {top_category[0]} (${top_category[1]:,.2f})")
        
        avg_transaction = total_spending / len(period_transactions) if period_transactions else 0
        print(f"• Average transaction: ${avg_transaction:.2f}")
        print(f"• Total transactions: {len(period_transactions)}")
        
        # Days in period
        days_in_period = (end_date - start_date).days + 1
        daily_average = total_spending / days_in_period if days_in_period > 0 else 0
        print(f"• Daily average spending: ${daily_average:.2f}")
    
    def financial_calculators(self):
        """Provide various financial calculators."""
        print("\n🧮 FINANCIAL CALCULATORS")
        print("-" * 30)
        
        print("1. Loan Payment Calculator")
        print("2. Savings Goal Calculator")
        print("3. Investment Return Calculator")
        print("4. Retirement Planning Calculator")
        print("5. Debt Payoff Calculator")
        print("6. Emergency Fund Calculator")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.loan_payment_calculator()
            elif choice == 2:
                self.savings_goal_calculator()
            elif choice == 3:
                self.investment_calculator()
            elif choice == 4:
                self.retirement_calculator()
            elif choice == 5:
                self.debt_payoff_calculator()
            elif choice == 6:
                self.emergency_fund_calculator()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def loan_payment_calculator(self):
        """Calculate loan payments and create amortization schedule."""
        print("\n🏠 LOAN PAYMENT CALCULATOR")
        print("-" * 35)
        
        try:
            loan_amount = float(input("Loan amount: $"))
            annual_rate = float(input("Annual interest rate (%): "))
            years = int(input("Loan term (years): "))
            
            if loan_amount <= 0 or annual_rate < 0 or years <= 0:
                print("❌ Please enter positive values!")
                return
            
            monthly_rate = annual_rate / 100 / 12
            num_payments = years * 12
            
            # Calculate monthly payment using formula
            if monthly_rate > 0:
                monthly_payment = loan_amount * (
                    monthly_rate * (1 + monthly_rate) ** num_payments
                ) / ((1 + monthly_rate) ** num_payments - 1)
            else:
                monthly_payment = loan_amount / num_payments
            
            total_paid = monthly_payment * num_payments
            total_interest = total_paid - loan_amount
            
            print(f"\n📊 LOAN SUMMARY")
            print("-" * 20)
            print(f"Loan Amount: ${loan_amount:,.2f}")
            print(f"Interest Rate: {annual_rate:.2f}% annual")
            print(f"Loan Term: {years} years")
            print(f"Monthly Payment: ${monthly_payment:,.2f}")
            print(f"Total Amount Paid: ${total_paid:,.2f}")
            print(f"Total Interest: ${total_interest:,.2f}")
            
            # Show amortization schedule (first year)
            if input("\nShow first year amortization schedule? (y/n): ").lower().startswith('y'):
                print(f"\n📋 FIRST YEAR AMORTIZATION SCHEDULE")
                print("-" * 50)
                print(f"{'Month':<6} {'Payment':<12} {'Principal':<12} {'Interest':<12} {'Balance'}")
                print("-" * 60)
                
                balance = loan_amount
                for month in range(1, min(13, num_payments + 1)):
                    interest_payment = balance * monthly_rate
                    principal_payment = monthly_payment - interest_payment
                    balance -= principal_payment
                    
                    print(f"{month:<6} ${monthly_payment:<10.2f} ${principal_payment:<10.2f} "
                          f"${interest_payment:<10.2f} ${balance:<10,.2f}")
        
        except ValueError:
            print("❌ Please enter valid numbers!")
    
    def savings_goal_calculator(self):
        """Calculate how to reach a savings goal."""
        print("\n🎯 SAVINGS GOAL CALCULATOR")
        print("-" * 35)
        
        try:
            goal_amount = float(input("Savings goal amount: $"))
            current_savings = float(input("Current savings: $"))
            months_to_goal = int(input("Months to reach goal: "))
            annual_return = float(input("Expected annual return (%): ")) / 100
            
            if goal_amount <= current_savings:
                print("✅ You've already reached your goal!")
                return
            
            needed_amount = goal_amount - current_savings
            monthly_return = annual_return / 12
            
            # Calculate required monthly payment
            if monthly_return > 0:
                # Future value of annuity formula
                required_monthly = needed_amount / (
                    ((1 + monthly_return) ** months_to_goal - 1) / monthly_return
                )
            else:
                required_monthly = needed_amount / months_to_goal
            
            total_contributions = required_monthly * months_to_goal
            interest_earned = goal_amount - current_savings - total_contributions
            
            print(f"\n🎯 SAVINGS PLAN")
            print("-" * 20)
            print(f"Goal Amount: ${goal_amount:,.2f}")
            print(f"Current Savings: ${current_savings:,.2f}")
            print(f"Amount Needed: ${needed_amount:,.2f}")
            print(f"Time Frame: {months_to_goal} months")
            print(f"Required Monthly Savings: ${required_monthly:,.2f}")
            print(f"Total Contributions: ${total_contributions:,.2f}")
            print(f"Interest Earned: ${interest_earned:,.2f}")
            
            # Provide recommendations
            print(f"\n💡 RECOMMENDATIONS")
            print("-" * 20)
            if required_monthly > 1000:
                print("• Consider extending your timeline to reduce monthly requirement")
            if annual_return < 0.02:
                print("• Look into higher-yield savings accounts or investments")
            print("• Automate your savings to stay on track")
            print("• Review and adjust your plan quarterly")
        
        except ValueError:
            print("❌ Please enter valid numbers!")
    
    def run(self):
        """Main program loop."""
        print("💰 Welcome to the Personal Finance Management System!")
        print("Take control of your finances with comprehensive tracking and analysis tools.")
        
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n💰 Thank you for using the Personal Finance Management System!")
                print("Remember: Small financial decisions today lead to big results tomorrow!")
                break
            elif choice == 1:
                self.manage_accounts()
            elif choice == 2:
                self.manage_transactions()
            elif choice == 3:
                self.budget_planning()
            elif choice == 4:
                print("🚧 Financial goals feature coming soon!")
            elif choice == 5:
                self.financial_reports()
            elif choice == 6:
                print("🚧 Investment portfolio feature coming soon!")
            elif choice == 7:
                print("🚧 Loan & debt management feature coming soon!")
            elif choice == 8:
                self.financial_calculators()
            elif choice == 9:
                print("🚧 Settings & categories feature coming soon!")
            elif choice == 10:
                print("🚧 Data import/export feature coming soon!")
            
            print("\n" + "=" * 60)
            input("Press Enter to continue...")

def main():
    """Main entry point for the program."""
    finance_system = PersonalFinanceSystem()
    finance_system.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Comprehensive account and transaction management
2. ✅ Advanced budgeting and spending analysis
3. ✅ Financial calculations and planning tools
4. ✅ Detailed reporting and trend analysis
5. ✅ Goal setting and progress tracking
6. ✅ Professional user interface and navigation
7. ✅ Financial mathematics implementation
8. ✅ Real-world applicability and usefulness

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Object-oriented design and class relationships
• Financial mathematics and calculation algorithms
• Complex data structures and management
• Advanced analysis and reporting techniques
• Professional user interface design
• Input validation and error handling
• Date/time processing and calculations
• Real-world application development

EXTENSION IDEAS:
===============
1. Add data persistence with file I/O
2. Implement graphical charts and visualizations
3. Add cryptocurrency and investment tracking
4. Create mobile app integration capabilities
5. Implement advanced forecasting algorithms
6. Add multi-user support for family finances
7. Create automated bill payment reminders
8. Add tax calculation and reporting features

This problem provides comprehensive practice with advanced programming
concepts while creating a genuinely useful personal finance tool!
"""