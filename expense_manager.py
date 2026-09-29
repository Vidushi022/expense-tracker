"""
expense_manager.py

This file contains the main functions used to manage expenses.
"""

from datetime import date, datetime
import storage

# categories available in the application
CATEGORIES = [
    "Food",
    "Travel",
    "Stationery",
    "Books",
    "Snacks",
    "Necessities",
    "Online Shopping",
    "Entertainment"
]


class ExpenseManager:

    def __init__(self):
        # load the data that was saved earlier
        data = storage.load_data()

        self.expenses = data["expenses"]
        self.budget = data["budget"]

    def save(self):
        # save the latest expenses and budget
        storage.save_data({
            "budget": self.budget,
            "expenses": self.expenses
        })

    def add_expense(self, amount_text, category, description, date_text):
        # first check if the amount is a valid number
        try:
            amount = float(amount_text)
        except ValueError:
            raise ValueError("Please enter a valid amount.")

        if amount <= 0:
            raise ValueError("Amount should be greater than zero.")

        if category not in CATEGORIES:
            raise ValueError("Please select a category.")

        # if the date is empty, use today's date
        date_text = date_text.strip()
        if not date_text:
            date_text = date.today().strftime("%d-%m-%Y")

        # check the date format
        try:
            datetime.strptime(date_text, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Date should be in DD-MM-YYYY format.")

        expense = {
            "amount": amount,
            "category": category,
            "description": description.strip(),
            "date": date_text
        }

        self.expenses.append(expense)
        self.save()   # save it immediately

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)
            self.save()
            return True
        return False

    def get_all(self):
        # enumerate gives the position and the expense together
        return list(enumerate(self.expenses))

    def search_by_category(self, category):
        results = []
        for index, expense in enumerate(self.expenses):
            if expense["category"] == category:
                results.append((index, expense))
        return results

    def search_by_text(self, text):
        results = []
        text = text.lower()

        for index, expense in enumerate(self.expenses):
            description = expense["description"].lower()
            category = expense["category"].lower()

            # match if the text is in the description or the category
            if text in description or text in category:
                results.append((index, expense))

        return results

    def highest_expense(self):
        if not self.expenses:
            return None
        return max(self.expenses, key=lambda expense: expense["amount"])

    def lowest_expense(self):
        if not self.expenses:
            return None
        return min(self.expenses, key=lambda expense: expense["amount"])

    def total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total

    def total_for_month(self,month,year):
        # dates are stored like 29-09-2026, so we check the start of the date
        total = 0

        for expense in self.expenses:
            date = datetime.strptime(expense["date"], "%d-%m-%Y")
            
            if date.month == month and date.year == year:
                total += expense["amount"]

        return total

        
    def category_total(self, category):
        total = 0
        for expense in self.expenses:
            if expense["category"] == category:
                total += expense["amount"]
        return total

    def set_budget(self, amount):
        if amount < 0:
            raise ValueError("Budget cannot be negative.")

        self.budget = amount
        self.save()
