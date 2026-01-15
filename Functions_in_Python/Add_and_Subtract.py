def sum_numbers(first_number: int, second_number: int):
    result = first_number + second_number
    return result

def subtract (result: int, third_number: int):
    subtract = result - third_number
    return subtract

def add_and_subtract(first_number: int, second_number: int, third_number: int):
    sum_of_numbers = sum_numbers(first_number, second_number)
    final_result = subtract(sum_of_numbers, third_number)
    return final_result

first_number = int(input())
second_number = int(input())
third_number = int(input())
add_and_subtract(first_number, second_number, third_number)
print(add_and_subtract(first_number, second_number, third_number))
