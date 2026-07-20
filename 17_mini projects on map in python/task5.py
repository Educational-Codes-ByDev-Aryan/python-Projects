# Create Email Addresses from Usernames
users = ["aryan", "rahul", "priya", "neha"]

gmails = list(map(lambda emails:emails+"@gmail.com",users))
print(gmails)