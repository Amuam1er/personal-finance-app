import tkinter as tk
from tkinter import messagebox
import datetime
import csv
from tkinter import filedialog

FONT = ("Segoe UI", 11)
HEADER_FONT = ("Segoe UI", 12, "bold")
# ========== VARIABLES ==========
income = 0
expenses = 0
transactions = []

# ========== FUNCTIONS ==========
def export_to_csv():
    if not transactions:
        messagebox.showinfo("No Data", "There are no transactions to export.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        title="Save transactions as CSV"
    )

    if file_path:
        try:
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Type", "Amount", "Note", "Timestamp"])
                for t in transactions:
                    writer.writerow([t["type"], t["amount"], t["note"], t["timestamp"]])
            messagebox.showinfo("Exported", f"Transactions exported successfully to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export:\n{str(e)}")

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
app.title(" My Personal Finance App")
app.geometry("600x500")  # Width x Height
app.configure(bg="#f5f5f5")

# Input Fields
amount_label = tk.Label(app, text="Amount:", font=HEADER_FONT, bg="#f5f5f5")
amount_label.pack(pady=(10, 0))  # Add some padding
amount_entry = tk.Entry(app, font=FONT, width=30)
amount_entry.pack(pady=5)

note_label = tk.Label(app, text="Note:", font=HEADER_FONT, bg="#f5f5f5")
note_label.pack(pady=(10, 0))  # Add some padding
note_entry = tk.Entry(app, font=FONT, width=30)
note_entry.pack(pady=5)

# Buttons
add_income_button = tk.Button(app, text="Add Income", font=FONT, bg="#4CAF50", fg="white", padx=10, pady=5, command=add_income)
add_income_button.pack(pady=5)

add_expense_button = tk.Button(app, text="Add Expense", font=FONT, bg="#F44336", fg="white", padx=10, pady=5, command=add_expense)
add_expense_button.pack(pady=5)

view_balance_button = tk.Button(app, text="View Balance Sheet", font=FONT, bg="#2196F3", fg="white", padx=10, pady=5, command=view_balance_sheet)
view_balance_button.pack(pady=5)

export_button = tk.Button(app, text="Export to CSV", font=FONT, bg="#FF9800", fg="white", padx=10, pady=5, command=export_to_csv)
export_button.pack(pady=(10, 0))

# Output Text Area
output_text = tk.Text(app, height=15, width=70, font=("Courier New", 10), bg="white", fg="black")
output_text.pack(padx=10, pady=10)

# Exit Button
exit_button = tk.Button(app, text="Exit", font=FONT, bg="#9E9E9E", fg="white", padx=10, pady=5, command=app.quit)
exit_button.pack(pady=5)

# ========== RUN THE APP ==========
app.mainloop()