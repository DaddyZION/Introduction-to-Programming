"""
Assignment 4 - Exercise 5: Comprehensive Validation Challenge
Difficulty: 🔴 Expert

TODO: Build a complete e-commerce order validation system.

This comprehensive exercise combines all validation concepts in a real-world scenario.
"""

# ==================== E-COMMERCE ORDER VALIDATION SYSTEM ====================

"""
SYSTEM REQUIREMENTS:
===================

Create a complete order validation system for an online store that validates:
1. Customer information
2. Shipping address
3. Product selections
4. Payment information
5. Order totals and discounts

DATA STRUCTURES:
---------------

Customer:
{
    'customer_id': '12345',
    'name': 'John Doe',
    'email': 'john@example.com',
    'phone': '123-456-7890',
    'member_since': '2020-01-15'
}

Shipping Address:
{
    'street': '123 Main St',
    'city': 'Springfield',
    'state': 'IL',
    'zip_code': '62701',
    'country': 'USA'
}

Product:
{
    'product_id': 'PROD001',
    'name': 'Widget',
    'price': 29.99,
    'quantity': 2,
    'in_stock': True
}

Payment:
{
    'card_number': '4532-1234-5678-9010',
    'expiry': '12/25',
    'cvv': '123',
    'billing_zip': '62701'
}

Order:
{
    'order_id': 'ORD12345',
    'customer': Customer,
    'shipping': Shipping Address,
    'products': [Product, Product, ...],
    'payment': Payment,
    'subtotal': 0.0,
    'tax': 0.0,
    'shipping_cost': 0.0,
    'discount': 0.0,
    'total': 0.0
}
"""


# ==================== VALIDATION FUNCTIONS ====================

def validate_customer_info(customer):
    """
    Validate customer information.
    
    Requirements:
    - customer_id: 5-digit number
    - name: 2-50 characters
    - email: valid format
    - phone: valid format
    - member_since: valid date format (YYYY-MM-DD)
    
    Returns: (is_valid, errors_list)
    """
    # TODO: Implement this function
    pass


def validate_shipping_address(address):
    """
    Validate shipping address.
    
    Requirements:
    - street: not empty, max 100 chars
    - city: not empty, max 50 chars
    - state: 2-letter code
    - zip_code: 5 digits (US) or appropriate format
    - country: valid country code
    
    Returns: (is_valid, errors_list)
    """
    # TODO: Implement this function
    pass


def validate_product(product):
    """
    Validate product information.
    
    Requirements:
    - product_id: not empty, alphanumeric
    - name: not empty
    - price: positive number, max 2 decimal places
    - quantity: positive integer, max 100
    - in_stock: boolean, must be True
    
    Returns: (is_valid, errors_list)
    """
    # TODO: Implement this function
    pass


def validate_payment_info(payment):
    """
    Validate payment information.
    
    Requirements:
    - card_number: valid length (13-16 digits)
    - expiry: valid format (MM/YY), not expired
    - cvv: 3 or 4 digits
    - billing_zip: 5 digits
    
    Returns: (is_valid, errors_list)
    """
    # TODO: Implement this function
    pass


def calculate_order_total(products, tax_rate=0.08, shipping_cost=5.99):
    """
    Calculate order totals.
    
    Requirements:
    - Calculate subtotal from all products
    - Apply tax rate
    - Add shipping cost
    - Free shipping if subtotal > $50
    - Return dictionary with breakdown
    
    Returns: {
        'subtotal': float,
        'tax': float,
        'shipping': float,
        'total': float
    }
    """
    # TODO: Implement this function
    pass


def apply_discount_code(order_total, discount_code):
    """
    Apply discount code to order.
    
    Valid codes:
    - 'SAVE10': 10% off
    - 'SAVE20': 20% off (only if subtotal > $100)
    - 'FREESHIP': Free shipping
    - 'FIRST': $15 off first order (check customer.member_since is recent)
    
    Returns: (new_total, discount_amount, message)
    """
    # TODO: Implement this function
    pass


def validate_complete_order(order):
    """
    Validate an entire order with all components.
    
    Requirements:
    - Validate customer info
    - Validate shipping address
    - Validate all products
    - Validate payment info
    - Validate totals are calculated correctly
    - Check for any fraud indicators
    
    Fraud checks:
    - Shipping state different from billing zip
    - Order total > $1000 (flag for review)
    - More than 10 items of same product
    
    Returns: (is_valid, validation_report)
    validation_report: {
        'customer_valid': bool,
        'shipping_valid': bool,
        'products_valid': bool,
        'payment_valid': bool,
        'totals_valid': bool,
        'fraud_flags': list,
        'errors': list,
        'warnings': list
    }
    """
    # TODO: Implement this function
    pass


def process_order_interactive():
    """
    Interactive order processing system.
    
    Steps:
    1. Collect customer information
    2. Collect shipping address
    3. Select products (menu-driven)
    4. Review order and edit if needed
    5. Enter payment information
    6. Apply discount code (optional)
    7. Validate complete order
    8. Display final order summary
    9. Confirm or cancel
    
    Features:
    - Input validation at each step
    - Allow going back to previous steps
    - Save order to "file" (dictionary/list)
    - Generate order confirmation
    """
    # TODO: Implement this function
    print("=== E-Commerce Order Processing System ===\n")
    
    # TODO: Step-by-step order collection
    
    # TODO: Validation at each step
    
    # TODO: Final order review and confirmation
    
    pass


# ==================== TEST DATA ====================

SAMPLE_CUSTOMER = {
    'customer_id': '12345',
    'name': 'John Doe',
    'email': 'john@example.com',
    'phone': '123-456-7890',
    'member_since': '2024-01-15'
}

SAMPLE_ADDRESS = {
    'street': '123 Main St',
    'city': 'Springfield',
    'state': 'IL',
    'zip_code': '62701',
    'country': 'USA'
}

SAMPLE_PRODUCTS = [
    {
        'product_id': 'PROD001',
        'name': 'Widget',
        'price': 29.99,
        'quantity': 2,
        'in_stock': True
    },
    {
        'product_id': 'PROD002',
        'name': 'Gadget',
        'price': 49.99,
        'quantity': 1,
        'in_stock': True
    }
]

SAMPLE_PAYMENT = {
    'card_number': '4532-1234-5678-9010',
    'expiry': '12/25',
    'cvv': '123',
    'billing_zip': '62701'
}


# ==================== TEST CODE ====================
if __name__ == "__main__":
    print("=== Testing E-Commerce Validation System ===\n")
    
    print("Test 1: Customer Validation")
    # result = validate_customer_info(SAMPLE_CUSTOMER)
    # print(f"  Result: {result}\n")
    
    print("Test 2: Address Validation")
    # result = validate_shipping_address(SAMPLE_ADDRESS)
    # print(f"  Result: {result}\n")
    
    print("Test 3: Product Validation")
    # for product in SAMPLE_PRODUCTS:
    #     result = validate_product(product)
    #     print(f"  {product['name']}: {result}")
    
    print("\nTest 4: Payment Validation")
    # result = validate_payment_info(SAMPLE_PAYMENT)
    # print(f"  Result: {result}\n")
    
    print("Test 5: Order Total Calculation")
    # result = calculate_order_total(SAMPLE_PRODUCTS)
    # print(f"  Order totals: {result}\n")
    
    print("Test 6: Complete Order Validation")
    # sample_order = {
    #     'order_id': 'ORD12345',
    #     'customer': SAMPLE_CUSTOMER,
    #     'shipping': SAMPLE_ADDRESS,
    #     'products': SAMPLE_PRODUCTS,
    #     'payment': SAMPLE_PAYMENT
    # }
    # result = validate_complete_order(sample_order)
    # print(f"  Validation report: {result}\n")
    
    print("\nTo test interactive system, uncomment and run:")
    print("  # process_order_interactive()")
