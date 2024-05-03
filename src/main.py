from b_plus_tree import BPlusTree
import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully!")
        data['Time Period Start Date'] = pd.to_datetime(data['Time Period Start Date']).dt.date
        data['Time Period End Date'] = pd.to_datetime(data['Time Period End Date']).dt.date
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def parse_date(date_string):
    try:
        date = pd.to_datetime(date_string).date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None
    return date


def main():
    # Load data
    data = load_data('data/practice_dataset.csv')

    # Initialize B+ Tree with max_keys set to 4 (adjust as necessary)
    bpt = BPlusTree(max_keys=4)

    # Insert data into B+ Tree
    for index, row in data.iterrows():
        key = (parse_date(row['Time Period Start Date']), parse_date(row['Time Period End Date']))
        bpt.insert(key, row)

    # Ask user for a date to search
    date_input = input("Enter a date to search (YYYY-MM-DD): ")
    target_date = parse_date(date_input)
    if target_date:
        # Search for the date in the B+ Tree
        search_result = bpt.search_range(target_date)
        print(f"Search results for {target_date}: {search_result}")

        if search_result:
            # Convert search_result to DataFrame
            results_df = pd.DataFrame(search_result)
            results_path = 'data/search_results.csv'
            # Ensure the columns match the original data
            results_df.to_csv(results_path, index=False)
            print(f"Search results saved to {results_path}")
        else:
            print("No records found within the range for the given date.")
    else:
        print("No search performed due to input error.")

if __name__ == '__main__':
    main()
