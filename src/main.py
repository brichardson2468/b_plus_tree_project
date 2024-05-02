from utils import load_data
from b_plus_tree import BPlusTree
import pandas as pd
import subprocess
import os


def main():
    # Load data
    data = load_data('data/project_dataset.csv')

    # Initialize B+ Tree with max_keys set to 4 (adjust as necessary)
    bpt = BPlusTree(max_keys=4)

    # Insert data into B+ Tree
    for index, row in data.iterrows():
        bpt.insert(row['Time Period Start Date'], row)

    # Ask user for a date to search
    search_date = pd.Timestamp(input("Enter a date to search (YYYY-MM-DD): "))

    # Search for the date in the B+ Tree
    search_result = bpt.search(search_date)
    print(f"Search result for {search_date}: {search_result}")

    if search_result:
        # Save the search result to a temporary file
        temp_path = 'temp/search_result.csv'
        os.makedirs(os.path.dirname(temp_path), exist_ok=True)
        pd.DataFrame([search_result]).to_csv(temp_path, index=False)
        print(f"Search result saved to {temp_path}")


        # Open the Jupyter Notebook
        notebook_path = 'notebooks/data_visualization.ipynb'
        subprocess.run(f"jupyter notebook {notebook_path}", shell=True)

    else:
        print("No records found for the given date.")

if __name__ == '__main__':
    # Create or overwrite the temp directory
    with open('temp/search_result.csv', 'w') as f:
        f.write("")
    main()
