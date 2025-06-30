# ------- Overloading the Addition Operator (+) -------

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # This calls the __add__ method
print(p3)  # Output: Point(4, 6)