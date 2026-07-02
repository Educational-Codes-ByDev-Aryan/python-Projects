# list of expenses added
expensesList = []

print("WELCOME TO EXPENSE TRACKER : bhaio or beheno kharcha km kia krro yaar!")

while True:
    print("===Menu===")
    print("1.Add Expense")
    print("2.View All Expenses")
    print("3.View Total Kharcha")
    print("4.Exit")

    choices = int(input("Please enter your choice : \n"))

    # Add Expenses
    if choices == 1:
        date = input("Kis date prr kharcha kia tha? : \n")
        cateogory = input("Kis type ka kharcha kiya tha ? (food,Travel,Makeup,Books) : \n")
        description = input("Aur details dedo : \n")
        amount = float(input("Enter the amount : \n"))

        expense = {
            "date": date,
            "cateogory": cateogory,
            "description": description,
            "amount": amount
        }
        expensesList.append(expense)
        print("\nExpenses added successfully")

    # View expense
    elif choices == 2:
        if len(expensesList) == 0:
            print("No expense added . jao pehele kharcha kro")
        else:
            print("Ye y aap ka sara expense")
            count = 1
            for eachKhrracha in expensesList:
                print(f"{count} -> {eachKhrracha['date']},{eachKhrracha['cateogory']},{eachKhrracha['description']},{eachKhrracha['amount']}")
                count += 1

    # View total expense
    elif choices == 3:
        total = 0
        for eachKhrracha in expensesList:
            total += eachKhrracha["amount"]
        print("TOTAL KHARRCHA IS :", total)

    elif choices == 4:
        print("Exiting expense tracker. Kharcha sambhal ke rakhna!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
