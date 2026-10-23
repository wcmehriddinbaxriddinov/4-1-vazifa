class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self, P):
        return P * (self.radius ** 2)

    def diameter(self):
        return 2 * self.radius

P = 3.14
circle = Circle(5)

print(f"Doira yuzi: {circle.area(P)}")
print(f"Doira diametri: {circle.diameter()}")
