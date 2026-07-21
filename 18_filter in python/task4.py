# ===========================================
# Python filter() Practice Task - 4 (Real World)
# ===========================================

# Imagine you are building a shopping website.

# The warehouse has products that are either in stock (True)
# or out of stock (False).

# products = [
#     {"name": "Laptop", "in_stock": True},
#     {"name": "Mouse", "in_stock": False},
#     {"name": "Keyboard", "in_stock": True},
#     {"name": "Monitor", "in_stock": False},
#     {"name": "Headphones", "in_stock": True}
# ]

# Task:
# Use filter() with a lambda function.

# Condition:
# Keep only the products that are in stock.

# Expected Output:
# [
#     {"name": "Laptop", "in_stock": True},
#     {"name": "Keyboard", "in_stock": True},
#     {"name": "Headphones", "in_stock": True}
# ]

# Rules:
# 1. Use filter()
# 2. Use lambda
# 3. Do NOT use a for loop.
# 4. Convert the filter object into a list before printing.

# Write your code below:
products = [
    {"name": "Laptop", "in_stock": True},
    {"name": "Mouse", "in_stock": False},
    {"name": "Keyboard", "in_stock": True},
    {"name": "Monitor", "in_stock": False},
    {"name": "Headphones", "in_stock": True}
]

instocks = list(filter(lambda x:x["in_stock"],products))
print(instocks)