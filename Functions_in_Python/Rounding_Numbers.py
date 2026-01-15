numbers_as_float = input().split(' ')
final_integer_list = []

for number in numbers_as_float:
    rounded_number = round(float(number))
    final_integer_list.append(rounded_number)

print(final_integer_list)
