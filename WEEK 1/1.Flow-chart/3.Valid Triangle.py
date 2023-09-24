# Input three numbers representing the lengths of the lines
a = float(input("Enter the length of the first line: "))
b = float(input("Enter the length of the second line: "))
c = float(input("Enter the length of the third line: "))

# Check if a valid triangle can be formed
if a + b > c and b + c > a and c + a > b:
    print("Yes")
else:
    print("No")
