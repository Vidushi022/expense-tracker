"""
budget.py

Some simple functions for checking the monthly budget.
"""


def parse_budget(text):
    # convert the text typed by the user into a number
    try:
        amount = float(text)
    except ValueError:
        raise ValueError("Please enter a valid budget.")

    if amount < 0:
        raise ValueError("Budget cannot be negative.")

    return amount


def check_budget(spent, budget):
    # checks how much of the budget is left and if we crossed it
    # returns a status word and a message to show on the screen

    if budget <= 0:
        # budget is not set yet
        return "none", "No monthly budget has been set."

    percentage = (spent / budget) * 100

    if spent > budget:
        return "over", "You have gone over your monthly budget."
    elif percentage >= 80:
        return "warning", "You have used more than 80% of your budget."
    else:
        remaining = budget - spent
        return "ok", f"You still have Rs. {remaining:.2f} left."
