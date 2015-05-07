from datastructures.queue import queue

from .common import node

def bfs(start, dest):
    dist = {start: 0}
    Q = queue()
    Q.push(start)
    while not Q.empty():
        n = Q.pop()

        if n == dest:
            return dist[n]

        for o in n.getNeighbors():
            if o not in dist:
                dist[o] = dist[n] + 1
                Q.push(o)

    assert False

