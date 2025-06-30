class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Create instances of Dog and Cat
animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())
# Output:
# Woof!
# Meow!