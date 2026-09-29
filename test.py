import unittest
from expense_manager import ExpenseManager


class TestExpenseManager(unittest.TestCase):

    def setUp(self):
        # Make a new expense manager before every test
        self.manager = ExpenseManager()

        # Remove old expenses so they don't affect our tests
        self.manager.expenses = []

    def test_add_expense(self):
        # Check if an expense gets added properly

        self.manager.add_expense(
            "100",
            "Food",
            "Lunch",
            "30-09-2026"
        )

        self.assertEqual(len(self.manager.expenses), 1)
        self.assertEqual(self.manager.expenses[0]["amount"], 100)

    def test_search_by_category(self):
        # Add some expenses to test the search function
        self.manager.add_expense(
            "100",
            "Food",
            "Lunch",
            "30-09-2026"
        )

        self.manager.add_expense(
            "50",
            "Travel",
            "Bus",
            "30-09-2026"
        )

         # Search for expenses in the Food category
        food_expenses = self.manager.search_by_category("Food")

        self.assertEqual(len(food_expenses), 1)
        self.assertEqual(food_expenses[0][1]["description"], "Lunch")

    def test_total_expenses(self):
        # Add two expenses and check their total
        self.manager.add_expense(
            "100",
            "Food",
            "Lunch",
            "30-09-2026"
        )

        self.manager.add_expense(
            "50",
            "Travel",
            "Bus",
            "30-09-2026"
        )

        total = self.manager.total_expenses()

        self.assertEqual(total, 150)

    def test_highest_expense(self):
        # Add two expenses and check which one is higher
        self.manager.add_expense(
            "100",
            "Food",
            "Lunch",
            "30-09-2026"
        )

        self.manager.add_expense(
            "200",
            "Online Shopping",
            "Notebook",
            "30-09-2026"
        )

        highest = self.manager.highest_expense()

        self.assertEqual(highest["amount"], 200)


if __name__ == "__main__":
    unittest.main()        # Run all the tests
