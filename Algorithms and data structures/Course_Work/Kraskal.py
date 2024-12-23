from DArray import *
from ReadMatrix import *
from Sort import *
from copy import *

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, rank, x, y):
    xroot = find(p, x)
    yroot = find(p, y)

    if rank[xroot] < rank[yroot]:
        p[xroot] = yroot;
    elif rank[xroot] > rank[yroot]:
            p[yroot] = xroot
    else:
        p[yroot] = xroot
        rank[xroot] += 1


def kraskal(edg):
    edg_list = deepcopy(edg)
    ins_sort(edg_list)

    res = DArray()

    parent = DArray()
    rank = DArray()

    for i in range(len(edg_list)):
        parent[i] = i
        rank[i] = 0

    j = 0
    while j < len(edg_list)- 1:
        x = find(parent, ord(edg_list[j + 1][0])-65)
        y = find(parent, ord(edg_list[j + 1][1])-65)

        if x != y:
            res.add(DArray())
            res[-1] += edg_list[j+1][0]
            res[-1] += edg_list[j+1][1]
            res[-1] += edg_list[j+1][2]
            union(parent, rank, x, y)

        j += 1

    weight = 0
    print("Получившееся остовное дерево:")
    for i in range(len(res)):
        print(res[i][0], res[i][1], res[i][2])
        weight += res[i][2]
    print("Вес:", weight)

