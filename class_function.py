class Car:  
    # Without __init__, directly defining attributes afterward  
    def start_engine(self):  
        status = "Engine started."  # Local variable  
        print(status)
        
# Creating an instance of Car  
my_car = Car()  

# Setting attributes directly after the instance is created  
my_car.make = "Toyota"  
my_car.model = "Corolla"  
my_car.year = 2022  

print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")  
my_car.start_engine()

class MyClass:
    def __init__(self, value):
        self.value = value

    def display_id(self):
        print(f"ID of self: {id(self)}")


# Create an instance of MyClass
class_instance = MyClass(10)
print(f"ID of instance: {id(class_instance)}")

# Calling the method to check IDs
class_instance.display_id()

class Car:  
    # Class variable to track the number of cars created  
    number_of_cars = 0  

    def __init__(self, make, model, year):  
        self.make = make          # Instance variable  
        self.model = model        # Instance variable  
        self.year = year          # Instance variable  

        # Increment the class variable whenever a new instance is created  
        Car.number_of_cars += 1  

    def display_info(self):  
        """Display the information of the car."""  
        print(f"{self.year} {self.make} {self.model}")  

    @classmethod  
    def get_number_of_cars(cls):  
        """Class method to return the number of car instances created."""  
        return cls.number_of_cars  

# Creating instances of Car  
car1 = Car("Toyota", "Corolla", 2022)  
car2 = Car("Honda", "Civic", 2023)  
car3 = Car("Ford", "Mustang", 2021)  

# Displaying information about individual cars  
car1.display_info()  # Output: "2022 Toyota Corolla"  
car2.display_info()  # Output: "2023 Honda Civic"  

# Accessing the class variable to get the number of cars created  
print(f"Total cars created: {Car.get_number_of_cars()}")  