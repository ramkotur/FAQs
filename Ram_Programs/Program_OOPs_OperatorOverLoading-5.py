# ------- Overloading the Multiplication Operator (*) -------

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
v1 = Vector(2, 3)
v2 = v1 * 3  # This calls the __mul__ method
print(v2)  # Output: Vector(6, 9)