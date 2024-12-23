from DArray import *


def get_edg_list(loc):
    with open(loc, 'r') as f:
        s = f.read()

    matrix = split(s, '\n')
    matrix[0] = split(matrix[0])
    l = len(matrix)

    edg_list = DArray()

    for i in range(1, l):
        matrix[i] = split(matrix[i])
        for j in range(l - 1):
            if matrix[i][j] != '0':
                edg_list.add(DArray())
                edg_list[-1] += matrix[0][i - 1]
                edg_list[-1] += matrix[0][j]
                edg_list[-1] += int(matrix[i][j])

    return edg_list

def get_edges(loc):
    with open(loc, 'r') as f:
        s = f.read()

    matrix = split(s, '\n')
    matrix[0] = split(matrix[0])
    l = len(matrix)

    edges = DArray()

    for i in range(1, l):
        matrix[i] = split(matrix[i])
        for j in range(i, l - 1):
            if matrix[i][j] != '0':
                edges.add(DArray())
                edges[-1] += matrix[0][i - 1]
                edges[-1] += matrix[0][j]
                edges[-1] += int(matrix[i][j])

    return edges

def get_vetex(loc):
    with open(loc, 'r') as f:
        s = f.read()

    matrix = split(s, '\n')
    return split(matrix[0])