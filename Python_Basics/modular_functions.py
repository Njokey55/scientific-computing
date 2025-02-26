import math  # Importing math module to use math.pi for π

# Function to calculate the area of different shapes
def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        # Area of circle: πr²
        return math.pi * dimension1 ** 2
    elif shape == "rectangle":
        # Area of rectangle: length × width
        return dimension1 * dimension2
    elif shape == "triangle":
        # Area of triangle: (1/2) × base × height
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

# Test the function with different shapes and print the results
circle_area = calculate_area("circle", 5)  # Circle with radius 5
rectangle_area = calculate_area("rectangle", 4, 6)  # Rectangle with length 4 and width 6
triangle_area = calculate_area("triangle", 3, 7)  # Triangle with base 3 and height 7

# Print the results
print(f"Area of the circle: {circle_area:.2f}")
print(f"Area of the rectangle: {rectangle_area:.2f}")
print(f"Area of the triangle: {triangle_area:.2f}")
