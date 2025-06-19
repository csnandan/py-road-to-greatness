favorite_movies = ['the shawshank redemption', 'spiderman across the spider-verse', "singin' in the rain", 'wall e', 'soul']

print(f"My favorite movies are:\n{favorite_movies}")
print(f"My top 3 are:\n{favorite_movies[0:3]}")
favorite_movies.remove("singin' in the rain")
favorite_movies.insert(2, 'up')
print(f"My current top 3 are:\n{favorite_movies}")
favorite_movies.append('kummatty')
print(f"My favorite movies are:\n{favorite_movies}")
