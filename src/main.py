from utils import load_data
from b_plus_tree import BPlusTree
import pandas as pd



def main():
    # Load data
    data = load_data('data/project_dataset.csv')

    # Initialize B+ Tree with max_keys set to 4 (adjust as necessary)
    bpt = BPlusTree(max_keys=4)

    # Insert data into B+ Tree
    for index, row in data.iterrows():
        bpt.insert(row['Time Period Start Date'], row)

    # Ask user for a date to search
    while True:
        try:
            search_date = pd.Timestamp(input("Enter a date to search (YYYY-MM-DD): "))
            break
        except ValueError:
            print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")

    # Search for the date in the B+ Tree
    search_result = bpt.search(search_date)
    print(f"Search result for {search_date}: {search_result}")

    if search_result:
        # Convert search_result to DataFrame
        results_df = pd.DataFrame(search_result)
        results_path = 'data/search_results.csv'
        # Ensure the columns match the original data
        results_df.to_csv(results_path, index=False)
        print(f"Search result saved to {results_path}")

    else:
        print("No records found for the given date.")

if __name__ == '__main__':
    main()
