class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person {self.name} is created.")

    # Destructor
    def __del__(self):
        print(f"Person {self.name} is deleted.")

    # Method to display person's details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an instance of the Person class
person1 = Person("Alice", 30)
person1.display()

# Delete the instance
del person1