COVERAGE = 400

length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
height = float(input("Enter the height of the room in feet: "))
coats = float(input("Enter the number of coats in the room: "))

surface_area = (length * width) + (2 * length * height) + (2 * width * height)

coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed / COVERAGE

print("The number of paint cans you require: ",cans_of_paint_required)
