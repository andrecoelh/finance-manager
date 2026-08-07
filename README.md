# Finance Manager

Finance Manager is a command-line application written in Python that helps users manage their personal finances. The application allows users to record income and expenses, store transactions in a CSV file, and generate financial summaries that include the current balance and expenses grouped by category.

Originally developed as the final project for **CS50's Introduction to Programming with Python**, this application is now an ongoing personal project. The goal is to continuously improve it by adding new features while applying software engineering best practices and expanding my Python knowledge.

## Features

* Record income transactions
* Record expense transactions
* Organize expenses into predefined categories
* Store all transactions in a CSV file
* Display the current financial balance
* Show expenses grouped by category
* Input validation for menu options and monetary values
* Unit tests with `pytest`

## Expense Categories

* Consumption Bills
* Food
* Transportation
* Health and Wellness
* Education
* Leisure and Entertainment
* Clothing and Personal Care
* Financial/Debts
* Miscellaneous Expenses

## Project Structure

```text
project.py          # Main application
test_project.py     # Unit tests
transactions.csv    # Transaction database (created automatically)
requirements.txt    # Project dependencies
```

## Design Decisions

The application is divided into small, focused functions instead of placing all logic inside `main()`. Each function has a single responsibility, making the project easier to understand, maintain, and test.

Examples include:

* `save_income()` and `save_expense()` write transactions to the CSV file.
* `load_transactions()` reads stored data.
* `calculate_totals()` computes the current balance.
* `calculate_category()` groups expenses by category.
* `show_summary()` displays the financial report.

Transactions are represented internally as a list of dictionaries, providing a simple and readable data structure.

## Data Storage

All transactions are stored in a file named `transactions.csv`.

CSV was chosen because it is lightweight, human-readable, supported by Python's built-in `csv` module, and can easily be opened in spreadsheet applications such as Microsoft Excel.

## Running the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/finance-manager.git
```

Enter the project directory:

```bash
cd finance-manager
```

Run the application:

```bash
python project.py
```

Run the tests:

```bash
pytest test_project.py
```

## Technologies

* Python
* CSV
* Pytest
* Git
* GitHub

## Roadmap

The project is under active development. Planned features include:

* Edit existing transactions
* Delete transactions
* Filter transactions by date
* Monthly financial reports
* Data visualization with charts
* PDF export
* Improved command-line interface
* Database support
* Graphical user interface (GUI)

## Learning Goals

This project serves both as a personal finance tool and as a long-term learning project. It allows me to practice Python programming, software design, testing, version control with Git, and gradually introduce more advanced technologies as the application evolves.
