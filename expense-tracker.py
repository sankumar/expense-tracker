import csv


expenses = []
budget_limit = 0.0
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expense():
    global expenses
    if not expenses:
        print("No expenses recorded.")
        return
    print("\n--- Expenses ---")
    for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense['date']} | {expense['category']} | ₹{expense['amount']} | {expense['description']}")
    print()

def track_budget():
    global budget_limit
    if budget_limit == 0:
        budget_limit = float(input("Enter your monthly budget: ₹"))
    total_spent = sum(e["amount"] for e in expenses)
    print(f"\n Total Spent: ₹{total_spent}")
    print(f"Budget Limit: ₹{budget_limit}")
    remaining = budget_limit - total_spent
    print(f"Remaining Budget: ₹{remaining}")
    if total_spent > budget_limit:
        print("Warning: You have exceeded your budget!\n")
    else:
        print("You're within the budget.\n")

def save_expenses():
    filename = "expenses.csv"
    with open(filename, mode="w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to '{filename}'\n")

def main():
    while True:
        print("--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")
        choice = input("Choose an option(1-5): ")
        print(f"User entered choice: {choice}")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            print("Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again! \n")
        main()