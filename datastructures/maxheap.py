from heapq import heappush, heappop

class maxheap:

    l = None

    def __init__(self):
        self.l = []
        pass

    def push(self, x):
        heappush(self.l, -x)

    def pop(self):
        return -heappop(self.l)

    def peek(self):
        x = heappop(self.l)
        heappush(self.l, x)
        return -x

    def count(self, x):
        return self.l.count(x)
