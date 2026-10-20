# Student Marks ETL Project

## About
A beginner-friendly Data Engineering project built using Python. It reads student marks from a CSV file, validates the data, calculates Pass/Fail results, and saves the processed data into a new CSV file.

## Technologies Used
- Python
- CSV
- VS Code

## ETL Process
1. **Extract:** Read student data from `Data/student.csv`.
2. **Transform:** Validate marks and calculate Pass/Fail.
3. **Load:** Save valid results to `output/results.csv`.

## Data Validation
- Handles missing marks.
- Detects invalid values such as `abc`.
- Rejects marks outside the 0–100 range.
- Uses 35 as the passing mark.

## How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Run the command:

   `python etl.py`

## Project Structure
```text
Student-ETL-project/
├── Data/
│   └── student.csv
├── output/
│   └── results.csv
├── etl.py
└── README.md
```

## Learning Outcomes
- Understanding ETL fundamentals.
- Reading and writing CSV files in Python.
- Applying data validation.
- Handling errors using `try` and `except`.

## Future Improvements
- Add automated tests.
- Store data in a database.
- Add logging and reporting.

