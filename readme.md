# Student Expense Tracker
## Overview
Student Expense Tracker is a small Python applica8on that
I made to note down my daily expenses and see how
much I am spending in a month. It has a simple window
(made with Tkinter) where we can add an expense, search
it, delete it, set a monthly budget and see a report. All the
data is saved in a JSON file on the computer, so nothing is
lost when the program is closed.


This is my first-semester Python project. While making it I
used the things we learned in class like func8ons, classes,
lists, dic8onaries, loops, condi8ons, file handling,
exceptional handling and basic GUI programming.


## Problem Statement
Students spend money many times in a day, for example
on food, travel, sta8onery, books, snacks and online
shopping. Most of us do not write these things down, so at
the end of the month we do not know where the money
went or whether we stayed inside our budget or we have
overspent this month. This project gives a simple way to
record all these expenses at one place and check them
later.


## Objectives
- Record daily expenses.
- Keep expenses in categories.
- Search and filter the saved expenses.
- Delete records that are not needed.
- Find the highest expense.
- Calculate how much is spent in the current month.
- Set a monthly budget and keep track of it.
- Generate a simple expense report.
- Save and load the data locally.
 
 
## Features
 
- Add an expense with amount, category,
descrip8on and date (the date box already shows
today's date, and if it is leT empty today's date is
used).

- Shows all the expenses in a table.

- Filter the table by category (there are 8 categories:
   Food, Travel, Stationery, Books, Snacks,
   Necessities, Online Shopping and
   Entertainment).Search using text (it checks the
    description and the category).
    
- Delete the selected expense (it asks for confirmation first).

- Show the highest expense.

- Set a monthly budget.

- Shows the money spent this month and the budget status in green, orange, red or grey colour.

- A warning box comes when 80% of the budget is used or when the budget is crossed.

- Generate an expense report (total, average, highest, lowest and category-wise spending).

- Saves everything in expenses.json .


## Technologies

- Python 3

- Tkinter (for the GUI)

- JSON (for saving data)

- Git/GitHub

- VS Code

- Matplotlib is not needed in the final version. Only the
 built-in Python modules are used, so nothing extra has to
 be installed.

 
## Project Structure

- expense_tracker/

  - main.py
  - gui.py
  - expense_manager.py
  - budget.py
  - reports.py
  - storage.py
  - expenses.json
  - README.md
  - statement.md
  - tests.py 
  
I want to add it before final submission
expenses.json is created by the program when the
first expense or budget is saved.



## File Description
- main.py - starts the application.

- gui.py - has the Tkinter window, the buttons and
what happens when they are clicked.

- expense_manager.py - has the ExpenseManager
class which adds, deletes, searches and
calculates expenses.

- budget.py - checks the budget entered by the
user and tells the budget status.

- reports.py makes the expense report and the
spending totals.

- storage.py saves the data to the JSON file and
loads it back.

- expenses.json the saved expenses and budget


## Installation and Running

1. Install Python 3 on your computer (Tkinter comes
along with it in most cases).

2. Open the project folder in VS Code.

5. Run this command in the terminal:
python3 main.py

On some computers the command may be.
python main.py instead. No external library is needed.


## Testing

I have a test the program by using I built functions. The things it tests are:

1. Add a valid expense.
2. Try an invalid amount or a wrong date and check the
error message.
3. Filter by category.
4. Search for an expense.
5. Delete a selected expense.
6. Set a monthly budget.
7. Check the budget warning/status.
8. Open the expense report.
9. Close the program, open it again and check that the
saved data is loaded.
I have written a tests.py file. I think it is a good idea
to add one for automatic testing before the
final submission


## Functional Requirements

1. Add expenses.
2. Display and delete expenses.
3. Search and filter expenses.
4. Calculate monthly spending.
5. Set a monthly budget.
6. Monitor the budget status.
7. Generate reports.
8. Save and load data.

   
## Non-functional Requirements

- Usability: the interface is simple, with forms, bubons
and a table, so user can use it easily.

- Reliability: saved data is loaded again when the
program starts, and wrong inputs are handled.

- Maintainability: each file does one job, so it is easier
to understand and change the code.

- Performance: it is fine for the normal number of
expenses a student will have.

- Resource eﬃciency: it only uses one small local JSON
file.

- Error handling: if the input is wrong, a clear message
is shown to the user.


## GitHub
The repository link will be in this format:
hbps://github.com/Vidushi022/expense_tracker


## Future Enhancements

- Add automated unit tests.

- Export the data to a CSV file.

- Let the user add custom categories.

- A calendar view for expenses.

- Different profiles for multiple users.

- Charts, if external libraries are allowed.
