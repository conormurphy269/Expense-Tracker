from datetime import datetime

class Expense: 
    def __init__(self, amount, category, date, description):
        self.amount = amount 
        self.category = category
        self.date = date 
        self.description = description
        
    def __str__(self):
        return f"{self.date.strftime('%D-%M-%Y')} - {self.category}: £{self.amount} - {self.description}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        
    def add_expense(self, amount, category, date, description):
        expense = Expense(amount, category, date, description)
        self.expenses.append(expense)
        
    def view_expenses(self):
        for expense in self.expenses:
            print(expense)
            