class Node:
    def __init__(self, v=0):
        self.weight = v
        self.start = None
        self.end = None


class Graph(Node):
    def __init__(self, v=0):
        super().__init__(v)

    def centre_walk(self):  # центрированный обход

        if self.left is not None:
            self.left.centre_walk()
        print(self.value, end=" ")
        if self.right is not None:
            self.right.centre_walk()

def get_from_file(graph):
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
