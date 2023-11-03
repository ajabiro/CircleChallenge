import math


class Circle:

    def __init__(self, radius):
        self.radius = radius
        # self.radius = float(input("Input a radius: "))

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def grow(self):
        self.radius = self.radius * 2

    def get_radius(self):
        return self.radius


while True:
    try:
        radius = float(input("Input a radius: "))
        # print(radius)
        break
    except ValueError:
        print("Invalid data. Please enter a number.")

c1 = Circle(radius)
print(f'Diameter: ', c1.calculate_diameter())
print(f'Circumference: ', c1.calculate_circumference())
print(f'Area: ', c1.calculate_area())

while True:
    grow_circle = input("Would you like your circle to grow? (y/n): ")
    if grow_circle == "y":
        c1.grow()
        print(f'Diameter: ', c1.calculate_diameter())
        print(f'Circumference: ', c1.calculate_circumference())
        print(f'Area: ', c1.calculate_area())
    elif grow_circle == "n":
        print("Goodbye!")
        break
    else:
        print("Enter either \"y\" or \"n\"")


