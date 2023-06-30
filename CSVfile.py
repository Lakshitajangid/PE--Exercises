import csv

def calculate_average(csv_file_path, target_column_name):
    """
    Calculates the average of a specific column in a CSV file.

    Args:
        csv_file_path (str): The path or name of the CSV file.
        target_column_name (str): The name of the column to calculate the average for.

    Returns:
        float: The average value of the specified column.
    """
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        column_values = [float(row[target_column_name]) for row in reader]

    # Calculate the average of the column values
    average = sum(column_values) / len(column_values)
    return average

def main():
    """
    Main function to run the DataMetrics data analytics program.
    """
    print("Welcome to DataMetrics Data Analytics!")
    csv_file_path = input("Please enter the path or name of the CSV file:\n")
    target_column_name = input("Please enter the name of the column to calculate the average for:\n")

    try:
        average = calculate_average(csv_file_path, target_column_name)
        print("\nThank you for providing the CSV file.")
        print(f"The average value of the '{target_column_name}' column is: ${average:.2f}")
    except FileNotFoundError:
        print("\nFile not found. Please check the path or name of the CSV file.")
    except KeyError:
        print(f"\n'{target_column_name}' column not found in the CSV file.")

# Run the program
if __name__ == '__main__':
    main()
