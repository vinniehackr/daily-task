a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"The area of the triangle is: {area:.2f}")
