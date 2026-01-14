numbers_as_string = input().split(' ')
opposite_numbers = []

for current_digit in numbers_as_string:
    digit = int(current_digit)
    opposite = -digit
    opposite_numbers.append(opposite)
print(opposite_numbers)
