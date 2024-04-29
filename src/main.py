import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully!")
        data['Time Period Start Date'] = pd.to_datetime(data['Time Period Start Date'])
        data['Time Period End Date'] = pd.to_datetime(data['Time Period End Date'])
        print(data.head())  # Display the first few rows
        print(data.dtypes)  # Display the data types of each column
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Load data
    load_data('data/project_dataset.csv')

if __name__ == '__main__':
    main()
