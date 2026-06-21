expenses = []

while True:
    expense = input("Enter expense (or 'q' to quit): ")

    if expense.lower() == 'q':
        break

    expenses.append(float(expense))

print("\nExpenses:", expenses)
print("Total Spent:", sum(expenses))