Personal Finance App

A simple personal finance tracker built with Python and Tkinter.
It allows you to add incomes and expenses with a descriptive note (like a GitHub commit message) and view a basic balance sheet at any time.

Features

	•	Add Income: Record money received along with a note.
	•	Add Expense: Record money spent along with a note.
	•	View Balance Sheet: See total income, total expenses, and net balance.
	•	Automatic Timestamps: Each transaction is timestamped.
	•	Local Storage: All transactions are saved in a transactions.json file.

Demo

App Interface:

	•	Simple window with buttons for actions.
	•	Pop-ups to enter amount and notes.
	•	Instant balance sheet summary with one click.

(Optional: You can later add a screenshot if you want.)

How to Run

	1.	Make sure you have Python 3.x installed.
	2.	Clone this repository or download the files.
	3.	In your terminal, navigate to the project folder and run:

python app.py


	4.	The app window will open!

File Structure

personal-finance-app/
├── app.py              # Main application code
├── transactions.json   # (Automatically created to store your data)
└── README.md           # Project description

Future Improvements

	•	Filter transactions by date range.
	•	Categorize expenses (e.g., Food, Transport, Entertainment).
	•	Export transactions to CSV.
	•	Edit or delete transactions.
	•	Add charts for visualization.

License

This project is open-source and free to use.