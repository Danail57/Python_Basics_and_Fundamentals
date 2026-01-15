def multiply_by(n):
    return lambda x: x * n

n = int(input("Enter the multiplier: "))
unknown_number = int(input("Enter the number to be multiplied: "))

multiplier = multiply_by(n)
result = multiplier(unknown_number)

print(f"Result: {result}")
