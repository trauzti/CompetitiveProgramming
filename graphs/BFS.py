from datastructures.Queue import Queue
from .common import Node

def BFS(start, dest):
    dist = {start: 0}
    Q = Queue()
    Q.push(start)
    while Q.size() > 0:
        node = Q.pop()

        if node == dest:
            return dist[node]

        for o in node.adjacency:
            if o not in dist:
                dist[o] = dist[node] + 1
                Q.push(o)

    assert False

