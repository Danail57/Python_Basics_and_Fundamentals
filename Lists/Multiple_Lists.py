factor = int(input())
count = int(input())

positive_ascending_numbers = []

for current_digit in range(1, count + 1):
    digit = factor * current_digit
    positive_ascending_numbers.append(digit)
print(positive_ascending_numbers)
