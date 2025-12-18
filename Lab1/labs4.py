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