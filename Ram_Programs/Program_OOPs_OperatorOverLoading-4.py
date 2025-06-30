# ------- Overloading the String Representation (str()) -------

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(1, 2)
print(str(p1))  # Output: Point(1, 2)