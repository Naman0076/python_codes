#1 append()
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#2 cleaer()
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)

#3 copy()
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print(fruits)

#4 count()
fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x)

#5  extend()
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

#6 index()
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)

#7 insert()
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)

#8 pop()
fruits = ['apple', 'banana', 'cherry']

fruits.pop(2)
print(fruits)

#9 remove()
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")
print(fruits)

#10 reverse()
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)

#11 sort()
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)