# Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...]. Compute
# the average rating, find the highest-rated movie, and list all movies with rating above the
# average.

movies = []   

n = int(input("How many movies do you want to enter? "))

for i in range(n):
    name = input(f"Enter movie {i+1} name: ")
    rating = float(input(f"Enter rating for {name}: "))
    movies.append((name, rating))

# in thi it is for the average
total = 0
for movie in movies:
    total += movie[1]

average = total / len(movies)
print("\nAverage rating:", average)


highest = movies[0]
for movie in movies:
    if movie[1] > highest[1]:
        highest = movie

print("Highest-rated movie:", highest[0],"is", highest[1])


# yesle average bhanda highest cha tyo deyako ho
print("\nMovies with rating above average:")
for movie in movies:
    if movie[1] > average:
        print(movie[0],"is", movie[1])


print("\nMovies with rating below average:")
for movie in movies:
    if movie[1] < average:
        print(movie[0],"is", movie[1])




# data = input("Enter movies and ratings: ")


# pairs = data.split(",")

# movies = []

# for p in pairs:
#     name, rating = p.split("-")
#     movies.append((name.strip(), float(rating.strip())))
#     # print(name)

# # for Average 
# total = 0
# for m in movies:
#     total += m[1]
# average = total / len(movies)

# # for Highest rated movie
# highest = movies[0]
# for m in movies:
#     if m[1] > highest[1]:
#         highest = m

# # for Above and below average lists
# above = []
# below = []

# for m in movies:
#     if m[1] > average:
#         above.append(m[0])
#     elif m[1] < average:
#         below.append(m[0])


# print("\nAverage rating:", round(average, 2))
# print("Highest rated movie:", highest[0])

# print("Movies above average:", above)
# print("Movies below average:", below)























# Create an empty list to store movies
# movies = []

# # Ask the user how many movies they want to enter
# n = int(input("How many movies do you want to enter? "))

# # Get movie names and ratings from the user
# for i in range(n):
#     name = input(f"Enter the name of movie {i+1}: ")
#     rating = float(input(f"Enter the rating of {name}: "))
#     movies.append((name, rating))

# # Calculate average rating
# total = 0
# for movie in movies:
#     total += movie[1]
# average = total / len(movies)

# # Find highest-rated movie
# highest = movies[0]
# for movie in movies:
#     if movie[1] > highest[1]:
#         highest = movie

# # List movies above average
# above_average = []
# for movie in movies:
#     if movie[1] > average:
#         above_average.append(movie[0])

# # Print results
# print(f"\nAverage rating: {average:.2f}")
# print(f"Highest-rated movie: {highest[0]} with rating {highest[1]}")
# print("Movies with rating above average:", above_average)
