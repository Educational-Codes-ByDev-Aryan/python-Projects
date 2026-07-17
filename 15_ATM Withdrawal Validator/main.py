
# ATM Withdrawal Validator using class and function
class AtmValidator:

        def __init__(self):
            self.bank = 5000

        def get_amount(self):

            while True:
                try:
                    amount = int(input("Enter the withdrawal amount: "))

                except ValueError:
                    print("Please enter a valid amount.")
                    continue

                if amount <= 0:
                    print("Invalid amount.")

                elif amount > self.bank:
                    print("Insufficient Balance.")

                else:
                    self.bank = self.bank - amount
                    print("Withdrawal Successful")
                    print(f"Remaining Balance: {self.bank}")
                    break


man = AtmValidator()
man.get_amount()
