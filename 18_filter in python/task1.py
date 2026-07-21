# ===========================================
# Python filter() Practice Task - 1
# ===========================================

# You have a list of ages.

# ages = [12, 18, 25, 15, 30, 10, 21]

# Task:
# Use filter() with a lambda function.

# Condition:
# Keep only the ages that are greater than or equal to 18.

# Expected Output:
# [18, 25, 30, 21]

# Rules:
# 1. Use filter()
# 2. Use lambda
# 3. Do NOT use a for loop.
# 4. Convert the filter object into a list before printing.

# Write your code below:

ages = [12, 18, 25, 15, 30, 10, 21]

greater= list(filter(lambda x:x>=18,ages))
print(greater)