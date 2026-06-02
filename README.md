# Expense Tracker

A command-line expense tracker that records expenses by name, amount and category, and permanently saves all data to a JSON file.

## Features

- Add expenses with name, amount and category
- Display all recorded expenses as a numbered list
- Calculate and display the total amount spent
- Ensuring data persistence by saving expenses to a JSON file, so data remains after the programme is closed
- Handling invalid inputs using try/except

## How to Run

1. Ensure Python 3 is installed
2. Clone this repository:

```bash
git clone https://github.com/KananHeybatov/Expense-Tracker.git
```

3. Navigate to the directory and run the file:

```bash
python expense_tracker.py
```

## How It Works

Expenses are stored as a list of dictionaries, each containing the expense name, amount and category. The programme loads existing data from a JSON file at startup and automatically saves it after each new expense is added. The total is calculated using a generator expression with Python’s built-in `sum()` function.

## What I’ve learnt

- Storing data as a list of dictionaries
- Saving and loading lists to and from JSON files
- Using `float()` for decimal number input
- Calculating totals with `sum()` and generator expressions
- Using `enumerate()` to display numbered lists

## Possible Improvements

- Filtering expenses by category
- Displaying a spending summary by category
- Setting a monthly budget and issuing a warning when it is exceeded
- Exporting expenses to a CSV file

## Author

Kanan Heybatov — 2026
