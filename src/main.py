from utils import load_data
from b_plus_tree import BPlusTree
import pandas as pd


def main():
    # Load data
    data = load_data('data/project_dataset.csv')

    # Check for the presence of the search date in the dataset
    search_date = pd.Timestamp('2020-04-23')
    print("Checking for date in dataset:", search_date in data['Time Period Start Date'].values)
    
    # Initialize B+ Tree with max_keys set to 4 (adjust as necessary)
    bpt = BPlusTree(max_keys=4)
    
    # Insert data into B+ Tree
    for index, row in data.iterrows():
        bpt.insert(row['Time Period Start Date'], row)
        #print(f"Inserted: {row['Time Period Start Date']} -> {row['Time Period End Date']}")

    # Example of a search for a specific date
    result = bpt.search(search_date)
    print(f"Search results for {search_date}: {result}")

if __name__ == '__main__':
    main()
