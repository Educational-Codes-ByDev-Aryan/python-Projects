# Upgraded logic using decorators
def my_decorators(my_func):
    def sourrounding():
        print("\nPassword Strength Checker Started!...\n")

        my_func()
        print("\nPassword Strength Checker Ended.....\n")

    return sourrounding

@my_decorators
def check():
    password = input("Enter a password\n")
    length = password.__len__()
    digit = 0
    count = 0
    print("The length of the password is", length)
    
    # conditions applied
    if length < 8:
        print("The password must be at least 8 characters")

    else:
        for n in password:
            if n.isdigit():
                digit += 1
        if digit <= 2:
            print("should contain at least 2 digits")
        else:
            for ch in password:
                if ch.isupper():
                    count += 1
        if count <= 3:
            print("should contain atleast 3 upper case letters")

        else:
            print("Your password is strongest password")


check()
