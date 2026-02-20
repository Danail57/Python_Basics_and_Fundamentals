from PIL.ImImagePlugin import j


def riverSizes(matrix):
    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                sizes.append(get_river_side(matrix, i, j))
    return sizes

def get_river_side(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return 0
    matrix[i][j] = 0
    size = 1
    size += get_river_side(matrix, i + 1, j)
    size += get_river_side(matrix, i - 1, j)
    size += get_river_side(matrix, i, j + 1)
    size += get_river_side(matrix, i, j - 1)
    return size
    pass

rows = int(input())
matrix = [list(map(int, input().split())) for i in range(rows)]


sizes = [get_river_side(matrix, i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 1]

print(sizes)