"""
reports.py

This file contains functions used to create simple expense reports.
"""


def total_spending(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def average_spending(expenses):
    if not expenses:
        return 0
    return total_spending(expenses) / len(expenses)


def highest_expense(expenses):
    if not expenses:
        return None
    return max(expenses, key=lambda expense: expense["amount"])


def lowest_expense(expenses):
    if not expenses:
        return None
    return min(expenses, key=lambda expense: expense["amount"])


def category_report(expenses):
    # makes a dictionary like {"Food": 500, "Books": 300}
    report = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in report:
            report[category] = 0

        report[category] += amount

    return report


def create_report(expenses):
    if not expenses:
        return "No expenses have been added yet."

    total = total_spending(expenses)
    average = average_spending(expenses)
    highest = highest_expense(expenses)
    lowest = lowest_expense(expenses)
    categories = category_report(expenses)

    # build the report as one big string
    report = "========== EXPENSE REPORT ==========\n\n"

    report += f"Total spending: Rs. {total:.2f}\n"
    report += f"Average expense: Rs. {average:.2f}\n"

    report += "\nHighest expense:\n"
    report += f"Rs. {highest['amount']:.2f} - {highest['category']} - {highest['description']}\n"

    report += "\nLowest expense:\n"
    report += f"Rs. {lowest['amount']:.2f} - {lowest['category']} - {lowest['description']}\n"

    report += "\nCategory-wise spending:\n"
    for category, amount in categories.items():
        report += f"{category}: Rs. {amount:.2f}\n"

    return report
