import pandas as pd
from datetime import datetime, timedelta

def read_input_file(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)
    return df

def analyze_employee_data(df):
    # Sort the DataFrame by employee and date
    df.sort_values(['Employee Name', 'Date'], inplace=True)

    # Initialize variables to keep track of consecutive days and shift details
    consecutive_days_count = 0
    prev_employee = None
    prev_end_time = None

    # Iterate through the DataFrame to analyze the data
    for index, row in df.iterrows():
        current_employee = row['Employee Name']
        current_date = datetime.strptime(row['Date'], '%Y-%m-%d')
        current_start_time = datetime.strptime(row['Start Time'], '%H:%M:%S')
        current_end_time = datetime.strptime(row['End Time'], '%H:%M:%S')

        # Check for consecutive days
        if current_employee == prev_employee and (current_date - prev_date).days == 1:
            consecutive_days_count += 1
        else:
            consecutive_days_count = 1

        # Check for less than 10 hours between shifts
        time_between_shifts = current_start_time - prev_end_time if prev_end_time else timedelta(hours=0)
        if time_between_shifts > timedelta(hours=1) and time_between_shifts < timedelta(hours=10):
            print(f"{current_employee} worked less than 10 hours between shifts on {current_date}")

        # Check for more than 14 hours in a single shift
        shift_duration = current_end_time - current_start_time
        if shift_duration > timedelta(hours=14):
            print(f"{current_employee} worked more than 14 hours on {current_date}")

        # Update previous values for the next iteration
        prev_employee = current_employee
        prev_date = current_date
        prev_end_time = current_end_time

    # Check for consecutive days worked
    if consecutive_days_count >= 7:
        print(f"{current_employee} worked for 7 consecutive days")

if __name__ == "__main__":
    # Replace 'your_input_file.csv' with the actual input file path
    input_file_path = 'your_input_file.csv'
    
    # Read input file
    employee_data = read_input_file(input_file_path)
    
    # Analyze employee data
    analyze_employee_data(employee_data)
