from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Boww Boww!"

# Create an instance of the Dog class
dog = Dog()
print(dog.speak())  # Output: Boww Boww!