#enumerate
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)

fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits, 1):
    print(i, fruit)

#zip
fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'blue']
for fruit, color in zip(fruits, colors):
    print(fruit, color)