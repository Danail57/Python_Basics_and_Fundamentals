sequence_of_numbers = [int(number) for number in input().split(', ')]
group = 10
while sequence_of_numbers:
    filtered_numbers = [number for number in sequence_of_numbers if number <= group]
    print(f"Group of {group}'s: {filtered_numbers}")
    sequence_of_numbers = [number for number in sequence_of_numbers if number not in filtered_numbers]
    group += 10
