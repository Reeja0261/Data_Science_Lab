
# Write a program that checks if a given number is even or odd
n=input("Enter a number")
if n.isdigit():
    num=int(n)
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd") 
else:
    print("enter a valid number")
