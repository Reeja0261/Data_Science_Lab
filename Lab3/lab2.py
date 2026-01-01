# 2. File Processing with Exception Handling
# ● Reads numbers from a text file (one number per line)
# ● Ignores invalid entries using exception handling
# ● Calculates and displays the sum and average of valid numbers


total = 0
count = 0

try:
    file = open("numbers.txt", "r")

    for line in file:
        try:
            num = float(line.strip())
            total += num
            count += 1
        except ValueError:
            print("Invalid")

    file.close()

    if count > 0:
        print("Sum:", total)
        print("Average:", total / count)
    else:
        print("No valid numbers found")

except FileNotFoundError:
    print("numbers.txt file not found")
