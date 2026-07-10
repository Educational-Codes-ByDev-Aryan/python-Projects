
# Python OOP Banking System
class Bankaccount :
    bank_name = "State Bank"

    def __init__(self,Customer_name,Balance):
        self.Customer_name = Customer_name
        self.Balance = Balance

    # instance method
    def show_account(self):
        print(f"Customer name is {self.Customer_name} and the balance is {self.Balance} an from bank {Bankaccount.bank_name} ")

    # class method
    @classmethod
    def change_bank(cls,new_bank):
        cls.bank_name = new_bank

    # static method
    @staticmethod
    def calculate_gst(amount):
     gst = amount * 18 / 100

     return gst
    
    
c1 = Bankaccount("Jack",600)
c1.show_account()
print(Bankaccount.calculate_gst(c1.Balance))

# changing the bank name
Bankaccount.change_bank("PostBank")

c2 = Bankaccount("Jack",600)
c2.show_account()
print(Bankaccount.calculate_gst(c2.Balance))

c3 = Bankaccount("John", 1200)
c3.show_account()
print(Bankaccount.calculate_gst(c3.Balance))

# Ex gst calculation
print(Bankaccount.calculate_gst(5000))