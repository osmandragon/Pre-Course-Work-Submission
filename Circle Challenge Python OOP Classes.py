import math

class Circle:
    Radius_Property = 0

    def __init__(self,radius):
        self.radius = radius

    def calculate_diameter(self):
        diameter = 2 * self.radius
        return diameter

    def calculate_circumference(self):
        circumference =  2 * math.pi * self.radius
        return circumference

    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        return area

numb1 = float(input("Enter a number for Radius:"))

c = Circle(numb1)
print(c)
print(c.radius)

print(c.calculate_diameter())
print(c.calculate_circumference())
print(c.calculate_area())
