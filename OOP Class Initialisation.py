from datetime import datetime
import pandas as pd 
import sqlite3
import os

class Expense: 
    def __init__(self, amount, category, date, description):
        self.amount = amount 
        self.category = category
        self.date = date 
        self.description = description
        
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.category}: £{self.amount} - {self.description}"

class ExpenseTracker:
    def __init__(self, filename='ExpenseTracker.xlsx'):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.create_excel_file()
        self.expenses = []

    def create_excel_file(self):
        # Create an empty DataFrame with the appropriate headers
        df = pd.DataFrame(columns=["Amount", "Category", "Date", "Description"])
        df.to_excel(self.filename, index=False)
        print(f"{self.filename} created successfully.")
        
    def expense_input(self):
        amount = float(input("Enter the amount: £"))
        category = input("Enter the category of the expense: ")
        date_input = input("Enter the date: (YYYY-MM-DD): ")
        date = datetime.strptime(date_input, '%Y-%m-%d').date()
        description = input("Enter description of expense: ")
        self.add_expense(amount, category, date, description)
            
    def add_expense(self, amount, category, date, description):
        # Read the existing Excel file into a DataFrame
        df = pd.read_excel(self.filename)

        # Create a new DataFrame with the new expense
        new_expense = pd.DataFrame({
            "Amount": [amount],
            "Category": [category],
            "Date": [date.strftime('%Y-%m-%d')],
            "Description": [description]
        })

        # Append the new expense to the existing DataFrame
        df = pd.concat([df, new_expense], ignore_index=True)

        # Save the updated DataFrame back to the Excel file
        df.to_excel(self.filename, index=False)
        print("Expense added successfully!")
        
    def view_expenses(self):
        # Read the Excel file into a DataFrame
        df = pd.read_excel(self.filename)

        if df.empty:
            print("No expenses recorded.")
        else:
            print(df)

    def save_to_excel(self, filename='ExpenseTracker.xlsx'):
        self.cursor.execute('SELECT * FROM expenses')
        expenses = self.cursor.fetchall()
        
        df = pd.DataFrame(expenses, columns=["ID", "Amount", "Category", "Date", "Description"])
        df.to_excel(filename, index=False)
        print(f"Expenses saved to {filename} successfully!")

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

