import pandas as pd
df = pd.read_csv("data.csv")
clean_df = df.drop_duplicates()
print("Cleaned DataFrame:")
print(clean_df)