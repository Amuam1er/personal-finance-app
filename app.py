import tkinter as tk
from tkinter import messagebox
import datetime

# ========== VARIABLES ==========
income = 0
expenses = 0
transactions = []

# ========== FUNCTIONS ==========

def add_income():
    global income
    try:
        amount = float(amount_entry.get())
        note = note_entry.get()

        income += amount
        transactions.append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "type": "Income",
            "amount": amount,
            "note": note
        })
        messagebox.showinfo("Success", f"Income of ${amount:.2f} added.")
        clear_inputs()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for amount.")

def add_expense():
    global expenses
    try:
        amount = float(amount_entry.get())
        note = note_entry.get()

        expenses += amount
        transactions.append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "type": "Expense",
            "amount": amount,
            "note": note
        })
        messagebox.showinfo("Success", f"Expense of ${amount:.2f} added.")
        clear_inputs()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for amount.")

def view_balance_sheet():
    output_text.delete("1.0", tk.END)  # Clear previous output
    if not transactions:
        output_text.insert(tk.END, "No transactions yet.\n")
    else:
        output_text.insert(tk.END, "Date        | Type     | Amount    | Note\n")
        output_text.insert(tk.END, "-" * 60 + "\n")
        for tx in transactions:
            line = f"{tx['date']} | {tx['type']:8} | ${tx['amount']:9.2f} | {tx['note']}\n"
            output_text.insert(tk.END, line)
        output_text.insert(tk.END, "-" * 60 + "\n")
    
    # Show totals
    output_text.insert(tk.END, f"\nTotal Income:    ${income:.2f}\n")
    output_text.insert(tk.END, f"Total Expenses:  ${expenses:.2f}\n")
    output_text.insert(tk.END, f"Current Balance: ${(income - expenses):.2f}\n")

def clear_inputs():
    amount_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

# ========== GUI SETUP ==========

app = tk.Tk()
app.title("Personal Finance App")
app.geometry("600x500")  # Width x Height

# Input Fields
amount_label = tk.Label(app, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(app)
amount_entry.pack()

note_label = tk.Label(app, text="Note:")
note_label.pack()
note_entry = tk.Entry(app)
note_entry.pack()

# Buttons
add_income_button = tk.Button(app, text="Add Income", command=add_income)
add_income_button.pack(pady=5)

add_expense_button = tk.Button(app, text="Add Expense", command=add_expense)
add_expense_button.pack(pady=5)

view_balance_button = tk.Button(app, text="View Balance Sheet", command=view_balance_sheet)
view_balance_button.pack(pady=5)

# Output Text Area
output_text = tk.Text(app, height=15, width=70)
output_text.pack(pady=10)

# Exit Button
exit_button = tk.Button(app, text="Exit", command=app.quit)
exit_button.pack(pady=5)

# ========== RUN THE APP ==========
app.mainloop()