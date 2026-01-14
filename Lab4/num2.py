# Use a list comprehension to create a new list containing only the even numbers between
# 1 and 20, demonstrating a more concise and readable alternative to traditional loops.


# Create a list containing only the even numbers between 1 and 20
# jesma first i bhanako expression ho what the value you want to keep and the another is loop jata for items and iteration than if condition inline(one line) ma bhayako cha

even_numbers = [i for i in range(1, 21) if i % 2 == 0]


print("Even numbers between 1 and 20:", even_numbers)