import os
import pandas as pd

def combine_csv_files():
    # Get a list of all CSV files in the current working directory
    csv_files = [file for file in os.listdir('.') if file.endswith('.csv') and file != 'transactions.csv']

    if not csv_files:
        print("No CSV files found in the current working directory (cwd).")
        return

    # Initialize an empty DataFrame to hold the combined data
    combined_df = pd.DataFrame()

    # Loop through each CSV file and concatenate its contents to the combined DataFrame
    for file in csv_files:
        df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    combined_df['Date'] = pd.to_datetime(combined_df['Date'],format='mixed')
    combined_df.sort_values(by='Date')

    # Write the combined DataFrame to a new CSV file called "transactions.csv"
    combined_df.to_csv('transactions.csv', index=False)

    print("CSV files combined successfully into 'transactions.csv'.")

if __name__ == "__main__":
    combine_csv_files()
