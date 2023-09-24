# Input a positive integer N
N = int(input("Enter a positive integer: "))

# Initialize the sum to 0
sum_of_evens = 0

# Calculate the sum of even numbers
for i in range(2, N + 1, 2):
    sum_of_evens += i

# Print the result
print("The sum of even numbers from 2 to", N, "is:", sum_of_evens)
