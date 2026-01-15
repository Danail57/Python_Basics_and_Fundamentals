def multiply_process(a, b):
    result = a * b
    return result


def divide_process(a, b):
    result = int(a / b)
    return result


def add_process(a, b):
    result = a + b
    return result


def subtract_process(a, b):
    result = a - b
    return result


def calculator():
    operator = input()
    a = int(input())
    b = int(input())
    if operator == 'multiply':
        return multiply_process(a, b)
    elif operator == 'divide':
        return divide_process(a, b)
    elif operator == 'add':
        return add_process(a, b)
    elif operator == 'subtract':
        return subtract_process(a, b)


result = calculator()
print(result)
