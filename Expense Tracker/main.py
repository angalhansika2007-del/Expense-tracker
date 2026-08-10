expenses = []

while True:
    print("\n" + "=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter Expense Name: ")

        try:
            amount = float(input("Enter Amount: "))
            expenses.append((item, amount))
            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\nExpense List")
            for item, amount in expenses:
                print(f"{item} - ₹{amount:.2f}")

    elif choice == "3":
        total = sum(amount for item, amount in expenses)
        print(f"\nTotal Expense: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")