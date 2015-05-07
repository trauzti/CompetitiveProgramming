class Queue():
    l = []
    def __init__(self):
        pass

    def push(self, x):
        self.l.append(x)

    def pop(self):
        v = self.l[0]
        self.l = self.l[1:]
        return v
    def size(self):
        return len(self.l)

