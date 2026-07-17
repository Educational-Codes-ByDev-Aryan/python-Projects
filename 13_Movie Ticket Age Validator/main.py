# Movie Ticket Age Validator

class AgeError(Exception): # custom Exception
    pass

class Movie :

    def __init__(self,movie_name,minimum_age): # constructor method
        self.movie_name = movie_name
        self.minimum_age = minimum_age

    def book_ticket(self,age): # method

        if age < self.minimum_age :

            #  raising error
            raise AgeError("Please enter the valid age")
        
        else:
            print("Ticket Booked Successfully !")

# object Created
p1 = Movie("My Fault",18)

# Exception Handling
try:

    p1.book_ticket(12)

except AgeError as e:

    print(e)