# ===========================================
# Python filter() Practice Task - 2
# ===========================================

# You have a list of names.

names = ["Aryan", "Rahul", "Amit", "Neha", "Ankit", "Priya"]

# Task:
# Use filter() with a lambda function.

# Condition:
# Keep only the names that start with the letter 'A'.

# Expected Output:
# ['Amit', 'Ankit']

# Rules:
# 1. Use filter()
# 2. Use lambda
# 3. Do NOT use a for loop.
# 4. Convert the filter object into a list before printing.

# Write your code below:

names = [ "Rahul", "Amit", "Neha", "Ankit", "Priya"]

startsWith = list(filter(lambda x:x.startswith("A"),names))
print(startsWith)

