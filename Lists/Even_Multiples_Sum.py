factor = int(input())
count = int(input())
sum_even = 0

positive_ascending_numbers = []

for index in range(1, count + 1):
    number = index * factor
    if number % 2 == 0:
        positive_ascending_numbers.append(number)
for number in positive_ascending_numbers:
    sum_even += number
print(positive_ascending_numbers)
print(sum_even)
