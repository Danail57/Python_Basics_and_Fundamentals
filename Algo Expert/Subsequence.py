def isValidSubsequence(array, sequence):
    sequence_index = 0
    for value in array:
        if sequence_index == len(sequence):
            break
        if sequence[sequence_index] == value:
            sequence_index += 1
    return sequence_index == len(sequence)
    pass


array_input = input("Array: ")
array = [int(x) for x in array_input.split(",")]

sequence_input = input("Sequence: ")
sequence = [int(x) for x in sequence_input.split(",")]
result = isValidSubsequence(array, sequence)
if result:
    print("true")
else:
    print("false")