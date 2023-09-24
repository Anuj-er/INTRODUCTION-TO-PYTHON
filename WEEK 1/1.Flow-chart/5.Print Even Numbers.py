# Input a positive integer N
N = int(input("Enter a positive integer: "))

# Check if N is greater than or equal to 2 (to ensure there are even numbers to print)
if N >= 2:
    print("Even numbers between 1 and", N, "are:")
    for i in range(2, N + 1, 2):
        print(i)
else:
    print("There are no even numbers between 1 and", N)
