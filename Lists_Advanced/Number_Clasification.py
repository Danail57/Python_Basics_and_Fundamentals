# Note: Zero is counted as a positive number.

numbers = [int(number) for number in input().split(', ')]

positive_numbers = [number for number in numbers if number >= 0]
negative_numbers = [number for number in numbers if number < 0]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]

print(f"Positive: {', '.join(map(str, positive_numbers))}")
print(f"Negative: {', '.join(map(str, negative_numbers))}")
print(f"Even: {', '.join(map(str, even_numbers))}")
print(f"Odd: {', '.join(map(str, odd_numbers))}")
