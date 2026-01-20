# Load a CSV file into a DataFrame.Display column names, data types, and basic statistics.

import pandas as pd
df = pd.read_csv("2numpy.csv")
print("the columns:")
print(df.columns)
print("the data types:")
print(df.dtypes)
print("the basic statistics:")
print(df.describe())