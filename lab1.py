# Write a program that takes two numbers as input from the user, and print their sum.
a = float(input("enter the first number"))
b = float(input("enter the second number"))

c = a+b

if c.is_integer():
    print(int(c))
else:
    print(c)



# Write a program that checks if a given string is palindrome.

a = "eyyea"
# print(a[-1])
print(a[-1:])
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")




# Write a program that prints all prime numbers up to a given number ‘n’.
a = int(input("enter the number"))

for num in range(2, a + 1):     
    for i in range(2, num):    
        if num % i == 0:
            break              
    else:
        print(num)


a = input("Enter a number: ")
if a.isdigit():
    num = int(a)
    for number in range(2, num+1):
        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(number)

else:
    print("Enter a valid positive number: ")


# Fibonacci series up to n terms

n = input("Enter the number of terms: ")

if n.isdigit():
    num = int(n)
    a = 0
    b = 1
    for i in range(num):
        print(a)
        temp = a
        a = b
        b = temp + b
else:
    print("enter a valid positive integer.")


# GDC
def GCD(a, b):
    while (b != 0):
        temp = a
        a = b
        b = temp % a
    return a

n1 = input("Enter first number: ")
n2 = input("Enter second number: ")

if n1.isdigit() and n2.isdigit():
    num1 = int(n1)
    num2 = int(n2)

    result = GCD(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}.")
else:
    print("Please enter valid positive integers.")



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


# Write a program that checks if a year is a leap year
year = input("Enter a year ")

if year.isdigit():
    y = int(year)

    if (y % 4 == 0 and y % 100 != 0):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")

else:
    print("enter a valid number")

year = input("Enter a year ")

if year.isdigit():
    y = int(year)

    if (y % 4 == 0 and y % 100 != 0) or (y%400==0):
        print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")

else:
    print("enter a valid number")


# Write a program that takes a temperature in Celsius, and converts it to Fahrenheit and Kelvin, based on the choice of user

temp = input("Enter temperature in Celsius: ")

if temp.isdigit():
    celsius = float(temp)

    print("Choose conversion type:")
    print("1. Fahrenheit")
    print("2. Kelvin")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}\u00B0C is equal to {fahrenheit}\u00B0F.")
    elif choice == "2":
        kelvin = celsius + 273.15
        print(f"{celsius}\u00B0C is equal to {kelvin} K.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
else:
    print("enter the valid number")   



# Write a program that takes a list of numbers as input, and returns the largest number in the list.

numbers = input("Enter numbers separated by space: ").split()

list = []
for n in numbers:
    list.append(float(n))
   
if list:
    largest = list[0]

    for num in list:
        if num > largest:
            largest = num
  
    if largest.is_integer():
        print("The largest number is:", int(largest))
    else:
        print("The largest number is:", largest)

else:
    print("No valid numbers entered.")


a="Reeja Maharjan"
a.split()
print(a.split())