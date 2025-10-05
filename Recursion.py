def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter number: "))
print("Factorial =", factorial(n))

# Explaination of Program

# Define a function factorial(n) to calculate the factorial of a number.

# If n is 0, return 1 (base case).

# Otherwise, return n multiplied by factorial(n - 1) (recursive step).

# Ask the user to enter a number and store it in n.

# Call factorial(n) and print the result.

# Output :- Enter number: 5
#           Factorial = 120
