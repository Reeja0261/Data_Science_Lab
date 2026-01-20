# Import pandas and create a DataFrame with columns: Name, Age, Marks.Display the first 5 rows and dataset shape.

import pandas as pd

students = {
    "Name": ["Rita","Sita","Gita","Mita","Zita"],
    "Age": [20,21,22,23,24],
    "Marks": [80,85,88,90,95]
}

df = pd.DataFrame(students)
print(df.head(5))
print(df.shape)