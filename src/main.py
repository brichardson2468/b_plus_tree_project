from b_plus_tree import BPlusTree
import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
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
    data = load_data('data/project_dataset.csv')

    # Initialize B+ Tree with max_keys set to 4 (adjust as necessary)
    bpt = BPlusTree(max_keys=4)

    # Insert data into B+ Tree
    for index, row in data.iterrows():
        key = (parse_date(row['Time Period Start Date']), parse_date(row['Time Period End Date']))
        bpt.insert(key, row)

    # Ask user for a date to search
    print("Welcome to my data searching, retrieval, and visualization program!")
    print("The dataset starts on 2020-04-23 and ends on 2024-03-04.")
    print("Think of a date range you want to search for in the data and be able to visualize!")
    start_date_input = input("Enter the start date you want (YYYY-MM-DD): ")
    end_date_input = input("Enter the end date you want (YYYY-MM-DD): ")
    start_date = parse_date(start_date_input)
    end_date = parse_date(end_date_input)
    if start_date and end_date:
        # Search for the date in the B+ Tree
        search_result = bpt.search_range(start_date, end_date)

        if search_result:
            # Convert search_result to DataFrame
            results_df = pd.DataFrame(search_result)
            # Ensure the columns match the original data
            results_df = results_df[data.columns]
            # Sort the DataFrame based on the date columns or other criteria
            results_df.sort_values(by=['Time Period Start Date'], inplace=True)
            results_path = 'data/search_results.csv'
            results_df.to_csv(results_path, index=False)
            print("Overwriting the previous search results file...")
            print(f"Your search results have been saved to {results_path}!")
            print(f"Open up {results_path} to view your search results.")
            print("Then you can run the notebook to visualize your chosen date range.")
            print("Thank you for using my program!")
        else:
            print("No records found within the range for the given date.")
    else:
        print("No search performed due to input error.")

if __name__ == '__main__':
    main()
