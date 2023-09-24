import math

# Input a non-negative integer N
N = int(input("Enter a non-negative integer: "))

# Function to check if a number is a perfect square
def is_perfect_square(num):
    return int(math.sqrt(num))**2 == num

# Check if N is part of the Fibonacci sequence
if is_perfect_square(5 * N**2 + 4) or is_perfect_square(5 * N**2 - 4):
    print("Yes")
else:
    print("No")
