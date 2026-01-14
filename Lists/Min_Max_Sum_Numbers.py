sequence_of_numbers = input().split( )

numbers = []

for current_number in sequence_of_numbers:
    numbers.append(int(current_number))

minimum_number = min(numbers)
maximum_number = max(numbers)
total_sum = sum(numbers)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f'"The sum number is: {total_sum}')
