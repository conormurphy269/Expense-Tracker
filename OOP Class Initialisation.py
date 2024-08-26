from datetime import datetime

class Expense: 
    def __init__(self, amount, category, date, description):
        self.amount = amount 
        self.category = category
        self.date = date 
        self.description = description
        
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.category}: £{self.amount} - {self.description}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        
    def expense_input(self):
        amount = float(input("Enter the amount: £"))
        category = input("Enter the category of the expense: ")
        date_input = input("Enter the date: (YYYY-MM-DD): ")
        date = datetime.strptime(date_input, '%Y-%m-%d').date()
        description = input("Enter description of expense: ")
        self.add_expense(amount, category, date, description)
            
    def add_expense(self, amount, category, date, description):
        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        
    def view_expenses(self):
        for expense in self.expenses:
            print(expense)


if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            tracker.expense_input()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

