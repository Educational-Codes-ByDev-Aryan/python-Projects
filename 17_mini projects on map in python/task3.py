# Find the Length of Each Name
names = ["aryan", "rahul", "priya", "neha"]

length_=list(map(lambda x:x.__len__(),names))
print(length_)