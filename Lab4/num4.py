# Write a Python script that takes a list of six student names and uses the
# random.sample() function to randomly select exactly three "Volunteers" for a
# presentation, ensuring that no student is picked more than once in the selection

import random
random.seed(4)

students = ["Reeja","Shristi","Manisha","Rita","Sita","Mita"]
# students = ["Reeja","Shristi","Manisha","Reeja","Shristi","Manisha"]
# students = ["Reeja","Reeja","Reeja","Reeja","Reeja","Reeja"]
# students = ["Reeja","Shristi"]

volunteers = random.sample(students,3)

print("the selected students",volunteers)
# print("the selected students:")
# for student in volunteers:
#     print(student)