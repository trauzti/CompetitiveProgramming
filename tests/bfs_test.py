from graphs.bfs import bfs
from graphs.common import node

def tc1():
    """
    0 -> 5,6
    5 -> 7
    7 -> 10
    BFS from 0 to 10 should have a distance of 3
    """
    nodes = [node(i) for i in xrange(11)]
    nodes[0].addNeighbors(filter(lambda x: x.name== 5 or x.name == 6, nodes))
    nodes[5].addNeighbors(filter(lambda x:x.name == 7, nodes))
    nodes[7].addNeighbors(filter(lambda x:x.name == 10, nodes))

    dist = bfs(nodes[0], nodes[10])
    assert dist == 3

def run():
    print "bfs TEST STARTING"
    tc1()
    print "bfs TEST COMPLETED"

if __name__ == "__main__":
    run()
