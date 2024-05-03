# B+ Tree Project
## Data Structures Semester Project on B+ Trees
### Motivation
My motivation for this project was incorporating a data set I was using for my data visualization class. It's a dataset that tracks U.S. Mental Health statistics starting at the beginning of the Covid-19 pandemic and extends to the current day. I chose this dataset because prior to starting my computer science program, I worked in the mental health field for over a decade and saw the effects first hand of the pandemic on worsening mental health. I wanted a way to visualize this. So the goal was to create this project so that I could more quickly change the search range of the data in order to more quickly visualize the data.
### About B+ Trees


# Project Description

# Installation
## To set up this project locally, follow these steps:
### 1. Clone the repository
    git clone https://github.com/brichardson2468/b_plus_tree_project.git
### 2. Navigate to the project directory:
    cd b_plus_tree_project
### 3. Install the required Python packages:
    pip install -r requirements.txt
# Usage
## Run the application using:
    python src/main.py
### After starting the program, you will be prompted to input a start and end date. The program will then search for records within that date range in the B+ tree and provide the results.
## Example
    Enter the start date you want (YYYY-MM-DD): 2022-01-01
    Enter the end date you want (YYYY-MM-DD): 2022-12-31
### This will search for all records between January 1, 2022, and December 31, 2022. The search results will be saved to data/search_results.csv, and you can then visualize these results immediately by running all cells in the visualization notebook.
# Features
## Data Loading
### Loads data from a CSV file, converting date strings into date objects.
## Interactive Search
### Allows users to input a date range and retrieve data that falls within this range.
## Data Output
### Outputs the search results into a CSV file, allowing for further analysis or visualization.
## Data Visualization
### Ready made visualizations to check out based on the dates you chose
## Error Handling
### Includes basic error handling for file not found and input validation.