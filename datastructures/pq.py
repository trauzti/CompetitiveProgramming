from Queue import PriorityQueue
"""     Entries are typically tuples of the form:  (priority number, data). """

class pq():
    def __init__(self):
        self.q = PriorityQueue()

    def push(self, x):
        self.q.put(x)

    def pop(self):
        return self.q.get()

    def empty(self):
        return self.q.empty()

