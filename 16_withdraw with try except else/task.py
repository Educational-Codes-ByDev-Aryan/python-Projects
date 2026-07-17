ATM_Balance = 10000


try:
    user = int(input("Enter the amount to withdraw : "))

except ValueError as e:
    print(e)
else:   
    if user > ATM_Balance :

        print("Insufficient Balance")

    elif(user<=0):
        print("Enter a valid amount.")

    else:
        ATM_Balance = ATM_Balance - user
        print(f"Withdrawal Successful!\nRemaining Balance: {ATM_Balance}")