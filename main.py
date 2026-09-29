"""
main.py

This is the file used to start/open the window of the Expense Tracker.
"""

import tkinter as tk

from expense_manager import ExpenseManager
from gui import ExpenseTrackerApp


def main():
    manager = ExpenseManager()   # object that manages all the expenses
    root = tk.Tk()               # main tkinter window
    ExpenseTrackerApp(root, manager)   # put our expense tracker inside the window
    root.mainloop()              # keep the program running


if __name__ == "__main__":
    main()
