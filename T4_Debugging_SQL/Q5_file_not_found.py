# Q5. Read a file and handle FileNotFoundError.

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error: File not found.")