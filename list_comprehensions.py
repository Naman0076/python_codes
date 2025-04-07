# Basic 
squares = [x**2 for x in range(1, 11)]
print(squares)

# Basic with filtering / conditions
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

# NEsted Loops
coordinates = [(x, y) for x in [1, 2] for y in [3, 4]]
print(coordinates)

# flatten a 2D list (Matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)

# with functions
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

# Remove vowels from a string
text = "List comprehensions are awesome!"
consonants = "".join([ch for ch in text if ch.lower() not in "aeiou"])
print(consonants)

# Common element in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [x for x in list1 if x in list2]
print(common_elements)

# List of prime numbers
primes = [x for x in range(2, 31) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))]
print(primes)