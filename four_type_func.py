# 1. Default Arguments in Python
def area(length, width = 1):
    return length * width

print(area(5))     # 5
print(area(5, 10)) # 50

# 2.Positional Arguments in Python
def greeting(name, title='Mr.'):
    return f'Hello, {title} {name}'

print(greeting('John'))         # Hello, Mr. John
print(greeting('Jack', 'Dr.'))  # Hello, Dr. Jack

# 3. Keyword Arguments in Python
def greeting(name, title='Mr.'):
    return f"Hello, {title} {name}"

print(greeting(name='John'))               # Hello, Mr. John
print(greeting(name='John', title='Dr.'))  # Hello, Dr. John

# 4.Nuances of Working With Functions
def product(**kwargs):
    result = 1
    for key, value in kwargs.items():
        result *= value
    return result

print(product(a = 2, b = 3, c = 4))   