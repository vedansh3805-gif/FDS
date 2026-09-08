# Q4. Demonstrate IndexError and handle it using try-except.

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Error: Index out of range.")