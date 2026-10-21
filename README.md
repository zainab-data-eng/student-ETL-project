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

## Sample Output

The ETL script processes student marks and saves valid records to `output/results.csv`.

| Name | Marks | Result |
|---|---:|---|
| Aisha | 85 | Pass |
| Rahul | 40 | Pass |
| Zoya | 0 | Fail |
| Aman | 30 | Fail |
| Priya | 76 | Pass |
| Arjun | 85 | Pass |
| Neha | 28 | Fail |
| Rohan | 67 | Pass |
| Sara | 95 | Pass |
| Vikram | 35 | Pass |
| Ananya | 81 | Pass |
| Kabir | 45 | Pass |
| Meera | 19 | Fail |
| Aditya | 72 | Pass |
| Isha | 88 | Pass |

### Data Validation Examples
- Missing marks are skipped.
- Non-numeric marks such as `abc` are rejected.
- Marks outside the 0–100 range are rejected.
- Marks of 35 or above result in Pass; marks below 35 result in Fail.
