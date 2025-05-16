def countdown(n):
    while n > 0:
        yield n
        n -= 1
        
for i in countdown(5):
 print(i)

def number_generator():
    for i in range(1, 11):
        yield i


def even_filter(generator):
    for value in generator:
        if value % 2 == 0:
            yield value


for value in even_filter(number_generator()):
    print(value)