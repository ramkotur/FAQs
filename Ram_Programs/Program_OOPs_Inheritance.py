# --- OOPs Inharitance -------

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

# Create an instance of the Dog class
dog = Dog("Charlie")
print(dog.speak())  # Output: Charlie barks!