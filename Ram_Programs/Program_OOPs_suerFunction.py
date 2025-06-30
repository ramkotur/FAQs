class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

# Create an instance of the Dog class
dog = Dog("Charlie", "Bulldog")
print(dog.breed)  # Output: Bulldog