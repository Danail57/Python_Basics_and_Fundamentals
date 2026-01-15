def sequence_of_absolute_numbers(numbers):
    result = []
    for number in numbers:
        result.append(abs(float(number)))
    return result

user_input = input().split()
result = sequence_of_absolute_numbers(user_input)
print(result)
