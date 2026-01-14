# You will be given two sequences of strings, separated by ", ". 
# Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.

first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_substrings = []

for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            new_substrings.append(first_string)
            break
print(new_substrings)
