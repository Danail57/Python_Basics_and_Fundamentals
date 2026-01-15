def even_number(number: int):
    return number % 2 == 0

sequence_of_numbers = input().split(' ')
even_numbers = []
for number in sequence_of_numbers:
    even_numbers.append(int(number))
final_result = list(filter(even_number, even_numbers))
print(final_result)
