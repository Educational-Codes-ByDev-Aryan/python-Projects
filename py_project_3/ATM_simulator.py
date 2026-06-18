# variables
bank = ["20000"]
balance = 20000
statements = ["show balance", "deposite", "my amount"]
pin = 882005

# starting point
choose_activity = input(f"Choose from : {statements}:\n")

# simple logic
match choose_activity:
    case "show balance":
        pinNum = int(input(f"Enter a pin : "))
        if pinNum == pin:
            print(f"Your balance is {balance}")

    case "deposite":
        deposite = int(input("Deposit amount: "))
        if deposite < 500:
            print("Please deposit amount greater than 500")
        else:
            balance += deposite
            print(f"The amount {deposite} successfully deposite")
            print(f"an your current balance is {balance}")

    case "my amount":
        withdraw_money = int(input("Enter the withdrawal amount: "))
        print(f"successfully withdrawed {withdraw_money}")
        if withdraw_money > balance:
            print(
                "Sorry Balance Insufficient! You can't withdraw money \n Please Enter Small amount"
            )
        else:
            balance -= withdraw_money
            print(f"Your availabel balance is {balance}")

    case _:
        print("Please choose a valid activity from the list")
