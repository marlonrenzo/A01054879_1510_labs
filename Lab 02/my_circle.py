pi = 3.14159
radius = 0
radius = float(input("Enter a radius for a circle: "))

circumference = 2 * pi * radius
print("Circumference: ",circumference)

area = pi * radius * radius
print("Area: ",area)

double_radius = 2 * radius
double_circumference = 2 * pi * double_radius
double_area = pi * double_radius * double_radius

print("Circumference increase when radius is doubled: ",double_circumference/circumference)
print("Area increase when radius is doubled: ",double_area/area)