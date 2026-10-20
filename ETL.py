
import csv
import os

# Output folder create karna
os.makedirs("output", exist_ok=True)

# Extract: CSV se data read karna
with open("Data/student.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    # Load: Output CSV create karna
    with open("output/results.csv", "w", newline="") as output_file:
        fieldnames = ["Name", "Marks", "Result"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        writer.writeheader()

        # Transform: Data validate karna aur result calculate karna
        for row in reader:
            name = row["Name"].strip()
            raw_marks = row["Marks"].strip()

            # Blank marks check
            if not raw_marks:
                print("Marks missing for", name)
                continue

            # Number check
            try:
                marks = int(raw_marks)
            except ValueError:
                print("Invalid marks for", name)
                continue

            # Marks range check
            if marks < 0 or marks > 100:
                print("Marks out of range for", name)
                continue

            # Pass/Fail calculate karna
            if marks >= 35:
                result = "Pass"
            else:
                result = "Fail"

            print(name, "-", result)

            # Valid data output CSV mein save karna
            writer.writerow({
                "Name": name,
                "Marks": marks,
                "Result": result
            })

print("ETL completed successfully!")
print("Results saved in output/results.csv")
