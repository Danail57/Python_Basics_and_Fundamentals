numbers = list(map(int, input().split(', ')))

even_numbers = [index for index, number in enumerate(numbers) if number % 2 == 0]
print(even_numbers)
