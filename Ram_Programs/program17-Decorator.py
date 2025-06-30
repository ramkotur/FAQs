# Define the decorator
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed.")
        return result
    return wrapper

# Use the decorator
@log_execution
def say_hello(name):
    return f"Hello, {name}!"

# Call the decorated function
print(say_hello("Alice"))
