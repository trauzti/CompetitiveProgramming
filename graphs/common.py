class node:

    def addNeighbors(self, l):
        for item in l:
            self.adjacency.append(item)
    def getNeighbors(self):
        return self.adjacency

    def __init__(self, name):
        self.name = name
        self.adjacency = []
        pass

    def __repr__(self):
        return u"Node(%s)" % self.name
