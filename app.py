import tkinter as tk
from tkinter import simpledialog, messagebox
import json
from datetime import datetime
import os

# Create the main app window
app = tk.Tk()
app.title("Personal Finance App")
app.geometry("300x200")

# Load existing transactions or start a new list
if os.path.exists("transactions.json"):
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
else:
    transactions = []

# Save transactions to file
def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

# Add a transaction (income or expense)
def add_transaction(t_type):
    amount = simpledialog.askfloat(f"Add {t_type.capitalize()}", "Enter amount:")
    note = simpledialog.askstring("Note", "Enter a note for this transaction:")
    
    if amount and note:
        transactions.append({
            "timestamp": datetime.now().isoformat(),
            "type": t_type,
            "amount": amount,
            "note": note
        })
        save_transactions()
        messagebox.showinfo("Success", f"{t_type.capitalize()} added!")

# Show balance sheet
def show_balance():
    income = sum(t["amount"] for t in transactions if t["type"] == "income")
    expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    balance = income - expense
    
    messagebox.showinfo("Balance Sheet", 
                        f"Total Income: ${income:.2f}\n"
                        f"Total Expenses: ${expense:.2f}\n"
                        f"Net Balance: ${balance:.2f}")

# Buttons
btn_income = tk.Button(app, text="Add Income", command=lambda: add_transaction("income"))
btn_income.pack(pady=5)

btn_expense = tk.Button(app, text="Add Expense", command=lambda: add_transaction("expense"))
btn_expense.pack(pady=5)

btn_balance = tk.Button(app, text="View Balance Sheet", command=show_balance)
btn_balance.pack(pady=5)

btn_exit = tk.Button(app, text="Exit", command=app.quit)
btn_exit.pack(pady=5)

# Run the app
app.mainloop()