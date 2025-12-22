class Person:
    # The __init__ method is the constructor. It initializes the object's attributes when a new instance is created.
    def __init__(self, id, name, city, income):
        self.id = id         # Assigns the argument 'id' to the object's attribute 'id'
        self.name = name     # Assigns the argument 'name' to the object's attribute 'name'
        self.city = city     # Assigns the argument 'city' to the object's attribute 'city'
        self.income = income # Assigns the argument 'income' to the object's attribute 'income'

    # The displayinfo method prints the attributes of the Person instance in a formatted string.
    def displayinfo(self):
        print(f"person:-- {self.id}-{self.name}-{self.city}-{self.income}")

# Create an instance of the Person class named p1, passing the required arguments to __init__.
p1 = Person(100, "narayan", "pune", 95000)
p5 = Person(100, "smith", "london", 75000)
p8 = Person(100, "---", "london", 75000)

# Call the displayinfo method on the p1 instance.
p1.displayinfo()
p5.displayinfo()
p8.displayinfo()

print("type of the p1 class:----",type(p1))