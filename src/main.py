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
        bpt.insert(row['Time Period Start Date'], row['Time Period End Date'])

    # Example of a search for a specific date
    search_date = pd.Timestamp('2022-01-01')
    result = bpt.search(search_date)
    print(f"Search results for {search_date}: {result}")

if __name__ == '__main__':
    main()
