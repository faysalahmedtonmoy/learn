def add_numbers(num1, num2):
    """Function to add two numbers."""
    return num1 + num2

# Get input from the user
# input() returns a string, so we convert it to a float for mathematical operations
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

# Call the function and print the result
result = add_numbers(n1, n2)
print(f"The sum of {n1} and {n2} is: {result}")
