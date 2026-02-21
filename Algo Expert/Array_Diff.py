def array_diff(a, b):
    set_b = set(b)

    return [i for i in a if i not in set_b]

a = [1, 2, 2, 3, 4]
b = [2]
print(array_diff(a, b))
