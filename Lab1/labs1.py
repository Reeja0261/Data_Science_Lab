# Write a program that takes two numbers as input from the user, and print their sum.
a = float(input("enter the first number"))
b = float(input("enter the second number"))

c = a+b

if c.is_integer():
    print(int(c))
else:
    print(c)