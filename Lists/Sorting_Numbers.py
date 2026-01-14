sequence_of_numbers = input().split(' ')
ascending_numbers = []

for current_number in sequence_of_numbers:
    ascending_numbers.append(int(current_number))
print(sorted(ascending_numbers))
