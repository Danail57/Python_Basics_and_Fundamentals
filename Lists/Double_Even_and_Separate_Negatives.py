n = int(input())
digits_even = []
negative_digits_even = []

for digit in range(n):
    current_digit = int(input())
    if current_digit % 2 == 0:
        if current_digit < 0:
            negative_digits_even.append(current_digit)
        else:
            digits_even.append(current_digit * 2)

print("Doubled even numbers (non-negative):", digits_even)
print("Negative even numbers:", negative_digits_even)
print(f"Count of doubled even numbers: {len(digits_even)}")
print(f"Count of negative even numbers: {len(negative_digits_even)}")

if digits_even:
    print(f"Max doubled even number: {max(digits_even)}")
    print(f"Min doubled even number: {min(digits_even)}")
else:
    print("No doubled even numbers")

if negative_digits_even:
    print(f"Max negative even number: {max(negative_digits_even)}")
    print(f"Min negative even number: {min(negative_digits_even)}")
else:
    print("No negative even numbers")
