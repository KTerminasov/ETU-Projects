from DArray import *
from ReadMatrix import *
from Kraskal import *
from Traversal import *
import os


stop = False

while not stop:
    os.system('cls')
    print("Курсовая работа\n")

    print("1.Алгоритм Краскала", "2.Обход графа в глубину", "3.Обход графа в ширину", "4.Выход", sep='\n')
    print("Выберите действие:", end = ' ')
    choice = int(input())

    os.system('cls')

    if choice == 1:
        edg_list = get_edg_list('Kraskal.txt')
        kraskal(edg_list)
        os.system("pause")
    if choice == 2:
        edges = get_edges('Kraskal.txt')
        print("Введите вершину начала обхода:", end=' ')
        vert = input()

        visited = DArray()
        for i in range(len(edges)):
            visited[i] = False

        print("Результат обхода графа в глубину:", end = ' ')
        depth(edges, vert, visited)
        print()
        os.system("pause")

    if choice == 3:
        edges = get_edges('Kraskal.txt')
        print("Введите вершину начала обхода:", end=' ')
        vert = input()

        visited = DArray()
        for i in range(len(edges)):
            visited[i] = False

        print("Результат обхода графа в ширину:", end=' ')
        width(edges, vert, visited)
        print()
        os.system("pause")

    if choice == 4:
        stop = True
