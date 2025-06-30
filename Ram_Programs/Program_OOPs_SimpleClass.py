class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

# Create an instance of the Animal class
dog = Animal("Charlie")
print(dog.speak())  # Output: Charlie says hello!