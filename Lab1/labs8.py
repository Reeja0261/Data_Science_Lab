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