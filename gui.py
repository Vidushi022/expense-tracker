"""
gui.py

This file creates the main window of the Student Expense Tracker.
Tkinter is used to make the buttons, forms and tables.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import date

import budget
import reports

from expense_manager import CATEGORIES


class ExpenseTrackerApp:

    def __init__(self, root, manager):
        self.root = root
        self.manager = manager

        self.root.title("Student Expense Tracker")
        self.root.geometry("900x650")

        # build all the sections of the window
        self.build_form()
        self.build_search()
        self.build_table()
        self.build_summary()
        self.build_buttons()

        # show the saved expenses when the program starts
        self.refresh_table()
        self.update_summary()

    # ---------------- ADD EXPENSE SECTION ----------------

    def build_form(self):
        frame = ttk.LabelFrame(self.root, text="Add New Expense")
        frame.pack(fill="x", padx=10, pady=8)

        ttk.Label(frame, text="Amount (Rs.)").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(frame, width=15)
        self.amount_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Category").grid(row=0, column=2, padx=5)
        self.category_box = ttk.Combobox(frame, values=CATEGORIES, state="readonly", width=18)
        self.category_box.grid(row=0, column=3, padx=5)

        ttk.Label(frame, text="Description").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(frame, width=30)
        self.desc_entry.grid(row=1, column=1, columnspan=2, padx=5)

        ttk.Label(frame, text="Date").grid(row=1, column=3, padx=5)
        self.date_entry = ttk.Entry(frame, width=14)
        # put today's date in the box by default
        self.date_entry.insert(0, date.today().strftime("%d-%m-%Y"))
        self.date_entry.grid(row=1, column=4, padx=5)

        ttk.Button(frame, text="Add Expense", command=self.add_expense).grid(row=0, column=4, padx=10)

    # ---------------- SEARCH SECTION ----------------

    def build_search(self):
        frame = ttk.LabelFrame(self.root, text="Search Expenses")
        frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(frame, text="Category:").pack(side="left", padx=5)

        self.filter_box = ttk.Combobox(frame, values=["All"] + CATEGORIES, state="readonly", width=18)
        self.filter_box.set("All")
        self.filter_box.pack(side="left", padx=5)

        ttk.Button(frame, text="Filter", command=self.search_category).pack(side="left", padx=3)
        ttk.Button(frame, text="Show All", command=self.refresh_table).pack(side="left", padx=3)

        ttk.Label(frame, text="Search:").pack(side="left", padx=(20, 5))

        self.search_entry = ttk.Entry(frame, width=20)
        self.search_entry.pack(side="left", padx=5)

        ttk.Button(frame, text="Search", command=self.search_text).pack(side="left", padx=3)

    # ---------------- TABLE SECTION ----------------

    def build_table(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=10, pady=8)

        columns = ("date", "category", "description", "amount")

        self.table = ttk.Treeview(frame, columns=columns, show="headings")

        # column headings
        self.table.heading("date", text="Date")
        self.table.heading("category", text="Category")
        self.table.heading("description", text="Description")
        self.table.heading("amount", text="Amount")

        # column widths
        self.table.column("date", width=110)
        self.table.column("category", width=150)
        self.table.column("description", width=350)
        self.table.column("amount", width=120, anchor="e")

        # scrollbar for the table
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    # ---------------- SUMMARY SECTION ----------------

    def build_summary(self):
        frame = ttk.LabelFrame(self.root, text="Monthly Budget")
        frame.pack(fill="x", padx=10, pady=5)

        self.summary_label = tk.Label(frame, text="", font=("Arial", 11), justify="left")
        self.summary_label.pack(side="left", padx=10, pady=7)

        ttk.Button(frame, text="Set Budget", command=self.set_budget).pack(side="right", padx=10)

    # ---------------- EXTRA BUTTONS ----------------

    def build_buttons(self):
        frame = ttk.Frame(self.root)
        frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame, text="Highest Expense", command=self.show_highest).pack(side="left", padx=3)
        ttk.Button(frame, text="Delete Selected", command=self.delete_selected).pack(side="left", padx=3)
        ttk.Button(frame, text="View Report", command=self.show_report).pack(side="left", padx=3)

    # ---------------- DISPLAY DATA ----------------

    def refresh_table(self, rows=None):
        # first remove everything that is currently shown
        for item in self.table.get_children():
            self.table.delete(item)

        # if no rows are given, show all the expenses
        if rows is None:
            rows = self.manager.get_all()

        for index, expense in rows:
            # the index is used as the row id so we know which expense to delete
            self.table.insert(
                "",
                "end",
                iid=str(index),
                values=(
                    expense["date"],
                    expense["category"],
                    expense["description"],
                    f"Rs. {expense['amount']:.2f}"
                )
            )

    def update_summary(self):
        today = date.today()

        spent = self.manager.total_for_month(today.month, today.year)
        status, message = budget.check_budget(spent, self.manager.budget)

        # text colour depends on the budget status
        colours = {
            "ok": "green",
            "warning": "orange",
            "over": "red",
            "none": "gray"
        }

        self.summary_label.config(
            text=(
                f"Spent this month: Rs. {spent:.2f}    "
                f"Budget: Rs. {self.manager.budget:.2f}\n"
                f"{message}"
            ),
            fg=colours[status]
        )

        return status, message

    # ---------------- BUTTON ACTIONS ----------------

    def add_expense(self):
        try:
            self.manager.add_expense(
                self.amount_entry.get(),
                self.category_box.get(),
                self.desc_entry.get(),
                self.date_entry.get()
            )
        except ValueError as error:
            messagebox.showerror("Invalid Input", str(error))
            return

        # clear the boxes after adding
        self.amount_entry.delete(0, "end")
        self.desc_entry.delete(0, "end")

        self.refresh_table()
        self.warn_if_needed()

        messagebox.showinfo("Expense Added", "Expense added successfully.")

    def delete_selected(self):
        selected = self.table.selection()

        if not selected:
            messagebox.showinfo("Delete", "Please select an expense first.")
            return

        answer = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this expense?")

        if answer:
            index = int(selected[0])
            self.manager.delete_expense(index)

            self.refresh_table()
            self.update_summary()

    def search_category(self):
        category = self.filter_box.get()

        if category == "All":
            self.refresh_table()
            return

        results = self.manager.search_by_category(category)
        self.refresh_table(results)

        if not results:
            messagebox.showinfo("Search", f"No expenses found in {category}.")

    def search_text(self):
        text = self.search_entry.get().strip()

        if not text:
            messagebox.showinfo("Search", "Please enter something to search.")
            return

        results = self.manager.search_by_text(text)
        self.refresh_table(results)

        if not results:
            messagebox.showinfo("Search", "No matching expenses were found.")

    def show_highest(self):
        expense = self.manager.highest_expense()

        if expense is None:
            messagebox.showinfo("Highest Expense", "No expenses have been added yet.")
            return

        messagebox.showinfo(
            "Highest Expense",
            f"Amount: Rs. {expense['amount']:.2f}\n"
            f"Category: {expense['category']}\n"
            f"Description: {expense['description']}\n"
            f"Date: {expense['date']}"
        )

    def set_budget(self):
        text = simpledialog.askstring("Monthly Budget", "Enter your monthly budget:")

        # user pressed cancel
        if text is None:
            return

        try:
            amount = budget.parse_budget(text)
            self.manager.set_budget(amount)
        except ValueError as error:
            messagebox.showerror("Invalid Budget", str(error))
            return

        self.update_summary()
        messagebox.showinfo("Budget Updated", "Your monthly budget has been updated.")
        self.warn_if_needed()

    def show_report(self):
        report = reports.create_report(self.manager.expenses)

        # open a small new window for the report
        report_window = tk.Toplevel(self.root)
        report_window.title("Expense Report")
        report_window.geometry("500x500")

        text_box = tk.Text(report_window, wrap="word", font=("Arial", 11))
        text_box.pack(fill="both", expand=True, padx=10, pady=10)

        text_box.insert("1.0", report)
        text_box.config(state="disabled")   # so the user cannot edit the report

    def warn_if_needed(self):
        status, message = self.update_summary()

        # same warning box for both cases
        if status == "warning" or status == "over":
            messagebox.showwarning("Budget Alert", message)
