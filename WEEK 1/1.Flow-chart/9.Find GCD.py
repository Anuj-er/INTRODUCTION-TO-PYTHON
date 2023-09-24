# Function to calculate the GCD using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the GCD
result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)
