"""
Assignment 3 - Example 7: COMPLETE ITERATION PROGRAM
====================================================

This is a comprehensive program that demonstrates all the iteration concepts
from Assignment 3. It implements a complete data analysis and reporting system
that uses every type of loop, control statement, and pattern we've learned.

PROGRAM PURPOSE:
This program analyzes sales data for a fictional company, demonstrating:
- All loop types (for, while, nested)
- Loop control (break, continue)
- Common patterns (accumulator, filter, find, etc.)
- Real-world data processing
- User interaction and menu systems
- Error handling and validation
- Comprehensive reporting

CONCEPTS DEMONSTRATED:
✓ For loops with sequences and ranges
✓ While loops with conditions
✓ Nested loops for 2D data processing
✓ Break and continue statements
✓ Loop patterns (accumulator, find, filter, etc.)
✓ Input validation
✓ Menu-driven programming
✓ Data analysis and reporting
"""

import random
import math

print("=" * 60)
print("     COMPANY SALES DATA ANALYSIS SYSTEM")
print("=" * 60)
print()

print("Welcome to the Sales Analysis System!")
print("This program demonstrates comprehensive iteration concepts")
print("through real-world data analysis.")
print()

# SECTION 1: DATA GENERATION AND INITIALIZATION
print("=== SECTION 1: DATA INITIALIZATION ===")
print()

# Generate sample sales data using loops
print("🔄 Generating sample sales data...")

# Company data structure
regions = ["North", "South", "East", "West"]
products = ["Laptop", "Desktop", "Tablet", "Phone", "Monitor"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Initialize 3D sales data structure using nested loops
# Structure: sales_data[region][product][month] = sales_amount
sales_data = {}

print("Setting up data structure with nested loops:")

# Outer loop: regions
for region_idx, region in enumerate(regions):
    print(f"  Initializing region {region_idx + 1}: {region}")
    sales_data[region] = {}
    
    # Middle loop: products  
    for product_idx, product in enumerate(products):
        print(f"    Setting up product {product_idx + 1}: {product}")
        sales_data[region][product] = {}
        
        # Inner loop: months
        for month_idx, month in enumerate(months):
            # Generate random sales data (1000-5000)
            sales_amount = random.randint(1000, 5000)
            sales_data[region][product][month] = sales_amount
            print(f"      {month}: ${sales_amount:,}")

print(f"✅ Generated data for {len(regions)} regions, {len(products)} products, {len(months)} months")
print(f"   Total data points: {len(regions) * len(products) * len(months)}")
print()

# SECTION 2: BASIC DATA EXPLORATION
print("=== SECTION 2: DATA EXPLORATION WITH FOR LOOPS ===")
print()

# PATTERN: Accumulator - Calculate total sales
print("📊 Calculating total company sales...")

total_company_sales = 0
month_totals = {}

# Initialize month totals
for month in months:
    month_totals[month] = 0

# Triple nested loop to sum all sales
print("Processing all sales data:")
for region in regions:
    region_total = 0
    print(f"\n📍 Region: {region}")
    
    for product in products:
        product_total = 0
        print(f"  📱 Product: {product}")
        
        for month in months:
            amount = sales_data[region][product][month]
            
            # Accumulator pattern - multiple accumulators
            total_company_sales += amount
            region_total += amount
            product_total += amount
            month_totals[month] += amount
            
            print(f"    {month}: ${amount:,}")
        
        print(f"    Product total: ${product_total:,}")
    
    print(f"  Region total: ${region_total:,}")

print(f"\n🎯 TOTAL COMPANY SALES: ${total_company_sales:,}")
print()

# Display monthly breakdown
print("📅 Monthly Sales Totals:")
for month in months:
    print(f"  {month}: ${month_totals[month]:,}")
print()

# SECTION 3: FIND PATTERNS - BEST AND WORST PERFORMERS
print("=== SECTION 3: FIND PATTERNS - PERFORMANCE ANALYSIS ===")
print()

# PATTERN: Find maximum - Best performing region
print("🏆 Finding best performing region...")

best_region = regions[0]
best_region_sales = 0
worst_region = regions[0]  
worst_region_sales = float('inf')

# Calculate sales by region
region_totals = {}
for region in regions:
    region_total = 0
    
    # Sum all products and months for this region
    for product in products:
        for month in months:
            region_total += sales_data[region][product][month]
    
    region_totals[region] = region_total
    print(f"  {region}: ${region_total:,}")
    
    # Find pattern - track best and worst
    if region_total > best_region_sales:
        best_region = region
        best_region_sales = region_total
    
    if region_total < worst_region_sales:
        worst_region = region
        worst_region_sales = region_total

print(f"\n🥇 Best Region: {best_region} with ${best_region_sales:,}")
print(f"🥉 Worst Region: {worst_region} with ${worst_region_sales:,}")
print(f"   Performance gap: ${best_region_sales - worst_region_sales:,}")
print()

# PATTERN: Find maximum - Best selling product overall
print("📱 Finding best selling product...")

product_totals = {}
best_product = products[0]
best_product_sales = 0

for product in products:
    product_total = 0
    
    for region in regions:
        for month in months:
            product_total += sales_data[region][product][month]
    
    product_totals[product] = product_total
    print(f"  {product}: ${product_total:,}")
    
    if product_total > best_product_sales:
        best_product = product
        best_product_sales = product_total

print(f"\n🎖️  Best Product: {best_product} with ${best_product_sales:,}")
print()

# SECTION 4: FILTER PATTERNS - DATA FILTERING
print("=== SECTION 4: FILTER PATTERNS - HIGH PERFORMERS ===")
print()

# PATTERN: Filter - Find high-performing combinations
print("🔍 Filtering high-performance region-product combinations...")

high_performance_threshold = 15000  # $15,000+ per combination
high_performers = []

print(f"Threshold: ${high_performance_threshold:,} per region-product combination")
print()

for region in regions:
    for product in products:
        # Calculate total for this region-product combination
        combination_total = 0
        
        for month in months:
            combination_total += sales_data[region][product][month]
        
        print(f"  {region}-{product}: ${combination_total:,}", end="")
        
        # Filter pattern - collect high performers
        if combination_total >= high_performance_threshold:
            high_performers.append({
                'region': region,
                'product': product,
                'total': combination_total
            })
            print(" 🌟 HIGH PERFORMER!")
        else:
            print()

print(f"\n✨ Found {len(high_performers)} high-performing combinations:")
for performer in high_performers:
    print(f"   {performer['region']}-{performer['product']}: ${performer['total']:,}")
print()

# SECTION 5: VALIDATION PATTERNS - DATA QUALITY
print("=== SECTION 5: VALIDATION PATTERNS - DATA QUALITY ===")
print()

print("🔍 Performing data quality checks...")

# PATTERN: Validate all - Check for missing data
print("\n1. Checking for missing data points:")
missing_data = []
total_expected = len(regions) * len(products) * len(months)
actual_count = 0

for region in regions:
    for product in products:
        for month in months:
            if region in sales_data and product in sales_data[region] and month in sales_data[region][product]:
                actual_count += 1
            else:
                missing_data.append(f"{region}-{product}-{month}")

if len(missing_data) == 0:
    print(f"   ✅ All {total_expected} data points present")
else:
    print(f"   ❌ Missing {len(missing_data)} data points:")
    for missing in missing_data:
        print(f"      {missing}")

# PATTERN: Validate range - Check for outliers
print("\n2. Checking for data outliers (unusually high/low values):")
outliers = []
normal_min = 800   # Minimum reasonable sales
normal_max = 6000  # Maximum reasonable sales

for region in regions:
    for product in products:
        for month in months:
            value = sales_data[region][product][month]
            
            if value < normal_min or value > normal_max:
                outliers.append({
                    'location': f"{region}-{product}-{month}",
                    'value': value,
                    'type': 'LOW' if value < normal_min else 'HIGH'
                })

if len(outliers) == 0:
    print(f"   ✅ All values within normal range (${normal_min:,} - ${normal_max:,})")
else:
    print(f"   ⚠️  Found {len(outliers)} outliers:")
    for outlier in outliers:
        print(f"      {outlier['location']}: ${outlier['value']:,} ({outlier['type']})")

print()

# SECTION 6: COUNTER PATTERNS - FREQUENCY ANALYSIS
print("=== SECTION 6: COUNTER PATTERNS - FREQUENCY ANALYSIS ===")
print()

# PATTERN: Count frequencies - Sales performance distribution
print("📈 Analyzing sales performance distribution...")

# Define performance categories
performance_ranges = [
    (0, 1500, "Poor"),
    (1500, 2500, "Fair"),
    (2500, 3500, "Good"), 
    (3500, 4500, "Very Good"),
    (4500, float('inf'), "Excellent")
]

# Initialize counters
performance_counts = {}
for min_val, max_val, category in performance_ranges:
    performance_counts[category] = 0

# Count each sale by performance category
print("Categorizing individual sales:")
total_sales_count = 0

for region in regions:
    for product in products:
        for month in months:
            amount = sales_data[region][product][month]
            total_sales_count += 1
            
            # Find which category this sale belongs to
            for min_val, max_val, category in performance_ranges:
                if min_val <= amount < max_val:
                    performance_counts[category] += 1
                    break

# Display distribution
print(f"\nSales Performance Distribution ({total_sales_count} total sales):")
for min_val, max_val, category in performance_ranges:
    count = performance_counts[category]
    percentage = (count / total_sales_count) * 100
    bar_length = int(percentage / 2)  # Scale bar
    bar = "█" * bar_length
    
    range_str = f"${min_val:,}+" if max_val == float('inf') else f"${min_val:,}-${max_val:,}"
    print(f"  {category:<12} ({range_str:<12}): {count:3} sales ({percentage:5.1f}%) {bar}")

print()

# SECTION 7: WHILE LOOPS - USER INTERACTION
print("=== SECTION 7: INTERACTIVE ANALYSIS WITH WHILE LOOPS ===")
print()

print("🖥️  Interactive Analysis Menu")
print("This section demonstrates while loops with user input validation")
print()

# Menu system using while loop
continue_analysis = True
analysis_count = 0

while continue_analysis:
    analysis_count += 1
    print(f"\n--- Analysis Session {analysis_count} ---")
    print("Available analyses:")
    print("1. Regional deep dive")
    print("2. Product performance trends") 
    print("3. Monthly comparison")
    print("4. Custom search")
    print("5. Exit analysis")
    
    # Input validation with while loop
    valid_choice = False
    while not valid_choice:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if 1 <= choice <= 5:
                valid_choice = True
            else:
                print("❌ Please enter a number between 1 and 5")
        except ValueError:
            print("❌ Please enter a valid number")
    
    # Process choice
    if choice == 1:
        print("\n📍 REGIONAL DEEP DIVE")
        print("Available regions:", ", ".join(regions))
        
        # Validate region input
        selected_region = ""
        while selected_region not in regions:
            selected_region = input("Enter region name: ").strip()
            if selected_region not in regions:
                print(f"❌ Invalid region. Choose from: {', '.join(regions)}")
        
        print(f"\n🔍 Analyzing {selected_region} region:")
        
        # Use nested loops to analyze selected region
        region_monthly = {}
        for month in months:
            region_monthly[month] = 0
            for product in products:
                amount = sales_data[selected_region][product][month]
                region_monthly[month] += amount
        
        # Find trends using accumulator and find patterns
        best_month = max(region_monthly, key=region_monthly.get)
        worst_month = min(region_monthly, key=region_monthly.get)
        
        print("Monthly performance:")
        for month in months:
            amount = region_monthly[month]
            print(f"  {month}: ${amount:,}")
        
        print(f"\n📊 {selected_region} Region Summary:")
        print(f"   Best month: {best_month} (${region_monthly[best_month]:,})")
        print(f"   Worst month: {worst_month} (${region_monthly[worst_month]:,})")
        
        # Growth analysis
        growth_rate = ((region_monthly[months[-1]] - region_monthly[months[0]]) / 
                      region_monthly[months[0]]) * 100
        print(f"   Growth rate: {growth_rate:.1f}% ({months[0]} to {months[-1]})")
        
    elif choice == 2:
        print("\n📱 PRODUCT PERFORMANCE TRENDS")
        
        # Analyze trends for each product using nested loops and patterns
        print("Product trend analysis:")
        
        for product in products:
            print(f"\n🔍 {product}:")
            
            # Calculate monthly totals for this product
            product_monthly = {}
            for month in months:
                monthly_total = 0
                for region in regions:
                    monthly_total += sales_data[region][product][month]
                product_monthly[month] = monthly_total
            
            # Find trend direction using pattern matching
            improving_months = 0
            declining_months = 0
            
            for i in range(1, len(months)):
                current = product_monthly[months[i]]
                previous = product_monthly[months[i-1]]
                
                if current > previous:
                    improving_months += 1
                elif current < previous:
                    declining_months += 1
            
            # Determine overall trend
            if improving_months > declining_months:
                trend = "📈 IMPROVING"
            elif declining_months > improving_months:
                trend = "📉 DECLINING"  
            else:
                trend = "📊 STABLE"
            
            total = sum(product_monthly.values())
            print(f"   Total sales: ${total:,}")
            print(f"   Trend: {trend}")
            print(f"   Monthly pattern: {list(product_monthly.values())}")
    
    elif choice == 3:
        print("\n📅 MONTHLY COMPARISON")
        
        # Compare all months using statistical analysis
        month_stats = {}
        
        for month in months:
            # Calculate statistics for this month
            month_values = []
            
            # Collect all sales for this month
            for region in regions:
                for product in products:
                    month_values.append(sales_data[region][product][month])
            
            # Calculate statistics using accumulator patterns
            total = sum(month_values)
            count = len(month_values) 
            average = total / count
            
            # Find min and max using find patterns
            minimum = min(month_values)
            maximum = max(month_values)
            
            # Calculate standard deviation
            variance_sum = 0
            for value in month_values:
                variance_sum += (value - average) ** 2
            std_deviation = math.sqrt(variance_sum / count)
            
            month_stats[month] = {
                'total': total,
                'average': average,
                'min': minimum,
                'max': maximum,
                'std_dev': std_deviation
            }
        
        print("Monthly statistics:")
        print(f"{'Month':<6} {'Total':<10} {'Average':<8} {'Min':<6} {'Max':<6} {'StdDev':<8}")
        print("-" * 50)
        
        for month in months:
            stats = month_stats[month]
            print(f"{month:<6} ${stats['total']:,<9} ${stats['average']:,.0f<7} "
                  f"${stats['min']:,<5} ${stats['max']:,<5} ${stats['std_dev']:,.0f<8}")
    
    elif choice == 4:
        print("\n🔍 CUSTOM SEARCH")
        
        # Custom search with validation loops
        print("Search for sales above a specific threshold")
        
        threshold = 0
        while threshold <= 0:
            try:
                threshold = float(input("Enter minimum sales amount: $"))
                if threshold <= 0:
                    print("❌ Please enter a positive number")
            except ValueError:
                print("❌ Please enter a valid number")
        
        print(f"\n🔍 Searching for sales above ${threshold:,.0f}...")
        
        # Search using filter pattern with nested loops
        matches = []
        
        for region in regions:
            for product in products:
                for month in months:
                    amount = sales_data[region][product][month]
                    
                    if amount > threshold:
                        matches.append({
                            'region': region,
                            'product': product,
                            'month': month,
                            'amount': amount
                        })
        
        if matches:
            print(f"✅ Found {len(matches)} sales above ${threshold:,.0f}:")
            
            # Sort matches by amount (highest first)
            for i in range(len(matches)):
                for j in range(i + 1, len(matches)):
                    if matches[i]['amount'] < matches[j]['amount']:
                        matches[i], matches[j] = matches[j], matches[i]
            
            # Display top 10 matches
            display_count = min(10, len(matches))
            for i in range(display_count):
                match = matches[i]
                print(f"   {match['region']}-{match['product']}-{match['month']}: ${match['amount']:,}")
            
            if len(matches) > 10:
                print(f"   ... and {len(matches) - 10} more")
        else:
            print(f"❌ No sales found above ${threshold:,.0f}")
    
    elif choice == 5:
        print("\n👋 Exiting analysis...")
        continue_analysis = False
        break
    
    # Ask if user wants to continue
    if continue_analysis:
        continue_choice = ""
        while continue_choice not in ['y', 'n', 'yes', 'no']:
            continue_choice = input("\nContinue analysis? (y/n): ").lower().strip()
            if continue_choice not in ['y', 'n', 'yes', 'no']:
                print("❌ Please enter 'y' for yes or 'n' for no")
        
        if continue_choice in ['n', 'no']:
            continue_analysis = False
            print("Analysis session ended.")

print()

# SECTION 8: FINAL COMPREHENSIVE REPORT
print("=== SECTION 8: COMPREHENSIVE FINAL REPORT ===")
print()

print("📋 SALES ANALYSIS SUMMARY REPORT")
print("=" * 50)

# Use all patterns to create comprehensive summary
summary_stats = {}

# Overall company performance (accumulator pattern)
summary_stats['total_sales'] = total_company_sales
summary_stats['avg_monthly'] = total_company_sales / len(months)
summary_stats['avg_regional'] = total_company_sales / len(regions)

# Best performers (find pattern)
summary_stats['best_region'] = best_region
summary_stats['best_product'] = best_product

# Growth analysis (transform + accumulator patterns)
first_month_total = month_totals[months[0]]
last_month_total = month_totals[months[-1]]
growth_rate = ((last_month_total - first_month_total) / first_month_total) * 100
summary_stats['growth_rate'] = growth_rate

# Data quality (validation patterns)
data_completeness = (actual_count / total_expected) * 100
summary_stats['data_completeness'] = data_completeness

# Performance distribution (counter patterns)
excellent_sales = performance_counts.get('Excellent', 0)
poor_sales = performance_counts.get('Poor', 0)
summary_stats['excellent_pct'] = (excellent_sales / total_sales_count) * 100
summary_stats['poor_pct'] = (poor_sales / total_sales_count) * 100

# Display comprehensive report
print(f"🏢 COMPANY OVERVIEW:")
print(f"   Total Sales Revenue: ${summary_stats['total_sales']:,}")
print(f"   Average Monthly Revenue: ${summary_stats['avg_monthly']:,.0f}")
print(f"   Average Regional Revenue: ${summary_stats['avg_regional']:,.0f}")
print(f"   Company Growth Rate: {summary_stats['growth_rate']:.1f}%")
print()

print(f"🏆 TOP PERFORMERS:")
print(f"   Best Region: {summary_stats['best_region']}")
print(f"   Best Product: {summary_stats['best_product']}")
print(f"   High Performers: {len(high_performers)} region-product combinations")
print()

print(f"📊 PERFORMANCE ANALYSIS:")
print(f"   Excellent Sales: {summary_stats['excellent_pct']:.1f}% of all transactions")
print(f"   Poor Sales: {summary_stats['poor_pct']:.1f}% of all transactions")
print(f"   Data Completeness: {summary_stats['data_completeness']:.1f}%")
print()

print(f"🎯 BUSINESS INSIGHTS:")

# Generate insights using various patterns
insights = []

# Growth insight
if growth_rate > 0:
    insights.append(f"✅ Company showing positive growth of {growth_rate:.1f}%")
else:
    insights.append(f"⚠️  Company showing decline of {abs(growth_rate):.1f}%")

# Performance insight  
if summary_stats['excellent_pct'] > 20:
    insights.append(f"✅ Strong performance with {summary_stats['excellent_pct']:.1f}% excellent sales")
else:
    insights.append(f"⚠️  Only {summary_stats['excellent_pct']:.1f}% of sales are excellent")

# Regional balance insight
best_sales = region_totals[best_region]
worst_sales = region_totals[worst_region]
regional_balance = (worst_sales / best_sales) * 100

if regional_balance > 80:
    insights.append("✅ Regions are well-balanced")
else:
    insights.append(f"⚠️  Regional imbalance: {regional_balance:.0f}% difference")

# Display insights
for insight in insights:
    print(f"   {insight}")

print()

# PROGRAM CONCLUSION
print("=" * 60)
print("           PROGRAM ANALYSIS COMPLETE")
print("=" * 60)
print()

print("🎓 CONCEPTS DEMONSTRATED IN THIS PROGRAM:")
print()
print("✅ FOR LOOPS:")
print("   • Iterating over lists and ranges")
print("   • Processing sequences and collections")
print("   • Enumeration with indices")
print()
print("✅ WHILE LOOPS:")
print("   • Input validation and menu systems")
print("   • Condition-based repetition")
print("   • Interactive user interfaces")
print()
print("✅ NESTED LOOPS:")
print("   • 3D data structure processing")
print("   • Multi-dimensional analysis")
print("   • Complex pattern generation")
print()
print("✅ LOOP CONTROL:")
print("   • break for early termination")
print("   • continue for conditional skipping")
print("   • Complex exit conditions")
print()
print("✅ LOOP PATTERNS:")
print("   • Accumulator (sum, count, statistics)")
print("   • Find (min, max, search)")
print("   • Filter (collect valid items)")
print("   • Transform (format conversion)")
print("   • Validate (data quality checks)")
print("   • Counter (frequency analysis)")
print("   • Flag (state monitoring)")
print()
print("🚀 REAL-WORLD APPLICATIONS:")
print("   • Data analysis and reporting")
print("   • Business intelligence")
print("   • Statistical computation") 
print("   • User interface design")
print("   • Data validation and cleaning")
print("   • Performance monitoring")
print()
print("💡 KEY LEARNING OUTCOMES:")
print("1. Loops are essential for data processing")
print("2. Different loop types serve different purposes")
print("3. Patterns provide reusable solutions")
print("4. Complex problems need multiple patterns")
print("5. User interaction requires validation loops")
print("6. Real programs combine all concepts together")
print()
print("🎯 YOU'VE MASTERED ITERATION CONCEPTS!")
print("   Ready for Assignment 4: Validation and Functions")

"""
PROGRAM SUMMARY:
================
This comprehensive program demonstrates ALL iteration concepts:

1. FOR LOOPS: Used for definite iteration over data structures
2. WHILE LOOPS: Used for indefinite iteration and user interaction  
3. NESTED LOOPS: Used for multi-dimensional data processing
4. LOOP CONTROL: Used break/continue for flow control
5. LOOP PATTERNS: Implemented all common algorithmic patterns

PRACTICAL APPLICATIONS:
=======================
• Business data analysis and reporting
• Interactive menu systems and user interfaces
• Statistical computation and trend analysis
• Data validation and quality assurance
• Performance monitoring and optimization
• Multi-dimensional data processing

ADVANCED CONCEPTS:
==================
• Combined multiple patterns in single solutions
• Implemented complex validation with nested conditions
• Created interactive analysis with user-driven exploration
• Generated comprehensive reports with statistical analysis
• Handled real-world data processing challenges

NEXT STEPS:
===========
You've now mastered iteration - the foundation of computational thinking!
Next you'll learn:
• Assignment 4: Data Validation and Input Handling
• Assignment 5: Functions and Modular Programming
• Assignment 6: One-Dimensional Arrays and Collections
• Assignment 7: Two-Dimensional Arrays and Advanced Data Structures

CONGRATULATIONS! 🎉
You can now solve complex computational problems using iteration!
"""