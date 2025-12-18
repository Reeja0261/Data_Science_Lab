#  Write a program that prints all prime numbers up to a given number ‘n’.


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