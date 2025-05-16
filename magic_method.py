class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'


person = Person('John Doe', 30)
print(person)
# Person(name=John Doe, age=30)