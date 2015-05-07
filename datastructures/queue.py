from Queue import Queue

class queue():
    def __init__(self):
        self.q = Queue()

    def push(self, x):
        self.q.put(x)

    def pop(self):
        return self.q.get()

    def empty(self):
        return self.q.empty()


class SlowQueue():
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        v = self.l[0]
        self.l = self.l[1:]
        return v

    def size(self):
        return len(self.l)

    def empty(self):
        return len(self.l) == 0
