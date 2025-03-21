#examle of *args (Non-Keyword Arguments) and **kwargs (Keyword Arguments) for my understanding:
def order_pizza(size, *args, **details):
    print(f"order a {size} of pizza")
    for topping in args:
        print(f"- {topping}")
    print(f"\nDetails of the order are: ")
    for key, value in details.items():
        print(f"-{key} : {value}")
order_pizza("Large","peperoni", "onions", delivery=True, tip="50rs")

#Lambda Function syntax + example :
print((lambda x,y: x + y)(5,78))


#exapmle
def my_map(my_func, my_iter):
    result=[]
    for item in my_iter:
        new_item = my_func(item)
        result.append(new_item)
    return(result)
nums = [4, 556, 245, 2, 100]
cubed = my_map(lambda x: x**3, nums)
print(cubed)