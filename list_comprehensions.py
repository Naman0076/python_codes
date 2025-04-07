# Basic 
squares = [x**2 for x in range(1, 11)]
print(squares)

x = []
for i in range(1, 11):
    x.append(i**2)

# Basic with filtering / conditions
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

x = []
for i in range (1, 21):
    if i %2 == 0:
        x.append(i)

# NEsted Loops
coordinates = [(x, y) for x in [1, 2] for y in [3, 4]]
print(coordinates)

a = []
for x in [1, 2]:
    for y in [3, 4]:
        a.append((x, y))
print(a)

# flatten a 2D list (Matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)

n = len(matrix)
m = len(matrix[0])
a = []
for i in range(n):
    for j in range(m):
        a.append(matrix[i][j])

# with functions
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

x = ["hello", "world", "python"]
for i in range(len(x)):
    x[i] = x[i].upper()
print(x)

# Remove vowels from a string
text = "List comprehensions are awesome!"
consonants = "".join([ch for ch in text if ch.lower() not in "aeiou"])
print(consonants)

c = ""
for ch in text:
    if ch.lower() not in "aeiou":
        c += ch
print(c)

# Common element in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [x for x in list1 if x in list2]
print(common_elements)

c_ele = []
for x in list1:
    if x in list2:
        c_ele.append(x)


# List of prime numbers
primes = [x for x in range(2, 31) if all(x % d != 0 for d in range(2, int(x**0.5) + 1))]
print(primes)

primes = []

for x in range(2, 31):
    is_prime = True
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)

print(primes)
