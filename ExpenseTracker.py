import customtkinter as ctk
import pandas as pd
from datetime import datetime
import os
import tkinter.messagebox as tkmb
import webbrowser  

class ExpenseTracker:
    def __init__(self, filename='expenses.xlsx'):
        self.filename = filename
        if not os.path.exists(self.filename):
            self.create_excel_file()

    def create_excel_file(self):
        df = pd.DataFrame(columns=["Amount", "Category", "Date", "Description"])
        df.to_excel(self.filename, index=False)
        print(f"{self.filename} created successfully.")

    def add_expense(self, amount, category, date, description):
        df = pd.read_excel(self.filename)

        new_expense = pd.DataFrame({
            "Amount": [amount],
            "Category": [category],
            "Date": [date.strftime('%Y-%m-%d')],
            "Description": [description]
        })

        df = pd.concat([df, new_expense], ignore_index=True)
        df.to_excel(self.filename, index=False)
        print("Expense added successfully!")

    def view_expenses(self):
        df = pd.read_excel(self.filename)
        return df if not df.empty else None

class ExpenseTrackerGUI:
    def __init__(self, tracker):
        self.tracker = tracker

        # Initialize the main window
        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.root = ctk.CTk()  # Create the main window
        self.root.title("Expense Tracker")

        # Set up the main frame
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Widgets for adding expenses
        self.amount_label = ctk.CTkLabel(master=self.frame, text="Amount (£):")
        self.amount_label.grid(row=0, column=0, pady=5, padx=10)

        self.amount_entry = ctk.CTkEntry(master=self.frame)
        self.amount_entry.grid(row=0, column=1, pady=5, padx=10)

        self.category_label = ctk.CTkLabel(master=self.frame, text="Category:")
        self.category_label.grid(row=1, column=0, pady=5, padx=10)

        self.category_entry = ctk.CTkEntry(master=self.frame)
        self.category_entry.grid(row=1, column=1, pady=5, padx=10)

        self.date_label = ctk.CTkLabel(master=self.frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0, pady=5, padx=10)

        self.date_entry = ctk.CTkEntry(master=self.frame)
        self.date_entry.grid(row=2, column=1, pady=5, padx=10)

        self.description_label = ctk.CTkLabel(master=self.frame, text="Description:")
        self.description_label.grid(row=3, column=0, pady=5, padx=10)

        self.description_entry = ctk.CTkEntry(master=self.frame)
        self.description_entry.grid(row=3, column=1, pady=5, padx=10)

        self.add_button = ctk.CTkButton(master=self.frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Widgets for viewing expenses
        self.view_button = ctk.CTkButton(master=self.frame, text="View Expenses", command=self.view_expenses)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)


    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_entry.get()
            date_input = self.date_entry.get()
            date = datetime.strptime(date_input, '%Y-%m-%d').date()
            description = self.description_entry.get()

            self.tracker.add_expense(amount, category, date, description)

            # Clear the entries after adding
            self.amount_entry.delete(0, ctk.END)
            self.category_entry.delete(0, ctk.END)
            self.date_entry.delete(0, ctk.END)
            self.description_entry.delete(0, ctk.END)

            tkmb.showinfo("Success", "Expense added successfully!")  # Use tkinter messagebox
        except ValueError:
            tkmb.showerror("Error", "Please enter valid data!")  # Use tkinter messagebox

    def view_expenses(self):
        # Open the Excel file with the default application
        try:
            os.startfile(self.tracker.filename)  # For Windows
            # For macOS: os.system(f'open "{self.tracker.filename}"')
            # For Linux: os.system(f'xdg-open "{self.tracker.filename}"')
        except Exception as e:
            tkmb.showerror("Error", f"Failed to open the file: {e}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    tracker = ExpenseTracker()
    gui = ExpenseTrackerGUI(tracker)
    gui.run()