from Stack import *
from DArray import *


def depth(edges, vert, vis):
    vis[ord(vert) - 65] = True
    print(vert, end=' ')

    for i in range(len(edges)):
        if edges[i][0] == vert and not vis[ord(edges[i][1]) - 65]:
            depth(edges, edges[i][1], vis)
        if edges[i][1] == vert and not vis[ord(edges[i][0]) - 65]:
            depth(edges, edges[i][0], vis)


def width(edges, start, vis):
    queue = DArray()
    vis[ord(start) - 65] = True
    queue[0] = start

    while not len(queue) == 0:
        curr = queue[0]
        queue.remove(0)
        print(curr, end=' ')

        for i in range(len(edges)):
            if edges[i][0] == curr and not vis[ord(edges[i][1]) - 65]:
                vis[ord(edges[i][1]) - 65] = True
                queue += edges[i][1]

            if edges[i][1] == curr and not vis[ord(edges[i][0]) - 65]:
                vis[ord(edges[i][0]) - 65] = True
                queue += edges[i][0]
