money_as_string = input().split(', ')
number_of_beggars = int(input())

money_as_integer = []
for coin in money_as_string:
    money_as_integer.append(int(coin))

final_list = []
for beggar_index in range(number_of_beggars):
    current_sum = 0
    for index in range(beggar_index, len(money_as_integer), number_of_beggars):
        current_sum += money_as_integer[index]
    final_list.append(current_sum)
print(final_list)
