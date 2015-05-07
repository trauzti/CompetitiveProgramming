from Queue import LifoQueue

class stack():
    def __init__(self):
        self.s = LifoQueue()

    def push(self, x):
        self.s.put(x)

    def pop(self):
        return self.s.get()

    def empty(self):
        return self.s.empty()


class slowstack():
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop()

    def size(self):
        return len(self.l)

