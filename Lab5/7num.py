# Create a new column by transforming Marks (e.g., Marks / 10).Rename columns and save the cleaned dataset to a CSV file.
import pandas as pd
df = pd.read_csv("2numpy.csv")
df['Marks_transformed'] = df['Marks'] / 10
print(df)

df.to_csv("cleaned_2numpy.csv",index=False)
print("Cleaned dataset saved successfully to a CSV file")






