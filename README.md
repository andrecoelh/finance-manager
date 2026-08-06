# Finance Manager

#### Video Demo: https://youtu.be/tNavcqQqUWA

#### Description:

Finance Manager is a command-line application written in Python that helps users keep track of their personal finances. The program allows users to record both income and expenses, store them in a CSV file, and generate a financial summary showing the current balance and expenses grouped by category. The goal of this project was to create a simple but useful financial management tool while applying the programming concepts learned throughout CS50's Introduction to Programming with Python.

The application presents a menu with four options: add income, add an expense, display a financial summary, or exit the program. The menu is displayed continuously until the user chooses to quit, allowing multiple transactions to be recorded in a single session.

Income transactions require the user to enter a monetary value and a short description. Expense transactions require the same information, but also ask the user to select one of several predefined categories. These categories include Consumption Bills, Food, Transportation, Health and Wellness, Education, Leisure and Entertainment, Clothing and Personal Care, Financial/Debts, and Miscellaneous Expenses.

All transactions are stored in a file named `transactions.csv`. I decided to use a CSV file because it is lightweight, human-readable, and supported by Python's built-in `csv` module. This choice also allows the file to be opened directly in spreadsheet software such as Microsoft Excel.

The project consists of three files:

- `project.py` contains the complete application. It includes the menu system, functions for saving transactions, loading transactions from the CSV file, calculating totals, calculating expenses by category, and displaying the financial summary.
- `test_project.py` contains unit tests written with `pytest`. These tests verify that the functions responsible for calculating totals and category expenses return the expected results under different scenarios.
- `requirements.txt` is included for compatibility with the project specification. Since this project only uses Python's standard library modules (`csv` and `sys`), there are no external dependencies to install.

One important design decision was separating the program into multiple small functions instead of writing everything inside `main()`. Each function has a single responsibility. For example, `save_receita()` and `save_despesa()` are responsible only for writing data to the CSV file, while `load_transactions()` only reads the stored data and converts it into Python dictionaries. Functions such as `calculate_totals()` and `calculate_category()` perform only calculations, leaving `show_summary()` responsible for displaying the results. This separation makes the code easier to understand, maintain, and test.

The application also includes input validation. All numerical inputs are protected with `try` and `except` blocks to prevent the program from crashing if the user enters invalid data. The menu only accepts valid options, monetary values must be positive numbers, and expense categories must be selected from the available list. If the transactions file does not exist yet, the program handles the situation gracefully by displaying an empty summary instead of raising an exception.

To represent transactions in memory, I chose to use a list of dictionaries. Each dictionary stores the information related to a single transaction, including its type, description, value, and category when applicable. I believe this structure is more readable than using nested lists because each field can be accessed by name instead of by index.

Although this project is intentionally simple, it demonstrates many of the concepts covered in CS50P, including functions, loops, conditionals, dictionaries, lists, file handling, CSV manipulation, exception handling, modular program design, and unit testing with `pytest`.

In the future, I would like to expand this project by adding features such as editing or deleting transactions, filtering transactions by date, monthly financial reports, charts showing spending habits, and exporting summaries as PDF files. These improvements would transform the application into a more complete personal finance management system.

Overall, this project allowed me to combine several Python concepts into a practical application that can be used to manage personal finances from the command line while maintaining clean, organized, and modular code.