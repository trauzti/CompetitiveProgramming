class Stack():
    l = []
    def __init__(self):
        pass

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop()

    def size(self):
        return len(self.l)

