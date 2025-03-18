#1 clear()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print(car)


#2 copy()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x)


#3 fromkeys()
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)


#4 get()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)


#5 items()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
print(x)


#6 keys()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)


#7 pop()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print(car)


#8 popitem()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car)


#9 setdefult()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")
print(x)


#10 update()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print(car)


#11 values()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)