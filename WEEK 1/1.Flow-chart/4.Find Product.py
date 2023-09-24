# Input a non-negative integer N
N = int(input("Enter a non-negative integer: "))

# Initialize the result to 1
factorial = 1

# Calculate the factorial using a loop
for i in range(1, N + 1):
    factorial *= i

# Print the result
print(f"{N}! = {factorial}")
