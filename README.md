# Financial Utility CLI Tool

## Project Overview
A command-line utility designed to perform financial calculations, including investment interest projections and bond repayment schedules. This tool emphasizes clean code organization, robust user input handling, and logical flow control.

## Technical Methodology
* **Input Sanitization**: Implemented `lower()` and `strip()` methods to ensure consistent data processing and prevent input-related errors.
* **Logic Architecture**: Used conditional branching to handle multiple execution paths, ensuring accurate outputs based on user-defined parameters.
* **Math Library Implementation**: Utilized Python's `math` module for precise financial calculations (compound interest and bond repayment formulas).

## Why This Matters
While this tool focuses on financial logic, the underlying methodology regarding **input validation** and **error handling** is a critical component of secure software development. Ensuring that a program handles unexpected user input gracefully is a fundamental step in preventing application-level vulnerabilities.

## How to Run
1. Ensure you have Python installed.
2. Run the script: `python finance_calculator.py`
3. Follow the on-screen prompts to select 'investment' or 'bond'.
