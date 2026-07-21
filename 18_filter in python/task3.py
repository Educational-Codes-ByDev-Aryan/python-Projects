# ===========================================
# Python filter() Practice Task - 3
# ===========================================

# You have a list of email addresses.

# emails = [
#     "rahul@yahoo.com",
#     "priya@gmail.com",
#     "neha@hotmail.com",
#     "amit@gmail.com"
# ]

# Task:
# Use filter() with a lambda function.

# Condition:
# Keep only the email addresses that end with "@gmail.com".

# Expected Output:
# [
#     "priya@gmail.com",
#     "amit@gmail.com"
# ]

# Rules:
# 1. Use filter()
# 2. Use lambda
# 3. Do NOT use a for loop.
# 4. Convert the filter object into a list before printing.

# Write your code below:

emails = [
    "rahul@yahoo.com",
    "priya@gmail.com",
    "neha@hotmail.com",
    "amit@gmail.com"
]

ending = list(filter(lambda x:x.endswith("@gmail.com"),emails))
print(ending)