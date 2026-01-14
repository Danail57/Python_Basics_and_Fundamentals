sequence_of_numbers = input().split()

final_list = []

for number in sequence_of_numbers:
    final_list.append(abs(float(number)))
print(final_list)
