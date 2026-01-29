# Create a dataset of hours studied and marks scored for 10 students.
# Calculate the covariance between the two variables.
# Plot the data using a scatter plot.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

studies={
    "hours" : [11,12,13,14,15,16,17,18,19,20],
    "marks" : [80,81,82,83,84,85,86,87,88,89]
}

df  = pd.DataFrame(studies)

covariance = df.cov()
print("the covarience:")
print(covariance)

plt.scatter(df["hours"], df["marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied and marks scored of 10 students")
plt.show()



