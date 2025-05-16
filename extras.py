#Lambda
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, numbers))
print(square) # [1, 4, 9, 16, 25]

#private attributes
class Person:
    def __init__(self, name, age):
        self.__private_attribute = 'This is a private attribute.'
        self.name = name
        self.age = age

person = Person('John Doe', 30)
print(person.__private_attribute) 


#public, private class
class Person:
    def __init__(self, name, age):
        self.__private_attribute = 'This is a private attribute.'
        self.name = name
        self.age = age

person = Person('John Doe', 30)
print(person.__private_attribute)  # AttributeError: 'Person' object has no attribute '__private_attribute'

class Person:
    def __init__(self, name, age):
        self._protected_attribute = 'This is a protected attribute.'
        self.name = name
        self.age = age


class Employee(Person):
    def display_protected_attribute(self):
        print(self._protected_attribute)


employee = Employee('Jane Doe', 25)
employee.display_protected_attribute()  # This is a protected attribute.
print(employee._protected_attribute)    # This is a protected attribute.


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    

#decorator 
def my_decorator(original_function):
    def new_function():
        # do something before the original function
        original_function()
        # do something after the original function
    return new_function

@my_decorator
def original_function():
    print('Hello, World!')

original_function()

