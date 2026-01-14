n = int(input())
positive_numbers = []
negative_numbers = []
sum_of_negatives = 0

for digit in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)
        sum_of_negatives += current_number

print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {len(positive_numbers)}')
print(f'Sum of negatives: {sum_of_negatives}')
