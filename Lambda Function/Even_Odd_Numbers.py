#No Lambda Used.

number_list = list(map(int, input().split()))
even_numbers = []
odd_numbers = []

for digit in number_list:
    if digit % 2 == 0:
        even_numbers.append(digit)
    else:
        odd_numbers.append(digit)

print(f'This is your primary number list: {number_list}')
print(f'Even numbers in your number list are: {even_numbers}')
print(f'Odd numbers in your number list are: {odd_numbers}')
