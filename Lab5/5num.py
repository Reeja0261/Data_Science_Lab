# Detect duplicate rows in the dataset.Remove duplicates and verify the result.

import pandas as pd

df = pd.read_csv("4numpy.csv")

print("checking the duplicate value")
print(df.duplicated(subset=["Name","Age","Marks"]))

print("remove the duplicate")
df_drop = df.drop_duplicates(subset=["Name","Age","Marks"],inplace=True)
print(df_drop)

print(df)