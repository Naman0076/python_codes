# Basic 
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Filtering 
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# Dictionary Comphrension
labels = {x: "Even" if x % 2 == 0 else "Odd" for x in range(1, 6)}
print(labels)

# Swapping key and values 
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)

# Filtering words by length
words = ["apple", "bat", "cherry", "dog", "elephant"]
long_words = {word: len(word) for word in words if len(word) > 4}
print(long_words)

# Create a dictionary from two lists 
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person = {k: v for k, v in zip(keys, values)}
print(person)

# Counting chracter occurences
text = "hello world"
char_count = {char: text.count(char) for char in set(text)}
print(char_count)

# Filtering dictionary 
scores = {"Alice": 45, "Bob": 82, "Charlie": 60, "David": 30}
high_scores = {k: v for k, v in scores.items() if v > 50}
print(high_scores)

# Generate multiplication table 
table_5 = {x: x * 5 for x in range(1, 11)}
print(table_5)

# Nested dictionary comphrension
numbers = {x: {"square": x**2, "cube": x**3} for x in range(1, 6)}
print(numbers)

