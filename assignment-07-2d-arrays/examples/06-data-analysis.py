"""
Assignment 7 - Example 6: Data Analysis with 2D Arrays
======================================================

This program demonstrates how 2D arrays are used for data analysis and
statistical computing. 2D arrays naturally represent datasets, matrices,
and tabular data, making them essential for data science applications.

Key Concepts Demonstrated:
- Dataset representation and manipulation
- Statistical calculations and analysis
- Data visualization with ASCII charts
- Correlation and regression analysis
- Data cleaning and preprocessing
- Time series analysis with 2D structures
"""

import math
import random
from collections import defaultdict

print("=== DATA ANALYSIS WITH 2D ARRAYS ===")
print()

print("2D arrays are fundamental to data analysis:")
print("• Datasets: Rows as records, columns as features")
print("• Matrices: Mathematical operations and transformations")
print("• Time series: Time points vs. multiple variables")
print("• Images: Pixel data for computer vision")
print("• Statistical analysis: Correlation, regression, clustering")
print("• Scientific computing: Numerical simulations and modeling")
print()

# DATASET REPRESENTATION AND BASIC STATISTICS
print("=== DATASET REPRESENTATION AND BASIC STATISTICS ===")
print()

class Dataset:
    """Simple dataset class for tabular data analysis."""
    
    def __init__(self, column_names=None):
        self.data = []
        self.column_names = column_names or []
        self.num_rows = 0
        self.num_cols = 0
    
    def add_row(self, row_data):
        """Add a row of data to the dataset."""
        if not self.column_names and row_data:
            self.num_cols = len(row_data)
            self.column_names = [f"Col_{i}" for i in range(self.num_cols)]
        
        if len(row_data) != self.num_cols:
            raise ValueError(f"Row must have {self.num_cols} columns")
        
        self.data.append(list(row_data))
        self.num_rows += 1
    
    def get_column(self, col_index):
        """Get all values from a specific column."""
        if col_index < 0 or col_index >= self.num_cols:
            raise IndexError("Column index out of range")
        
        return [row[col_index] for row in self.data]
    
    def get_row(self, row_index):
        """Get a specific row."""
        if row_index < 0 or row_index >= self.num_rows:
            raise IndexError("Row index out of range")
        
        return self.data[row_index][:]
    
    def set_value(self, row, col, value):
        """Set a specific cell value."""
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            self.data[row][col] = value
    
    def get_value(self, row, col):
        """Get a specific cell value."""
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return self.data[row][col]
        return None
    
    def display(self, max_rows=10, precision=2):
        """Display the dataset in tabular format."""
        if not self.data:
            print("Dataset is empty")
            return
        
        # Display column headers
        header = "| " + " | ".join(f"{name:>8}" for name in self.column_names) + " |"
        separator = "+" + "+".join("-" * 10 for _ in self.column_names) + "+"
        
        print(separator)
        print(header)
        print(separator)
        
        # Display data rows
        rows_to_show = min(max_rows, self.num_rows)
        for i in range(rows_to_show):
            row_str = "| "
            for j, value in enumerate(self.data[i]):
                if isinstance(value, float):
                    formatted_value = f"{value:.{precision}f}"
                else:
                    formatted_value = str(value)
                row_str += f"{formatted_value:>8} | "
            print(row_str)
        
        if self.num_rows > max_rows:
            print(f"... ({self.num_rows - max_rows} more rows)")
        
        print(separator)
        print(f"Shape: {self.num_rows} rows × {self.num_cols} columns")
        print()
    
    def describe_column(self, col_index):
        """Generate descriptive statistics for a column."""
        column_data = self.get_column(col_index)
        numeric_data = []
        
        # Filter numeric values
        for value in column_data:
            try:
                numeric_data.append(float(value))
            except (ValueError, TypeError):
                pass
        
        if not numeric_data:
            return {"error": "No numeric data found"}
        
        # Calculate statistics
        n = len(numeric_data)
        mean = sum(numeric_data) / n
        
        # Calculate variance and standard deviation
        variance = sum((x - mean) ** 2 for x in numeric_data) / n
        std_dev = math.sqrt(variance)
        
        # Calculate min, max, and range
        min_val = min(numeric_data)
        max_val = max(numeric_data)
        
        # Calculate median
        sorted_data = sorted(numeric_data)
        if n % 2 == 0:
            median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            median = sorted_data[n//2]
        
        # Calculate quartiles
        q1_index = n // 4
        q3_index = 3 * n // 4
        q1 = sorted_data[q1_index]
        q3 = sorted_data[q3_index]
        
        return {
            'count': n,
            'mean': mean,
            'median': median,
            'std_dev': std_dev,
            'variance': variance,
            'min': min_val,
            'max': max_val,
            'range': max_val - min_val,
            'q1': q1,
            'q3': q3,
            'iqr': q3 - q1
        }

def create_sample_dataset():
    """Create a sample dataset for demonstration."""
    dataset = Dataset(['ID', 'Age', 'Height', 'Weight', 'Income'])
    
    # Generate sample data
    random.seed(42)
    for i in range(20):
        age = random.randint(18, 65)
        height = random.normalvariate(170, 10)  # cm
        weight = random.normalvariate(70, 15)   # kg
        # Income somewhat correlated with age
        income = 25000 + age * 800 + random.normalvariate(0, 10000)
        income = max(income, 20000)  # Minimum income
        
        dataset.add_row([i+1, age, height, weight, income])
    
    return dataset

# Demonstrate dataset operations
print("Dataset Operations:")
sample_data = create_sample_dataset()
print("Sample dataset:")
sample_data.display()

# Show column statistics
print("Column Statistics:")
for col_idx, col_name in enumerate(sample_data.column_names[1:], 1):  # Skip ID column
    stats = sample_data.describe_column(col_idx)
    if 'error' not in stats:
        print(f"\n{col_name}:")
        print(f"  Count: {stats['count']}")
        print(f"  Mean: {stats['mean']:.2f}")
        print(f"  Median: {stats['median']:.2f}")
        print(f"  Std Dev: {stats['std_dev']:.2f}")
        print(f"  Range: {stats['min']:.2f} - {stats['max']:.2f}")

print()

# CORRELATION ANALYSIS
print("=== CORRELATION ANALYSIS ===")
print()

def calculate_correlation(x_data, y_data):
    """Calculate Pearson correlation coefficient between two variables."""
    if len(x_data) != len(y_data) or len(x_data) < 2:
        return None
    
    n = len(x_data)
    
    # Convert to numeric
    try:
        x_numeric = [float(x) for x in x_data]
        y_numeric = [float(y) for y in y_data]
    except (ValueError, TypeError):
        return None
    
    # Calculate means
    x_mean = sum(x_numeric) / n
    y_mean = sum(y_numeric) / n
    
    # Calculate correlation components
    numerator = sum((x_numeric[i] - x_mean) * (y_numeric[i] - y_mean) for i in range(n))
    x_variance = sum((x - x_mean) ** 2 for x in x_numeric)
    y_variance = sum((y - y_mean) ** 2 for y in y_numeric)
    
    denominator = math.sqrt(x_variance * y_variance)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

def correlation_matrix(dataset, numeric_columns):
    """Calculate correlation matrix for numeric columns."""
    n_cols = len(numeric_columns)
    correlation_matrix = [[0.0 for _ in range(n_cols)] for _ in range(n_cols)]
    
    for i in range(n_cols):
        for j in range(n_cols):
            col_i_data = dataset.get_column(numeric_columns[i])
            col_j_data = dataset.get_column(numeric_columns[j])
            
            if i == j:
                correlation_matrix[i][j] = 1.0
            else:
                corr = calculate_correlation(col_i_data, col_j_data)
                correlation_matrix[i][j] = corr if corr is not None else 0.0
    
    return correlation_matrix

def display_correlation_matrix(correlation_matrix, column_names):
    """Display correlation matrix in a formatted way."""
    print("Correlation Matrix:")
    
    # Header
    header = "        "
    for name in column_names:
        header += f"{name[:7]:>8}"
    print(header)
    
    # Matrix rows
    for i, row_name in enumerate(column_names):
        row_str = f"{row_name[:7]:>7} "
        for j in range(len(correlation_matrix[i])):
            corr_val = correlation_matrix[i][j]
            row_str += f"{corr_val:>8.3f}"
        print(row_str)
    print()

# Demonstrate correlation analysis
print("Correlation Analysis:")
numeric_cols = [1, 2, 3, 4]  # Age, Height, Weight, Income
col_names = [sample_data.column_names[i] for i in numeric_cols]

corr_matrix = correlation_matrix(sample_data, numeric_cols)
display_correlation_matrix(corr_matrix, col_names)

# Interpret correlations
print("Correlation Interpretation:")
for i in range(len(col_names)):
    for j in range(i+1, len(col_names)):
        corr = corr_matrix[i][j]
        col1, col2 = col_names[i], col_names[j]
        
        if abs(corr) > 0.7:
            strength = "Strong"
        elif abs(corr) > 0.4:
            strength = "Moderate"
        elif abs(corr) > 0.2:
            strength = "Weak"
        else:
            strength = "Very weak"
        
        direction = "positive" if corr > 0 else "negative"
        print(f"  {col1} vs {col2}: {strength} {direction} correlation ({corr:.3f})")

print()

# LINEAR REGRESSION ANALYSIS
print("=== LINEAR REGRESSION ANALYSIS ===")
print()

def simple_linear_regression(x_data, y_data):
    """Perform simple linear regression: y = mx + b"""
    if len(x_data) != len(y_data) or len(x_data) < 2:
        return None
    
    n = len(x_data)
    
    # Convert to numeric
    try:
        x_numeric = [float(x) for x in x_data]
        y_numeric = [float(y) for y in y_data]
    except (ValueError, TypeError):
        return None
    
    # Calculate means
    x_mean = sum(x_numeric) / n
    y_mean = sum(y_numeric) / n
    
    # Calculate slope (m) and intercept (b)
    numerator = sum((x_numeric[i] - x_mean) * (y_numeric[i] - y_mean) for i in range(n))
    denominator = sum((x - x_mean) ** 2 for x in x_numeric)
    
    if denominator == 0:
        return None
    
    slope = numerator / denominator
    intercept = y_mean - slope * x_mean
    
    # Calculate R-squared (coefficient of determination)
    y_pred = [slope * x + intercept for x in x_numeric]
    ss_res = sum((y_numeric[i] - y_pred[i]) ** 2 for i in range(n))
    ss_tot = sum((y - y_mean) ** 2 for y in y_numeric)
    
    r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
    
    # Calculate standard error
    mse = ss_res / (n - 2) if n > 2 else 0
    std_error = math.sqrt(mse)
    
    return {
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_squared,
        'std_error': std_error,
        'n': n
    }

def predict_value(regression_result, x_value):
    """Predict y value using regression equation."""
    if regression_result is None:
        return None
    
    return regression_result['slope'] * x_value + regression_result['intercept']

# Demonstrate linear regression
print("Linear Regression Analysis:")

# Analyze Age vs Income relationship
age_data = sample_data.get_column(1)  # Age
income_data = sample_data.get_column(4)  # Income

regression = simple_linear_regression(age_data, income_data)

if regression:
    print("Age vs Income Regression:")
    print(f"  Equation: Income = {regression['slope']:.2f} × Age + {regression['intercept']:.2f}")
    print(f"  R² = {regression['r_squared']:.3f} ({regression['r_squared']*100:.1f}% variance explained)")
    print(f"  Standard Error: {regression['std_error']:.2f}")
    print()
    
    # Make predictions
    test_ages = [25, 35, 45, 55]
    print("Income Predictions:")
    for age in test_ages:
        predicted_income = predict_value(regression, age)
        print(f"  Age {age}: ${predicted_income:,.0f}")

print()

# DATA VISUALIZATION WITH ASCII CHARTS
print("=== DATA VISUALIZATION WITH ASCII CHARTS ===")
print()

def create_histogram(data, bins=10, max_width=50):
    """Create ASCII histogram of data."""
    numeric_data = []
    for value in data:
        try:
            numeric_data.append(float(value))
        except (ValueError, TypeError):
            pass
    
    if not numeric_data:
        print("No numeric data for histogram")
        return
    
    min_val = min(numeric_data)
    max_val = max(numeric_data)
    
    if min_val == max_val:
        print("All values are the same")
        return
    
    # Create bins
    bin_width = (max_val - min_val) / bins
    bin_counts = [0] * bins
    bin_labels = []
    
    # Count values in each bin
    for value in numeric_data:
        bin_index = min(int((value - min_val) / bin_width), bins - 1)
        bin_counts[bin_index] += 1
    
    # Create bin labels
    for i in range(bins):
        bin_start = min_val + i * bin_width
        bin_end = min_val + (i + 1) * bin_width
        bin_labels.append(f"{bin_start:.1f}-{bin_end:.1f}")
    
    # Scale bars to fit max width
    max_count = max(bin_counts)
    if max_count == 0:
        return
    
    print("Histogram:")
    for i in range(bins):
        count = bin_counts[i]
        bar_length = int((count / max_count) * max_width)
        bar = "█" * bar_length
        print(f"{bin_labels[i]:>10} |{bar:<{max_width}} {count}")
    print()

def create_scatter_plot(x_data, y_data, width=60, height=20):
    """Create ASCII scatter plot."""
    # Convert to numeric
    points = []
    for i in range(min(len(x_data), len(y_data))):
        try:
            x = float(x_data[i])
            y = float(y_data[i])
            points.append((x, y))
        except (ValueError, TypeError):
            pass
    
    if len(points) < 2:
        print("Not enough numeric data points for scatter plot")
        return
    
    # Find ranges
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)
    
    if x_min == x_max or y_min == y_max:
        print("Data range too small for scatter plot")
        return
    
    # Create plot grid
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    # Plot points
    for x, y in points:
        # Scale to grid coordinates
        grid_x = int((x - x_min) / (x_max - x_min) * (width - 1))
        grid_y = int((y - y_min) / (y_max - y_min) * (height - 1))
        
        # Y is flipped for display
        grid_y = height - 1 - grid_y
        
        grid[grid_y][grid_x] = '*'
    
    print("Scatter Plot:")
    print(f"Y: {y_max:.1f} ┐")
    
    # Display grid
    for row in grid:
        print("   │" + "".join(row))
    
    print(f"   └" + "─" * width)
    print(f"    {x_min:.1f}" + " " * (width - 10) + f"{x_max:.1f} X")
    print()

# Demonstrate data visualization
print("Data Visualization Examples:")

# Create histogram for age distribution
age_column = sample_data.get_column(1)
print("Age Distribution:")
create_histogram(age_column, bins=8)

# Create scatter plot for height vs weight
height_column = sample_data.get_column(2)
weight_column = sample_data.get_column(3)
print("Height vs Weight Scatter Plot:")
create_scatter_plot(height_column, weight_column)

# TIME SERIES ANALYSIS
print("=== TIME SERIES ANALYSIS ===")
print()

class TimeSeries:
    """Simple time series data structure."""
    
    def __init__(self):
        self.data = []  # List of [timestamp, value] pairs
        self.sorted = True
    
    def add_point(self, timestamp, value):
        """Add a data point."""
        self.data.append([timestamp, value])
        self.sorted = False
    
    def sort_by_time(self):
        """Sort data by timestamp."""
        if not self.sorted:
            self.data.sort(key=lambda x: x[0])
            self.sorted = True
    
    def get_values(self):
        """Get list of values."""
        return [point[1] for point in self.data]
    
    def get_timestamps(self):
        """Get list of timestamps."""
        return [point[0] for point in self.data]
    
    def calculate_moving_average(self, window_size):
        """Calculate moving average."""
        if len(self.data) < window_size:
            return []
        
        self.sort_by_time()
        moving_averages = []
        
        for i in range(window_size - 1, len(self.data)):
            window_values = [self.data[j][1] for j in range(i - window_size + 1, i + 1)]
            avg = sum(window_values) / window_size
            moving_averages.append([self.data[i][0], avg])
        
        return moving_averages
    
    def calculate_trend(self):
        """Calculate linear trend."""
        if len(self.data) < 2:
            return None
        
        timestamps = [float(point[0]) for point in self.data]
        values = [float(point[1]) for point in self.data]
        
        return simple_linear_regression(timestamps, values)
    
    def detect_peaks(self, threshold=1.0):
        """Detect peaks in the time series."""
        if len(self.data) < 3:
            return []
        
        self.sort_by_time()
        peaks = []
        
        for i in range(1, len(self.data) - 1):
            current_value = self.data[i][1]
            prev_value = self.data[i-1][1]
            next_value = self.data[i+1][1]
            
            # Check if current point is a local maximum
            if (current_value > prev_value and current_value > next_value and
                current_value - min(prev_value, next_value) >= threshold):
                peaks.append(self.data[i])
        
        return peaks

def create_sample_time_series():
    """Create sample time series data."""
    ts = TimeSeries()
    
    # Generate sample data with trend and noise
    random.seed(123)
    base_value = 100
    trend = 0.5
    
    for t in range(30):
        # Add trend, seasonal component, and noise
        seasonal = 10 * math.sin(2 * math.pi * t / 7)  # Weekly pattern
        noise = random.normalvariate(0, 5)
        value = base_value + trend * t + seasonal + noise
        
        ts.add_point(t, value)
    
    return ts

def display_time_series(ts, width=60, height=15):
    """Display time series as ASCII line chart."""
    if not ts.data:
        return
    
    ts.sort_by_time()
    values = ts.get_values()
    
    min_val = min(values)
    max_val = max(values)
    
    if min_val == max_val:
        print("All values are constant")
        return
    
    # Create display grid
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Plot points
    for i, (timestamp, value) in enumerate(ts.data):
        x = int(i * (width - 1) / (len(ts.data) - 1))
        y = int((value - min_val) / (max_val - min_val) * (height - 1))
        y = height - 1 - y  # Flip Y axis
        
        grid[y][x] = '*'
        
        # Connect points with lines (simple approximation)
        if i > 0:
            prev_x = int((i-1) * (width - 1) / (len(ts.data) - 1))
            prev_y = int((ts.data[i-1][1] - min_val) / (max_val - min_val) * (height - 1))
            prev_y = height - 1 - prev_y
            
            # Simple line drawing
            if abs(x - prev_x) <= 1:
                for y_line in range(min(y, prev_y), max(y, prev_y) + 1):
                    grid[y_line][x] = '|'
            else:
                for x_line in range(min(x, prev_x), max(x, prev_x) + 1):
                    grid[y][x_line] = '-'
    
    print("Time Series Plot:")
    print(f"{max_val:6.1f} ┐")
    
    for row in grid:
        print("       │" + "".join(row))
    
    print("       └" + "─" * width)
    print(f"        0" + " " * (width - 10) + f"{len(ts.data)-1}")
    print()

# Demonstrate time series analysis
print("Time Series Analysis:")
sample_ts = create_sample_time_series()

# Display the time series
display_time_series(sample_ts)

# Calculate trend
trend_result = sample_ts.calculate_trend()
if trend_result:
    print(f"Trend Analysis:")
    print(f"  Slope: {trend_result['slope']:.3f} units per time period")
    print(f"  R²: {trend_result['r_squared']:.3f}")
    
    if trend_result['slope'] > 0.1:
        print("  → Upward trend detected")
    elif trend_result['slope'] < -0.1:
        print("  → Downward trend detected")
    else:
        print("  → No significant trend")
    print()

# Calculate moving average
moving_avg = sample_ts.calculate_moving_average(5)
print(f"5-period moving average calculated ({len(moving_avg)} points)")

# Detect peaks
peaks = sample_ts.detect_peaks(threshold=8.0)
print(f"Peaks detected: {len(peaks)}")
for i, (timestamp, value) in enumerate(peaks[:5]):  # Show first 5 peaks
    print(f"  Peak {i+1}: Time {timestamp}, Value {value:.1f}")

print()

# STATISTICAL HYPOTHESIS TESTING
print("=== STATISTICAL HYPOTHESIS TESTING ===")
print()

def t_test_one_sample(sample_data, population_mean, alpha=0.05):
    """Perform one-sample t-test."""
    n = len(sample_data)
    if n < 2:
        return None
    
    # Calculate sample statistics
    sample_mean = sum(sample_data) / n
    sample_variance = sum((x - sample_mean) ** 2 for x in sample_data) / (n - 1)
    sample_std = math.sqrt(sample_variance)
    
    # Calculate t-statistic
    standard_error = sample_std / math.sqrt(n)
    t_stat = (sample_mean - population_mean) / standard_error
    
    # Degrees of freedom
    df = n - 1
    
    # Critical value (approximation for common alpha levels)
    critical_values = {0.05: 2.0, 0.01: 2.6, 0.001: 3.3}
    critical_t = critical_values.get(alpha, 2.0)
    
    # Determine significance
    significant = abs(t_stat) > critical_t
    
    return {
        'sample_mean': sample_mean,
        'population_mean': population_mean,
        't_statistic': t_stat,
        'degrees_freedom': df,
        'critical_value': critical_t,
        'significant': significant,
        'alpha': alpha,
        'n': n
    }

def chi_square_goodness_of_fit(observed, expected):
    """Perform chi-square goodness of fit test."""
    if len(observed) != len(expected):
        return None
    
    chi_square = 0
    for i in range(len(observed)):
        if expected[i] > 0:
            chi_square += (observed[i] - expected[i]) ** 2 / expected[i]
    
    df = len(observed) - 1
    
    # Critical value (approximation)
    critical_chi = 7.815 if df == 3 else 9.488 if df == 4 else 11.071
    
    significant = chi_square > critical_chi
    
    return {
        'chi_square': chi_square,
        'degrees_freedom': df,
        'critical_value': critical_chi,
        'significant': significant
    }

# Demonstrate hypothesis testing
print("Statistical Hypothesis Testing:")

# One-sample t-test for height data
height_data = [float(x) for x in sample_data.get_column(2)]
population_height = 165  # Assumed population mean height

t_test_result = t_test_one_sample(height_data, population_height)

if t_test_result:
    print("One-Sample t-Test (Height vs Population Mean):")
    print(f"  Sample mean: {t_test_result['sample_mean']:.2f} cm")
    print(f"  Population mean: {t_test_result['population_mean']:.2f} cm")
    print(f"  t-statistic: {t_test_result['t_statistic']:.3f}")
    print(f"  Critical value: ±{t_test_result['critical_value']:.3f}")
    
    if t_test_result['significant']:
        print("  → Significant difference detected (reject null hypothesis)")
    else:
        print("  → No significant difference (fail to reject null hypothesis)")
    print()

print("=== SUMMARY ===")
print()
print("Data Analysis with 2D Arrays Summary:")
print("1. 2D arrays naturally represent tabular datasets")
print("2. Statistical calculations are straightforward with array operations")
print("3. Correlation analysis reveals relationships between variables")
print("4. Linear regression provides predictive modeling capabilities")
print("5. ASCII visualization enables quick data exploration")
print("6. Time series analysis handles temporal data patterns")
print("7. Hypothesis testing supports statistical inference")
print("8. 2D arrays form the foundation of data science workflows")

"""
KEY TAKEAWAYS:
==============
1. 2D arrays are the foundation of data analysis and statistics
2. Tabular data maps naturally to row-column array structures
3. Statistical calculations involve array operations and iterations
4. Visualization helps understand data patterns and relationships
5. Time series data requires specialized analysis techniques
6. Hypothesis testing provides scientific rigor to conclusions
7. Correlation doesn't imply causation - careful interpretation needed
8. Data preprocessing and cleaning are crucial steps

DATA REPRESENTATION:
====================
• Rows: Individual records, observations, or data points
• Columns: Features, variables, or attributes
• Cells: Individual measurements or values
• Missing data: Requires special handling techniques
• Data types: Numeric, categorical, ordinal, temporal

STATISTICAL MEASURES:
=====================
• Central tendency: Mean, median, mode
• Variability: Standard deviation, variance, range
• Distribution: Skewness, kurtosis, percentiles
• Relationships: Correlation, covariance
• Inference: Confidence intervals, hypothesis tests

ANALYSIS TECHNIQUES:
====================
• Descriptive statistics: Summarize data characteristics
• Correlation analysis: Measure variable relationships
• Regression analysis: Model relationships and predictions
• Time series analysis: Handle temporal dependencies
• Hypothesis testing: Statistical significance testing
• Clustering: Group similar observations

VISUALIZATION METHODS:
======================
• Histograms: Show distribution of single variables
• Scatter plots: Visualize relationships between variables
• Line charts: Display trends over time
• Box plots: Show quartiles and outliers
• Heat maps: Display correlation matrices
• Bar charts: Compare categorical data

REAL-WORLD APPLICATIONS:
========================
• Business intelligence: Sales analysis, customer segmentation
• Scientific research: Experimental data analysis
• Finance: Risk analysis, portfolio optimization
• Healthcare: Clinical trial analysis, epidemiology
• Social sciences: Survey data analysis
• Engineering: Quality control, performance monitoring

ADVANCED TECHNIQUES:
====================
• Machine learning: Pattern recognition, classification
• Multivariate analysis: Principal component analysis
• Bayesian analysis: Probabilistic inference
• Survival analysis: Time-to-event modeling
• Experimental design: A/B testing, factorial experiments
• Big data: Distributed computing, streaming analysis

TOOLS AND LIBRARIES:
====================
• Python: NumPy, Pandas, SciPy, Matplotlib
• R: Built-in statistical functions, ggplot2
• Excel: Built-in statistical functions, pivot tables
• SQL: Aggregation functions, window functions
• Specialized: SPSS, SAS, Stata for advanced statistics

NEXT STEP:
Go to 07-complete-program.py for a comprehensive 2D array application!
"""