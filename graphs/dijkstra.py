from datastructures.priorityqueue import minpriorityqueue

from .common import node

# HOW TO GIVE THE EDGE SOME WEIGHT

def dijkstra(weights, start, dest):

    cost = {start: 0}
    done = set()
    Q = minpriorityqueue()
    Q.push((0, start))

    while not Q.empty():
        rank, n = Q.pop()

        if n in done:
            continue

        done.add(n)

        if n == dest:
            return cost[n]

        for o in n.getNeighbors():
            if o not in done:
                thiscost = cost[n] + weights[n,o] # weight from n to o
                shouldAdd = False
                if o in cost and thiscost < cost[o]:
                    shouldAdd = True

                if o not in cost:
                    shouldAdd = True

                if shouldAdd:
                    cost[o] = thiscost
                    Q.push((thiscost, o))

    assert False

