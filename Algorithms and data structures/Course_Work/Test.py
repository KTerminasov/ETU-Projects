import random

MINIMUM = 25

# Класс, представляющий ребро графа
class Edge:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w

# Класс для реализации хэш-таблицы
class HashTable:
    def __init__(self):
        self.table = {}

    def add(self, key, value):
        self.table[key] = value

    def get(self, key, default=None):
        return self.table.get(key, default)

    def contains(self, key):
        return key in self.table

    def remove(self, key):
        if key in self.table:
            del self.table[key]

    def keys(self):
        return list(self.table.keys())

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.add(key, value)

    def __contains__(self, key):
        return self.contains(key)

# Класс, представляющий узел двусвязного списка
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

# Класс для реализации двусвязного списка
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def remove_first(self):
        if self.is_empty():
            raise IndexError("Список пуст")
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def remove_last(self):
        if self.is_empty():
            raise IndexError("Список пуст")
        else:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.prev.next = None

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def get_length(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

# Класс для реализации стека на основе двусвязного списка
class Stack(DoublyLinkedList):
    def push(self, data):
        self.add_first(data)

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_data = self.head.data
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
            return popped_data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

# Класс для реализации динамического массива
class DynamicArray:
    def __init__(self):
        self.array = []

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value

    def __len__(self):
        return len(self.array)

    def append(self, item):
        self.array.append(item)

    def remove(self, item):
        self.array.remove(item)

    def display(self):
        for item in self.array:
            print(item, end=" ")
        print()

# Функция для вычисления minrun в алгоритме сортировки TimSort
def find_minrun(n):
    r = 0
    while n >= MINIMUM:
        r |= n & 1
        n >>= 1
    return n + r

# Функция сортировки вставками
def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        element = array[i]
        j = i - 1
        while j >= left and element.w < array[j].w:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    return array

# Функция слияния для сортировки TimSort
def merge(array, l, m, r):
    array_length1 = m - l + 1
    array_length2 = r - m
    left = array[l:l + array_length1]
    right = array[m + 1:m + 1 + array_length2]

    i = j = 0
    k = l

    while j < array_length2 and i < array_length1:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < array_length1:
        array[k] = left[i]
        k += 1
        i += 1

    while j < array_length2:
        array[k] = right[j]
        k += 1
        j += 1

# Функция сортировки TimSort
def tim_sort(array):
    n = len(array)
    minrun = find_minrun(n)

    for start in range(0, n, minrun):
        end = min(start + minrun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minrun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            merge(array, left, mid, right)

        size = 2 * size

# Функция для получения лидера множества в структуре Union-Find
def get_leader(x):
    if x == leader[x]:
        return x
    leader[x] = get_leader(leader[x])
    return leader[x]

# Функция для объединения двух множеств в структуре Union-Find
def unite(x, y):
    x = get_leader(x)
    y = get_leader(y)

    if x == y:
        return False

    if random.randint(0, 1) == 0:
        x, y = y, x

    leader[x] = y
    return True

# Функция обхода в глубину (Depth-First Search)
def dfs(adj, v, t, visited, path):
    path.append(v)

    if v == t:
        return True

    if v in visited:
        path.pop()
        return False

    visited.add(v)

    current = adj.head
    while current is not None:
        neighbor = current.data[1]
        if neighbor not in visited:
            reached = dfs(adj, neighbor, t, visited, path)
            if reached:
                return True
        current = current.next

    path.pop()
    return False

# Функция обхода в ширину (Breadth-First Search)
def bfs(adj, start, target):
    visited = set()
    queue = Stack()  # Используем стек вместо очереди
    queue.push((start, [start]))

    while not queue.is_empty():
        current_vertex, path = queue.pop()

        if current_vertex == target:
            print("BFS Путь:", " -> ".join(path))
            return True

        if current_vertex not in visited:
            visited.add(current_vertex)
            current = adj.head
            while current is not None:
                neighbor = current.data[1]
                queue.push((neighbor, path + [neighbor]))
                current = current.next

    print("BFS: Путь не найден.")
    return False

# Основная часть программы
if __name__ == "__main__":
    # Считывание пути к файлу с консоли
    file_path = 'Kraskal.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()

    vertices = lines[0].split()
    n = len(vertices)

    edges = DynamicArray()  # Используем динамический массив вместо списка

    for i in range(1, n + 1):
        row = list(map(int, lines[i].split()))
        for j in range(n):
            if row[j] > 0:
                edges.append(Edge(vertices[i - 1], vertices[j], row[j]))

    tim_sort(edges)

    adjacency_list = DoublyLinkedList()  # Используем двусвязный список вместо списка
    for e in edges:
        adjacency_list.add_first((e.x, e.y))
        adjacency_list.add_first((e.y, e.x))

    leader = HashTable()

    for v in vertices:
        leader.add(v, v)
    result_edges = DynamicArray()  # Используем динамический массив вместо списка

    for e in edges:
        x, y = e.x, e.y

        if unite(x, y):
            result_edges.append(e)

    total_weight = sum(e.w for e in result_edges)

    for e in result_edges:
        print(f"{e.x} {e.y}")

    # Вывод дополнительной строки с суммарным весом
    print(total_weight)

    start_vertex_bfs = input("Введите начальную вершину для обхода BFS: ")
    target_vertex_bfs = input("Введите целевую вершину для обхода BFS: ")

    bfs_result = bfs(adjacency_list, start_vertex_bfs, target_vertex_bfs)

    # Пример использования dfs
    start_vertex = input("Введите начальную вершину для обхода DFS: ")
    target_vertex = input("Введите целевую вершину для обхода DFS: ")

    dfs_path = DynamicArray()  # Используем динамический массив вместо списка
    dfs_result = dfs(adjacency_list, start_vertex, target_vertex, set(), dfs_path)
    print(f"DFS Путь: {' -> '.join(dfs_path)}")
