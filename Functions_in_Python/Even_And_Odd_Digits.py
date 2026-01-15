def even_and_odd_digits(number: str):
    even_digit = []
    odd_digit = []

    for current_number in number:
        if int(current_number) % 2 == 0:
            even_digit.append(int(current_number))
        else:
            odd_digit.append(int(current_number))
    even_digit = sum(even_digit)
    odd_digit = sum(odd_digit)

    return f'Odd sum = {odd_digit}, Even sum = {even_digit}'

number = input()
print(even_and_odd_digits(number))
