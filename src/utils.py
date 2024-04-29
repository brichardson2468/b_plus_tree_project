import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully!")
        data['Time Period Start Date'] = pd.to_datetime(data['Time Period Start Date'])
        data['Time Period End Date'] = pd.to_datetime(data['Time Period End Date'])
        return data
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")