import pandas as pd
def analyze_column(csv_file, column_name):
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
        return
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the CSV file.")
        return
    df = df.dropna(subset=[column_name])
    column_sum = df[column_name].sum()
    column_mean = df[column_name].mean()
    column_std = df[column_name].std()
    print(f"Analysis for column '{column_name}':")
    print(f"Sum: {column_sum}")
    print(f"Mean: {column_mean}")
    print(f"Standard Deviation: {column_std}")
csv_file = 'IRIS1.csv'  
column_name = 'sepal_length' 
analyze_column(csv_file, column_name)