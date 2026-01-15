#Lambda Used.

number_list = list(map(int, input("Enter numbers separated by space: ").split()))

even_numbers = list(filter(lambda x: x % 2 == 0, number_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, number_list))

print(f'This is your primary number list: {number_list}')
print(f'Even numbers in your number list are: {even_numbers}')
print(f'Odd numbers in your number list are: {odd_numbers}')
