"""
storage.py

This file is used to save and load expense data.
The data is stored in a JSON file so that it stays saved even afterthe program is closed.
"""

import json
import os


DATA_FILE = "expenses.json"


def load_data():

    # Default data used when the expense file is not found.
    default_data = {
        "budget": 0.0,
        "expenses": []
    }

    if not os.path.exists(DATA_FILE):
        return default_data

    # Check if the JSON file exists. if not os.path.exists(DATA_FILE): return default_data

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        # Add these values if they are missing from the file.
        data.setdefault("budget", 0.0)
        data.setdefault("expenses", [])

        return data

    except (json.JSONDecodeError, OSError):
        # If the file cannot be read properly.
        # use the default data instead.
        return default_data


def save_data(data):

    # Add these values if they are missing from the file.
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
