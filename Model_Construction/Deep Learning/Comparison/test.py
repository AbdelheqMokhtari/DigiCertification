import csv

# Specify the path to the CSV file
csv_file = 'classification rapport/CNCC/classification_report.csv'

# Specify the target value
target_value = 'E7'

# Open the CSV file in read mode
with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    # Iterate over the rows
    for row in reader:
        # Iterate over the columns in each row
        for column in row:
            # Check if the current value matches the target value
            if column == target_value:
                print('Found:', column)
                break