# Input the lengths of three sides of the triangle
a = float(input("Enter the length of side A: "))
b = float(input("Enter the length of side B: "))
c = float(input("Enter the length of side C: "))

# Check the nature of the triangle
if a == b == c:
    print(1)  # Equilateral triangle
elif a == b or b == c or c == a:
    print(0)  # Isosceles triangle
else:
    print(-1)  # Scalene triangle
