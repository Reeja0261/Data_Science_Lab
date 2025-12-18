# Write a program that checks if a given string is palindrome.

a = "eyyea"
# print(a[-1])
print(a[-1:])
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")