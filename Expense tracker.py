import json

try:
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses = []


while True:

    print("Welcome to the Expense Tracker")
    print("1. Add expense"
          "\n2. View all expenses"
          "\n3. View total"
          "\n4. Exit")
    try:

        choice = int(input("Enter your choice: "))
        if choice == 1:
            expense_name = input("Enter expense: ").strip().title()
            expense_amount = float(input("Enter expense amount: "))
            expense_category = input("Enter expense category: ").strip().title()
            expenses.append({
                "name": expense_name,
                "amount": expense_amount,
                "category": expense_category
            })
            print(f"Expense {expense_name} added!")
            with open("expenses.json", "w") as f:
                json.dump(expenses, f)

        elif choice == 2:
            if not expenses:
                print("No expenses found!")
            else:
                for i, expense in enumerate(expenses, 1):
                    print(f"{i}, {expense['name']} - £{expense['amount']} {expense['category']}")

        elif choice == 3:
            total = sum(expense['amount'] for expense in expenses)
            print(f"Total spending is £{total:.2f}")

        elif choice == 4:
            print("Goodbye!")
            break

    except ValueError:
        print("Please enter valid choice")