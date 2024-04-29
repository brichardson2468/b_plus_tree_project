import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully!")
        print(data.head())  # Display the first few rows
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Load data
    load_data('data/project_dataset.csv')

if __name__ == '__main__':
    main()
