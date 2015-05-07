from Queue import PriorityQueue
"""     Entries are typically tuples of the form:  (priority number, data). """

class minpriorityqueue():
    def __init__(self):
        self.pq = PriorityQueue()

    def push(self, x):
        rank, key = x
        self.pq.put((rank, key))

    def pop(self):
        rank, key = self.pq.get()
        return (rank, key)

    def empty(self):
        return self.pq.empty()

class maxpriorityqueue():
    def __init__(self):
        self.pq = PriorityQueue()

    def push(self, x):
        rank, key = x
        self.pq.put((-rank, key))

    def pop(self):
        rank, key = self.pq.get()
        return (-rank, key)

    def empty(self):
        return self.pq.empty()

