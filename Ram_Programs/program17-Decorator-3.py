class MyClass:
    class_variable = "Hello, Class!"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        return cls.class_variable

# Calling the class method
print(MyClass.class_method())  # Output: Hello, Class!

# Creating an instance of MyClass
my_instance = MyClass("Hello, Instance!")

# Calling the class method from an instance
print(my_instance.class_method())  # Output: Hello, Class!
