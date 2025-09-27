"""
Practice Problem 09: E-Commerce Analytics Platform
=================================================

DIFFICULTY: Expert ⭐⭐⭐⭐
CONCEPTS: Big Data Processing, Business Intelligence, Advanced Analytics
ASSIGNMENTS: Complete mastery of all assignments (1-7) plus business applications
ESTIMATED TIME: 140-180 minutes

PROBLEM DESCRIPTION:
===================
Create a comprehensive e-commerce analytics platform that processes sales data,
customer behavior, inventory management, and business intelligence reporting.
The system should handle large datasets, provide real-time analytics, generate
business insights, and support data-driven decision making for online retail.

This capstone problem integrates all programming concepts with real-world business
applications, advanced data processing, statistical analysis, and enterprise
software architecture patterns.

REQUIREMENTS:
============
1. Customer data management and segmentation analysis
2. Product catalog and inventory tracking with automated alerts
3. Sales analytics with trend analysis and forecasting
4. Revenue optimization and pricing strategy tools
5. Marketing campaign effectiveness measurement
6. Supply chain and logistics optimization
7. Real-time dashboard and business intelligence reporting
8. Machine learning-powered recommendation system

LEARNING OBJECTIVES:
===================
- Master enterprise-level software architecture and scalability
- Understand business intelligence and analytics concepts
- Practice advanced data processing and statistical analysis
- Implement machine learning and predictive analytics
- Design professional business applications and dashboards
- Work with complex business logic and optimization algorithms

STARTER CODE:
============
"""

import random
import math
import json
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional, Any
from enum import Enum
from collections import defaultdict, Counter
import statistics

class CustomerSegment(Enum):
    NEW = "new"
    REGULAR = "regular"
    VIP = "vip"
    AT_RISK = "at_risk"
    CHURNED = "churned"

class OrderStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURNED = "returned"

class ProductCategory(Enum):
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    HOME_GARDEN = "home_garden"
    BOOKS = "books"
    SPORTS = "sports"
    HEALTH_BEAUTY = "health_beauty"
    AUTOMOTIVE = "automotive"
    TOYS = "toys"

class Customer:
    """Customer data model with analytics tracking."""
    
    def __init__(self, customer_id: str, name: str, email: str, registration_date: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.registration_date = registration_date
        self.total_orders = 0
        self.total_spent = 0.0
        self.average_order_value = 0.0
        self.last_order_date = None
        self.segment = CustomerSegment.NEW
        self.preferred_categories = []
        self.shipping_addresses = []
        self.payment_methods = []
        self.order_history = []
        self.loyalty_points = 0
        self.satisfaction_score = 5.0  # 1-10 scale
        
    def update_analytics(self):
        """Update customer analytics based on order history."""
        if self.order_history:
            self.total_orders = len(self.order_history)
            self.total_spent = sum(order.total_amount for order in self.order_history)
            self.average_order_value = self.total_spent / self.total_orders
            self.last_order_date = max(order.order_date for order in self.order_history)
            
            # Update customer segment
            self.update_segment()
            
            # Update preferred categories
            category_counts = Counter()
            for order in self.order_history:
                for item in order.items:
                    category_counts[item.product.category] += item.quantity
            
            self.preferred_categories = [cat for cat, count in category_counts.most_common(3)]
    
    def update_segment(self):
        """Update customer segment based on behavior."""
        days_since_registration = (datetime.now() - datetime.strptime(self.registration_date, "%Y-%m-%d")).days
        days_since_last_order = float('inf')
        
        if self.last_order_date:
            days_since_last_order = (datetime.now() - datetime.strptime(self.last_order_date, "%Y-%m-%d")).days
        
        if days_since_last_order > 365:
            self.segment = CustomerSegment.CHURNED
        elif days_since_last_order > 180:
            self.segment = CustomerSegment.AT_RISK
        elif self.total_spent >= 10000:
            self.segment = CustomerSegment.VIP
        elif self.total_orders >= 5:
            self.segment = CustomerSegment.REGULAR
        else:
            self.segment = CustomerSegment.NEW

class Product:
    """Product data model with inventory and performance tracking."""
    
    def __init__(self, product_id: str, name: str, category: ProductCategory, 
                 price: float, cost: float, stock_quantity: int):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.cost = cost
        self.stock_quantity = stock_quantity
        self.min_stock_level = 10  # Reorder threshold
        self.max_stock_level = 1000
        self.total_sold = 0
        self.total_revenue = 0.0
        self.total_profit = 0.0
        self.average_rating = 5.0
        self.review_count = 0
        self.return_rate = 0.0
        self.seasonal_multiplier = 1.0
        self.competitor_price = price * random.uniform(0.8, 1.2)
        self.supplier_info = {}
        self.last_restocked = datetime.now().strftime("%Y-%m-%d")
        
    def update_performance_metrics(self):
        """Update product performance analytics."""
        if self.total_sold > 0:
            profit_per_unit = self.price - self.cost
            self.total_profit = self.total_sold * profit_per_unit
            
            # Calculate profit margin
            self.profit_margin = profit_per_unit / self.price
            
            # Update inventory turnover
            days_since_launch = max(1, (datetime.now() - datetime.strptime(self.last_restocked, "%Y-%m-%d")).days)
            self.inventory_turnover = (self.total_sold / max(1, self.stock_quantity)) * (365 / days_since_launch)
    
    def needs_restock(self) -> bool:
        """Check if product needs restocking."""
        return self.stock_quantity <= self.min_stock_level
    
    def get_recommended_price(self) -> float:
        """Calculate recommended price based on competition and demand."""
        demand_factor = min(2.0, self.total_sold / 100)  # Higher demand allows higher prices
        competition_factor = 0.95 if self.price > self.competitor_price else 1.05
        seasonal_factor = self.seasonal_multiplier
        
        base_price = self.cost * 1.5  # 50% markup minimum
        recommended = base_price * demand_factor * competition_factor * seasonal_factor
        
        return round(recommended, 2)

class OrderItem:
    """Individual item within an order."""
    
    def __init__(self, product: Product, quantity: int, price_at_purchase: float):
        self.product = product
        self.quantity = quantity
        self.price_at_purchase = price_at_purchase
        self.total_price = quantity * price_at_purchase
        self.discount_applied = 0.0

class Order:
    """Customer order with comprehensive tracking."""
    
    def __init__(self, order_id: str, customer: Customer, order_date: str):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.items = []
        self.subtotal = 0.0
        self.tax_amount = 0.0
        self.shipping_cost = 0.0
        self.discount_amount = 0.0
        self.total_amount = 0.0
        self.status = OrderStatus.PENDING
        self.shipping_address = {}
        self.payment_method = ""
        self.tracking_number = ""
        self.estimated_delivery = ""
        self.actual_delivery = ""
        self.customer_rating = 0
        self.customer_review = ""
        
    def add_item(self, product: Product, quantity: int):
        """Add item to order."""
        price = product.price
        item = OrderItem(product, quantity, price)
        self.items.append(item)
        self.calculate_totals()
        
        # Update product stock
        product.stock_quantity -= quantity
        product.total_sold += quantity
        product.total_revenue += item.total_price
    
    def calculate_totals(self):
        """Calculate order totals."""
        self.subtotal = sum(item.total_price for item in self.items)
        self.tax_amount = self.subtotal * 0.08  # 8% tax
        self.shipping_cost = 0.0 if self.subtotal > 50 else 9.99  # Free shipping over $50
        
        total_before_discount = self.subtotal + self.tax_amount + self.shipping_cost
        self.total_amount = total_before_discount - self.discount_amount
    
    def apply_discount(self, discount_percent: float, reason: str = ""):
        """Apply discount to order."""
        discount = self.subtotal * (discount_percent / 100)
        self.discount_amount += discount
        self.calculate_totals()

class ECommerceAnalytics:
    """Main e-commerce analytics platform."""
    
    def __init__(self):
        """Initialize the analytics platform."""
        self.customers = {}  # customer_id -> Customer
        self.products = {}   # product_id -> Product
        self.orders = {}     # order_id -> Order
        self.marketing_campaigns = {}
        self.business_metrics = {
            'total_revenue': 0.0,
            'total_orders': 0,
            'average_order_value': 0.0,
            'customer_acquisition_cost': 0.0,
            'customer_lifetime_value': 0.0,
            'conversion_rate': 0.0,
            'churn_rate': 0.0
        }
        
        # Initialize with sample data
        self.initialize_sample_data()
        
        # Analytics engines
        self.recommendation_engine = RecommendationEngine(self)
        self.pricing_optimizer = PricingOptimizer(self)
        self.inventory_manager = InventoryManager(self)
        
    def initialize_sample_data(self):
        """Initialize platform with realistic sample data."""
        # Generate sample products
        self.generate_sample_products()
        
        # Generate sample customers
        self.generate_sample_customers()
        
        # Generate sample orders
        self.generate_sample_orders()
        
        # Update all analytics
        self.update_all_analytics()
    
    def generate_sample_products(self):
        """Generate realistic product catalog."""
        product_templates = [
            # Electronics
            ("Wireless Headphones", ProductCategory.ELECTRONICS, 149.99, 75.00, 50),
            ("Smartphone Case", ProductCategory.ELECTRONICS, 29.99, 8.00, 200),
            ("Laptop Stand", ProductCategory.ELECTRONICS, 79.99, 35.00, 30),
            ("Bluetooth Speaker", ProductCategory.ELECTRONICS, 199.99, 89.00, 25),
            ("USB-C Cable", ProductCategory.ELECTRONICS, 19.99, 4.00, 150),
            
            # Clothing
            ("Cotton T-Shirt", ProductCategory.CLOTHING, 24.99, 8.00, 100),
            ("Jeans", ProductCategory.CLOTHING, 69.99, 28.00, 75),
            ("Running Shoes", ProductCategory.CLOTHING, 129.99, 52.00, 40),
            ("Winter Jacket", ProductCategory.CLOTHING, 199.99, 89.00, 20),
            ("Baseball Cap", ProductCategory.CLOTHING, 19.99, 6.00, 80),
            
            # Home & Garden
            ("Coffee Maker", ProductCategory.HOME_GARDEN, 89.99, 45.00, 15),
            ("Garden Hose", ProductCategory.HOME_GARDEN, 39.99, 18.00, 25),
            ("Throw Pillow", ProductCategory.HOME_GARDEN, 29.99, 12.00, 60),
            ("LED Desk Lamp", ProductCategory.HOME_GARDEN, 49.99, 22.00, 35),
            ("Plant Pot Set", ProductCategory.HOME_GARDEN, 34.99, 15.00, 40),
            
            # Books
            ("Python Programming Guide", ProductCategory.BOOKS, 39.99, 12.00, 50),
            ("Mystery Novel", ProductCategory.BOOKS, 14.99, 4.00, 100),
            ("Cookbook", ProductCategory.BOOKS, 29.99, 9.00, 75),
            ("Self-Help Book", ProductCategory.BOOKS, 19.99, 6.00, 90),
            ("Technical Manual", ProductCategory.BOOKS, 59.99, 20.00, 30),
            
            # Sports
            ("Yoga Mat", ProductCategory.SPORTS, 49.99, 20.00, 45),
            ("Basketball", ProductCategory.SPORTS, 29.99, 12.00, 30),
            ("Tennis Racket", ProductCategory.SPORTS, 159.99, 75.00, 15),
            ("Water Bottle", ProductCategory.SPORTS, 19.99, 6.00, 80),
            ("Exercise Bands", ProductCategory.SPORTS, 24.99, 8.00, 60),
        ]
        
        for i, (name, category, price, cost, stock) in enumerate(product_templates, 1):
            product_id = f"P{i:04d}"
            product = Product(product_id, name, category, price, cost, stock)
            
            # Add some variation to make it more realistic
            product.price *= random.uniform(0.9, 1.1)
            product.stock_quantity = int(stock * random.uniform(0.7, 1.3))
            product.average_rating = random.uniform(3.5, 5.0)
            product.review_count = random.randint(5, 200)
            
            self.products[product_id] = product
    
    def generate_sample_customers(self):
        """Generate sample customer base."""
        first_names = ["John", "Jane", "Michael", "Sarah", "David", "Emily", "Robert", "Jessica", 
                      "William", "Ashley", "James", "Amanda", "Christopher", "Stephanie", "Daniel"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", 
                     "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez"]
        
        # Generate 500 customers
        for i in range(1, 501):
            customer_id = f"C{i:05d}"
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            email = f"{name.lower().replace(' ', '.')}@email.com"
            
            # Registration date within last 2 years
            registration_date = (datetime.now() - timedelta(days=random.randint(1, 730))).strftime("%Y-%m-%d")
            
            customer = Customer(customer_id, name, email, registration_date)
            
            # Add some random attributes
            customer.loyalty_points = random.randint(0, 5000)
            customer.satisfaction_score = random.uniform(3.0, 10.0)
            
            self.customers[customer_id] = customer
    
    def generate_sample_orders(self):
        """Generate realistic order history."""
        order_counter = 1
        
        # Generate orders for each customer based on their behavior
        for customer in self.customers.values():
            # Determine number of orders based on customer registration time
            days_since_registration = (datetime.now() - datetime.strptime(customer.registration_date, "%Y-%m-%d")).days
            
            # More established customers tend to have more orders
            max_orders = min(20, max(1, int(days_since_registration / 30)))
            num_orders = random.randint(0, max_orders)
            
            for _ in range(num_orders):
                order_id = f"O{order_counter:06d}"
                
                # Order date within customer's active period
                order_date = (datetime.strptime(customer.registration_date, "%Y-%m-%d") + 
                             timedelta(days=random.randint(1, days_since_registration))).strftime("%Y-%m-%d")
                
                order = Order(order_id, customer, order_date)
                
                # Add items to order (1-5 items per order)
                num_items = random.randint(1, 5)
                available_products = list(self.products.values())
                
                for _ in range(num_items):
                    product = random.choice(available_products)
                    quantity = random.randint(1, 3)
                    
                    # Only add if enough stock
                    if product.stock_quantity >= quantity:
                        order.add_item(product, quantity)
                
                # Apply random discount chance
                if random.random() < 0.2:  # 20% chance of discount
                    discount = random.uniform(5, 25)
                    order.apply_discount(discount, "Promotional discount")
                
                # Set order status
                order.status = random.choice(list(OrderStatus))
                
                # Add customer rating for completed orders
                if order.status in [OrderStatus.DELIVERED]:
                    order.customer_rating = random.randint(3, 5)
                
                self.orders[order_id] = order
                customer.order_history.append(order)
                order_counter += 1
        
        print(f"Generated {len(self.orders)} sample orders")
    
    def update_all_analytics(self):
        """Update all analytics across the platform."""
        # Update customer analytics
        for customer in self.customers.values():
            customer.update_analytics()
        
        # Update product performance
        for product in self.products.values():
            product.update_performance_metrics()
        
        # Update business metrics
        self.update_business_metrics()
    
    def update_business_metrics(self):
        """Update high-level business metrics."""
        total_revenue = sum(order.total_amount for order in self.orders.values())
        total_orders = len(self.orders)
        
        self.business_metrics.update({
            'total_revenue': total_revenue,
            'total_orders': total_orders,
            'average_order_value': total_revenue / max(1, total_orders),
            'total_customers': len(self.customers),
            'active_customers': sum(1 for c in self.customers.values() 
                                  if c.segment not in [CustomerSegment.CHURNED])
        })
        
        # Calculate conversion rate (simplified)
        website_visitors = len(self.customers) * 5  # Assume 5 visitors per customer
        self.business_metrics['conversion_rate'] = (len(self.customers) / website_visitors) * 100
        
        # Calculate churn rate
        churned_customers = sum(1 for c in self.customers.values() 
                              if c.segment == CustomerSegment.CHURNED)
        self.business_metrics['churn_rate'] = (churned_customers / len(self.customers)) * 100
    
    def display_main_menu(self):
        """Display the main analytics dashboard menu."""
        print("=" * 70)
        print("                E-COMMERCE ANALYTICS PLATFORM")
        print("=" * 70)
        print("📊 Business Intelligence Dashboard")
        print("1. Executive Summary & KPIs")
        print("2. Sales Analytics & Revenue Insights")
        print("3. Customer Analytics & Segmentation")
        print("4. Product Performance & Inventory")
        print("5. Marketing Analytics & Campaign ROI")
        print("6. Operational Analytics & Logistics")
        print("7. Predictive Analytics & Forecasting")
        print("8. Recommendation Engine")
        print("9. Competitive Intelligence")
        print("10. Data Export & Reporting")
        print("0. Exit")
        print("=" * 70)
    
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
    
    def executive_summary(self):
        """Display executive summary dashboard."""
        print("\n📊 EXECUTIVE SUMMARY & KEY PERFORMANCE INDICATORS")
        print("=" * 60)
        
        self.update_business_metrics()
        metrics = self.business_metrics
        
        # Revenue Metrics
        print("💰 REVENUE PERFORMANCE")
        print("-" * 30)
        print(f"Total Revenue: ${metrics['total_revenue']:,.2f}")
        print(f"Total Orders: {metrics['total_orders']:,}")
        print(f"Average Order Value: ${metrics['average_order_value']:.2f}")
        
        # Calculate month-over-month growth (simplified)
        current_month_revenue = sum(
            order.total_amount for order in self.orders.values()
            if order.order_date.startswith(datetime.now().strftime("%Y-%m"))
        )
        
        last_month = (datetime.now() - timedelta(days=30)).strftime("%Y-%m")
        last_month_revenue = sum(
            order.total_amount for order in self.orders.values()
            if order.order_date.startswith(last_month)
        )
        
        if last_month_revenue > 0:
            growth_rate = ((current_month_revenue - last_month_revenue) / last_month_revenue) * 100
            growth_emoji = "📈" if growth_rate > 0 else "📉"
            print(f"Monthly Growth: {growth_emoji} {growth_rate:+.1f}%")
        
        # Customer Metrics
        print(f"\n👥 CUSTOMER METRICS")
        print("-" * 25)
        print(f"Total Customers: {metrics['total_customers']:,}")
        print(f"Active Customers: {metrics['active_customers']:,}")
        print(f"Conversion Rate: {metrics['conversion_rate']:.2f}%")
        print(f"Churn Rate: {metrics['churn_rate']:.2f}%")
        
        # Customer segmentation
        segment_counts = Counter(customer.segment for customer in self.customers.values())
        print(f"\nCustomer Segmentation:")
        for segment, count in segment_counts.items():
            percentage = (count / len(self.customers)) * 100
            print(f"  {segment.value.title()}: {count} ({percentage:.1f}%)")
        
        # Product Performance
        print(f"\n📦 INVENTORY & PRODUCTS")
        print("-" * 30)
        print(f"Total Products: {len(self.products)}")
        
        low_stock_count = sum(1 for p in self.products.values() if p.needs_restock())
        print(f"Low Stock Alerts: {low_stock_count}")
        
        # Top performers
        top_revenue_products = sorted(self.products.values(), 
                                    key=lambda p: p.total_revenue, reverse=True)[:5]
        
        print(f"\nTop 5 Revenue Generators:")
        for i, product in enumerate(top_revenue_products, 1):
            print(f"  {i}. {product.name}: ${product.total_revenue:,.2f}")
        
        # Operational Metrics
        print(f"\n⚡ OPERATIONAL EFFICIENCY")
        print("-" * 35)
        
        status_counts = Counter(order.status for order in self.orders.values())
        total_orders = len(self.orders)
        
        delivered_orders = status_counts.get(OrderStatus.DELIVERED, 0)
        fulfillment_rate = (delivered_orders / total_orders * 100) if total_orders > 0 else 0
        print(f"Order Fulfillment Rate: {fulfillment_rate:.1f}%")
        
        returned_orders = status_counts.get(OrderStatus.RETURNED, 0)
        return_rate = (returned_orders / total_orders * 100) if total_orders > 0 else 0
        print(f"Return Rate: {return_rate:.1f}%")
        
        cancelled_orders = status_counts.get(OrderStatus.CANCELLED, 0)
        cancellation_rate = (cancelled_orders / total_orders * 100) if total_orders > 0 else 0
        print(f"Cancellation Rate: {cancellation_rate:.1f}%")
        
        # Recommendations
        print(f"\n💡 EXECUTIVE RECOMMENDATIONS")
        print("-" * 35)
        
        recommendations = []
        
        if metrics['churn_rate'] > 15:
            recommendations.append("🔴 High churn rate - implement retention campaigns")
        
        if metrics['conversion_rate'] < 2:
            recommendations.append("🟡 Low conversion rate - optimize website UX")
        
        if low_stock_count > 10:
            recommendations.append("⚠️ Multiple low stock alerts - review inventory management")
        
        if return_rate > 10:
            recommendations.append("📦 High return rate - investigate product quality issues")
        
        if not recommendations:
            recommendations.append("✅ All key metrics are within healthy ranges")
        
        for rec in recommendations[:5]:
            print(f"  • {rec}")
    
    def sales_analytics(self):
        """Comprehensive sales analytics and insights."""
        print("\n💰 SALES ANALYTICS & REVENUE INSIGHTS")
        print("-" * 45)
        
        print("1. Revenue Trends & Patterns")
        print("2. Sales by Product Category")
        print("3. Geographic Sales Analysis")
        print("4. Seasonal Sales Patterns")
        print("5. Sales Funnel Analysis")
        print("6. Revenue Optimization Opportunities")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.revenue_trends_analysis()
            elif choice == 2:
                self.category_sales_analysis()
            elif choice == 3:
                print("🚧 Geographic analysis coming soon!")
            elif choice == 4:
                print("🚧 Seasonal patterns analysis coming soon!")
            elif choice == 5:
                print("🚧 Sales funnel analysis coming soon!")
            elif choice == 6:
                self.revenue_optimization_analysis()
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def revenue_trends_analysis(self):
        """Analyze revenue trends over time."""
        print("\n📈 REVENUE TRENDS ANALYSIS")
        print("-" * 35)
        
        # Group orders by month
        monthly_revenue = defaultdict(float)
        monthly_orders = defaultdict(int)
        
        for order in self.orders.values():
            month_key = order.order_date[:7]  # YYYY-MM format
            monthly_revenue[month_key] += order.total_amount
            monthly_orders[month_key] += 1
        
        # Sort by date
        sorted_months = sorted(monthly_revenue.keys())
        
        print("Monthly Revenue Trend:")
        print(f"{'Month':<10} {'Revenue':<12} {'Orders':<8} {'AOV':<8} {'Growth'}")
        print("-" * 50)
        
        previous_revenue = 0
        for month in sorted_months[-12:]:  # Last 12 months
            revenue = monthly_revenue[month]
            orders = monthly_orders[month]
            aov = revenue / orders if orders > 0 else 0
            
            growth = ""
            if previous_revenue > 0:
                growth_rate = ((revenue - previous_revenue) / previous_revenue) * 100
                growth = f"{growth_rate:+.1f}%"
            
            print(f"{month:<10} ${revenue:<10,.0f} {orders:<8} ${aov:<6.0f} {growth}")
            previous_revenue = revenue
        
        # Calculate overall trends
        if len(sorted_months) >= 2:
            first_month_revenue = monthly_revenue[sorted_months[0]]
            last_month_revenue = monthly_revenue[sorted_months[-1]]
            
            if first_month_revenue > 0:
                total_growth = ((last_month_revenue - first_month_revenue) / first_month_revenue) * 100
                print(f"\nOverall Growth Rate: {total_growth:+.1f}%")
        
        # Best and worst performing months
        best_month = max(sorted_months, key=lambda m: monthly_revenue[m])
        worst_month = min(sorted_months, key=lambda m: monthly_revenue[m])
        
        print(f"\nBest Month: {best_month} (${monthly_revenue[best_month]:,.2f})")
        print(f"Worst Month: {worst_month} (${monthly_revenue[worst_month]:,.2f})")
    
    def category_sales_analysis(self):
        """Analyze sales performance by product category."""
        print("\n📦 SALES BY PRODUCT CATEGORY")
        print("-" * 35)
        
        category_metrics = defaultdict(lambda: {
            'revenue': 0.0,
            'orders': 0,
            'quantity_sold': 0,
            'avg_price': 0.0,
            'profit': 0.0
        })
        
        # Calculate metrics by category
        for order in self.orders.values():
            for item in order.items:
                category = item.product.category
                category_metrics[category]['revenue'] += item.total_price
                category_metrics[category]['orders'] += 1
                category_metrics[category]['quantity_sold'] += item.quantity
                
                profit = (item.price_at_purchase - item.product.cost) * item.quantity
                category_metrics[category]['profit'] += profit
        
        # Calculate averages
        for category_data in category_metrics.values():
            if category_data['quantity_sold'] > 0:
                category_data['avg_price'] = category_data['revenue'] / category_data['quantity_sold']
        
        # Display results
        print(f"{'Category':<15} {'Revenue':<12} {'Orders':<8} {'Qty Sold':<10} {'Profit':<12} {'Margin'}")
        print("-" * 75)
        
        # Sort by revenue
        sorted_categories = sorted(category_metrics.items(), 
                                 key=lambda x: x[1]['revenue'], reverse=True)
        
        total_revenue = sum(data['revenue'] for data in category_metrics.values())
        
        for category, data in sorted_categories:
            revenue = data['revenue']
            orders = data['orders']
            quantity = data['quantity_sold']
            profit = data['profit']
            margin = (profit / revenue * 100) if revenue > 0 else 0
            market_share = (revenue / total_revenue * 100) if total_revenue > 0 else 0
            
            print(f"{category.value:<15} ${revenue:<10,.0f} {orders:<8} {quantity:<10} "
                  f"${profit:<10,.0f} {margin:<5.1f}%")
        
        print("-" * 75)
        print(f"{'TOTAL':<15} ${total_revenue:<10,.0f}")
        
        # Category insights
        print(f"\n💡 CATEGORY INSIGHTS")
        print("-" * 25)
        
        best_revenue_cat = max(sorted_categories, key=lambda x: x[1]['revenue'])
        best_margin_cat = max(sorted_categories, key=lambda x: x[1]['profit']/max(1, x[1]['revenue']))
        
        print(f"Highest Revenue: {best_revenue_cat[0].value} (${best_revenue_cat[1]['revenue']:,.0f})")
        print(f"Best Profit Margin: {best_margin_cat[0].value} ({(best_margin_cat[1]['profit']/max(1, best_margin_cat[1]['revenue'])*100):.1f}%)")
        
        # Growth opportunities
        underperforming = [cat for cat, data in sorted_categories 
                          if data['revenue'] < total_revenue * 0.05]  # Less than 5% of total
        
        if underperforming:
            print(f"\nGrowth Opportunities:")
            for category, _ in underperforming[:3]:
                print(f"  • {category.value} - Consider marketing campaigns or product expansion")
    
    def customer_analytics(self):
        """Comprehensive customer analytics and segmentation."""
        print("\n👥 CUSTOMER ANALYTICS & SEGMENTATION")
        print("-" * 45)
        
        print("1. Customer Segmentation Analysis")
        print("2. Customer Lifetime Value Analysis")
        print("3. Customer Behavior Patterns")
        print("4. Churn Analysis & Retention")
        print("5. Customer Satisfaction Metrics")
        print("6. Acquisition & Retention Costs")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.customer_segmentation_analysis()
            elif choice == 2:
                self.customer_lifetime_value_analysis()
            elif choice == 3:
                self.customer_behavior_patterns()
            elif choice == 4:
                print("🚧 Churn analysis coming soon!")
            elif choice == 5:
                print("🚧 Satisfaction metrics coming soon!")
            elif choice == 6:
                print("🚧 Acquisition costs coming soon!")
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def customer_segmentation_analysis(self):
        """Detailed customer segmentation analysis."""
        print("\n🎯 CUSTOMER SEGMENTATION ANALYSIS")
        print("-" * 40)
        
        # Group customers by segment
        segment_data = defaultdict(lambda: {
            'count': 0,
            'total_revenue': 0.0,
            'total_orders': 0,
            'avg_order_value': 0.0,
            'avg_satisfaction': 0.0
        })
        
        for customer in self.customers.values():
            segment = customer.segment
            segment_data[segment]['count'] += 1
            segment_data[segment]['total_revenue'] += customer.total_spent
            segment_data[segment]['total_orders'] += customer.total_orders
            segment_data[segment]['avg_satisfaction'] += customer.satisfaction_score
        
        # Calculate averages
        for segment, data in segment_data.items():
            count = data['count']
            if count > 0:
                data['avg_order_value'] = data['total_revenue'] / max(1, data['total_orders'])
                data['avg_satisfaction'] = data['avg_satisfaction'] / count
        
        # Display segment analysis
        total_customers = len(self.customers)
        total_revenue = sum(data['total_revenue'] for data in segment_data.values())
        
        print(f"{'Segment':<12} {'Count':<8} {'%':<6} {'Revenue':<12} {'AOV':<8} {'Satisfaction'}")
        print("-" * 70)
        
        for segment in CustomerSegment:
            data = segment_data[segment]
            count = data['count']
            percentage = (count / total_customers * 100) if total_customers > 0 else 0
            revenue = data['total_revenue']
            aov = data['avg_order_value']
            satisfaction = data['avg_satisfaction']
            
            print(f"{segment.value:<12} {count:<8} {percentage:<5.1f}% "
                  f"${revenue:<10,.0f} ${aov:<6.0f} {satisfaction:<.1f}/10")
        
        print("-" * 70)
        
        # Segment insights
        print(f"\n📊 SEGMENT INSIGHTS")
        print("-" * 25)
        
        # Most valuable segment
        most_valuable = max(segment_data.items(), key=lambda x: x[1]['total_revenue'])
        print(f"Most Valuable Segment: {most_valuable[0].value} (${most_valuable[1]['total_revenue']:,.0f} revenue)")
        
        # Largest segment
        largest = max(segment_data.items(), key=lambda x: x[1]['count'])
        print(f"Largest Segment: {largest[0].value} ({largest[1]['count']} customers)")
        
        # Highest AOV
        highest_aov = max(segment_data.items(), key=lambda x: x[1]['avg_order_value'])
        print(f"Highest AOV: {highest_aov[0].value} (${highest_aov[1]['avg_order_value']:.2f})")
        
        # Action recommendations
        print(f"\n💡 RECOMMENDATIONS")
        print("-" * 20)
        
        vip_count = segment_data[CustomerSegment.VIP]['count']
        regular_count = segment_data[CustomerSegment.REGULAR]['count']
        at_risk_count = segment_data[CustomerSegment.AT_RISK]['count']
        
        if vip_count < total_customers * 0.1:
            print("• Focus on converting regular customers to VIP status")
        
        if at_risk_count > total_customers * 0.15:
            print("• Implement retention campaigns for at-risk customers")
        
        if regular_count > total_customers * 0.5:
            print("• Develop loyalty programs to upgrade regular customers")
        
        new_count = segment_data[CustomerSegment.NEW]['count']
        if new_count > total_customers * 0.3:
            print("• Create onboarding campaigns for new customers")
    
    def product_performance(self):
        """Product performance and inventory management."""
        print("\n📦 PRODUCT PERFORMANCE & INVENTORY")
        print("-" * 40)
        
        print("1. Top Performing Products")
        print("2. Inventory Status & Alerts")
        print("3. Product Profitability Analysis")
        print("4. Price Optimization Recommendations")
        print("5. Product Lifecycle Analysis")
        print("6. Competitive Pricing Analysis")
        
        try:
            choice = int(input("Enter choice (1-6): "))
            
            if choice == 1:
                self.top_performing_products()
            elif choice == 2:
                self.inventory_status_alerts()
            elif choice == 3:
                self.product_profitability_analysis()
            elif choice == 4:
                print("🚧 Price optimization coming soon!")
            elif choice == 5:
                print("🚧 Product lifecycle analysis coming soon!")
            elif choice == 6:
                print("🚧 Competitive pricing analysis coming soon!")
            else:
                print("❌ Invalid choice!")
        
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def top_performing_products(self):
        """Display top performing products across different metrics."""
        print("\n🏆 TOP PERFORMING PRODUCTS")
        print("-" * 35)
        
        print("📈 Top 10 by Revenue:")
        print(f"{'Rank':<4} {'Product':<25} {'Revenue':<12} {'Units Sold':<10} {'Rating'}")
        print("-" * 65)
        
        top_by_revenue = sorted(self.products.values(), 
                               key=lambda p: p.total_revenue, reverse=True)[:10]
        
        for i, product in enumerate(top_by_revenue, 1):
            print(f"{i:<4} {product.name:<25} ${product.total_revenue:<10,.0f} "
                  f"{product.total_sold:<10} {product.average_rating:.1f}★")
        
        print(f"\n💰 Top 10 by Profit Margin:")
        print(f"{'Rank':<4} {'Product':<25} {'Margin':<8} {'Profit':<12} {'Price'}")
        print("-" * 65)
        
        products_with_margin = []
        for product in self.products.values():
            if product.total_sold > 0:
                profit_per_unit = product.price - product.cost
                margin = (profit_per_unit / product.price) * 100
                products_with_margin.append((product, margin, profit_per_unit * product.total_sold))
        
        top_by_margin = sorted(products_with_margin, key=lambda x: x[1], reverse=True)[:10]
        
        for i, (product, margin, total_profit) in enumerate(top_by_margin, 1):
            print(f"{i:<4} {product.name:<25} {margin:<7.1f}% "
                  f"${total_profit:<10,.0f} ${product.price:.2f}")
        
        print(f"\n⭐ Top 10 by Customer Rating:")
        print(f"{'Rank':<4} {'Product':<25} {'Rating':<8} {'Reviews':<8} {'Sales'}")
        print("-" * 65)
        
        # Filter products with at least 5 reviews
        rated_products = [p for p in self.products.values() if p.review_count >= 5]
        top_by_rating = sorted(rated_products, 
                              key=lambda p: p.average_rating, reverse=True)[:10]
        
        for i, product in enumerate(top_by_rating, 1):
            print(f"{i:<4} {product.name:<25} {product.average_rating:.2f}★ "
                  f"{product.review_count:<8} {product.total_sold}")
    
    def inventory_status_alerts(self):
        """Display inventory status and generate alerts."""
        print("\n⚠️ INVENTORY STATUS & ALERTS")
        print("-" * 35)
        
        # Critical stock alerts
        critical_stock = [p for p in self.products.values() 
                         if p.stock_quantity <= p.min_stock_level]
        
        if critical_stock:
            print("🔴 CRITICAL STOCK ALERTS:")
            print(f"{'Product':<25} {'Current':<8} {'Min Level':<10} {'Reorder'}")
            print("-" * 55)
            
            for product in sorted(critical_stock, key=lambda p: p.stock_quantity):
                recommended_order = (product.max_stock_level - product.stock_quantity)
                print(f"{product.name:<25} {product.stock_quantity:<8} "
                      f"{product.min_stock_level:<10} {recommended_order}")
        
        # Overstock alerts
        overstock = [p for p in self.products.values() 
                    if p.stock_quantity > p.max_stock_level * 0.8 and p.total_sold < 5]
        
        if overstock:
            print(f"\n🟡 OVERSTOCK ALERTS:")
            print(f"{'Product':<25} {'Current':<8} {'Sales':<8} {'Recommendation'}")
            print("-" * 65)
            
            for product in overstock[:10]:
                print(f"{product.name:<25} {product.stock_quantity:<8} "
                      f"{product.total_sold:<8} Consider promotion/discount")
        
        # Inventory turnover analysis
        print(f"\n📊 INVENTORY TURNOVER ANALYSIS")
        print("-" * 40)
        
        high_turnover = [p for p in self.products.values() 
                        if hasattr(p, 'inventory_turnover') and p.inventory_turnover > 12]
        low_turnover = [p for p in self.products.values() 
                       if hasattr(p, 'inventory_turnover') and p.inventory_turnover < 4]
        
        print(f"High Turnover Products (>12x/year): {len(high_turnover)}")
        print(f"Low Turnover Products (<4x/year): {len(low_turnover)}")
        
        if high_turnover:
            print("\nTop High Turnover Products:")
            for product in sorted(high_turnover, 
                                key=lambda p: p.inventory_turnover, reverse=True)[:5]:
                print(f"  • {product.name}: {product.inventory_turnover:.1f}x turnover")
        
        # Summary statistics
        total_inventory_value = sum(p.stock_quantity * p.cost for p in self.products.values())
        print(f"\n📈 INVENTORY SUMMARY")
        print("-" * 25)
        print(f"Total Inventory Value: ${total_inventory_value:,.2f}")
        print(f"Products Below Min Stock: {len(critical_stock)}")
        print(f"Products Overstocked: {len(overstock)}")
        print(f"Average Stock Level: {statistics.mean([p.stock_quantity for p in self.products.values()]):.1f} units")
    
    def run(self):
        """Main analytics platform loop."""
        print("📊 Welcome to the E-Commerce Analytics Platform!")
        print("Comprehensive business intelligence for data-driven retail success.")
        
        while True:
            self.display_main_menu()
            choice = self.get_menu_choice()
            
            if choice == 0:
                print("\n📊 Thank you for using the E-Commerce Analytics Platform!")
                print("Data-driven decisions lead to business success!")
                break
            elif choice == 1:
                self.executive_summary()
            elif choice == 2:
                self.sales_analytics()
            elif choice == 3:
                self.customer_analytics()
            elif choice == 4:
                self.product_performance()
            elif choice == 5:
                print("🚧 Marketing analytics coming soon!")
            elif choice == 6:
                print("🚧 Operational analytics coming soon!")
            elif choice == 7:
                print("🚧 Predictive analytics coming soon!")
            elif choice == 8:
                print("🚧 Recommendation engine coming soon!")
            elif choice == 9:
                print("🚧 Competitive intelligence coming soon!")
            elif choice == 10:
                print("🚧 Data export coming soon!")
            
            print("\n" + "=" * 70)
            input("Press Enter to continue...")

class RecommendationEngine:
    """AI-powered product recommendation system."""
    
    def __init__(self, analytics_platform):
        self.platform = analytics_platform
    
    def generate_recommendations(self, customer_id: str) -> List[str]:
        """Generate product recommendations for a customer."""
        # This would contain collaborative filtering logic
        return []

class PricingOptimizer:
    """Automated pricing optimization system."""
    
    def __init__(self, analytics_platform):
        self.platform = analytics_platform
    
    def optimize_prices(self) -> Dict[str, float]:
        """Generate optimized pricing recommendations."""
        # This would contain pricing algorithm logic
        return {}

class InventoryManager:
    """Intelligent inventory management system."""
    
    def __init__(self, analytics_platform):
        self.platform = analytics_platform
    
    def predict_demand(self, product_id: str) -> float:
        """Predict future demand for a product."""
        # This would contain demand forecasting logic
        return 0.0

def main():
    """Main entry point for the program."""
    analytics_platform = ECommerceAnalytics()
    analytics_platform.run()

if __name__ == "__main__":
    main()

"""
SOLUTION REQUIREMENTS:
=====================
Your solution should include:
1. ✅ Enterprise-level e-commerce data processing and analytics
2. ✅ Advanced customer segmentation and behavior analysis
3. ✅ Comprehensive business intelligence dashboard and reporting
4. ✅ Product performance optimization and inventory management
5. ✅ Revenue analytics with trend analysis and forecasting
6. ✅ Professional business application architecture and design
7. ✅ Statistical analysis and data-driven insights generation
8. ✅ Real-world applicability for retail business operations

LEARNING OUTCOMES:
==================
After completing this problem, you will have mastered:
• Enterprise software development and scalable system architecture
• Business intelligence and analytics platform development
• Advanced data processing, analysis, and statistical computation
• Professional dashboard design and business reporting systems
• E-commerce domain knowledge and retail business operations
• Machine learning concepts applied to business problems
• Complex algorithm optimization and performance considerations
• Real-world application development for business intelligence

EXTENSION IDEAS:
===============
1. Add real-time data streaming and live dashboard updates
2. Implement machine learning algorithms for advanced analytics
3. Create API endpoints for integration with external systems
4. Add advanced data visualization with charts and graphs
5. Implement A/B testing framework for marketing campaigns
6. Add fraud detection and security analytics modules
7. Create mobile analytics app with push notifications
8. Add integration with popular e-commerce platforms (Shopify, etc.)

This capstone problem demonstrates mastery of all programming concepts
while creating an enterprise-grade business intelligence platform!
"""