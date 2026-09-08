# Q3. Handle both ValueError and TypeError.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Sum =", a + b)

except ValueError:
    print("Error: Please enter valid integers.")

except TypeError:
    print("Error: Invalid data type.")