# Expense Tracker

A desktop expense tracker for college students, using python and tkinter. 
It lets you record daily spending, track where your money goes, and check whether you stay within a monthly budget or not.
The main function of this project is to help college students to keep an eye on their daily expenses and monthly budget.

## Features this project have which are suitable for college students

- Add an expense with a title, amount, category, and date
- Categories :
  -Stationery
  -Food
  -Travel 
  -Snacks 
  -Books
  -Necessities 
  -Online Shopping
- View all expenses entered in the application
- Filter the expense by their category
- Delete a selected expense from the list
- calculate the total spent, find the expense with the highet amount , see how much has been spent in each category , set the mothly budget, calculate how much of the budget is still remaining 
- check whether the monthly budget has ben exeeded
- enter data safely using validation 


## Requirements

- Python 3
- Tkinter, which comes with Python on Windows and macOS. On Linux, install it with:

 apt install python3-tk


## Setup and run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run the app: python gui.py


On some systems the command is "python3" instead of "python".

## Project structure


expense_tracker

├── tracker.py   # (Expense and ExpenseTracker classes (data and calculations) and does not contain the screen or tkinter interface)
   - add_expense()  # (the new expense is added)
   - delete_expense() #(delete an expense)
   - total() #(total ammout spent)
   - total_by_category() #(totals according tothe category) 
   - search_by_category() #(filter the expenses by category) 
   - ighest_expense() #(finds the highest expense in all category)
   - set_budget() #(stores mothly budget entered by user) 
   - month_total() #(totals the monthly expense) 
   - remaining_budget() #(calculate how much money is left from the monthly budget) 
   - is_over_budget()| #(find if user exeeds their monthly budget or not)

     
├── gui.py       # Tkinter window (run this file) imprts function from  tracker.py file and contains screen 
   - add an expense 
   - expense table 
   - filter and delete (The user can select a category from the filter option)
   - Summary(The summary section shows useful information about the expenses)
   - Budget(The user can enter a monthly budget through the GUI)
   - Input Validation(I added input validation so that incorrect values do not cause the program to crash)

     
└── README.md


## How it works
User enters expense
        ↓
gui.py checks the input
        ↓
Expense object is created
        ↓
tracker.py stores the expense
        ↓
GUI refreshes the table
        ↓
Summary is updated
- 'tracker.py' stores the expenses and does the calculations, while it has no screen code.
- "gui.py" takes the user's input, displays the information, and calls the functions from `tracker.py`. it has screen code 
- Every time an expense is added, deleted, filtered, or the budget changes, the table and summary are redrawn from the tracker's data.
- The budget covers the current calendar month. Only expenses dated in this month count toward it.

## Python concepts used

- Classes and objects ('Expense', 'ExpenseTracker', 'ExpenseApp')
- Tuple (the fixed list of categories)
- list (all expenses)
- dictionary (totals by category)
- Loops and if-else statements
- Functions and a user-defined module ('tracker.py' is imported by 'gui.py')
- String slicing
- string formatting
- type conversion
- Tkinter for the graphical interface

## Notes
The expenses are currently stored only while the program is running.
If the application is closed, the expenses are lost because the
project does not currently use a database or file for permanent
storage.
A future version could add a database or file so that expenses are
saved automatically.
Author-
Expense Tracker project made as a Python/Tkinter project.
 
---

# 4. Final project structure

Your GitHub repository can therefore look like this:

expense_tracker/
│
├── tracker.py
├── gui.py
└── README.md
